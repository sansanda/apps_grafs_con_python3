import sys
sys.path.append(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos")
import random as r
from acierta_palabras import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.mi_tiempo = QtCore.QTimer()
        self.mi_tiempo.setInterval(1000)

        self.ui.barra_segundos.setVisible(False)

        self.ui.boton_inicio.clicked.connect(self.inicio)
        self.ui.boton_comenzar.clicked.connect(self.comenzar)
        self.ui.boton_parar.clicked.connect(self.parar)
        self.mi_tiempo.timeout.connect(self.mueve_barra)
        self.ui.entrada.returnPressed.connect(self.comprueba)

    def inicializa(self):
        self.ui.boton_comenzar.blockSignals(False)
        self.ui.salida.clear()
        self.ui.panel_palabras.clear()
        self.ui.entrada.setEnabled(True)
        self.ui.barra_segundos.setVisible(True)
        self.ui.barra_segundos.setValue(60)
        self.ui.segundos_restantes.setText("Número de segundos restantes: 60")

        self.mi_diccionario = {}
        self.mis_indices = []
        self.segundos = 60
        self.mi_tiempo.stop()
        self.parado = False

    def cuenta_palabras_fichero(self):
        num_palabras = 0
        fichero = open(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos\definiciones.txt", "r")
        for dato in fichero:
            if dato.count('*') != 0:
                num_palabras += 1
        fichero.close()
        return num_palabras

    def inicio(self):
        self.inicializa()
        caracteres_no_en_nombre = ['*',' ',',','.','\n']
        while len(self.mi_diccionario) < 6:
            fichero = open(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos\definiciones.txt", "r")
            nombre_sacado = saca_definicion = False
            nombre = definicion = ''
            num_asteriscos = 0
            n_pal = r.randint(1,self.cuenta_palabras_fichero())
            while n_pal in self.mis_indices:
                n_pal = r.randint(1, self.cuenta_palabras_fichero())
            self.mis_indices.append(n_pal)
            for dato in fichero:
                if dato.count('*') != 0:
                    num_asteriscos += 1
                if num_asteriscos == n_pal and nombre_sacado == False:
                    nombre = dato
                    nombre_sacado = True
                    saca_definicion = True
                    continue
                if saca_definicion == True and dato.count('1.') == 1:
                    definicion = dato
                    for car in caracteres_no_en_nombre:
                        if car in nombre:
                            if car == ',':
                                hasta = nombre.find(car)
                                nombre = nombre[0:hasta]
                            else:
                                nombre = nombre.replace(car, '')
                    self.mi_diccionario[nombre] = definicion
                    break
            fichero.close()
        for palabra in self.mi_diccionario.keys():
            self.ui.panel_palabras.addItem(palabra.upper()[0:4])


    def comenzar(self):
        self.palabras = list(self.mi_diccionario.keys())
        r.shuffle(self.palabras)
        self.ui.boton_comenzar.blockSignals(True)
        self.ui.panel_definicion.setText(self.mi_diccionario[self.palabras[0]])
        self.ui.entrada.setFocus(True)
        self.mi_tiempo.start()

    def comprueba(self):
        try:
            respuesta = self.ui.entrada.text()
            self.ui.entrada.clear()
            if self.mi_diccionario[respuesta] == self.ui.panel_definicion.text():
                self.ui.salida.setText("¡Correcto!")
                QtCore.QTimer.singleShot(1500, lambda: self.ui.salida.clear())
                self.palabras.pop(0)
                del self.mi_diccionario[respuesta]
                self.ui.panel_palabras.clear()
                for palabra in self.mi_diccionario.keys():
                    self.ui.panel_palabras.addItem(palabra.upper()[0:4])
                if len(self.palabras) != 0:
                    self.ui.panel_definicion.setText(self.mi_diccionario[self.palabras[0]])
                else:
                    self.ui.panel_definicion.clear()
                    self.ui.salida.setText("¡Enhorabuena, has ganado!")
                    self.ui.entrada.setEnabled(False)
                    self.mi_tiempo.stop()
        except:
            self.ui.salida.setText("No es correcto")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.salida.clear())

    def mueve_barra(self):
        self.segundos -= 1
        self.ui.barra_segundos.setValue(self.segundos)
        texto = "Número de segundos restantes: " + str(self.segundos)
        if self.segundos == 0:
            self.ui.salida.setText("Has perdido.")
            self.ui.entrada.setEnabled(False)
            self.mi_tiempo.stop()
        self.ui.segundos_restantes.setText(texto)

    def parar(self):
        if self.parado == True:
            self.mi_tiempo.start()
            self.parado = False
            self.ui.boton_parar.setText("Parar")
        else:
            self.mi_tiempo.stop()
            self.parado = True
            self.ui.boton_parar.setText("Continuar")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



