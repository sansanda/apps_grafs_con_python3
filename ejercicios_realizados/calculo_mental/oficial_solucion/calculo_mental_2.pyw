import sys
sys.path.append(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos")
import random
from calculo_mental import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.mi_tiempo = QtCore.QTimer()
        self.mi_tiempo.setInterval(1000)
        self.parado = False

        self.ui.boton_inicio.clicked.connect(self.inicio)
        self.ui.boton_comenzar.clicked.connect(self.comenzar)
        self.ui.boton_parar.clicked.connect(self.parar)
        self.ui.entrada.editingFinished.connect(self.comprueba_op)
        self.mi_tiempo.timeout.connect(self.mueve_barra)
        self.inicio()


    def inicio(self):
        self.ui.boton_comenzar.blockSignals(False)
        self.mi_tiempo.stop()
        self.segundos = 60
        self.operando1 = random.randint(3,10)
        self.operando2 = 0
        self.res = 0
        self.aciertos = 0
        self.ui.panel.setText(str(self.operando1))
        self.ui.salida.clear()
        self.ui.mensaje.setText("Número de segundos restantes: 60")
        self.ui.barra_segundos.setValue(60)


    def comenzar(self):
        self.ui.entrada.setReadOnly(False)
        #self.ui.entrada.setFocus(True)
        self.mi_tiempo.start()
        self.saca_operacion()
        self.ui.boton_comenzar.blockSignals(True)


    def parar(self):
        if self.parado == True:
            self.parado = False
            self.mi_tiempo.start()
            self.ui.entrada.setReadOnly(False)
            self.ui.entrada.setFocus()
            self.ui.boton_parar.setText("Parar")
        else:
            self.parado = True
            self.mi_tiempo.stop()
            self.ui.entrada.setReadOnly(True)
            self.ui.boton_parar.setText("Seguir")


    def mueve_barra(self):
        self.segundos -= 1
        self.ui.barra_segundos.setValue(self.segundos - 1)
        texto = "Número de segundos restantes: " + str(self.segundos)
        if self.segundos == 0:
            self.ui.salida.setText("Has perdido")
            self.mi_tiempo.stop()
        self.ui.mensaje.setText(texto)

    def saca_operacion(self):
        texto = ''
        operacion = random.randint(1,4)
        if operacion == 1:
            self.operando2 = random.randint(3,25)
            texto = ' + '+ str(self.operando2)
            self.res = self.operando1 + self.operando2
        elif operacion == 2:
            self.operando2 = random.randint(3,25)
            if self.operando2 < self.operando1:
                texto = ' - '+ str(self.operando2)
                self.res = self.operando1 - self.operando2
            else:
                self.saca_operacion()
        elif operacion == 3:
            self.operando2 = random.randint(2,5)
            if self.operando1 // 100 == 0:
                texto = ' * '+ str(self.operando2)
                self.res = self.operando1 * self.operando2
            else:
                self.saca_operacion()
        elif operacion == 4:
            self.operando2 = random.randint(2,5)
            if self.operando1 % self.operando2 == 0:
                texto = ' / '+ str(self.operando2)
                self.res = self.operando1 // self.operando2
            else:
                self.saca_operacion()
        if texto != '':
            self.ui.panel.setText(texto)


    def comprueba_op(self):
        try:
            if self.ui.entrada.text() != '':
                if int(self.ui.entrada.text()) == int(self.res):
                    self.ui.salida.setStyleSheet('color: green')
                    self.ui.salida.setText("¡CORRECTO!")
                    QtCore.QTimer.singleShot(500, lambda:self.ui.entrada.clear())
                    self.operando1 = self.res
                    self.aciertos +=1
                    if self.aciertos == 10:
                        self.ui.salida.setText("¡Has ganado!")
                        self.ui.panel.clear()
                        self.mi_tiempo.stop()
                    else:
                        QtCore.QTimer.singleShot(500, lambda:self.ui.salida.clear())
                        QtCore.QTimer.singleShot(500, lambda:self.saca_operacion())
                else:
                    self.ui.salida.setStyleSheet('color: red')
                    self.ui.salida.setText(("INCORRECTO"))
                    QtCore.QTimer.singleShot(500, lambda: self.ui.entrada.clear())
                    QtCore.QTimer.singleShot(500, lambda: self.ui.salida.clear())
        except:
            self.ui.salida.setStyleSheet('color: magenta; font-size: 18px')
            self.ui.salida.setText("No es una respuesta válida")
            QtCore.QTimer.singleShot(1000, lambda: self.ui.salida.clear())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



