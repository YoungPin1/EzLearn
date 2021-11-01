import sqlite3

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

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

    def init_UI(self):
        table.create_table(self)
        self.lbl_name.setText(self.module_name)

    def run(self):
        self.btn_exit.clicked.connect(self.back_to_main)
        self.fill_table(self.words_from_db())

    def fill_table(self, list_of_words):
        pass
        print(list_of_words)
        # for i, row in enumerate(list_of_words):
        #     self.tbl_wdt.setRowCount(
        #         self.tbl_wdt.rowCount() + 1)
        #     for j, elem in enumerate(row):
        #         self.tbl_wdt.setItem(
        #             i, j, QTableWidgetItem(elem))

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
