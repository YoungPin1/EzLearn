from PyQt5.QtWidgets import QMessageBox, QMainWindow

import main_windowpy
import query_db
import table
from Designs.design_add_module import Ui_MainWindow
from constants import *


class AddModule(QMainWindow, Ui_MainWindow):
    def __init__(self, logged_user_id):
        super().__init__()
        self.setupUi(self)
        self.logged_user_id = int(logged_user_id)
        self.run()
        self.init_table()

    def init_table(self):
        table.create_table(self)

    def run(self):
        self.btn_add.clicked.connect(self.add_row)
        self.btn_del.clicked.connect(self.del_row)
        self.btn_create.clicked.connect(self.save_table)
        self.btn_exit.clicked.connect(self.message_show)

    def change_ui(self):
        self.lbl_create.setText(EDIT_MODULE_TEXT)
        self.ledit_name.setText(self.module_name)

    def back_to_main(self):
        self.main_window = main_windowpy.EzMain(self.logged_user_id)
        self.hide()
        self.main_window.show()

    def message_show(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(DELETE_MESSAGE)
        msg_box.setWindowTitle(MESSAGE)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.back_to_main()

    def add_row(self):
        row_count = self.tbl_wdt.rowCount()
        self.tbl_wdt.insertRow(row_count)

    def del_row(self):
        if self.ledit_del.text() != '':
            self.tbl_wdt.removeRow(int((self.ledit_del.text())) - 1)

    def save_table(self):
        all_words = []
        for i in range(self.tbl_wdt.rowCount()):
            row = []
            for j in range(self.tbl_wdt.columnCount()):
                item = self.tbl_wdt.item(i, j)
                if item is not None:
                    row.append(str(item.text()))
            all_words.append(row)
        # для работы всех тестов требуется не менее 5 пар
        if len(all_words) >= 5:
            module_id = query_db.Database().create_db_table(self.logged_user_id, self.ledit_name.text())
            for row in all_words:
                query_db.Database().add_row_to_db(row, module_id)
            self.success_message()
        else:
            self.statusBar().showMessage(NO_LESS_THAN_5_WORDS)

    def success_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(SUCCESS_MESSAGE)
        msg_box.setWindowTitle(MESSAGE)
        msg_box.setStandardButtons(QMessageBox.Ok)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.back_to_main()
