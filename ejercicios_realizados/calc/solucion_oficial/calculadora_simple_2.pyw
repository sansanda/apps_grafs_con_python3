
import sys
sys.path.append(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos")
from calculadora_simple_2 import *

class MiFormulario(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.boton_calcular.clicked.connect(self.calcula)

    def calcula(self):
        try:
            num1 = float(self.ui.num_1.text())
            num2 = float(self.ui.num_2.text())
            if self.ui.op_sum.isChecked():
                op = "suma"
                res = num1 + num2
            elif self.ui.op_res.isChecked() :
                op = "resta"
                res = num1 - num2
            elif self.ui.op_mul.isChecked():
                op = "multiplicación"
                res = num1 * num2
            elif self.ui.op_div.isChecked():
                op = "división"
                res = num1 / num2
            else:
                self.ui.salida.setText("No hay seleccionada ninguna operación")
                return None
            self.ui.salida.setText("La {} de {} y {} es {:.5f}".format(op, num1, num2, res))
        except:
            self.ui.salida.setText("Los operandos no son correctos")


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())
