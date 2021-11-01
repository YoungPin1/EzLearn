import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import main_windowpy
import table
from constants import *


class MainLearn(QMainWindow):
    def __init__(self, module_id, module_name, logged_user_id):
        super().__init__()
        uic.loadUi('../Designs/learn_main.ui', self)
        self.logged_user_id = logged_user_id
        self.module_name = module_name
        self.module_id = module_id
        self.run()
        self.init_UI()

    def run(self):
        self.btn_exit.clicked.connect(self.back_to_main)
        print(self.words_from_db())

    def init_UI(self):
        table.create_table(self)
        self.lbl_name.setText(self.module_name)

    def words_from_db(self):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        words = cur.execute(get_words_from_db.format(self.module_id)).fetchall()
        con.close()
        return words

    def back_to_main(self):
        self.main_window = main_windowpy.EzMain(self.logged_user_id)
        self.hide()
        self.main_window.show()
