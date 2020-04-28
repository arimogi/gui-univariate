# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcess.setGeometry(QtCore.QRect(20, 340, 89, 25))
        self.btnProcess.setObjectName("btnProcess")
        self.btnAbout = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbout.setGeometry(QtCore.QRect(430, 340, 89, 25))
        self.btnAbout.setObjectName("btnAbout")
        self.txFile1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txFile1.setGeometry(QtCore.QRect(110, 70, 311, 25))
        self.txFile1.setObjectName("txFile1")
        self.txFile2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txFile2.setGeometry(QtCore.QRect(110, 110, 311, 25))
        self.txFile2.setObjectName("txFile2")
        self.lbTitle = QtWidgets.QLabel(self.centralwidget)
        self.lbTitle.setGeometry(QtCore.QRect(10, 10, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbTitle.setFont(font)
        self.lbTitle.setObjectName("lbTitle")
        self.lbFile1 = QtWidgets.QLabel(self.centralwidget)
        self.lbFile1.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.lbFile1.setObjectName("lbFile1")
        self.lbFile2 = QtWidgets.QLabel(self.centralwidget)
        self.lbFile2.setGeometry(QtCore.QRect(10, 110, 67, 17))
        self.lbFile2.setObjectName("lbFile2")
        self.btnBrowse1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse1.setGeometry(QtCore.QRect(430, 70, 89, 25))
        self.btnBrowse1.setObjectName("btnBrowse1")
        self.btnBrowse2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse2.setGeometry(QtCore.QRect(430, 110, 89, 25))
        self.btnBrowse2.setObjectName("btnBrowse2")
        self.txLog = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txLog.setGeometry(QtCore.QRect(10, 170, 511, 161))
        self.txLog.setObjectName("txLog")
        self.lbLog = QtWidgets.QLabel(self.centralwidget)
        self.lbLog.setGeometry(QtCore.QRect(10, 150, 91, 17))
        self.lbLog.setObjectName("lbLog")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(120, 340, 89, 25))
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open1 = QtWidgets.QAction(MainWindow)
        self.action_Open1.setObjectName("action_Open1")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Open2 = QtWidgets.QAction(MainWindow)
        self.action_Open2.setObjectName("action_Open2")
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Open1)
        self.menu_File.addAction(self.action_Open2)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application Univariate - Juni Asrini"))
        self.btnProcess.setText(_translate("MainWindow", "&Process"))
        self.btnAbout.setText(_translate("MainWindow", "&About"))
        self.lbTitle.setText(_translate("MainWindow", "Application Univariate "))
        self.lbFile1.setText(_translate("MainWindow", "File 1"))
        self.lbFile2.setText(_translate("MainWindow", "File 2"))
        self.btnBrowse1.setText(_translate("MainWindow", "Browse..."))
        self.btnBrowse2.setText(_translate("MainWindow", "Browse..."))
        self.txLog.setPlainText(_translate("MainWindow", "Log of process..."))
        self.lbLog.setText(_translate("MainWindow", "Log Process:"))
        self.btnExit.setText(_translate("MainWindow", "E&xit"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Open1.setText(_translate("MainWindow", "Open File &1"))
        self.action_Close.setText(_translate("MainWindow", "&Close Files"))
        self.action_Exit.setText(_translate("MainWindow", "E&xit"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.action_Open2.setText(_translate("MainWindow", "Open File &2"))
