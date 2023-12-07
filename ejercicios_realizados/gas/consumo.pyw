import sys

from ejercicios_realizados.gas.grafico_consumo_gas import Ui_consumo
import matplotlib.ticker as ticker
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QWidget, QApplication


class MiFormulario(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_consumo()
        self.ui.setupUi(self)
        self.ui.enero_lineEdit.setText("62")
        self.ui.febrero_lineEdit.setText("67")
        self.ui.marzo_lineEdit.setText("51")
        self.ui.abril_lineEdit.setText("24")
        self.ui.mayo_lineEdit.setText("33")
        self.ui.junio_lineEdit.setText("45")
        self.ui.julio_lineEdit.setText("66")
        self.ui.agosto_lineEdit.setText("78")
        self.ui.sept_lineEdit.setText("98")
        self.ui.octubre_lineEdit.setText("55")
        self.ui.nov_lineEdit.setText("10")
        self.ui.dic_lineEdit.setText("12")
        self.ui.generar_grafico_button.clicked.connect(self.graficar_funcion)

    def graficar_funcion(self):
        meses = ["Ene", "Febr", "Marz", "Abr", "May", "Jun", "Jul", "Ago", "Sept", "Oct", "Nov",
                 "Dic", "", "", "", "", "", "", "", ""]
        X = [i for i in range(12)]
        data = []
        data.append(int(self.ui.enero_lineEdit.text()))
        data.append(int(self.ui.febrero_lineEdit.text()))
        data.append(int(self.ui.marzo_lineEdit.text()))
        data.append(int(self.ui.abril_lineEdit.text()))
        data.append(int(self.ui.mayo_lineEdit.text()))
        data.append(int(self.ui.junio_lineEdit.text()))
        data.append(int(self.ui.julio_lineEdit.text()))
        data.append(int(self.ui.agosto_lineEdit.text()))
        data.append(int(self.ui.sept_lineEdit.text()))
        data.append(int(self.ui.octubre_lineEdit.text()))
        data.append(int(self.ui.nov_lineEdit.text()))
        data.append(int(self.ui.dic_lineEdit.text()))

        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.axis([-0.5, 11.5, 0, max(data) + 10])
        self.ui.widget.canvas.ax.xaxis.set_major_locator(ticker.FixedLocator(X))
        self.ui.widget.canvas.ax.xaxis.set_major_formatter(ticker.FixedFormatter(meses))
        self.ui.widget.canvas.ax.bar(X, data, align='center', width=1)
        self.ui.widget.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())
