import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from constants import *
import main_windowpy


class Authorization(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../Designs/authorization.ui', self)
        app.setStyle(app_style)
        self.run()

    def run(self):
        self.btn_login.clicked.connect(self.login)
        self.btn_sign_up.clicked.connect(self.sign_up)

    def login(self):
        login_inp, pswd_inp = self.ledit_login.text(), self.ledit_pswd.text()
        user_data_from_db = self.get_log_pswd_db(login_inp)
        check_inp = self.check_login_pswd(login_inp, pswd_inp, origin='sign_in', db_log_pswd=user_data_from_db)
        if check_inp == 'ok':
            self.save_user_id(login_inp, pswd_inp)
            self.next_window(login_inp, pswd_inp)
        else:
            self.statusBar().showMessage(check_inp)

    def sign_up(self):
        login_inp, pswd_inp = self.ledit_login.text(), self.ledit_pswd.text()
        user_data_from_db, check_inp = self.get_log_pswd_db(login_inp), self.check_login_pswd(login_inp, pswd_inp)
        if check_inp == 'ok':
            if user_data_from_db is None:
                self.insert_to_db(login_inp, pswd_inp)
                self.next_window(login_inp, pswd_inp)
            else:
                self.statusBar().showMessage('Такой пользователь уже существует')
        else:
            self.statusBar().showMessage(check_inp)

    def get_log_pswd_db(self, login_inp):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        res = cur.execute(only_login, (login_inp,)).fetchone()
        con.commit()
        con.close()
        return res

    def insert_to_db(self, login_inp, pswd_inp):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        cur.execute(insert_data, (login_inp, pswd_inp)).fetchall()
        self.save_user_id(login_inp, pswd_inp)
        con.commit()
        con.close()

    def save_user_id(self, login_inp, pswd_inp):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        logged_user_id = cur.execute(get_logged_user_id, (login_inp, pswd_inp)).fetchall()
        con.close()
        return logged_user_id

    def next_window(self, login_inp, pswd_inp):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        logged_user_id = cur.execute(get_logged_user_id, (login_inp, pswd_inp)).fetchone()
        con.close()
        self.main_window = main_windowpy.EzMain(logged_user_id[0])
        self.hide()
        self.main_window.show()

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
