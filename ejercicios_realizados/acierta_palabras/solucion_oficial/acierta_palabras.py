# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\flop\Desktop\Ejercicios_Python_Resueltos\acierta_palabras.ui'
#
# Created: Fri Mar 17 03:14:48 2017
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
        Dialog.resize(1119, 586)
        self.boton_comenzar = QtGui.QPushButton(Dialog)
        self.boton_comenzar.setGeometry(QtCore.QRect(431, 420, 151, 82))
        self.boton_comenzar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.boton_comenzar.setCheckable(False)
        self.boton_comenzar.setAutoDefault(False)
        self.boton_comenzar.setObjectName(_fromUtf8("boton_comenzar"))
        self.barra_segundos = QtGui.QProgressBar(Dialog)
        self.barra_segundos.setGeometry(QtCore.QRect(920, 330, 121, 21))
        self.barra_segundos.setMaximum(60)
        self.barra_segundos.setProperty("value", 60)
        self.barra_segundos.setTextVisible(False)
        self.barra_segundos.setFormat(_fromUtf8(""))
        self.barra_segundos.setObjectName(_fromUtf8("barra_segundos"))
        self.panel_definicion = QtGui.QLabel(Dialog)
        self.panel_definicion.setGeometry(QtCore.QRect(80, 100, 821, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.panel_definicion.setFont(font)
        self.panel_definicion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.panel_definicion.setText(_fromUtf8(""))
        self.panel_definicion.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_definicion.setObjectName(_fromUtf8("panel_definicion"))
        self.entrada = QtGui.QLineEdit(Dialog)
        self.entrada.setGeometry(QtCore.QRect(240, 230, 531, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.entrada.setFont(font)
        self.entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.entrada.setObjectName(_fromUtf8("entrada"))
        self.salida = QtGui.QLabel(Dialog)
        self.salida.setGeometry(QtCore.QRect(240, 340, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.salida.setFont(font)
        self.salida.setFrameShape(QtGui.QFrame.NoFrame)
        self.salida.setText(_fromUtf8(""))
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.segundos_restantes = QtGui.QLabel(Dialog)
        self.segundos_restantes.setGeometry(QtCore.QRect(880, 350, 201, 20))
        self.segundos_restantes.setText(_fromUtf8(""))
        self.segundos_restantes.setAlignment(QtCore.Qt.AlignCenter)
        self.segundos_restantes.setObjectName(_fromUtf8("segundos_restantes"))
        self.boton_parar = QtGui.QPushButton(Dialog)
        self.boton_parar.setGeometry(QtCore.QRect(622, 420, 151, 82))
        self.boton_parar.setAutoDefault(False)
        self.boton_parar.setObjectName(_fromUtf8("boton_parar"))
        self.boton_inicio = QtGui.QPushButton(Dialog)
        self.boton_inicio.setGeometry(QtCore.QRect(240, 420, 151, 82))
        self.boton_inicio.setFocusPolicy(QtCore.Qt.TabFocus)
        self.boton_inicio.setCheckable(False)
        self.boton_inicio.setAutoDefault(False)
        self.boton_inicio.setObjectName(_fromUtf8("boton_inicio"))
        self.panel_palabras = QtGui.QListWidget(Dialog)
        self.panel_palabras.setGeometry(QtCore.QRect(920, 100, 121, 231))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.panel_palabras.setFont(font)
        self.panel_palabras.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.panel_palabras.setFrameShape(QtGui.QFrame.HLine)
        self.panel_palabras.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.panel_palabras.setViewMode(QtGui.QListView.IconMode)
        self.panel_palabras.setObjectName(_fromUtf8("panel_palabras"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Acierta palabras", None))
        self.boton_comenzar.setText(_translate("Dialog", "Comenzar", None))
        self.boton_parar.setText(_translate("Dialog", "Parar", None))
        self.boton_inicio.setText(_translate("Dialog", "Inicio", None))

