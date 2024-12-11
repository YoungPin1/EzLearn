# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/young_cucumber/Desktop/help/main_window.ui'
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
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scroll_ar = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_ar.setGeometry(QtCore.QRect(50, 50, 700, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_ar.sizePolicy().hasHeightForWidth())
        self.scroll_ar.setSizePolicy(sizePolicy)
        self.scroll_ar.setMinimumSize(QtCore.QSize(230, 120))
        self.scroll_ar.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scroll_ar.setWidgetResizable(True)
        self.scroll_ar.setObjectName("scroll_ar")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 698, 398))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scroll_ar.setWidget(self.scrollAreaWidgetContents_2)
        self.lbl_last = QtWidgets.QLabel(self.centralwidget)
        self.lbl_last.setGeometry(QtCore.QRect(30, 10, 211, 21))
        self.lbl_last.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.lbl_last.setObjectName("lbl_last")
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(30, 480, 251, 41))
        self.btn_create.setStyleSheet("background-color: rgb(242, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btn_create.setObjectName("btn_create")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_exit_acc = QtWidgets.QAction(MainWindow)
        self.action_exit_acc.setObjectName("action_exit_acc")
        self.action_exit_app = QtWidgets.QAction(MainWindow)
        self.action_exit_app.setObjectName("action_exit_app")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EzLearn - Учите и Запоминайте"))
        self.lbl_last.setText(_translate("MainWindow", "Модули"))
        self.btn_create.setText(_translate("MainWindow", "Создать новый модуль"))
        self.action_exit_acc.setText(_translate("MainWindow", "Выйти из аккаунта"))
        self.action_exit_app.setText(_translate("MainWindow", "Выйти из приложения"))
