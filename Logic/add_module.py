import csv

from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox, QMainWindow, QTableWidgetItem

import learn_mainpy
import main_windowpy
import query_db
import table
from constants import *


class AddModule(QMainWindow):
    def __init__(self, logged_user_id, module_words='None', module_id='None', module_name='None'):
        super().__init__()
        uic.loadUi('../Designs/add_module.ui', self)
        self.logged_user_id = int(logged_user_id)
        self.module_id = module_id
        self.module_words = module_words
        self.module_name = module_name
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
        if self.module_id != 'None':
            self.change_ui()
            self.table_data(self.module_words)

    def change_ui(self):
        self.lbl_create.setText('Редактировать учебный модуль')
        self.ledit_name.setText(self.module_name)

    def table_data(self, module_words):
        self.tbl_wdt.setRowCount(len(module_words))
        for i in range(len(module_words)):
            for j in range(2):
                self.tbl_wdt.setItem(i, j, QTableWidgetItem(module_words[i][j]))

    def back_to_main(self):
        self.main_window = main_windowpy.EzMain(self.logged_user_id)
        self.hide()
        self.main_window.show()

    def message_show(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Все ваши данные не будут сохранены\n"
                        "Вы точно хотите выйти?")
        msg_box.setWindowTitle('Сообщение')
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.back_to_main()

    def sucsess_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Модуль успешно сохранен\n"
                        "Возвращаю на главную страницу")
        msg_box.setWindowTitle('Сообщение')
        msg_box.setStandardButtons(QMessageBox.Ok)
        exit_value = msg_box.exec()
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
            with open(IMPORT_MODULE_DIR, mode='w', encoding="utf8") as csvfile:
                for i in file.readlines():
                    line = i.replace(quote, '"').strip().split(delim)
                    csvfile.write(';'.join(line) + '\n')

    def import_table(self):
        self.transform_to_csv()
        with open(IMPORT_MODULE_DIR, mode='r', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for i, row in enumerate(reader):
                self.tbl_wdt.setRowCount(
                    self.tbl_wdt.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tbl_wdt.setItem(
                        i, j, QTableWidgetItem(elem))

    def save_table(self):
        all_words = []
        for i in range(self.tbl_wdt.rowCount()):
            row = []
            for j in range(self.tbl_wdt.columnCount()):
                item = self.tbl_wdt.item(i, j)
                if item is not None:
                    row.append(str(item.text()))
            all_words.append(row)
        if len(all_words) > 4:
            module_id = query_db.Database().create_db_table(self.logged_user_id, self.ledit_name.text())
            for row in all_words:
                query_db.Database().add_row_to_db(row, module_id)
            self.sucsess_message()
        else:
            self.statusBar().showMessage('Введите слова более 4 слов')
