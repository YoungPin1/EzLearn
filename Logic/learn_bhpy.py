import random

from PyQt5.QtWidgets import QMainWindow

import learn_mainpy
import load_words_for_learning
import query_db
import same_functions
from Designs.design_learn_bh import Ui_MainWindow
from constants import *


class ByHeart(QMainWindow, Ui_MainWindow):
    def __init__(self, module_id=None):
        super().__init__()
        self.setupUi(self)
        self.module_id = module_id
        self.count = 0
        self.done = False
        self.run()

    def run(self):
        self.get_words()
        self.btn_ans_1.clicked.connect(self.check)
        self.btn_ans_2.clicked.connect(self.check)
        self.btn_ans_3.clicked.connect(self.check)
        self.btn_ans_4.clicked.connect(self.check)
        self.btn_exit.clicked.connect(self.back_to_main)
        self.btn_next.clicked.connect(self.next_word)

    def get_words(self):
        self.all_words, self.learned, self.left = load_words_for_learning.load_words(self.module_id)
        self.start()

    def start(self):
        if self.count < 10 and len(self.left) != 0:
            self.prbar_block.setValue(self.count * 10)
            self.count += 1
            self.line = random.choice(self.left)
            # Под певрвым индексом находится само слово
            self.ledit_defin.setText(self.line[1])
            definitions = self.get_definitions()
            # Под вторым его объяснение
            self.btn_ans_1.setText(definitions[0][2])
            self.btn_ans_2.setText(definitions[1][2])
            self.btn_ans_3.setText(definitions[2][2])
            self.btn_ans_4.setText(definitions[3][2])
        else:
            same_functions.show_sucsess_message(self, BLOCK_LEARNED)

    def get_definitions(self):
        right_btn = random.randint(1, 4)
        words_without_correct = self.left + self.learned
        words_without_correct.remove(self.line)
        definitions = random.sample(words_without_correct, 4)
        # всего 4 кнопки
        for i in range(1, 5):
            if i == right_btn:
                definitions.pop(i - 1)
                definitions.insert(i - 1, self.line)
        return definitions

    def check(self):
        if not self.done:
            self.done = True
            if self.sender().text() == self.line[2]:
                self.sender().setStyleSheet(GREEN_BTN_STYLE)
                self.cor_ans()
            else:
                self.sender().setStyleSheet(RED_BTN_STYLE)
                self.lbl_correct.setText(self.line[2])

    def cor_ans(self):
        self.left.remove(self.line)
        self.line_list = list(self.line)
        # на 4 позиции находится изученность слова
        self.line_list[4] += 1
        if int(self.line_list[4]) == 2:
            self.learned.append(self.line)
            query_db.Database().mark_as_learned(2, self.module_id, self.line[0])
        else:
            query_db.Database().mark_as_learned(1, self.module_id, self.line[0])
            self.line = tuple(self.line_list)
            self.left.append(self.line)

    def next_word(self):
        self.done = False
        self.lbl_correct.setText('')
        self.btn_ans_1.setStyleSheet(NORMAL_STYLE_SHEET)
        self.btn_ans_2.setStyleSheet(NORMAL_STYLE_SHEET)
        self.btn_ans_3.setStyleSheet(NORMAL_STYLE_SHEET)
        self.btn_ans_4.setStyleSheet(NORMAL_STYLE_SHEET)
        self.start()

    def back_to_main(self):
        self.exit_window = learn_mainpy.MainLearn(self.module_id)
        self.hide()
        self.exit_window.show()
