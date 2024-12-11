from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox

import learn_bhpy
import learn_cardspy
import learnwritepy
import main_windowpy
import query_db
import table
from Designs.design_learn_main import Ui_MainWindow
from constants import *


class MainLearn(QMainWindow, Ui_MainWindow):
    def __init__(self, module_id=None):
        super().__init__()
        self.setupUi(self)
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

    def run(self):
        self.btn_exit.clicked.connect(self.back_to_main)
        self.fill_table(self.db_words)
        self.btn_delete.clicked.connect(self.detele_message)
        self.btn_cards.clicked.connect(self.check_if_progress_100)
        self.btn_learbh.clicked.connect(self.check_if_progress_100)
        self.btn_write.clicked.connect(self.check_if_progress_100)
        self.btn_reset.clicked.connect(self.reset)

    def write(self):
        self.write_window = learnwritepy.Write(module_id=self.module_id)
        self.hide()
        self.write_window.show()

    def count_progress(self):
        all_words = query_db.Database().get_progress(self.module_id)
        # делится на 2 для счета процентов, потому что степень изученности хранится в формате от 0 до 2
        # на 4 позиции в кортеже стоит этот прогресс
        total = [float(i[4] / 2) for i in all_words]
        if len(all_words) != 0:
            # 100 отображается в процентах
            self.progress = int((sum(total) / len(all_words)) * 100)
            self.prbar.setValue(self.progress)
        return self.progress

    def reset(self):
        query_db.Database().reset_progress(self.module_id)
        self.count_progress()

    def fill_table(self, reader):
        # 2 - количество столбцов в таблице
        self.tbl_wdt.setColumnCount(2)
        self.tbl_wdt.setRowCount(len(reader))
        for i in range(len(reader)):
            for j in range(2):
                self.tbl_wdt.setItem(i, j, QTableWidgetItem(reader[i][j]))

    def check_if_progress_100(self):
        # 100 - максимальный прогресс в процентах
        if self.progress == 100:
            self.reset()
        if self.sender().text() == 'Карточки':
            self.cards()
        elif self.sender().text() == 'Заучивание':
            self.by_hard()
        elif self.sender().text() == 'Письмо':
            self.write()

    def by_hard(self):
        self.cards_window = learn_bhpy.ByHeart(module_id=self.module_id)
        self.hide()
        self.cards_window.show()

    def detele_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(DELETE_MODULE_TEXT)
        msg_box.setWindowTitle(MESSAGE)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.delete_module(self.module_id)

    def delete_module(self, module_id):
        query_db.Database().delete(module_id)
        self.back_to_main()

    def cards(self):
        self.cards_window = learn_cardspy.Cards(module_id=self.module_id)
        self.hide()
        self.cards_window.show()

    def back_to_main(self):
        self.main_window = main_windowpy.EzMain(self.logged_user_id)
        self.hide()
        self.main_window.show()

    def show_warning(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(MODULE_RESET)
        msg_box.setWindowTitle(MESSAGE)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exit_value = msg_box.exec()
        if exit_value == QMessageBox.Ok:
            self.edit()
