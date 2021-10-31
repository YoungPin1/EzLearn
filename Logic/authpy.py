import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from constants import *
from main_windowpy import EzMain


class Authorization(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../Designs/authorization.ui', self)
        app.setStyle(app_style)
        self.main_window_open = EzMain()
        self.run()

    def run(self):
        self.btn_login.clicked.connect(self.login)
        self.btn_sign_up.clicked.connect(self.sign_up)

    def login(self):
        login_inp, pswd_inp = self.ledit_login.text(), self.ledit_pswd.text()
        user_data_from_db = self.get_log_pswd_db(login_inp)
        check_inp = self.check_login_pswd(login_inp, pswd_inp, origin='sign_in', db_log_pswd=user_data_from_db)
        if check_inp == 'ok':
            self.hide()
            self.main_window_open.show()
        else:
            self.statusBar().showMessage(check_inp)

    def sign_up(self):
        login_inp, pswd_inp = self.ledit_login.text(), self.ledit_pswd.text()
        user_data_from_db, check_inp = self.get_log_pswd_db(login_inp), self.check_login_pswd(login_inp, pswd_inp)
        if check_inp == 'ok':
            if user_data_from_db is None:
                self.insert_to_db(login_inp, pswd_inp)
                self.hide()
                self.main_window_open.show()
            else:
                self.statusBar().showMessage('Такой пользователь уже существует')
        else:
            self.statusBar().showMessage(check_inp)

    def get_log_pswd_db(self, login_inp):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM auth_data
         WHERE login = ? """, (login_inp,)).fetchone()
        con.close()
        return res

    def insert_to_db(self, login_inp, pswd_inp):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        cur.execute("""INSERT INTO auth_data(login, password)  
                        VALUES(?, ?)""", (login_inp, pswd_inp)).fetchall()
        con.commit()
        con.close()

    def check_login_pswd(self, login_inp, pswd_inp, origin='sign_up', db_log_pswd=None):
        try:
            if len(login_inp) == 0:
                raise Exception('Введите логин')
            elif origin == 'sign_in' and db_log_pswd is None:
                raise Exception('Такого пользователя не существует')
            elif len(pswd_inp) == 0:
                return 'Введите пароль'
            elif origin == 'sign_in' and pswd_inp != str(db_log_pswd[2]):
                raise Exception('Неправильный пароль')
            else:
                raise Exception('ok')
        except Exception as error:
            return str(error)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorization()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
