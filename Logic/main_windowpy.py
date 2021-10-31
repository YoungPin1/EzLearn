from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import add_module


class EzMain(QMainWindow):
    def __init__(self, logged_user_id):
        self.logged_user_id = logged_user_id
        super().__init__()
        uic.loadUi('../Designs/main_window.ui', self)
        self.run()

    def run(self):
        self.btn_create.clicked.connect(self.create)

    def create(self):
        self.add_module_run = add_module.AddModule(self.logged_user_id)
        self.hide()
        self.add_module_run.show()
