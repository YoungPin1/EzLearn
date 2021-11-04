from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox, QFileDialog

import add_module
import learn_bhpy
import learn_cardspy
import main_windowpy
import query_db
import table


class MainLearn(QMainWindow):
    def __init__(self, module_id=''):
        super().__init__()
        uic.loadUi('../Designs/learn_main.ui', self)
        self.logged_user_id, self.module_name = query_db.Database().get_name_id(module_id)[0]
        self.module_id = module_id
        self.db_words = query_db.Database().words_from_db(self.module_id)
        self.init_ui()
        self.run()

    def init_ui(self):
        table.create_table(self)
        self.tbl_wdt.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lbl_name.setText(self.module_name)
        self.count_progress()

    def count_progress(self):
        all_words = query_db.Database().get_progress(self.module_id)
        total = [float(i[2] / 2) for i in all_words]
        if len(all_words) != 0:
            self.prbar.setValue((sum(total) / len(all_words)) * 100)

    def run(self):
        self.btn_exit.clicked.connect(self.back_to_main)
        self.fill_table(self.db_words)
        self.btn_edit.clicked.connect(self.edit)
        self.btn_download.clicked.connect(self.download)
        self.btn_delete.clicked.connect(self.detele_message)
        self.btn_cards.clicked.connect(self.cards)
        self.btn_learbh.clicked.connect(self.by_hard)
        self.btn_reset.clicked.connect(self.reset)

    def reset(self):
        query_db.Database().reset_progress(self.module_id)
        self.count_progress()

    def fill_table(self, reader):
        self.tbl_wdt.setColumnCount(2)
        self.tbl_wdt.setRowCount(len(reader))
        for i in range(len(reader)):
            for j in range(2):
                self.tbl_wdt.setItem(i, j, QTableWidgetItem(reader[i][j]))

    def by_hard(self):
        self.cards_window = learn_bhpy.ByHeart(module_id=self.module_id)
        self.hide()
        self.cards_window.show()

    def back_to_main(self):
        self.main_window = main_windowpy.EzMain(self.logged_user_id)
        self.hide()
        self.main_window.show()

    def detele_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Модуль будет удален без возможности восстановления\n"
                        "Вы точно хотите выйти?")
        msg_box.setWindowTitle('Сообщение')
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.delete_module(self.module_id)

    def delete_module(self, module_id):
        query_db.Database().delete(module_id)
        self.back_to_main()

    def edit(self):
        self.edit_window = add_module.AddModule(self.logged_user_id, module_words=self.db_words,
                                                module_id=self.module_id, module_name=self.module_name)
        self.hide()
        self.edit_window.show()

    def download(self):
        table_dir = QFileDialog.getSaveFileName(self, "Сохранить файл", "", ".csv")[0]
        with open(table_dir, mode='w', encoding='utf8') as file:
            for i in range(self.tbl_wdt.rowCount()):
                row = []
                for j in range(self.tbl_wdt.columnCount()):
                    item = self.tbl_wdt.item(i, j)
                    if item is not None:
                        row.append(item.text())
                file.write(';'.join(row) + '\n')
        self.download_message()

    def download_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Модуль успещно сохранен")
        msg_box.setWindowTitle('Сообщение')
        msg_box.setStandardButtons(QMessageBox.Ok)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            msg_box.done(1)

    def show_warning(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("После редактирования прогресс будет сброшен\n"
                        "Вы точно хотите изменить модуль?")
        msg_box.setWindowTitle('Сообщение')
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.edit()

    def cards(self):
        self.cards_window = learn_cardspy.Cards(module_id=self.module_id)
        self.hide()
        self.cards_window.show()
