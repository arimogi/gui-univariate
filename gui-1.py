import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDesktopWidget, QGridLayout, QWidget, QLineEdit, QLabel, QFileDialog
from mainWindow import Ui_MainWindow
from frAbout import Ui_frAbout

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
            self.ui.txLog.appendPlainText('File 1: ' + fileName + ' has been selected.')

    def browseFile2(self):
        self.ui.txLog.appendPlainText('Browse file 2.')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Excel files (*.xlsx)", options=options)
        if fileName:
            self.ui.txFile2.setText(fileName)
            self.ui.txLog.appendPlainText('File 2: ' + fileName + ' has been selected.')

    # Process the files
    def doProcess(self):
        self.ui.txLog.appendPlainText('Processing all files.')

    # Exit application
    def exitApp(self):
        self.ui.txLog.appendPlainText('Exit application.')
        sys.exit()

    # Open form About
    def openAbout(self):
        frAbout = FrAbout()
        frAbout.show()

# call the main program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
