# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 411, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 30, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 140, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 140, 81, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 140, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 140, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_server = QtWidgets.QLabel(self.centralwidget)
        self.label_server.setGeometry(QtCore.QRect(100, 70, 421, 16))
        self.label_server.setObjectName("label_server")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 70, 101, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(650, 70, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.pressed.connect(MainWindow.checkProject)
        self.pushButton_2.pressed.connect(MainWindow.openProject)
        self.pushButton_3.pressed.connect(MainWindow.openHotfixMessage)
        self.pushButton_4.pressed.connect(MainWindow.openInnerMessage)
        self.pushButton_5.pressed.connect(MainWindow.openOuterMessage)
        self.pushButton_6.pressed.connect(MainWindow.proto2CS)
        self.pushButton_7.pressed.connect(MainWindow.openServerProject)
        self.pushButton_8.pressed.connect(MainWindow.openServerFolder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unity项目实用工具4ET"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "选择unity项目"))
        self.label_2.setText(_translate("MainWindow", "ClientFolder:"))
        self.pushButton_2.setText(_translate("MainWindow", "打开项目"))
        self.pushButton_3.setText(_translate("MainWindow", "HotfixMessage"))
        self.pushButton_4.setText(_translate("MainWindow", "InnerMessage"))
        self.pushButton_5.setText(_translate("MainWindow", "OuterMessage"))
        self.pushButton_6.setText(_translate("MainWindow", "Proto2CS"))
        self.label_3.setText(_translate("MainWindow", "ServerFolder:"))
        self.label_server.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_7.setText(_translate("MainWindow", "选择server项目"))
        self.pushButton_8.setText(_translate("MainWindow", "打开项目"))
