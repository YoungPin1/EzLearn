import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Calendar(QMainWindow):
    def __init__(self):
        super().__init__()
        app.setStyle('Fusion')
        uic.loadUi('authorization.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calendar()
    ex.show()
    sys.exit(app.exec_())
