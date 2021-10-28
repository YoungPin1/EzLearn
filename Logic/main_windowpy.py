import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from add_module import AddModule
from exit_func import ExitDialog

class EzMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../Designs/main_window.ui', self)
        self.add_module_run = AddModule()
        self.run()

    def run(self):
        self.btn_create.clicked.connect(self.create)
        self.action_exit_acc.triggered.connect(self.exit)

    def create(self):
        self.hide()
        self.add_module_run.show()

    def exit(self):
        dlg = ExitDialog()
        dlg.exec()
