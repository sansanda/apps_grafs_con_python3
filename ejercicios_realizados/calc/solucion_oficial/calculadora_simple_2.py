# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora_simple_2.ui'
#
# Created: Sat May 20 12:48:01 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(494, 355)
        self.salida = QtGui.QLabel(Form)
        self.salida.setGeometry(QtCore.QRect(60, 280, 381, 31))
        self.salida.setText(_fromUtf8(""))
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(150, 40, 192, 80))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.num_1 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.num_1.setObjectName(_fromUtf8("num_1"))
        self.gridLayout_2.addWidget(self.num_1, 0, 1, 1, 1)
        self.num_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.num_2.setObjectName(_fromUtf8("num_2"))
        self.gridLayout_2.addWidget(self.num_2, 1, 1, 1, 1)
        self.op_sum = QtGui.QRadioButton(Form)
        self.op_sum.setGeometry(QtCore.QRect(110, 140, 82, 17))
        self.op_sum.setObjectName(_fromUtf8("op_sum"))
        self.op_res = QtGui.QRadioButton(Form)
        self.op_res.setGeometry(QtCore.QRect(110, 170, 82, 17))
        self.op_res.setObjectName(_fromUtf8("op_res"))
        self.op_mul = QtGui.QRadioButton(Form)
        self.op_mul.setGeometry(QtCore.QRect(110, 200, 82, 17))
        self.op_mul.setObjectName(_fromUtf8("op_mul"))
        self.op_div = QtGui.QRadioButton(Form)
        self.op_div.setGeometry(QtCore.QRect(110, 230, 82, 17))
        self.op_div.setObjectName(_fromUtf8("op_div"))
        self.boton_calcular = QtGui.QPushButton(Form)
        self.boton_calcular.setGeometry(QtCore.QRect(220, 140, 161, 111))
        self.boton_calcular.setObjectName(_fromUtf8("boton_calcular"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Número 1:", None))
        self.label_2.setText(_translate("Form", "Número 2:", None))
        self.op_sum.setText(_translate("Form", "+", None))
        self.op_res.setText(_translate("Form", "-", None))
        self.op_mul.setText(_translate("Form", "*", None))
        self.op_div.setText(_translate("Form", "/", None))
        self.boton_calcular.setText(_translate("Form", "Calcular", None))

