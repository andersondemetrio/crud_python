import sys
from PySide6.QtWidgets import QApplication

from crud.controller.cliente_dao import DataBase
from crud.view.tela_principal import MainWindow

db = DataBase()
db.connect()
db.create_table_cliente()
db.close_connection()

args = sys.argv

app = QApplication(sys.argv)
principal = MainWindow()
principal.show()
app.exec()
