
import sys
sys.path.append(r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos")
import random
import os
from sopa_de_letras import *
from PyQt4.QtGui import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.mi_tabla = [0 for i in range(15) for j in range(15)]
        self.mi_letra = ''
        self.mi_palabra = ''
        self.mis_x = []
        self.mis_y = []
        self.celdas_marcadas = []

        self.ui.tabla.cellClicked.connect(self.maneja_clic)
        self.ui.boton_nueva.clicked.connect(self.distribuye)
        self.ui.marcar_palabra.clicked.connect(self.marca_palabra)
        self.ui.boton_comprobar.clicked.connect(self.comprueba)


    def maneja_clic(self, x, y):
        self.celdas_marcadas.append((x,y))
        self.mis_x.append(x)
        self.mis_y.append(y)
        self.ui.tabla.currentItem().setBackgroundColor(QtGui.QColor(0,255,255))
        self.mi_letra = self.ui.tabla.currentItem().text()
        self.mi_palabra += self.mi_letra


    def inicializa(self):
        self.mi_tabla = [0 for i in range(15) for j in range(15)]
        self.ui.tabla.clear()
        self.ui.salida1.clear()


    def distribuye(self):
        self.ui.tabla.setEnabled(True)
        self.inicializa()
        palabras_totales = []
        dir = r"C:\Users\flop\Desktop\Ejercicios_Python_Resueltos\productos_campo.txt"
        if os.path.isfile(dir):
            f = open(dir, 'r')
            for linea in f:
                if linea != '\n':
                    palabras_totales.append(linea.replace('\n', ''))
            f.close()
        else:
            self.ui.salida1.setText("Error al leer el fichero de palabras")
            QtCore.QTimer.singleShot(2000, lambda: self.ui.salida1.setText(''))

        self.mis_palabras = []
        num_pal = 0
        ya_sacadas = []
        tope = len(palabras_totales)
        while num_pal < 5:
            indice = random.randint(0, tope-1)
            if indice not in ya_sacadas:
                self.mis_palabras.append(palabras_totales[indice])
                ya_sacadas.append(indice)
                num_pal += 1
        self.mis_palabras_mayusculas = [i.upper() for i in self.mis_palabras]

        self.restantes = len(self.mis_palabras)
        self.ui.salida2.setText("Palabras restantes: " + str(self.restantes))
        for self.palabra in self.mis_palabras:
            self.coloca_palabra()
        self.rellena_huecos()


    def coloca_palabra(self):
        self.x = random.randint(0,14)
        self.y = random.randint(0,14)
        self.orientacion = random.randint(1,8)
        if self.dentro_limite() == True and self.se_solapa() == False:
            self.imprime_palabra()
        else:
            self.coloca_palabra()


    def rellena_huecos(self):
        for i in range(15*15):
            if self.mi_tabla[i] == 0:
                elemento_tabla = QTableWidgetItem()
                letra_azar = chr(random.randint(65,90))
                elemento_tabla.setText(letra_azar.upper())
                elemento_tabla.setTextAlignment(0x0084)
                self.ui.tabla.setItem(i//15, i%15, elemento_tabla)


    def dentro_limite(self):
        n = len(self.palabra) - 1
        x = 0
        y = 0
        if self.orientacion == 1:
            x = self.x - n
        elif self.orientacion == 2:
            x = self.x - n
            y = self.y + n
        elif self.orientacion == 3:
            y = self.y + n
        elif self.orientacion == 4:
            x = self.x + n
            y = self.y + n
        elif self.orientacion == 5:
            x = self.x + n
        elif self.orientacion == 6:
            x = self.x + n
            y = self.y - n
        elif self.orientacion == 7:
            y = self.y - n
        elif self.orientacion == 8:
            x = self.x - n
            y = self.y -n

        if 0 <= x <= 14 and 0 <= y <=14:
            return True
        else:
            return False


    def se_solapa(self):
        se_solapa = False
        x = self.x
        y = self.y
        for letra in self.palabra:
            if self.mi_tabla[15*x + y] == 1:
                return True
            if self.orientacion == 1:
                x = x - 1
            elif self.orientacion == 2:
                x = x - 1
                y = y + 1
            elif self.orientacion == 3:
                y = y + 1
            elif self.orientacion == 4:
                x = x + 1
                y = y + 1
            elif self.orientacion == 5:
                x = x + 1
            elif self.orientacion == 6:
                x = x + 1
                y = y - 1
            elif self.orientacion == 7:
                y = y - 1
            elif self.orientacion == 8:
                x = x - 1
                y = y -1
        return se_solapa


    def marca_palabra(self):
        for celda in self.celdas_marcadas:
            elemento_tabla = self.ui.tabla.item(celda[0], celda[1])
            elemento_tabla.setBackgroundColor(QtGui.QColor(255,255,255))
            self.ui.tabla.setItem(celda[0], celda[1], elemento_tabla)
        self.mi_palabra = ''


    def comprueba(self):
        self.celdas_marcadas = []
        if self.mis_palabras_mayusculas.count(self.mi_palabra) != 0:
            self.restantes -=1
            self.ui.salida1.setText("Palabra correcta")
            if self.restantes > 0:
                QtCore.QTimer.singleShot(2000, lambda: self.ui.salida1.setText(''))
            self.mi_palabra = ''

            self.mis_x.clear()
            self.mis_y.clear()
            self.ui.salida2.setText("Palabras restantes: " + str(self.restantes))

        else:
            self.ui.salida1.setText("Palabra incorrecta")
            QtCore.QTimer.singleShot(2000, lambda: self.ui.salida1.setText(''))
            self.mi_palabra = ''
            for i in range(len(self.mis_x)):
                self.ui.tabla.item(self.mis_x[i], self.mis_y[i]).setBackgroundColor(QtGui.QColor('transparent'))
        if self.restantes == 0:
            self.ui.salida1.setText("¡Enhorabuena, sopa de letras completada!")
            self.ui.tabla.setAutoFillBackground(True)
            self.ui.tabla.setEnabled(False)


    def imprime_palabra(self):
        x = self.x
        y = self.y
        for letra in self.palabra:
            elemento_tabla = QTableWidgetItem()
            elemento_tabla.setText(letra.upper())
            elemento_tabla.setTextAlignment(0x0084)
            self.ui.tabla.setItem(x, y, elemento_tabla)
            self.mi_tabla[15*x + y] = 1
            if self.orientacion == 1:
                x = x - 1
            elif self.orientacion == 2:
                x = x - 1
                y = y + 1
            elif self.orientacion == 3:
                y = y + 1
            elif self.orientacion == 4:
                x = x + 1
                y = y + 1
            elif self.orientacion == 5:
                x = x + 1
            elif self.orientacion == 6:
                x = x + 1
                y = y - 1
            elif self.orientacion == 7:
                y = y - 1
            elif self.orientacion == 8:
                x = x - 1
                y = y -1


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


