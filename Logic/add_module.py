import csv
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class AddModule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../Designs/add_module.ui', self)
        self.run()
        self.init_table()

    def init_table(self):
        self.tbl_wdt.horizontalHeader().setStyleSheet("::section{Background-color:rgb(40,40,40)}")
        self.tbl_wdt.verticalHeader().setStyleSheet("::section{Background-color:rgb(40,40,40)}")
        self.tbl_wdt.setColumnCount(2)
        self.tbl_wdt.setHorizontalHeaderLabels(['Термин', 'Определение'])
        self.tbl_wdt.setRowCount(0)
        head_view = self.tbl_wdt.horizontalHeader()
        head_view.setSectionResizeMode(0, 1)
        head_view.setSectionResizeMode(1, 1)
        self.tbl_wdt.resizeColumnsToContents()

    def run(self):
        self.btn_import.clicked.connect(self.import_table)
        self.btn_add.clicked.connect(self.add_row)
        self.btn_del.clicked.connect(self.del_row)
        self.btn_create.clicked.connect(self.create_module)

    def create_module(self):
        with open('user_block.csv', 'w', newline='', encoding='utf8') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(
                [self.tbl_wdt.horizontalHeaderItem(i).text()
                 for i in range(self.tbl_wdt.columnCount())])
            for i in range(self.tbl_wdt.rowCount()):
                row = []
                for j in range(self.tbl_wdt.columnCount()):
                    item = self.tbl_wdt.item(i, j)
                    if item is not None:
                        row.append(item.text())
                writer.writerow(row)
    def add_row(self):
        row_count = self.tbl_wdt.rowCount()
        self.tbl_wdt.insertRow(row_count)

    def del_row(self):
        self.tbl_wdt.removeRow(int((self.ledit_del.text())) - 1)

    def import_table(self):
        del_quo, ok_pressed = QInputDialog.getText(self, "Разделитель",
                                                   "Введите delimiter и quotechar\n"
                                                   "вашего файла через пробел")
        delim, quote = del_quo.split(' ')
        table_dir = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        with open(table_dir, mode='r', encoding='utf8') as file:
            with open('block.csv', mode='w', encoding="utf8") as csvfile:
                for i in file.readlines():
                    line = i.replace(quote, '"').strip().split(delim)
                    csvfile.write(';'.join(line) + '\n')

        with open('block.csv', mode='r', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tbl_wdt.setColumnCount(len(title))
            self.tbl_wdt.setHorizontalHeaderLabels(title)
            self.tbl_wdt.setRowCount(0)
            for i, row in enumerate(reader):
                self.tbl_wdt.setRowCount(
                    self.tbl_wdt.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tbl_wdt.setItem(
                        i, j, QTableWidgetItem(elem))