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

"""
UNIVARIATE
"""
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt


qtcreator_file  = "main-window.ui" # Enter file GUI here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.action_Exit.clicked.connect(self.ExitApp)

    def ExitApp(self):
        sys.exit()

    def CalcUnivariate(self):
        df1 = pd.read_excel(r'D:\S3 Jhu_nee\Research\Project 5_Statistical Process Control\Final Data 3\DataProcessed10.xlsx')
        df2 = pd.read_excel(r'D:\S3 Jhu_nee\Research\Project 5_Statistical Process Control\Final Data 3\DataProcessed11.xlsx')
        all_df_list = [df2 , df1]
        data = pd.concat (all_df_list)
        var = []
        mean = []
        var1 = []
        mu1 = []
        stdev1 = []
        ucl = []
        lcl = []
        center = []
        variablelist = ['Y1_1','Y1_2','Y2_1','Y2_2','Y3','Y4']
        x = 0
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
