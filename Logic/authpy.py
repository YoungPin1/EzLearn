import sqlite3
import sys
from main_windowpy import EzMain
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

import pswd_login_check


class Authorization(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../Designs/authorization.ui', self)
        app.setStyle('Fusion')
        self.main_window_open = EzMain()
        self.run()

    def run(self):
        self.action_pswd.triggered.connect(self.show_rule_pswd)
        self.action_login.triggered.connect(self.show_rule_login)
        self.btn_login.clicked.connect(self.login)
        self.btn_sign_up.clicked.connect(self.sign_up)

    def show_rule_login(self):
        msg = QMessageBox()
        msg.setStyleSheet('background-color: rgb(40, 40, 40);'
                          'color: rgb(255, 255, 255)')
        msg.setWindowTitle('Критерии логина')
        msg.setText('1. Длина логина не менее 5 символ\n'
                    '2. Хотя бы один заглавный и один прописной символ\n'
                    '3. Не допускается использование пробела\n')
        msg.exec_()

    def show_rule_pswd(self):
        msg = QMessageBox()
        msg.setStyleSheet('background-color: rgb(40, 40, 40);'
                          'color: rgb(255, 255, 255)')
        msg.setWindowTitle('Критерии пароля')
        msg.setText('1. Длина пароля не менее 8 символ\n'
                    '2. Хотя бы один заглавный и один прописной символ\n'
                    '3. Хотя бы одна цифра\n')
        msg.exec_()

    def login(self):
        self.statusBar().setStyleSheet("color : red")
        con = sqlite3.connect('../EzLearndb.db')
        cur = con.cursor()
        login_inp = self.ledit_login.text()
        result = cur.execute("""SELECT * FROM auth_data
         WHERE login = ?""", (login_inp,)).fetchone()
        if len(login_inp) == 0:
            self.statusBar().showMessage('Введите логин')
        elif result is None:
            self.statusBar().showMessage('Такого пользователя не существует')
        else:
            password_inp = self.ledit_pswd.text()
            if len(password_inp) == 0:
                self.statusBar().showMessage('Введите пароль')
            else:
                if password_inp != str(result[2]):
                    self.statusBar().showMessage('Неправильный пароль')
                else:
                    self.statusBar().setStyleSheet("color : green")
                    self.statusBar().showMessage('Успешно!')
                    self.hide()
                    self.main_window_open.show()
        con.close()

    def sign_up(self):
        self.statusBar().setStyleSheet("color : red")
        login_inp = self.ledit_login.text()
        pswd_inp = self.ledit_pswd.text()
        check_login = pswd_login_check.login_check(login_inp)
        check_pswd = pswd_login_check.pswd_check(pswd_inp)
        if check_login != 'good':
            self.statusBar().showMessage(check_login)
        else:
            if check_pswd != 'good':
                self.statusBar().showMessage(check_pswd)
            else:
                con = sqlite3.connect('../EzLearndb.db')
                cur = con.cursor()
                result = cur.execute("""SELECT * FROM auth_data
                 WHERE login = ? and password = ?""", (login_inp, pswd_inp)).fetchone()
                if result is None:
                    cur.execute("""INSERT INTO auth_data(login, password)  
                    VALUES(?, ?)""", (login_inp, pswd_inp)).fetchall()
                    self.statusBar().setStyleSheet("color : green")
                    self.statusBar().showMessage('Успешно!')
                    con.commit()
                    con.close()
                    self.hide()
                    self.main_window_open.show()
                else:
                    self.statusBar().showMessage('Такой пользователь уже существует')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorization()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
