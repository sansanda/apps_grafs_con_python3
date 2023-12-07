import sys

from PyQt5.QtWidgets import QApplication
from ejemplos.ejemplo_GUI_2.ejemplo_GUI_2 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MiFormulario(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.i_mensaje.clicked.connect(self.sacatexto)

    def sacatexto(self):
        self.ui.mensaje.setText("Hola mundooooo!!!!!")

if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = MiFormulario()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())