# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\flop\Desktop\Ejercicios_Python_Resueltos\calculo_mental.ui'
#
# Created: Fri Mar 24 12:43:15 2017
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
        Dialog.resize(577, 660)
        self.boton_comenzar = QtGui.QPushButton(Dialog)
        self.boton_comenzar.setGeometry(QtCore.QRect(215, 510, 151, 82))
        self.boton_comenzar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.boton_comenzar.setCheckable(False)
        self.boton_comenzar.setAutoDefault(False)
        self.boton_comenzar.setObjectName(_fromUtf8("boton_comenzar"))
        self.mensaje = QtGui.QLabel(Dialog)
        self.mensaje.setGeometry(QtCore.QRect(130, 440, 302, 21))
        self.mensaje.setText(_fromUtf8(""))
        self.mensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.mensaje.setObjectName(_fromUtf8("mensaje"))
        self.barra_segundos = QtGui.QProgressBar(Dialog)
        self.barra_segundos.setGeometry(QtCore.QRect(80, 470, 421, 21))
        self.barra_segundos.setMaximum(60)
        self.barra_segundos.setProperty("value", 60)
        self.barra_segundos.setTextVisible(True)
        self.barra_segundos.setObjectName(_fromUtf8("barra_segundos"))
        self.panel = QtGui.QLabel(Dialog)
        self.panel.setGeometry(QtCore.QRect(120, 70, 326, 171))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.panel.setFont(font)
        self.panel.setFrameShape(QtGui.QFrame.Panel)
        self.panel.setText(_fromUtf8(""))
        self.panel.setAlignment(QtCore.Qt.AlignCenter)
        self.panel.setObjectName(_fromUtf8("panel"))
        self.entrada = QtGui.QLineEdit(Dialog)
        self.entrada.setGeometry(QtCore.QRect(120, 240, 326, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.entrada.setFont(font)
        self.entrada.setFrame(True)
        self.entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.entrada.setReadOnly(True)
        self.entrada.setObjectName(_fromUtf8("entrada"))
        self.salida = QtGui.QLabel(Dialog)
        self.salida.setGeometry(QtCore.QRect(120, 330, 326, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.salida.setFont(font)
        self.salida.setFrameShape(QtGui.QFrame.NoFrame)
        self.salida.setText(_fromUtf8(""))
        self.salida.setScaledContents(True)
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.boton_parar = QtGui.QPushButton(Dialog)
        self.boton_parar.setGeometry(QtCore.QRect(406, 510, 101, 82))
        self.boton_parar.setAutoDefault(False)
        self.boton_parar.setObjectName(_fromUtf8("boton_parar"))
        self.boton_inicio = QtGui.QPushButton(Dialog)
        self.boton_inicio.setGeometry(QtCore.QRect(74, 510, 101, 82))
        self.boton_inicio.setFocusPolicy(QtCore.Qt.TabFocus)
        self.boton_inicio.setCheckable(False)
        self.boton_inicio.setAutoDefault(False)
        self.boton_inicio.setObjectName(_fromUtf8("boton_inicio"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Cálculo mental", None))
        self.boton_comenzar.setText(_translate("Dialog", "Comenzar", None))
        self.boton_parar.setText(_translate("Dialog", "Parar", None))
        self.boton_inicio.setText(_translate("Dialog", "Inicio", None))

