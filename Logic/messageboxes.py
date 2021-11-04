from PyQt5.QtWidgets import QMessageBox

import entre_mainlearn


def show_sucsess_message(self, text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(text)
    msg_box.setWindowTitle('Сообщение')
    msg_box.setStandardButtons(QMessageBox.Ok)
    exit_value = msg_box.exec()
    if exit_value == QMessageBox.Ok:
        entre_mainlearn.back_to_main(self)
