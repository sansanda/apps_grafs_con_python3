# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'words_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QButtonGroup, QRadioButton, QSizePolicy, QLayout, \
    QAbstractScrollArea, QFrame

from utils.ui.ui_components import WordsSearch_2DArrayOfButtons_Widget


class UiSudokuForm(object):
    width = 600
    heigth = 800

    def setupUi(self, SudokuForm):
        SudokuForm.setObjectName("Sudoku_Form")
        SudokuForm.resize(UiSudokuForm.width, UiSudokuForm.heigth)

        self.vertical_layout = QtWidgets.QVBoxLayout(SudokuForm)
        self.vertical_layout.setContentsMargins(20, 20, 20, 20)
        self.vertical_layout.setSpacing(50)
        self.vertical_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_1.setSpacing(10)
        self.horizontal_layout_0 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_0.setSpacing(10)

        # create a table of 9x9
        self.n_rows = self.n_columns = 9
        self.row_heigth = self.column_width = 60
        self.sudoku_table = QTableWidget(self.n_rows, self.n_columns, SudokuForm)
        self.sudoku_table.setMinimumSize(self.n_columns * self.column_width + 2,
                                         self.n_rows * self.row_heigth + 2)
        self.sudoku_table.setContentsMargins(5, 5, 5, 5)
        self.sudoku_table.verticalHeader().setVisible(False)
        self.sudoku_table.horizontalHeader().setVisible(False)

        for r in range(0, self.n_rows):
            self.sudoku_table.setRowHeight(r, self.row_heigth)
        for c in range(0, self.n_columns):
            self.sudoku_table.setColumnWidth(c, self.column_width)

        for r in range(1, self.n_rows + 1):
            for c in range(1, self.n_columns + 1):
                item = QTableWidgetItem()
                self.sudoku_table.setItem(r, c, item)

        self.vertical_layout.addWidget(self.sudoku_table, 2, Qt.AlignCenter)

        # create and add the group of radio buttons
        self.difficulty_level_radio_buttons_group = QButtonGroup(SudokuForm)  # Number group
        difficulty_levels = 5
        for level_number in range(1, difficulty_levels + 1):
            rb = QRadioButton(str(level_number))
            self.difficulty_level_radio_buttons_group.addButton(rb)
            self.horizontal_layout_1.addWidget(rb)
        last_rb = QRadioButton('Solution')
        self.difficulty_level_radio_buttons_group.addButton(last_rb)
        self.horizontal_layout_1.addWidget(last_rb)
        self.vertical_layout.addLayout(self.horizontal_layout_1, 0)

        # create and add the buttons
        self.generar_sudoku_pushButton = QtWidgets.QPushButton(SudokuForm)
        self.generar_sudoku_pushButton.setMaximumSize(200, 75)
        self.generar_sudoku_pushButton.setMinimumSize(200, 75)
        self.generar_sudoku_pushButton.setObjectName("generar_sudoku_pushButton")
        self.generar_sudoku_pushButton.setText('Generar Sudoku')
        self.horizontal_layout_0.addWidget(self.generar_sudoku_pushButton, 0, Qt.AlignCenter)

        self.visualizar_sudoku_pushButton = QtWidgets.QPushButton(SudokuForm)
        self.visualizar_sudoku_pushButton.setMaximumSize(200, 75)
        self.visualizar_sudoku_pushButton.setMinimumSize(200, 75)
        self.visualizar_sudoku_pushButton.setObjectName("visualizar_sudoku_pushButton")
        self.visualizar_sudoku_pushButton.setText('Visualizar Sudoku')
        self.horizontal_layout_0.addWidget(self.visualizar_sudoku_pushButton, 0, Qt.AlignCenter)

        self.comprobar_solucion_pushButton = QtWidgets.QPushButton(SudokuForm)
        self.comprobar_solucion_pushButton.setMaximumSize(200, 75)
        self.comprobar_solucion_pushButton.setMinimumSize(200, 75)
        self.comprobar_solucion_pushButton.setObjectName("comprobar_solucion_pushButton")
        self.comprobar_solucion_pushButton.setText('Visualizar Sudoku')
        self.horizontal_layout_0.addWidget(self.comprobar_solucion_pushButton, 0, Qt.AlignCenter)
        self.vertical_layout.addLayout(self.horizontal_layout_0, 0)

        SudokuForm.setLayout(self.vertical_layout)

        self.retranslateUi(SudokuForm)
        QtCore.QMetaObject.connectSlotsByName(SudokuForm)

    def retranslateUi(self, Sudoku_Form):
        _translate = QtCore.QCoreApplication.translate
        Sudoku_Form.setWindowTitle(_translate("Sudoku_Form", "FRUITS Words Search"))
        self.generar_sudoku_pushButton.setText(_translate("Sudoku_Form", "Generar Sudoku"))
        self.visualizar_sudoku_pushButton.setText(_translate("Sudoku_Form", "Visualizar Sudoku"))
        self.comprobar_solucion_pushButton.setText(_translate("Sudoku_Form", "Comprobar Solución"))

    def ui_init_status(self, remaining_time):
        pass

    def ui_running_status(self):
        pass

    def ui_paused_status(self):
        pass

    def ui_over_status(self):
        pass
