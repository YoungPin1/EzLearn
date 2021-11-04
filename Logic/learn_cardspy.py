import random

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import constants
import entre_mainlearn
import messageboxes
import query_db


class Cards(QMainWindow):
    def __init__(self, module_id=''):
        super().__init__()
        uic.loadUi('../Designs/learn_cards.ui', self)
        self.module_id = module_id
        self.all_words, self.learned, self.left = [], [], []
        self.run()

    def run(self):
        self.load_words()
        self.btn_know.clicked.connect(self.learned_word)
        self.btn_learn_more.clicked.connect(self.show_words)

    def load_words(self):
        self.all_words = query_db.Database().get_all_data_module(self.module_id)
        print(self.all_words)
        for i in self.all_words:
            if i[3] == 2:
                self.learned.append(i)
            else:
                self.left.append(i)
        self.show_words()

    def show_words(self):
        self.ledit_all.setText(str(len(self.all_words)))
        self.ledit_know.setText(str(len(self.learned)))
        self.ledit_left.setText(str(len(self.left)))
        if len(self.left) != 0:
            self.display_word()
        else:
            messageboxes.show_sucsess_message(self, constants.MODULE_LEANED_TEXT)

    def display_word(self):
        self.line = random.choice(self.left)
        self.btn_word_def.setText(self.line[1])

    def learned_word(self):
        self.left.remove(self.line)
        self.learned.append(self.line)
        query_db.Database().mark_as_learned(self.module_id, self.line[0])
        self.show_words()
