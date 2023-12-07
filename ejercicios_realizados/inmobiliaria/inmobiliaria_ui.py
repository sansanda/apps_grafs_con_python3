# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inmobiliaria_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(894, 822)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 802, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.localidad_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.localidad_comboBox.setObjectName("localidad_comboBox")
        self.localidad_comboBox.addItems(["Barcelona", "Madrid", "Bilbao", "Valencia"])
        self.gridLayout_2.addWidget(self.localidad_comboBox, 0, 1, 1, 1)
        self.tipo_inmueble_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tipo_inmueble_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tipo_inmueble_label.setObjectName("tipo_inmueble_label")
        self.gridLayout_2.addWidget(self.tipo_inmueble_label, 1, 0, 1, 1)
        self.num_ba_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.num_ba_horizontalSlider.setMinimum(1)
        self.num_ba_horizontalSlider.setMaximum(3)
        self.num_ba_horizontalSlider.setPageStep(1)
        self.num_ba_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.num_ba_horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.num_ba_horizontalSlider.setTickInterval(1)
        self.num_ba_horizontalSlider.setObjectName("num_ba_horizontalSlider")
        self.gridLayout_2.addWidget(self.num_ba_horizontalSlider, 3, 1, 1, 1)
        self.localidad_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.localidad_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.localidad_label.setObjectName("localidad_label")
        self.gridLayout_2.addWidget(self.localidad_label, 0, 0, 1, 1)
        self.num_hab_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.num_hab_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num_hab_label.setObjectName("num_hab_label")
        self.gridLayout_2.addWidget(self.num_hab_label, 2, 0, 1, 1)
        self.plaza_garaje_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.plaza_garaje_checkBox.setObjectName("plaza_garaje_checkBox")
        self.gridLayout_2.addWidget(self.plaza_garaje_checkBox, 4, 1, 1, 1)
        self.num_ba_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.num_ba_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num_ba_label.setObjectName("num_ba_label")
        self.gridLayout_2.addWidget(self.num_ba_label, 3, 0, 1, 1)
        self.num_hab_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.num_hab_horizontalSlider.setMinimum(1)
        self.num_hab_horizontalSlider.setMaximum(5)
        self.num_hab_horizontalSlider.setPageStep(1)
        self.num_hab_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.num_hab_horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.num_hab_horizontalSlider.setTickInterval(1)
        self.num_hab_horizontalSlider.setObjectName("num_hab_horizontalSlider")
        self.gridLayout_2.addWidget(self.num_hab_horizontalSlider, 2, 1, 1, 1)
        self.tipo_inmueble_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.tipo_inmueble_comboBox.setObjectName("tipo_inmueble_comboBox")
        self.tipo_inmueble_comboBox.addItems(["nuevo", "segunda mano", "alquiler"])
        self.gridLayout_2.addWidget(self.tipo_inmueble_comboBox, 1, 1, 1, 1)
        self.selected_num_hab_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_num_hab_label.sizePolicy().hasHeightForWidth())
        self.selected_num_hab_label.setSizePolicy(sizePolicy)
        self.selected_num_hab_label.setMinimumSize(QtCore.QSize(20, 0))
        self.selected_num_hab_label.setObjectName("selected_num_hab_label")
        self.gridLayout_2.addWidget(self.selected_num_hab_label, 2, 2, 1, 1)
        self.selected_num_ba_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.selected_num_ba_label.setMinimumSize(QtCore.QSize(20, 0))
        self.selected_num_ba_label.setObjectName("selected_num_ba_label")
        self.gridLayout_2.addWidget(self.selected_num_ba_label, 3, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.buscar_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buscar_pushButton.sizePolicy().hasHeightForWidth())
        self.buscar_pushButton.setSizePolicy(sizePolicy)
        self.buscar_pushButton.setMinimumSize(QtCore.QSize(200, 200))
        self.buscar_pushButton.setMaximumSize(QtCore.QSize(200, 200))
        self.buscar_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.buscar_pushButton.setObjectName("buscar_pushButton")
        self.horizontalLayout.addWidget(self.buscar_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.resultado_busqueda_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultado_busqueda_label.sizePolicy().hasHeightForWidth())
        self.resultado_busqueda_label.setSizePolicy(sizePolicy)
        self.resultado_busqueda_label.setMinimumSize(QtCore.QSize(800, 50))
        self.resultado_busqueda_label.setMaximumSize(QtCore.QSize(800, 50))
        self.resultado_busqueda_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultado_busqueda_label.setText("")
        self.resultado_busqueda_label.setObjectName("resultado_busqueda_label")
        self.verticalLayout.addWidget(self.resultado_busqueda_label)

        self.retranslateUi(Form)
        self.num_hab_horizontalSlider.valueChanged['int'].connect(self.selected_num_hab_label.setNum) # type: ignore
        self.num_ba_horizontalSlider.valueChanged['int'].connect(self.selected_num_ba_label.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tipo_inmueble_label.setText(_translate("Form", "Tipo de inmueble:"))
        self.localidad_label.setText(_translate("Form", "Localidad:"))
        self.num_hab_label.setText(_translate("Form", "Número de habitaciones:"))
        self.plaza_garaje_checkBox.setText(_translate("Form", "Plaza de garaje"))
        self.num_ba_label.setText(_translate("Form", "Número de baños/aseos:"))
        self.selected_num_hab_label.setText(_translate("Form", "1"))
        self.selected_num_ba_label.setText(_translate("Form", "1"))
        self.buscar_pushButton.setText(_translate("Form", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
