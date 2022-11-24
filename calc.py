# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 420)
        MainWindow.setStyleSheet("background-color: rgb(215, 194, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NullButton = QtWidgets.QPushButton(self.centralwidget)
        self.NullButton.setGeometry(QtCore.QRect(0, 290, 150, 90))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.NullButton.setFont(font)
        self.NullButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.NullButton.setObjectName("NullButton")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(0, 0, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.labelResult.setFont(font)
        self.labelResult.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.labelResult.setObjectName("labelResult")
        self.ButtonResult = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonResult.setGeometry(QtCore.QRect(150, 290, 150, 90))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonResult.setFont(font)
        self.ButtonResult.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.ButtonResult.setObjectName("ButtonResult")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(0, 210, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(100, 210, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(200, 210, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.threeButton.setObjectName("threeButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(100, 130, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(0, 129, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(200, 130, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.sixButton.setObjectName("sixButton")
        self.nineButon = QtWidgets.QPushButton(self.centralwidget)
        self.nineButon.setGeometry(QtCore.QRect(200, 50, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nineButon.setFont(font)
        self.nineButon.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.nineButon.setObjectName("nineButon")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(100, 50, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(0, 50, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.sevenButton.setObjectName("sevenButton")
        self.concatBtn = QtWidgets.QPushButton(self.centralwidget)
        self.concatBtn.setGeometry(QtCore.QRect(300, 50, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.concatBtn.setFont(font)
        self.concatBtn.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.concatBtn.setObjectName("concatBtn")
        self.minusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.minusBtn.setGeometry(QtCore.QRect(300, 130, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.minusBtn.setFont(font)
        self.minusBtn.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.minusBtn.setObjectName("minusBtn")
        self.multipleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.multipleBtn.setGeometry(QtCore.QRect(300, 210, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.multipleBtn.setFont(font)
        self.multipleBtn.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.multipleBtn.setObjectName("multipleBtn")
        self.devideBtn = QtWidgets.QPushButton(self.centralwidget)
        self.devideBtn.setGeometry(QtCore.QRect(300, 290, 71, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.devideBtn.setFont(font)
        self.devideBtn.setStyleSheet("background-color: rgb(107, 166, 255);")
        self.devideBtn.setObjectName("devideBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.isEqual = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NullButton.setText(_translate("MainWindow", "0"))
        self.labelResult.setText(_translate("MainWindow", "0"))
        self.ButtonResult.setText(_translate("MainWindow", "="))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.nineButon.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.concatBtn.setText(_translate("MainWindow", "+"))
        self.minusBtn.setText(_translate("MainWindow", "-"))
        self.multipleBtn.setText(_translate("MainWindow", "*"))
        self.devideBtn.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.NullButton.clicked.connect(lambda: self.writeNumber(self.NullButton.text()))
        self.oneButton.clicked.connect(lambda: self.writeNumber(self.oneButton.text()))
        self.twoButton.clicked.connect(lambda: self.writeNumber(self.twoButton.text))
        self.threeButton.clicked.connect(lambda: self.writeNumber(self.threeButton.text()))
        self.fourButton.clicked.connect(lambda: self.writeNumber(self.fourButton.text()))
        self.fiveButton.clicked.connect(lambda: self.writeNumber(self.fiveButton.text()))
        self.sixButton.clicked.connect(lambda: self.writeNumber(self.sixButton.text()))
        self.sevenButton.clicked.connect(lambda: self.writeNumber(self.sevenButton.text()))
        self.eightButton.clicked.connect(lambda: self.writeNumber(self.eightButton.text()))
        self.nineButon.clicked.connect(lambda: self.writeNumber(self.nineButon.text()))
        self.concatBtn.clicked.connect(lambda: self.writeNumber(self.concatBtn.text()))
        self.minusBtn.clicked.connect(lambda: self.writeNumber(self.minusBtn.text()))
        self.multipleBtn.clicked.connect(lambda: self.writeNumber(self.multipleBtn.text()))
        self.devideBtn.clicked.connect(lambda: self.writeNumber(self.devideBtn.text()))

        self.ButtonResult.clicked.connect(self.results)


    def writeNumber(self, number):
        if self.labelResult.text() == "0" or self.isEqual:
            self.labelResult.setText(number)
            self.isEqual = False
        else:
            self.labelResult.setText(self.labelResult.text() + number)

    def results(self):
        if not self.isEqual:
            
            res =  eval(self.labelResult.text())
            self.labelResult.setText("Результат: " + str(res))
            self.isEqual = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.Reset|QMessageBox.Ok|QMessageBox.Cancel)
            #error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Двойное нажатие не допускается программой")
            error.buttonClicked.connect(self.popup_action)

            error.exec_()

    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("Print Ok")
        elif btn.text == "Reset":
            self.labelResult.setText("")
            self.isEqual = False




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
