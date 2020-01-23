# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OCR_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(1010, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Monitor.setWindowIcon(icon)
        Monitor.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(Monitor)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainlayerout = QtWidgets.QHBoxLayout()
        self.mainlayerout.setObjectName("mainlayerout")
        self.Control_box = QtWidgets.QVBoxLayout()
        self.Control_box.setObjectName("Control_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Remote_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Remote_label.setFont(font)
        self.Remote_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Remote_label.setObjectName("Remote_label")
        self.verticalLayout.addWidget(self.Remote_label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.IP_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.IP_entry.setObjectName("IP_entry")
        self.gridLayout.addWidget(self.IP_entry, 2, 3, 1, 1)
        self.Disconnect_cam = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Disconnect_cam.setFont(font)
        self.Disconnect_cam.setObjectName("Disconnect_cam")
        self.gridLayout.addWidget(self.Disconnect_cam, 5, 1, 1, 1)
        self.Port_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Port_entry.setObjectName("Port_entry")
        self.gridLayout.addWidget(self.Port_entry, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.Connect_cam = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Connect_cam.setFont(font)
        self.Connect_cam.setObjectName("Connect_cam")
        self.gridLayout.addWidget(self.Connect_cam, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.Run_OCR = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Run_OCR.setFont(font)
        self.Run_OCR.setObjectName("Run_OCR")
        self.gridLayout.addWidget(self.Run_OCR, 5, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.timer_output = QtWidgets.QSpinBox(self.centralwidget)
        self.timer_output.setObjectName("timer_output")
        self.gridLayout_4.addWidget(self.timer_output, 1, 1, 1, 1)
        self.run_program = QtWidgets.QPushButton(self.centralwidget)
        self.run_program.setObjectName("run_program")
        self.gridLayout_4.addWidget(self.run_program, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 1, 3, 1, 1)
        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setObjectName("test")
        self.gridLayout_4.addWidget(self.test, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.boxes = QtWidgets.QComboBox(self.centralwidget)
        self.boxes.setObjectName("boxes")
        self.gridLayout_2.addWidget(self.boxes, 1, 1, 1, 1)
        self.ChoosePDFbutton = QtWidgets.QPushButton(self.centralwidget)
        self.ChoosePDFbutton.setObjectName("ChoosePDFbutton")
        self.gridLayout_2.addWidget(self.ChoosePDFbutton, 0, 1, 1, 1)
        self.PDF_file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_file_name.setReadOnly(True)
        self.PDF_file_name.setObjectName("PDF_file_name")
        self.gridLayout_2.addWidget(self.PDF_file_name, 0, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 5, 1, 1)
        self.pdf_position_set = QtWidgets.QPushButton(self.centralwidget)
        self.pdf_position_set.setObjectName("pdf_position_set")
        self.gridLayout_2.addWidget(self.pdf_position_set, 3, 4, 1, 1)
        self.pdf_position_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pdf_position_reset.setObjectName("pdf_position_reset")
        self.gridLayout_2.addWidget(self.pdf_position_reset, 3, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.PositionX = QtWidgets.QLineEdit(self.centralwidget)
        self.PositionX.setObjectName("PositionX")
        self.gridLayout_3.addWidget(self.PositionX, 0, 1, 1, 1)
        self.PositionY = QtWidgets.QLineEdit(self.centralwidget)
        self.PositionY.setObjectName("PositionY")
        self.gridLayout_3.addWidget(self.PositionY, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.Control_box.addLayout(self.verticalLayout_2)
        self.mainlayerout.addLayout(self.Control_box)
        spacerItem10 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainlayerout.addItem(spacerItem10)
        self.horizontalLayout.addLayout(self.mainlayerout)
        Monitor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Monitor)
        self.statusbar.setObjectName("statusbar")
        Monitor.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Monitor)
        self.toolBar.setObjectName("toolBar")
        Monitor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(Monitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName("menubar")
        self.menuSet_Camera = QtWidgets.QMenu(self.menubar)
        self.menuSet_Camera.setObjectName("menuSet_Camera")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        Monitor.setMenuBar(self.menubar)
        self.actionLocal_Camera = QtWidgets.QAction(Monitor)
        self.actionLocal_Camera.setObjectName("actionLocal_Camera")
        self.actionRemote_Camera = QtWidgets.QAction(Monitor)
        self.actionRemote_Camera.setObjectName("actionRemote_Camera")
        self.actionBox_set = QtWidgets.QAction(Monitor)
        self.actionBox_set.setObjectName("actionBox_set")
        self.actionBox_manage = QtWidgets.QAction(Monitor)
        self.actionBox_manage.setObjectName("actionBox_manage")
        self.menuSet_Camera.addSeparator()
        self.menuSet_Camera.addAction(self.actionLocal_Camera)
        self.menuSet_Camera.addAction(self.actionRemote_Camera)
        self.menuSetting.addAction(self.actionBox_manage)
        self.menubar.addAction(self.menuSet_Camera.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "OCR Monitor"))
        self.Remote_label.setText(_translate("Monitor", "Remote Camera setting"))
        self.Disconnect_cam.setText(_translate("Monitor", "Disconnect"))
        self.label.setText(_translate("Monitor", "Camera IP Address:"))
        self.Connect_cam.setText(_translate("Monitor", "Connect"))
        self.label_2.setText(_translate("Monitor", "Port:"))
        self.Run_OCR.setText(_translate("Monitor", "Play/Pause"))
        self.label_3.setText(_translate("Monitor", "Output file"))
        self.label_6.setText(_translate("Monitor", "Set  digital  timer"))
        self.run_program.setText(_translate("Monitor", "Run"))
        self.test.setText(_translate("Monitor", "Server"))
        self.ChoosePDFbutton.setText(_translate("Monitor", "Choose PDF file"))
        self.pdf_position_set.setText(_translate("Monitor", "Set"))
        self.pdf_position_reset.setText(_translate("Monitor", "Reset"))
        self.label_5.setText(_translate("Monitor", "Position_Y:"))
        self.label_4.setText(_translate("Monitor", "Position_X:"))
        self.toolBar.setWindowTitle(_translate("Monitor", "toolBar"))
        self.menuSet_Camera.setTitle(_translate("Monitor", "Set Camera"))
        self.menuSetting.setTitle(_translate("Monitor", "Setting"))
        self.actionLocal_Camera.setText(_translate("Monitor", "Local Camera"))
        self.actionRemote_Camera.setText(_translate("Monitor", "Remote Camera"))
        self.actionBox_set.setText(_translate("Monitor", "Box set"))
        self.actionBox_manage.setText(_translate("Monitor", "Box manage"))
import resource.res_rc
