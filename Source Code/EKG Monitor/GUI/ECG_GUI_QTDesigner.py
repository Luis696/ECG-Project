# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/ECG_GUI_QTDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1335, 940)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Date = QtWidgets.QLabel(self.headerFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Date.setFont(font)
        self.Date.setObjectName("Date")
        self.horizontalLayout_5.addWidget(self.Date)
        self.Stopwatch = QtWidgets.QLabel(self.headerFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Stopwatch.setFont(font)
        self.Stopwatch.setObjectName("Stopwatch")
        self.horizontalLayout_5.addWidget(self.Stopwatch)
        self.Clock = QtWidgets.QLabel(self.headerFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Clock.setFont(font)
        self.Clock.setObjectName("Clock")
        self.horizontalLayout_5.addWidget(self.Clock)
        self.verticalLayout.addWidget(self.headerFrame)
        self.MiddleFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.MiddleFrame.sizePolicy().hasHeightForWidth())
        self.MiddleFrame.setSizePolicy(sizePolicy)
        self.MiddleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MiddleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MiddleFrame.setObjectName("MiddleFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.MiddleFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PlotFrame = QtWidgets.QFrame(self.MiddleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotFrame.sizePolicy().hasHeightForWidth())
        self.PlotFrame.setSizePolicy(sizePolicy)
        self.PlotFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PlotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlotFrame.setObjectName("PlotFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PlotFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.PlotFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.HeartratePlot = PlotWidget(self.frame)
        self.HeartratePlot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HeartratePlot.setObjectName("HeartratePlot")
        self.verticalLayout_15.addWidget(self.HeartratePlot)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.PlotFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.AF_ETCO2_Plot = PlotWidget(self.frame_3)
        self.AF_ETCO2_Plot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AF_ETCO2_Plot.setObjectName("AF_ETCO2_Plot")
        self.verticalLayout_17.addWidget(self.AF_ETCO2_Plot)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.PlotFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.SPO2Plot = PlotWidget(self.frame_2)
        self.SPO2Plot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SPO2Plot.setObjectName("SPO2Plot")
        self.verticalLayout_16.addWidget(self.SPO2Plot)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.PlotFrame)
        self.number_frame = QtWidgets.QFrame(self.MiddleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_frame.sizePolicy().hasHeightForWidth())
        self.number_frame.setSizePolicy(sizePolicy)
        self.number_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.number_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.number_frame.setObjectName("number_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.number_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.heartrate_frame = QtWidgets.QFrame(self.number_frame)
        self.heartrate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.heartrate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.heartrate_frame.setObjectName("heartrate_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.heartrate_frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.heartrate_header = QtWidgets.QLabel(self.heartrate_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.heartrate_header.sizePolicy().hasHeightForWidth())
        self.heartrate_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.heartrate_header.setFont(font)
        self.heartrate_header.setAutoFillBackground(False)
        self.heartrate_header.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.heartrate_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.heartrate_header.setObjectName("heartrate_header")
        self.verticalLayout_12.addWidget(self.heartrate_header)
        self.heartrate_value = QtWidgets.QLabel(self.heartrate_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.heartrate_value.sizePolicy().hasHeightForWidth())
        self.heartrate_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(67)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.heartrate_value.setFont(font)
        self.heartrate_value.setAutoFillBackground(False)
        self.heartrate_value.setObjectName("heartrate_value")
        self.verticalLayout_12.addWidget(self.heartrate_value)
        self.verticalLayout_4.addWidget(self.heartrate_frame)
        self.AF_ETCO_Frame = QtWidgets.QFrame(self.number_frame)
        self.AF_ETCO_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AF_ETCO_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AF_ETCO_Frame.setObjectName("AF_ETCO_Frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.AF_ETCO_Frame)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.AF_Frame = QtWidgets.QFrame(self.AF_ETCO_Frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.AF_Frame.setFont(font)
        self.AF_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AF_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AF_Frame.setObjectName("AF_Frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.AF_Frame)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.AF_header = QtWidgets.QLabel(self.AF_Frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AF_header.setFont(font)
        self.AF_header.setAutoFillBackground(False)
        self.AF_header.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.AF_header.setObjectName("AF_header")
        self.verticalLayout_13.addWidget(self.AF_header)
        self.AF_value = QtWidgets.QLabel(self.AF_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AF_value.sizePolicy().hasHeightForWidth())
        self.AF_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AF_value.setFont(font)
        self.AF_value.setAutoFillBackground(False)
        self.AF_value.setObjectName("AF_value")
        self.verticalLayout_13.addWidget(self.AF_value)
        self.verticalLayout_11.addWidget(self.AF_Frame)
        self.ETCO2_Frame = QtWidgets.QFrame(self.AF_ETCO_Frame)
        self.ETCO2_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ETCO2_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ETCO2_Frame.setObjectName("ETCO2_Frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.ETCO2_Frame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.ETCO2_header = QtWidgets.QLabel(self.ETCO2_Frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ETCO2_header.setFont(font)
        self.ETCO2_header.setAutoFillBackground(False)
        self.ETCO2_header.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.ETCO2_header.setObjectName("ETCO2_header")
        self.verticalLayout_14.addWidget(self.ETCO2_header)
        self.ETCO2_value = QtWidgets.QLabel(self.ETCO2_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.ETCO2_value.sizePolicy().hasHeightForWidth())
        self.ETCO2_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ETCO2_value.setFont(font)
        self.ETCO2_value.setAutoFillBackground(False)
        self.ETCO2_value.setObjectName("ETCO2_value")
        self.verticalLayout_14.addWidget(self.ETCO2_value)
        self.verticalLayout_11.addWidget(self.ETCO2_Frame)
        self.verticalLayout_4.addWidget(self.AF_ETCO_Frame)
        self.SPO2_Frame = QtWidgets.QFrame(self.number_frame)
        self.SPO2_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SPO2_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SPO2_Frame.setObjectName("SPO2_Frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.SPO2_Frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.SPO2_header_frame = QtWidgets.QFrame(self.SPO2_Frame)
        self.SPO2_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SPO2_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SPO2_header_frame.setObjectName("SPO2_header_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SPO2_header_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SPO2_header = QtWidgets.QLabel(self.SPO2_header_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SPO2_header.setFont(font)
        self.SPO2_header.setAutoFillBackground(False)
        self.SPO2_header.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SPO2_header.setObjectName("SPO2_header")
        self.verticalLayout_9.addWidget(self.SPO2_header)
        self.verticalLayout_7.addWidget(self.SPO2_header_frame)
        self.SPO2_footer_frame = QtWidgets.QFrame(self.SPO2_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.SPO2_footer_frame.sizePolicy().hasHeightForWidth())
        self.SPO2_footer_frame.setSizePolicy(sizePolicy)
        self.SPO2_footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SPO2_footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SPO2_footer_frame.setObjectName("SPO2_footer_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.SPO2_footer_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.SPO2_value_frame = QtWidgets.QFrame(self.SPO2_footer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPO2_value_frame.sizePolicy().hasHeightForWidth())
        self.SPO2_value_frame.setSizePolicy(sizePolicy)
        self.SPO2_value_frame.setAutoFillBackground(False)
        self.SPO2_value_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SPO2_value_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SPO2_value_frame.setObjectName("SPO2_value_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.SPO2_value_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.SPO2_value = QtWidgets.QLabel(self.SPO2_value_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPO2_value.sizePolicy().hasHeightForWidth())
        self.SPO2_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(71)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SPO2_value.setFont(font)
        self.SPO2_value.setAutoFillBackground(False)
        self.SPO2_value.setAlignment(QtCore.Qt.AlignCenter)
        self.SPO2_value.setObjectName("SPO2_value")
        self.verticalLayout_10.addWidget(self.SPO2_value)
        self.horizontalLayout_6.addWidget(self.SPO2_value_frame)
        self.statusbar_frame = QtWidgets.QFrame(self.SPO2_footer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar_frame.sizePolicy().hasHeightForWidth())
        self.statusbar_frame.setSizePolicy(sizePolicy)
        self.statusbar_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.statusbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusbar_frame.setObjectName("statusbar_frame")
        self.SPO2_status_bar = QtWidgets.QProgressBar(self.statusbar_frame)
        self.SPO2_status_bar.setGeometry(QtCore.QRect(20, 20, 21, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.SPO2_status_bar.setFont(font)
        self.SPO2_status_bar.setStyleSheet("selection-background-color: rgb(255, 255, 0);\n"
"gridline-color: rgb(255, 255, 0);\n"
"")
        self.SPO2_status_bar.setProperty("value", 24)
        self.SPO2_status_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.SPO2_status_bar.setOrientation(QtCore.Qt.Vertical)
        self.SPO2_status_bar.setInvertedAppearance(False)
        self.SPO2_status_bar.setObjectName("SPO2_status_bar")
        self.horizontalLayout_6.addWidget(self.statusbar_frame)
        self.verticalLayout_7.addWidget(self.SPO2_footer_frame)
        self.verticalLayout_4.addWidget(self.SPO2_Frame)
        self.horizontalLayout_4.addWidget(self.number_frame)
        self.verticalLayout.addWidget(self.MiddleFrame)
        self.footer_Frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.footer_Frame.sizePolicy().hasHeightForWidth())
        self.footer_Frame.setSizePolicy(sizePolicy)
        self.footer_Frame.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.footer_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_Frame.setObjectName("footer_Frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer_Frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.footer_frame_1 = QtWidgets.QFrame(self.footer_Frame)
        self.footer_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame_1.setObjectName("footer_frame_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.footer_frame_1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addWidget(self.footer_frame_1)
        self.footer_frame_2 = QtWidgets.QFrame(self.footer_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer_frame_2.sizePolicy().hasHeightForWidth())
        self.footer_frame_2.setSizePolicy(sizePolicy)
        self.footer_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame_2.setObjectName("footer_frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footer_frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.footer_frame_2)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.footer_frame_2)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.footer_frame_2)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayout.addWidget(self.footer_frame_2)
        self.footer_frame_3 = QtWidgets.QFrame(self.footer_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer_frame_3.sizePolicy().hasHeightForWidth())
        self.footer_frame_3.setSizePolicy(sizePolicy)
        self.footer_frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame_3.setObjectName("footer_frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.footer_frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.foot_frame_3_check = QtWidgets.QFrame(self.footer_frame_3)
        self.foot_frame_3_check.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foot_frame_3_check.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot_frame_3_check.setObjectName("foot_frame_3_check")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.foot_frame_3_check)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.heartrate_CheckBox = QtWidgets.QCheckBox(self.foot_frame_3_check)
        self.heartrate_CheckBox.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.heartrate_CheckBox.setChecked(True)
        self.heartrate_CheckBox.setObjectName("heartrate_CheckBox")
        self.horizontalLayout_3.addWidget(self.heartrate_CheckBox)
        self.AF_CheckBox = QtWidgets.QCheckBox(self.foot_frame_3_check)
        self.AF_CheckBox.setChecked(True)
        self.AF_CheckBox.setObjectName("AF_CheckBox")
        self.horizontalLayout_3.addWidget(self.AF_CheckBox)
        self.ETCO2_CheckBox = QtWidgets.QCheckBox(self.foot_frame_3_check)
        self.ETCO2_CheckBox.setChecked(True)
        self.ETCO2_CheckBox.setObjectName("ETCO2_CheckBox")
        self.horizontalLayout_3.addWidget(self.ETCO2_CheckBox)
        self.SPO2_CheckBox = QtWidgets.QCheckBox(self.foot_frame_3_check)
        self.SPO2_CheckBox.setChecked(True)
        self.SPO2_CheckBox.setObjectName("SPO2_CheckBox")
        self.horizontalLayout_3.addWidget(self.SPO2_CheckBox)
        self.verticalLayout_5.addWidget(self.foot_frame_3_check)
        self.foot_frame_3_slider = QtWidgets.QFrame(self.footer_frame_3)
        self.foot_frame_3_slider.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foot_frame_3_slider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot_frame_3_slider.setObjectName("foot_frame_3_slider")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.foot_frame_3_slider)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.foot_frame_3_slider)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.x_Axis_Slider = QtWidgets.QSlider(self.frame_4)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.x_Axis_Slider.setFont(font)
        self.x_Axis_Slider.setMinimum(401)
        self.x_Axis_Slider.setMaximum(800)
        self.x_Axis_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.x_Axis_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.x_Axis_Slider.setObjectName("x_Axis_Slider")
        self.verticalLayout_8.addWidget(self.x_Axis_Slider)
        self.y_Axis_Slider = QtWidgets.QSlider(self.frame_4)
        self.y_Axis_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.y_Axis_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.y_Axis_Slider.setTickInterval(1)
        self.y_Axis_Slider.setObjectName("y_Axis_Slider")
        self.verticalLayout_8.addWidget(self.y_Axis_Slider)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.foot_frame_3_slider)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.x_Axis_Slider_value = QtWidgets.QLCDNumber(self.frame_5)
        self.x_Axis_Slider_value.setObjectName("x_Axis_Slider_value")
        self.verticalLayout_18.addWidget(self.x_Axis_Slider_value)
        self.y_Axis_Slider_value = QtWidgets.QLCDNumber(self.frame_5)
        self.y_Axis_Slider_value.setObjectName("y_Axis_Slider_value")
        self.verticalLayout_18.addWidget(self.y_Axis_Slider_value)
        self.horizontalLayout_7.addWidget(self.frame_5)
        self.verticalLayout_5.addWidget(self.foot_frame_3_slider)
        self.horizontalLayout.addWidget(self.footer_frame_3)
        self.footer_frame_4 = QtWidgets.QFrame(self.footer_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer_frame_4.sizePolicy().hasHeightForWidth())
        self.footer_frame_4.setSizePolicy(sizePolicy)
        self.footer_frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.footer_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame_4.setObjectName("footer_frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.footer_frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dial = QtWidgets.QDial(self.footer_frame_4)
        self.dial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        self.dial.setSizeIncrement(QtCore.QSize(0, 0))
        self.dial.setObjectName("dial")
        self.verticalLayout_6.addWidget(self.dial)
        self.horizontalLayout.addWidget(self.footer_frame_4)
        self.verticalLayout.addWidget(self.footer_Frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1335, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Date.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">05/02/2023</span></p></body></html>"))
        self.Stopwatch.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">00:00:00</span></p></body></html>"))
        self.Clock.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">19:24</span></p></body></html>"))
        self.heartrate_header.setText(_translate("MainWindow", "HF:"))
        self.heartrate_value.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">--</span></p></body></html>"))
        self.AF_header.setText(_translate("MainWindow", "AF:"))
        self.AF_value.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55ff7f;\">--</span></p></body></html>"))
        self.ETCO2_header.setText(_translate("MainWindow", "EtCO2mmHg:"))
        self.ETCO2_value.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">--</span></p></body></html>"))
        self.SPO2_header.setText(_translate("MainWindow", "SpO2 :"))
        self.SPO2_value.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffff00;\">--</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.heartrate_CheckBox.setText(_translate("MainWindow", "enable heartrate"))
        self.AF_CheckBox.setText(_translate("MainWindow", "enable AF"))
        self.ETCO2_CheckBox.setText(_translate("MainWindow", "enable ETCO2"))
        self.SPO2_CheckBox.setText(_translate("MainWindow", "enable SpO2"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
