import typing
from enum import IntFlag, auto

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

from sortedcontainers import SortedList

class State(IntFlag):
    """
    Auxiliary class create for translating the instance states string into
    an Enum_IntEnum that will help to the app to manage such states.
    """
    ENABLE = auto()
    SELECTED = auto()
    SELECTABLE = auto()


class CellIn2DArray(QPushButton):

    def __init__(self, parent: typing.Optional[QWidget] = ..., row=0, column=0, width=30, height=30, text='X') -> None:
        super().__init__(parent)
        self.setText(text)
        # zero based position inside a 2D array
        self.row = row
        self.column = column
        self.position_in_array = self.row * 100 + self.column
        self.setFixedSize(width, height)
        self.background_color = ''
        self.enable = None
        self.selected = None

        self.set_enable(True)
        self.set_selected(False)

    def __lt__(self, other):
        comp = False
        if self.position_in_array < other.position_in_array:
            comp = True
        return comp

    def set_enable(self, enable):
        self.setEnabled(enable)
        self.setEnabled(enable)
        self.enable = enable
        self.update_background_color()

    def set_selected(self, selected):
        self.selected = selected
        self.update_background_color()

    def update_background_color(self):
        if self.enable:
            self.background_color = 'Lightgreen'
            if self.selected:
                self.background_color = 'Orange'
        else:
            self.background_color = 'Lightgrey'
            if self.selected:
                self.background_color = 'Lightorange'
        self.setStyleSheet("background-color: " + self.background_color)

    def __str__(self) -> str:
        r = super().__str__() + ':\n'
        r = r + '{\n'
        r = r + '\ttext = ' + self.text() + '\n'
        r = r + '\trow, column = ' + str(self.row) + ',' + str(self.column) + '\n'
        r = r + '\tposition in array = ' + str(self.position_in_array) + '\n'
        r = r + '\twidth, height = ' + str(self.width()) + ',' + str(self.height()) + '\n'
        r = (r + '\tenable, selected = ' +
             str(self.enable) + ', ' + str(self.selected) + ', ' + '\n')
        r = r + '\tbackground_color = ' + self.background_color + '\n'
        r = r + '}'
        return r


class Buttons2DArrayWidget(QWidget):

    valid_cell_neighbours = ['ALL', 'COLUMN', 'ROW', 'RISING_DIAGONAL', 'FALLING_DIAGONAL']

    def __init__(self, parent=..., flags=..., n_rows=15, n_columns=15):
        super().__init__(parent, flags)
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.selected_buttons = SortedList()
        self.layout = QtWidgets.QGridLayout
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                cell = CellIn2DArray(self, r, c)
                cell.clicked.connect(lambda foo_param, x=cell: self.clicked_event_handler(x))
                self.layout.addWidget(cell, r, c)
        self.setLayout(self.layout)

    def get_neighbours(self, cell: CellIn2DArray, which_neighbours: str):
        nbs = which_neighbours.upper()
        if which_neighbours not in self.valid_cell_neighbours:
            raise Exception("Not valid value for neighbours\n. Valid types are:  %s", self.valid_cell_neighbours)
        item = self.layout().itemAtPosition(cell.row, cell.column)
        if cell != item:
            raise Exception("Cell not found in GridLayout.\n")
        

    def clicked_event_handler(self, cell):
        if self.selected:
            self.set_selected(False)
            self.selected_buttons.remove(cell)
        else:
            self.set_selected(True)
            self.selected_buttons.add(cell)

    def __str__(self):
        r = ''
        r = r + super().__str__() + ':\n'
        r = r + '{\n'

        r = r + '}'

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    b = CellIn2DArray(None, 0, 1, 30, 30, 'X')
    print(b)
    b.set_selected(True)
    print(b)
    b.set_enable(False)
    print(b)
    sys.exit(app.exec_())
