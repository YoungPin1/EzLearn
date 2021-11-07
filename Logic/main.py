from PyQt5.QtWidgets import QApplication
from authpy import Authorization
import sys
from constants import APP_STYLE


app = QApplication(sys.argv)
app.setStyle(APP_STYLE)
ex = Authorization()
ex.show()
sys.exit(app.exec())