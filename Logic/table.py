def create_table(self):
    self.tbl_wdt.horizontalHeader().setStyleSheet("::section{Background-color:rgb(40,40,40)}")
    self.tbl_wdt.verticalHeader().setStyleSheet("::section{Background-color:rgb(40,40,40)}")
    self.tbl_wdt.setColumnCount(2)
    self.tbl_wdt.setHorizontalHeaderLabels(['Термин', 'Определение'])
    head_view = self.tbl_wdt.horizontalHeader()
    head_view.setSectionResizeMode(0, 1)
    head_view.setSectionResizeMode(1, 1)
    self.tbl_wdt.resizeColumnsToContents()