
import sys
sys.path.append(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos")
from calculadora_simple import *

class MiFormulario(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.boton_sum.clicked.connect(self.calcular)
        self.ui.boton_res.clicked.connect(self.calcular)
        self.ui.boton_mul.clicked.connect(self.calcular)
        self.ui.boton_div.clicked.connect(self.calcular)

    def calcular(self):
        try:
            num1 = float(self.ui.num_1.text())
            num2 = float(self.ui.num_2.text())
            operacion = self.sender().text()
            if operacion == '+':
                op = "suma"
                res = num1 + num2
            elif operacion == '-':
                op = "resta"
                res = num1 - num2
            elif operacion == '*':
                op = "multiplicación"
                res = num1 * num2
            elif operacion == '/':
                op = "división"
                res = num1 / num2
            self.ui.salida.setText("La {} de {} y {} es {:.5f}".format(op, num1, num2, res))
        except:
            self.ui.salida.setText("Los operandos no son correctos")


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())

