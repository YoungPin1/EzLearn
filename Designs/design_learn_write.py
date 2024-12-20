# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/young_cucumber/Desktop/help/learn_write.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_right_word = QtWidgets.QLabel(self.centralwidget)
        self.lbl_right_word.setGeometry(QtCore.QRect(100, 230, 331, 21))
        self.lbl_right_word.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.lbl_right_word.setObjectName("lbl_right_word")
        self.prbar_block = QtWidgets.QProgressBar(self.centralwidget)
        self.prbar_block.setGeometry(QtCore.QRect(340, 500, 331, 31))
        self.prbar_block.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(40, 40, 40);")
        self.prbar_block.setProperty("value", 24)
        self.prbar_block.setObjectName("prbar_block")
        self.lbl_defin = QtWidgets.QLabel(self.centralwidget)
        self.lbl_defin.setGeometry(QtCore.QRect(100, 100, 331, 21))
        self.lbl_defin.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.lbl_defin.setObjectName("lbl_defin")
        self.lbl_progress = QtWidgets.QLabel(self.centralwidget)
        self.lbl_progress.setGeometry(QtCore.QRect(110, 500, 211, 21))
        self.lbl_progress.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.lbl_progress.setObjectName("lbl_progress")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(40, 10, 40, 40))
        self.btn_exit.setStyleSheet("background-color: rgb(242, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btn_exit.setObjectName("btn_exit")
        self.ledit_defin = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_defin.setGeometry(QtCore.QRect(100, 150, 601, 41))
        self.ledit_defin.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.ledit_defin.setText("")
        self.ledit_defin.setReadOnly(True)
        self.ledit_defin.setObjectName("ledit_defin")
        self.ledit_ans = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_ans.setGeometry(QtCore.QRect(100, 280, 601, 41))
        self.ledit_ans.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.ledit_ans.setText("")
        self.ledit_ans.setReadOnly(False)
        self.ledit_ans.setObjectName("ledit_ans")
        self.btn_ans = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ans.setGeometry(QtCore.QRect(100, 400, 121, 41))
        self.btn_ans.setStyleSheet("background-color: rgb(242, 180, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btn_ans.setObjectName("btn_ans")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(580, 400, 121, 41))
        self.btn_next.setStyleSheet("background-color: rgb(242, 180, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btn_next.setObjectName("btn_next")
        self.lbl_correct = QtWidgets.QLabel(self.centralwidget)
        self.lbl_correct.setGeometry(QtCore.QRect(110, 350, 591, 31))
        self.lbl_correct.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 0);")
        self.lbl_correct.setText("")
        self.lbl_correct.setObjectName("lbl_correct")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EzLearn - Учите и Запоминайте"))
        self.lbl_right_word.setText(_translate("MainWindow", "Напишите правильный ответ"))
        self.lbl_defin.setText(_translate("MainWindow", "Опредение"))
        self.lbl_progress.setText(_translate("MainWindow", "До завершения блока"))
        self.btn_exit.setText(_translate("MainWindow", "🠔"))
        self.ledit_defin.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ledit_ans.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_ans.setText(_translate("MainWindow", "Ответить"))
        self.btn_next.setText(_translate("MainWindow", "Следующее слово"))
