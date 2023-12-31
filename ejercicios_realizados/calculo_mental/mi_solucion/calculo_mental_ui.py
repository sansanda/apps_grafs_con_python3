# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculo_mental_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 381, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.operand1_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.operand1_label.setFont(font)
        self.operand1_label.setText("")
        self.operand1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.operand1_label.setObjectName("operand1_label")
        self.horizontalLayout_4.addWidget(self.operand1_label)
        self.operator_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.operator_label.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.operator_label.setFont(font)
        self.operator_label.setText("")
        self.operator_label.setAlignment(QtCore.Qt.AlignCenter)
        self.operator_label.setObjectName("operator_label")
        self.horizontalLayout_4.addWidget(self.operator_label)
        self.operand2_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.operand2_label.setFont(font)
        self.operand2_label.setText("")
        self.operand2_label.setObjectName("operand2_label")
        self.horizontalLayout_4.addWidget(self.operand2_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.feedback = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.feedback.setFont(font)
        self.feedback.setText("")
        self.feedback.setObjectName("feedback")
        self.horizontalLayout_6.addWidget(self.feedback)
        self.result_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_lineEdit.sizePolicy().hasHeightForWidth())
        self.result_lineEdit.setSizePolicy(sizePolicy)
        self.result_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.result_lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.result_lineEdit.setFont(font)
        self.result_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lineEdit.setObjectName("result_lineEdit")
        self.horizontalLayout_6.addWidget(self.result_lineEdit)
        self.feedback2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.feedback2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.feedback2.setFont(font)
        self.feedback2.setText("")
        self.feedback2.setObjectName("feedback2")
        self.horizontalLayout_6.addWidget(self.feedback2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.aciertos_progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.aciertos_progressBar.setMaximumSize(QtCore.QSize(325, 16777215))
        self.aciertos_progressBar.setProperty("value", 100)
        self.aciertos_progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.aciertos_progressBar.setObjectName("aciertos_progressBar")
        self.horizontalLayout.addWidget(self.aciertos_progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.tiempo_restante_progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.tiempo_restante_progressBar.setMaximumSize(QtCore.QSize(325, 16777215))
        self.tiempo_restante_progressBar.setMaximum(60)
        self.tiempo_restante_progressBar.setProperty("value", 60)
        self.tiempo_restante_progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tiempo_restante_progressBar.setObjectName("tiempo_restante_progressBar")
        self.horizontalLayout_2.addWidget(self.tiempo_restante_progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reset_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_pushButton.setSizePolicy(sizePolicy)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout_3.addWidget(self.reset_pushButton)
        self.stop_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_pushButton.sizePolicy().hasHeightForWidth())
        self.stop_pushButton.setSizePolicy(sizePolicy)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.horizontalLayout_3.addWidget(self.stop_pushButton)
        self.start_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy)
        self.start_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout_3.addWidget(self.start_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculo Mental"))
        self.label_2.setText(_translate("Form", "Aciertos"))
        self.label_3.setText(_translate("Form", "Tiempo"))
        self.tiempo_restante_progressBar.setFormat(_translate("Form", "%v"))
        self.reset_pushButton.setText(_translate("Form", "Reset"))
        self.stop_pushButton.setText(_translate("Form", "Stop"))
        self.start_pushButton.setText(_translate("Form", "Start"))

    def ui_init_status(self):
        self.start_pushButton.setDisabled(False)
        self.reset_pushButton.setDisabled(True)
        self.stop_pushButton.setDisabled(True)
        self.result_lineEdit.setDisabled(True)
        self.start_pushButton.setText('Start')
        self.operator_label.setText('')
        self.operand1_label.setText('')
        self.operand2_label.setText('')
        self.result_lineEdit.setText('')
        self.feedback.setText('')
        self.feedback2.setText('')
        self.start_pushButton.setFocus()

    def ui_running_status(self):
        self.reset_pushButton.setDisabled(True)
        self.start_pushButton.setDisabled(True)
        self.stop_pushButton.setDisabled(False)
        self.result_lineEdit.setDisabled(False)

    def ui_paused_status(self):
        self.start_pushButton.setDisabled(False)
        self.reset_pushButton.setDisabled(False)
        self.stop_pushButton.setDisabled(True)
        self.result_lineEdit.setDisabled(True)
        self.start_pushButton.setText('Resume')

    def ui_over_status(self):
        self.start_pushButton.setDisabled(True)
        self.reset_pushButton.setDisabled(True)
        self.stop_pushButton.setDisabled(True)
        self.result_lineEdit.setDisabled(True)
        self.start_pushButton.setText('Start')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
