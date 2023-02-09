#
# This file is used to call the GUI generated by QT Designer and manage the updates of the different widgets
#
import numpy
from PyQt5.QtCore import QObject

from GUI.ECG_GUI_QTDesigner import Ui_MainWindow  # GUI main Class and File
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QApplication
import time
from random import randint
import pyqtgraph as pg
import numpy as np

_translate = QtCore.QCoreApplication.translate


class TIMER:
    def __init__(self, update_interval_ms, function):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(update_interval_ms)
        self.timer.timeout.connect(function)
        self.timer.start()


class Ui_Build(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__()   # inheritances all GUI attributes and methods from GUI Main file
        self.setupUi(MainWindow)  # calls setup function from GUI file to build GUI
        # adding Plots into Graphics Widget: HeartratePlot,SPO2Plot,AF_ETCO2_Plot:
        self.heartrate_curve_back = pg.PlotDataItem()
        self.heartrate_curve_front = pg.PlotDataItem()
        self.HeartratePlot.addItem(self.heartrate_curve_back)
        self.HeartratePlot.addItem(self.heartrate_curve_front)

        # init Thread for to update the header
        self.Header = GUI_HEADER()
        self.Header_Thread = QThread()
        self.Header.moveToThread(self.Header_Thread)
        self.Header.send_current_time_Signal.connect(self.Clock.setText, Qt.QueuedConnection)
        self.Header.send_StopWatch_Signal.connect(self.Stopwatch.setText, Qt.QueuedConnection)
        self.Header.send_date_Signal.connect(self.Date.setText, Qt.QueuedConnection)
        self.Header_Thread.started.connect(self.Header.update)
        self.Header_Thread.start()

        # init Thread for the number fields:
        self.NumberFields = GUI_NUMBERFIELDS()
        self.NumberFields_Thread = QThread()
        self.NumberFields.moveToThread(self.NumberFields_Thread)
        self.NumberFields.send_AF_Signal.connect(self.AF_value.setText, Qt.QueuedConnection)
        self.NumberFields.send_SPO2_Signal.connect(self.SPO2_value.setText, Qt.QueuedConnection)
        self.NumberFields.send_ETCO2_Signal.connect(self.ETCO2_value.setText, Qt.QueuedConnection)
        self.NumberFields.send_heartrate_Signal.connect(self.heartrate_value.setText, Qt.QueuedConnection)
        self.NumberFields_Thread.started.connect(self.NumberFields.update)
        self.NumberFields_Thread.start()

        # init Thread to update Plots:
        self.PlotFields = GUI_PLOTS()
        self.PlotFields_Thread = QThread()
        self.PlotFields.moveToThread(self.PlotFields_Thread)
        self.PlotFields.send_Plot_x_Range.connect(self.HeartratePlot.setXRange, Qt.QueuedConnection)
        self.PlotFields.send_heartratePlot_Signal.connect(self.heartrate_curve_back.setData, Qt.QueuedConnection)
        self.PlotFields.send_heartratePlot_front_Signal.connect(self.heartrate_curve_front.setData, Qt.QueuedConnection)
        self.PlotFields_Thread.started.connect(self.PlotFields.update)
        self.PlotFields_Thread.start()

        #
        QApplication.sendPostedEvents()
        QApplication.processEvents()


class GUI_HEADER(QObject):
    send_current_time_Signal = pyqtSignal(str)  # init QThread Signal to send updated value for the Clock
    send_StopWatch_Signal = pyqtSignal(str)  # init QThread Signal to send updated value for the StopWatch
    send_date_Signal = pyqtSignal(str)  # init QThread Signal to send updated date to the GUI

    def __init__(self):
        super().__init__()
        self.time = datetime
        self.start_time = time.time()

    def update(self):
        # sends the date to the GUI
        self.send_date_Signal.emit(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">{date}</span></p></body></html>").format(date=self.time.now().date().today().strftime('%d.%m.%y')))
        while True: # init updating loop for the Clock and StopWatch of the GUI
            # Enable time convertion for stop watch:
            sec = time.time() - self.start_time
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            mins = mins % 60
            # sends current values for Clock and Stop watch to the GUI
            self.send_current_time_Signal.emit(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">{time}</span></p></body></html>".format(time=self.time.now().strftime("%H:%M:%S"))))
            self.send_StopWatch_Signal.emit(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">{:0>2}:{:0>2}:{:0>2}</span></p></body></html>".format(int(hours), int(mins), int(sec))))
            QApplication.sendPostedEvents()
            QApplication.processEvents()
            QThread.msleep(500)  # ms


class GUI_NUMBERFIELDS(QObject):
    send_heartrate_Signal = pyqtSignal(str)
    send_SPO2_Signal = pyqtSignal(str)
    send_ETCO2_Signal = pyqtSignal(str)
    send_AF_Signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.y = 0

    def update(self):
        while True:
            self.y = randint(1,100)  # generates Test Signal
            self.send_heartrate_Signal.emit(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">{heartrate}</span></p></body></html>".format(heartrate=self.y)))
            self.send_SPO2_Signal.emit(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffff00;\">{SPO2}</span></p></body></html>".format(SPO2=self.y)))
            self.send_AF_Signal.emit(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55ff7f;\">{AF}</span></p></body></html>".format(AF=self.y)))
            self.send_ETCO2_Signal.emit(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">{ETCO2}</span></p></body></html>".format(ETCO2=self.y)))
            QThread.msleep(500)


class GUI_PLOTS(QObject):

    send_heartratePlot_Signal = pyqtSignal(numpy.ndarray, numpy.ndarray)
    send_heartratePlot_front_Signal = pyqtSignal(numpy.ndarray, numpy.ndarray)
    send_AF_ETCO2_Plot_Signal = pyqtSignal(numpy.ndarray)
    send_SPO2Plot_Signal = pyqtSignal(numpy.ndarray)
    send_Plot_x_Range = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.x_axis_Data = np.zeros(401)
        self.Heartrate_Data_new_y = np.zeros(401)
        self.datapoint = 200
        self.x_axis_Data = np.arange(0, 401, 1)  # x Data

    def update(self):
        while True:
            if self.datapoint <= 400:
                self.Heartrate_Data_new_y[self.datapoint] = 100*np.cos(self.datapoint/10)  # y-Data generate dummy Signal
                self.datapoint += 1
            else:
                self.datapoint = 0

            self.send_heartratePlot_Signal.emit(self.x_axis_Data[0:self.datapoint], self.Heartrate_Data_new_y[0:self.datapoint])
            self.send_heartratePlot_front_Signal.emit(self.x_axis_Data[self.datapoint + 2:-1], self.Heartrate_Data_new_y[self.datapoint + 2:-1])
            self.send_Plot_x_Range.emit(0, 401)  # TODO: Why does it have to be in the Loop ?
            QThread.msleep(10)  # refresh Time




