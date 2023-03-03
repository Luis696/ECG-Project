import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from GUI.updateGUI import*
from Backend.Sensor_read import SensorBoard
from multiprocessing import Process, Pipe

os.system("pyuic5 -x GUI/ECG_GUI_QTDesigner.ui -o GUI/ECG_GUI_QTDesigner.py")
SensorBoard = SensorBoard(name="ESP32", com_port="COM4", baude_rate=115200, num_sensors=1)
SensorBoard.set_serial_input_order(["Heartrate"])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # defines QT Application as app
    MainWindow = QtWidgets.QMainWindow()  # generates main Window
    ui = Ui_Build(MainWindow, SensorBoard)  # Builds GUI from updateGUI, connected with SensorBoard
    SensorBoard.print_properties()
    MainWindow.show()  # shows App Window
    sys.exit(app.exec_())  # if window closed, stop program

