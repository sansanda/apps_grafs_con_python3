
import sys
sys.path.append(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos")
from calculadora_simple_3 import *

class MiFormulario(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.op_sum.clicked.connect(lambda: self.calcula(1))
        self.ui.op_res.clicked.connect(lambda: self.calcula(2))
        self.ui.op_mul.clicked.connect(lambda: self.calcula(3))
        self.ui.op_div.clicked.connect(lambda: self.calcula(4))

    def calcula(self, num_op):
        try:
            num1 = float(self.ui.num_1.text())
            num2 = float(self.ui.num_2.text())
            if num_op == 1:
                op = "suma"
                res = num1 + num2
            elif num_op == 2 :
                op = "resta"
                res = num1 - num2
            elif num_op == 3:
                op = "multiplicación"
                res = num1 * num2
            elif num_op == 4:
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
