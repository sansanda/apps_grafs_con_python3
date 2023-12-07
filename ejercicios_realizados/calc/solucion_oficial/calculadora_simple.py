# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora_simple.ui'
#
# Created: Fri May 19 18:01:46 2017
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
        Form.resize(550, 358)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 150, 381, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.boton_sum = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_sum.setObjectName(_fromUtf8("boton_sum"))
        self.horizontalLayout.addWidget(self.boton_sum)
        self.boton_res = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_res.setObjectName(_fromUtf8("boton_res"))
        self.horizontalLayout.addWidget(self.boton_res)
        self.boton_mul = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_mul.setObjectName(_fromUtf8("boton_mul"))
        self.horizontalLayout.addWidget(self.boton_mul)
        self.boton_div = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_div.setObjectName(_fromUtf8("boton_div"))
        self.horizontalLayout.addWidget(self.boton_div)
        self.salida = QtGui.QLabel(Form)
        self.salida.setGeometry(QtCore.QRect(80, 250, 381, 31))
        self.salida.setText(_fromUtf8(""))
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(190, 40, 160, 80))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.boton_sum.setText(_translate("Form", "+", None))
        self.boton_res.setText(_translate("Form", "-", None))
        self.boton_mul.setText(_translate("Form", "*", None))
        self.boton_div.setText(_translate("Form", "/", None))
        self.label.setText(_translate("Form", "Número 1:", None))
        self.label_2.setText(_translate("Form", "Número 2:", None))

