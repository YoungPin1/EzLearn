import csv
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

import main_windowpy
from constants import *
import table

class AddModule(QMainWindow):
    def __init__(self, logged_user_id):
        super().__init__()
        uic.loadUi('../Designs/add_module.ui', self)
        self.logged_user_id = int(logged_user_id)
        self.run()
        self.init_table()

    def init_table(self):
        table.create_table(self)

    def run(self):
        self.btn_import.clicked.connect(self.import_table)
        self.btn_add.clicked.connect(self.add_row)
        self.btn_del.clicked.connect(self.del_row)
        self.btn_create.clicked.connect(self.save_table)
        self.btn_exit.clicked.connect(self.message_show)

    def back_to_main(self):
        self.main_window = main_windowpy.EzMain(self.logged_user_id)
        self.hide()
        self.main_window.show()

    def message_show(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Все ваши данные не будут сохранены\n"
                       "Вы точно хотите выйти?")
        msgBox.setWindowTitle('Сообщение')
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msgBox.exec()
        if exit_value == QMessageBox.Ok:
            self.back_to_main()

    def sucsess_message(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Модуль успешно сохранен\n"
                       "Возвращаю на главную страницу")
        msgBox.setWindowTitle('Сообщение')
        msgBox.setStandardButtons(QMessageBox.Ok)
        exit_value = msgBox.exec()
        if exit_value == QMessageBox.Ok:
            self.back_to_main()

    def add_row(self):
        row_count = self.tbl_wdt.rowCount()
        self.tbl_wdt.insertRow(row_count)

    def del_row(self):
        self.tbl_wdt.removeRow(int((self.ledit_del.text())) - 1)

    def transform_to_csv(self):
        del_quo, ok_pressed = QInputDialog.getText(self, "Разделитель",
                                                   "Введите delimiter и quotechar\n"
                                                   "вашего файла через пробел")
        delim, quote = del_quo.split(' ')
        table_dir = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        with open(table_dir, mode='r', encoding='utf8') as file:
            with open(import_module_dir, mode='w', encoding="utf8") as csvfile:
                for i in file.readlines():
                    line = i.replace(quote, '"').strip().split(delim)
                    csvfile.write(';'.join(line) + '\n')

    def import_table(self):
        self.transform_to_csv()
        with open(import_module_dir, mode='r', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            print(len(title))
            self.tbl_wdt.setColumnCount(len(title))
            self.tbl_wdt.setHorizontalHeaderLabels(title)
            self.tbl_wdt.setRowCount(0)
            for i, row in enumerate(reader):
                self.tbl_wdt.setRowCount(
                    self.tbl_wdt.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tbl_wdt.setItem(
                        i, j, QTableWidgetItem(elem))

    def save_table(self):
        module_id = self.create_db_table(self.logged_user_id, self.ledit_name.text())
        for i in range(self.tbl_wdt.rowCount()):
            row = []
            for j in range(self.tbl_wdt.columnCount()):
                item = self.tbl_wdt.item(i, j)
                if item is not None:
                    row.append(item.text())
            self.add_row_to_db(row, module_id)
            self.sucsess_message()

    def create_db_table(self, logged_user_id, table_name):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        cur.execute(user_module_save_data, (logged_user_id, table_name)).fetchone()
        module_id = cur.execute(get_module_id_from_user_modules, (logged_user_id, table_name)).fetchone()[0]
        cur.execute(new_module_db.format(str(module_id))).fetchone()
        con.commit()
        con.close()
        return module_id

    def add_row_to_db(self, row, module_id):
        con = sqlite3.connect(db_location)
        cur = con.cursor()
        cur.execute(insert_row_to_db.format(str(module_id)), (str(row[0]), str(row[1]))).fetchone()
        con.commit()
        con.close()
