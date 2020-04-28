# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frAbout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frAbout(object):
    def setupUi(self, frAbout):
        frAbout.setObjectName("frAbout")
        frAbout.resize(400, 300)
        self.label = QtWidgets.QLabel(frAbout)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 211))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnAboutOk = QtWidgets.QPushButton(frAbout)
        self.btnAboutOk.setGeometry(QtCore.QRect(160, 240, 89, 25))
        self.btnAboutOk.setObjectName("btnAboutOk")

        self.retranslateUi(frAbout)
        QtCore.QMetaObject.connectSlotsByName(frAbout)

    def retranslateUi(self, frAbout):
        _translate = QtCore.QCoreApplication.translate
        frAbout.setWindowTitle(_translate("frAbout", "About the Application"))
        self.label.setText(_translate("frAbout", "(C) 2020 \n- Created by Juni Asrini -"))
        self.btnAboutOk.setText(_translate("frAbout", "&Ok"))
