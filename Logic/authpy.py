from PyQt5.QtWidgets import QMainWindow

import main_windowpy
import query_db
from Designs.design_authorization import Ui_MainWindow
from constants import *


class Authorization(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run()

    def run(self):
        self.btn_login.clicked.connect(self.login)
        self.btn_sign_up.clicked.connect(self.sign_up)

    def login(self):
        login_inp, pswd_inp = self.ledit_login.text(), self.ledit_pswd.text()
        user_data_from_db = query_db.Database().get_log_pswd_db(login_inp)
        check_inp = self.check_login_pswd(login_inp, pswd_inp, origin=SIGN_IN, db_log_pswd=user_data_from_db)
        if check_inp == OK:
            query_db.Database().save_user_id(login_inp, pswd_inp)
            self.next_window(login_inp, pswd_inp)
        else:
            self.statusBar().showMessage(check_inp)

    def sign_up(self):
        login_inp, pswd_inp = self.ledit_login.text(), self.ledit_pswd.text()
        user_data_from_db, check_inp = query_db.Database().get_log_pswd_db(login_inp), self.check_login_pswd(login_inp,
                                                                                                             pswd_inp)
        if check_inp == OK:
            if user_data_from_db is None:
                query_db.Database().insert_to_db(login_inp, pswd_inp)
                self.next_window(login_inp, pswd_inp)
            else:
                self.statusBar().showMessage(USER_EXISTS)
        else:
            self.statusBar().showMessage(check_inp)

    def next_window(self, login_inp, pswd_inp):
        logged_user_id = query_db.Database().save_user_id(login_inp, pswd_inp)
        self.main_window = main_windowpy.EzMain(logged_user_id)
        self.hide()
        self.main_window.show()

    def check_login_pswd(self, login_inp, pswd_inp, origin=SIGN_UP, db_log_pswd=None):
        try:
            if len(login_inp) == 0:
                raise Exception(ENTER_LOGIN)
            elif origin == SIGN_IN and db_log_pswd is None:
                raise Exception(USER_DOES_NOT_EXIST)
            elif len(pswd_inp) == 0:
                raise Exception(ENTER_PASSWORD)
            elif origin == SIGN_IN and pswd_inp != str(db_log_pswd[2]):
                raise Exception(WROGN_PASSWORD)
            else:
                raise Exception(OK)
        except Exception as error:
            return str(error)
