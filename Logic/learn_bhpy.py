import random
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import constants
import load_words_for_learning
import messageboxes


class ByHeart(QMainWindow):
    def __init__(self, module_id=''):
        super().__init__()
        uic.loadUi('../Designs/learn_bh.ui', self)
        self.module_id = module_id
        self.lbl_right_if_error.setHidden(True)
        self.run()

    def run(self):
        self.get_words()
        self.btn_opt_1.clicked.connect(self.check)
        self.btn_opt_2.clicked.connect(self.check)
        self.btn_opt_3.clicked.connect(self.check)
        self.btn_opt_4.clicked.connect(self.check)

    def get_words(self):
        self.all_words, self.learned, self.left = load_words_for_learning.load_words(self.module_id)
        if len(self.left) != 0:
            self.start()
        else:
            messageboxes.show_sucsess_message(self, constants.MODULE_LEANED_TEXT)

    def start(self):
        self.line = random.choice(self.left)
        self.ledit_defin.setText(self.line[1])
        definitions = self.get_definitions()
        self.btn_opt_1.setText(definitions[0][2])
        self.btn_opt_2.setText(definitions[1][2])
        self.btn_opt_3.setText(definitions[2][2])
        self.btn_opt_4.setText(definitions[3][2])

    def get_definitions(self):
        right_btn = random.randint(1, 4)
        definitions = []
        for i in range(1, 5):
            if i == right_btn:
                definitions.append(self.line)
            else:
                definitions.append(random.choice(self.all_words))
        return definitions
#пока очень плохо работает
    def check(self):
        if self.sender().text() == self.line[2]:
            self.sender().setStyleSheet('background-color:rgb(0,255,0)')
            if int(self.line[3]) == 2:
                self.left.remove(self.line)
                self.learned.append(self.line)
            else:
                self.line_list = list(self.line)
                self.line_list[3] += 1
                self.line = self.line_list
        else:
            self.sender().setStyleSheet('background-color:rgb(255,0,0)')
            self.lbl_right_if_error.setHidden(False)
            self.lbl_right_if_error.setText(self.line[2])
        time.sleep(0.5)
        self.lbl_right_if_error.setHidden(True)
        self.btn_opt_1.setStyleSheet(constants.NORMAL_COLOR)
        self.btn_opt_2.setStyleSheet(constants.NORMAL_COLOR)
        self.btn_opt_3.setStyleSheet(constants.NORMAL_COLOR)
        self.btn_opt_4.setStyleSheet(constants.NORMAL_COLOR)
        self.start()
