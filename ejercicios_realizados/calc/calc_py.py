# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        Form.setMinimumSize(QtCore.QSize(600, 600))
        Form.setMaximumSize(QtCore.QSize(600, 600))
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setGeometry(QtCore.QRect(30, 380, 521, 31))
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.numbers = QtWidgets.QSplitter(Form)
        self.numbers.setGeometry(QtCore.QRect(230, 80, 133, 91))
        self.numbers.setOrientation(QtCore.Qt.Vertical)
        self.numbers.setObjectName("numbers")
        self.number1_label = QtWidgets.QLabel(self.numbers)
        self.number1_label.setObjectName("number1_label")
        self.number1_lineEdit = QtWidgets.QLineEdit(self.numbers)
        self.number1_lineEdit.setObjectName("number1_lineEdit")
        self.number2_label = QtWidgets.QLabel(self.numbers)
        self.number2_label.setObjectName("number2_label")
        self.number2_lineEdit = QtWidgets.QLineEdit(self.numbers)
        self.number2_lineEdit.setObjectName("number2_lineEdit")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(140, 270, 300, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.sum_pushButton = QtWidgets.QPushButton(self.splitter)
        self.sum_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.sum_pushButton.setObjectName("sum_pushButton")
        self.subs_pushButton = QtWidgets.QPushButton(self.splitter)
        self.subs_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.subs_pushButton.setObjectName("subs_pushButton")
        self.mult_pushButton = QtWidgets.QPushButton(self.splitter)
        self.mult_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.mult_pushButton.setObjectName("mult_pushButton")
        self.div_pushButton = QtWidgets.QPushButton(self.splitter)
        self.div_pushButton.setObjectName("div_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.number1_label.setText(_translate("Form", "Número 1:"))
        self.number2_label.setText(_translate("Form", "Número 2:"))
        self.sum_pushButton.setText(_translate("Form", "+"))
        self.subs_pushButton.setText(_translate("Form", "-"))
        self.mult_pushButton.setText(_translate("Form", "*"))
        self.div_pushButton.setText(_translate("Form", "/"))
