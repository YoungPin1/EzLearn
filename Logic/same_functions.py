from PyQt5.QtWidgets import QMessageBox

from constants import *


def show_sucsess_message(self, text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(text)
    msg_box.setWindowTitle(MESSAGE)
    msg_box.setStandardButtons(QMessageBox.Ok)
    exit_value = msg_box.exec()
    if exit_value == QMessageBox.Ok:
        self.back_to_main()
