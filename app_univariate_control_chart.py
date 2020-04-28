# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:38:47 2020

@author: Juni Asrini
"""

"""
GUI
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDesktopWidget, QGridLayout, QWidget, QLineEdit, QLabel, QFileDialog
from mainWindow import Ui_MainWindow
from frAbout import Ui_frAbout

"""
UNIVARIATE
"""
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt

# define the About Program
class FrAbout(QtWidgets.QMainWindow, Ui_frAbout):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_frAbout.__init__(self)
        self.ui = Ui_frAbout()
        self.ui.setupUi(self)


# define the main window
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Set MyWindow to the center of the desktop
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # set other functions
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.action_Open1.clicked.connect(self.browseFile1)
        #self.ui.action_Open2.clicked.connect(self.browseFile2)
        self.ui.btnBrowse1.clicked.connect(self.browseFile1)
        self.ui.btnBrowse2.clicked.connect(self.browseFile2)

        #self.ui.action_Close.clicked.connect(self.closeFiles)

        self.ui.btnExit.clicked.connect(self.exitApp)
        self.ui.btnProcess.clicked.connect(self.doProcess)
        self.ui.btnAbout.clicked.connect(self.openAbout)

    # Close all files
    def closeFiles(self):
        self.ui.txLog.appendPlainText('Close all files.')

    # Browse for files
    def browseFile1(self):
        self.ui.txLog.appendPlainText('Browse file 1.')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Excel files (*.xlsx)", options=options)
        if fileName:
            self.ui.txFile1.setText(fileName)
            self.df1 = fileName
            self.ui.txLog.appendPlainText('File 1: ' + fileName + ' has been selected.')

    def browseFile2(self):
        self.ui.txLog.appendPlainText('Browse file 2.')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Excel files (*.xlsx)", options=options)
        if fileName:
            self.ui.txFile2.setText(fileName)
            self.df2 = fileName
            self.ui.txLog.appendPlainText('File 2: ' + fileName + ' has been selected.')

    # Process the files
    def doProcess(self):
        self.ui.txLog.appendPlainText('Processing all files.')
        self.CalcUnivariate()

    # Exit application
    def exitApp(self):
        self.ui.txLog.appendPlainText('Exit application.')
        sys.exit()

    # Open form About
    def openAbout(self):
        frAbout = FrAbout()
        frAbout.show()

    # Univariate Functions
    def CalcUnivariate(self):
        self.ui.txLog.appendPlainText("Reading file " + self.df1 + " using panda library.")
        df1 = pd.read_excel(r'' + self.df1 + '')

        self.ui.txLog.appendPlainText("Reading file " + self.df2 + " using panda library.")
        df2 = pd.read_excel(r'' + self.df2 + '')

        all_df_list = [df2 , df1]
        data = pd.concat (all_df_list)

        var     = []
        mean    = []
        var1    = []
        mu1     = []
        stdev1  = []
        ucl     = []
        lcl     = []
        center  = []
        x       = 0

        variablelist = ['Y1_1','Y1_2','Y2_1','Y2_2','Y3','Y4']

        #"""
        for i in variablelist:
            var.append(data[[i,'subgroup']])
            mean.append(var[x].groupby('subgroup').mean()) ## mean sample by subgroup
            var1.append(data[i])
            mu1.append(stat.mean(var1[x])) ## population mean
            stdev1.append(stat.stdev(var1[x]))
            a = mu1[x]+ 3*stdev1[x]
            b = mu1[x]- 3*stdev1[x]
            ucl.append(a)
            lcl.append(b)
            center.append(stat.mean(mean[x][i]))
            mean[x].plot ()
            plt.title('X-bar Chart Variable ' + i)
            ucl1 = plt.axhline(ucl[x], linestyle = '--', color = 'r', linewidth = 2)
            ctr = plt.axhline(center[x], color = 'r', linewidth = 2)
            lcl1 = plt.axhline(lcl[x], linestyle = '--', color = 'r', linewidth = 2)
            spec = plt.axhline(0, linestyle = '--', color = 'y', linewidth = 3)
            plt.show()
            print('UCL variable ' + i, '=' , a)
            print('LCL variable ' + i, '=' , b)
            x += 1
        #"""

# call the main program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
