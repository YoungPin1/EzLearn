import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget

import add_module
import learn_mainpy
import query_db
from Designs.design_main_window import Ui_MainWindow


class EzMain(QMainWindow, Ui_MainWindow):
    def __init__(self, logged_user_id):
        super().__init__()
        self.setupUi(self)
        self.logged_user_id = logged_user_id
        self.run()

    def run(self):
        self.create_layout()
        self.btn_create.clicked.connect(self.create)

    def create_layout(self):
        self.grid = QGridLayout()
        self.widget = QWidget()
        self.mark_widgets()
        self.scroll_ar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_ar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.widget.setLayout(self.grid)
        self.scroll_ar.setWidget(self.widget)

    def mark_widgets(self):
        self.names_ids = query_db.Database().get_module_names(self.logged_user_id) \
            # 3 в этой функции - количество столбцов в таблице
        rows = math.ceil(len(self.names_ids) / 3)
        while len(self.names_ids) < rows * 3:
            self.names_ids.append(('', ''))
        self.positions = [(i, j) for i in range(rows) for j in range(3)]
        self.add_buttons()

    def add_buttons(self):
        for position, name in zip(self.positions, self.names_ids):
            if name == ('', ''):
                continue
            self.btn_name = QPushButton(self)
            self.btn_name.setText(str(name[0]))
            self.btn_name.setAccessibleName(str(name[1]))
            self.btn_name.setStyleSheet('color : white')
            self.btn_name.setMinimumSize(210, 120)
            self.btn_name.clicked.connect(self.entre_module)
            self.grid.addWidget(self.btn_name, *position)

    def entre_module(self):
        module_id = self.sender().accessibleName()
        self.main_learn = learn_mainpy.MainLearn(module_id=module_id)
        self.hide()
        self.main_learn.show()

    def create(self):
        self.add_module_run = add_module.AddModule(self.logged_user_id)
        self.hide()
        self.add_module_run.show()
