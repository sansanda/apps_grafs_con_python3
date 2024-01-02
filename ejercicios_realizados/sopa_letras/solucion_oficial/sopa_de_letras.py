# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\flop\Desktop\Ejercicios_Python_Resueltos\sopa_de_letras.ui'
#
# Created: Fri Mar 17 19:14:09 2017
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(819, 807)
        self.tabla = QtGui.QTableWidget(Dialog)
        self.tabla.setGeometry(QtCore.QRect(160, 50, 482, 482))
        self.tabla.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tabla.setShowGrid(True)
        self.tabla.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla.setRowCount(15)
        self.tabla.setColumnCount(15)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        item = QtGui.QTableWidgetItem()
        self.tabla.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tabla.setItem(0, 1, item)
        self.tabla.horizontalHeader().setVisible(False)
        self.tabla.horizontalHeader().setDefaultSectionSize(32)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.verticalHeader().setDefaultSectionSize(32)
        self.tabla.verticalHeader().setMinimumSectionSize(15)
        self.boton_nueva = QtGui.QPushButton(Dialog)
        self.boton_nueva.setGeometry(QtCore.QRect(154, 590, 326, 82))
        self.boton_nueva.setAutoDefault(False)
        self.boton_nueva.setObjectName(_fromUtf8("boton_nueva"))
        self.marcar_palabra = QtGui.QPushButton(Dialog)
        self.marcar_palabra.setGeometry(QtCore.QRect(154, 690, 326, 82))
        self.marcar_palabra.setAutoDefault(False)
        self.marcar_palabra.setObjectName(_fromUtf8("marcar_palabra"))
        self.boton_comprobar = QtGui.QPushButton(Dialog)
        self.boton_comprobar.setGeometry(QtCore.QRect(480, 590, 168, 182))
        self.boton_comprobar.setAutoDefault(False)
        self.boton_comprobar.setObjectName(_fromUtf8("boton_comprobar"))
        self.salida1 = QtGui.QLabel(Dialog)
        self.salida1.setGeometry(QtCore.QRect(160, 550, 271, 16))
        self.salida1.setText(_fromUtf8(""))
        self.salida1.setObjectName(_fromUtf8("salida1"))
        self.salida2 = QtGui.QLabel(Dialog)
        self.salida2.setGeometry(QtCore.QRect(450, 550, 191, 16))
        self.salida2.setText(_fromUtf8(""))
        self.salida2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.salida2.setObjectName(_fromUtf8("salida2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Sopa de letras", None))
        __sortingEnabled = self.tabla.isSortingEnabled()
        self.tabla.setSortingEnabled(False)
        self.tabla.setSortingEnabled(__sortingEnabled)
        self.boton_nueva.setText(_translate("Dialog", "Nueva sopa de letras", None))
        self.marcar_palabra.setText(_translate("Dialog", "Marcar palabra", None))
        self.boton_comprobar.setText(_translate("Dialog", "Comprobar", None))

