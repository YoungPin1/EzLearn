import random

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import constants
import entre_mainlearn
import messageboxes
import query_db


class ByHeart(QMainWindow):
    def __init__(self, module_id=''):
        super().__init__()
        uic.loadUi('../Designs/learn_bh.ui', self)
        self.module_id = module_id
        self.all_words, self.learned, self.left = [], [], []
        self.run()

    def run(self):
        pass
