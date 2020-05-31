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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Users/Administrator/.designer/backup/flutter.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.chooseDirBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chooseDirBtn.setObjectName("chooseDirBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chooseDirBtn)
        self.replaceContentBtn = QtWidgets.QPushButton(self.centralwidget)
        self.replaceContentBtn.setObjectName("replaceContentBtn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.replaceContentBtn)
        self.copykeytoandroidDir = QtWidgets.QPushButton(self.centralwidget)
        self.copykeytoandroidDir.setObjectName("copykeytoandroidDir")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.copykeytoandroidDir)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 85, 0)")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        self.chooseDirBtn.clicked.connect(MainWindow.chooseRootDir)
        self.replaceContentBtn.clicked.connect(MainWindow.replaceContent)
        self.copykeytoandroidDir.clicked.connect(MainWindow.copykeytoandroiddir)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "flutter打包发布部分自动配置"))
        self.label_2.setText(_translate("MainWindow", "路径:"))
        self.chooseDirBtn.setText(_translate("MainWindow", "选择项目文件夹..."))
        self.replaceContentBtn.setText(_translate("MainWindow", "替换内容"))
        self.copykeytoandroidDir.setText(_translate("MainWindow", "复制key到android文件夹"))
        self.label_3.setText(_translate("MainWindow", "按顺序执行上边的操作,之后到pubspect.yaml配置 图标,splash,之后,项目(打开android项目,下载gradle等,不需要更新gradle.此步骤不做也可以)执行命令:flutter build apk "))
        self.label_4.setText(_translate("MainWindow", "flutter packages pub run flutter_launcher_icons:main\n"
"####    启动页\n"
"[flutter_native_splash](https://pub.dev/packages/flutter_native_splash)"))
        self.menuabout.setTitle(_translate("MainWindow", "about"))
