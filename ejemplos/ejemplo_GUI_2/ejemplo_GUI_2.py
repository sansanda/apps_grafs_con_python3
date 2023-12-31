# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemplo_GUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 526)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 80, 461, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.i_mensaje = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.i_mensaje.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.i_mensaje.sizePolicy().hasHeightForWidth())
        self.i_mensaje.setSizePolicy(sizePolicy)
        self.i_mensaje.setIconSize(QtCore.QSize(16, 16))
        self.i_mensaje.setObjectName("i_mensaje")
        self.verticalLayout.addWidget(self.i_mensaje)
        self.mensaje = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mensaje.sizePolicy().hasHeightForWidth())
        self.mensaje.setSizePolicy(sizePolicy)
        self.mensaje.setText("")
        self.mensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.mensaje.setObjectName("mensaje")
        self.verticalLayout.addWidget(self.mensaje)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_mensaje = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_mensaje.sizePolicy().hasHeightForWidth())
        self.b_mensaje.setSizePolicy(sizePolicy)
        self.b_mensaje.setObjectName("b_mensaje")
        self.horizontalLayout.addWidget(self.b_mensaje)
        self.salir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.salir.sizePolicy().hasHeightForWidth())
        self.salir.setSizePolicy(sizePolicy)
        self.salir.setObjectName("salir")
        self.horizontalLayout.addWidget(self.salir)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.i_mensaje.clicked.connect(self.mensaje.show) # type: ignore
        self.b_mensaje.clicked.connect(self.mensaje.hide) # type: ignore
        self.salir.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.i_mensaje.setText(_translate("Form", "Imprimir mensaje"))
        self.b_mensaje.setText(_translate("Form", "Borrar mensaje"))
        self.salir.setText(_translate("Form", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
