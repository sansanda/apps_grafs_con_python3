import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class ejemplo_GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,300,300)
        self.setWindowTitle("Primer Ejemplo de GUI con PyQt")
        salir = QtWidgets.QPushButton("Salir", self)
        salir.setGeometry(100,100,100,100)
        salir.clicked.connect(self.close)

app = QtWidgets.QApplication(sys.argv)
mi_app = ejemplo_GUI()
mi_app.show()
sys.exit(app.exec_())