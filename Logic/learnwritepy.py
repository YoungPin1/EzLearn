import random

from PyQt5.QtWidgets import QMainWindow

import learn_mainpy
import load_words_for_learning
import query_db
import same_functions
from Designs.design_learn_write import Ui_MainWindow
from constants import *


class Write(QMainWindow, Ui_MainWindow):
    def __init__(self, module_id=None):
        super().__init__()
        self.setupUi(self)
        self.module_id = module_id
        self.all_words, self.learned, self.left = load_words_for_learning.load_words(self.module_id)
        self.count = 0
        self.done = False
        self.run()

    def run(self):
        self.begin()
        self.btn_exit.clicked.connect(self.back_to_main)
        self.btn_ans.clicked.connect(self.compare)
        self.btn_next.clicked.connect(self.next_word)

    def back_to_main(self):
        self.prev_window = learn_mainpy.MainLearn(self.module_id)
        self.hide()
        self.prev_window.show()

    def begin(self):
        # 10 слов в одном блоке
        if self.count < 10 and len(self.left) != 0:
            self.prbar_block.setValue(self.count * 10)
            self.count += 1
            self.line = random.choice(self.left)
            # пишем слово на экран
            self.ledit_defin.setText(self.line[2])
        else:
            same_functions.show_sucsess_message(self, BLOCK_LEARNED)

    def compare(self):
        if not self.done:
            self.done = True
            self.ledit_ans.setReadOnly(True)
            if self.ledit_ans.text() == self.line[1]:
                self.ledit_ans.setStyleSheet(LEDIT_GREEN)
                self.change_data()
            else:
                self.ledit_ans.setStyleSheet(LEDIT_RED)
                self.lbl_correct.setText(self.line[1])

    def change_data(self):
        self.line_change = list(self.line)
        # увеличиваем прогресс
        self.line_change[4] += 1
        self.left.remove(self.line)
        if int(self.line_change[4]) < 2:
            query_db.Database().mark_as_learned(1, self.module_id, self.line[0])
            self.left.append(tuple(self.line_change))
        else:
            self.learned.append(self.line)
            query_db.Database().mark_as_learned(2, self.module_id, self.line[0])

    def next_word(self):
        self.done = False
        self.ledit_ans.setReadOnly(False)
        self.ledit_ans.setStyleSheet(LEDIT_WHITE)
        self.lbl_correct.setText('')
        self.ledit_ans.setText('')
        self.begin()
