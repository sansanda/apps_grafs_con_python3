import sys
from ejercicios_realizados.inmobiliaria.inmobiliaria_ui import *


class calc_GUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.buscar_pushButton.clicked.connect(self.buscar)

    def buscar(self):
        str_busqueda = "Busco piso {} en {} con {} habitaciones y {} baños/aseos".format(
            self.ui.tipo_inmueble_comboBox.currentText(),
            self.ui.localidad_comboBox.currentText(),
            self.ui.num_hab_horizontalSlider.value(),
            self.ui.num_ba_horizontalSlider.value()
        )
        if self.ui.plaza_garaje_checkBox.isChecked():
            str_busqueda = str_busqueda + " y plaza de garaje."
        else:
            str_busqueda = str_busqueda + "."
        self.ui.resultado_busqueda_label.setText(str_busqueda)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = calc_GUI()
    myapp.show()
    sys.exit(app.exec_())
