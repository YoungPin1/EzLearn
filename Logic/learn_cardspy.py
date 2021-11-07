import random

from PyQt5.QtWidgets import QMainWindow

import learn_mainpy
import load_words_for_learning
import query_db
import same_functions
from Designs.design_learn_cards import Ui_MainWindow
from constants import *


class Cards(QMainWindow, Ui_MainWindow):
    def __init__(self, module_id=None):
        super().__init__()
        self.setupUi(self)
        self.module_id = module_id
        self.run()

    def run(self):
        self.get_words()
        self.btn_know.clicked.connect(self.learned_word)
        self.btn_learn_more.clicked.connect(self.show_words)
        self.btn_exit.clicked.connect(self.back_to_main)
        self.btn_word_def.clicked.connect(self.flip)

    def flip(self):
        if self.btn_word_def.text() == self.line[2]:
            self.btn_word_def.setText(self.line[1])
        else:
            self.btn_word_def.setText(self.line[2])

    def get_words(self):
        self.all_words, self.learned, self.left = load_words_for_learning.load_words(self.module_id)
        self.show_words()

    def show_words(self):
        self.ledit_all.setText(str(len(self.all_words)))
        self.ledit_know.setText(str(len(self.learned)))
        self.ledit_left.setText(str(len(self.left)))
        if len(self.left) != 0:
            self.display_word()
        else:
            same_functions.show_sucsess_message(self, BLOCK_LEARNED)

    def display_word(self):
        self.line = random.choice(self.left)
        self.btn_word_def.setText(self.line[1])

    def learned_word(self):
        self.left.remove(self.line)
        self.learned.append(self.line)
        query_db.Database().mark_as_learned(2, self.module_id, self.line[0])
        self.show_words()

    def back_to_main(self):
        self.exit_window = learn_mainpy.MainLearn(self.module_id)
        self.hide()
        self.exit_window.show()
