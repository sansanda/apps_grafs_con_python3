import random
import string
from enum import IntFlag, auto
from time import sleep

from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from sortedcontainers import SortedList

import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class CellIn2DArray(QPushButton):

    def __init__(self, parent=None, row=0, column=0, width=30, height=30, text='X') -> None:
        super().__init__(parent)
        self.setText(text)
        # zero based position inside a 2D array
        self.row = row
        self.column = column
        self.position_in_array = self.row * 100 + self.column
        self.setFixedSize(width, height)
        self.background_color = ''
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
        self.update_background_color()

    def set_selected(self, selected):
        self.selected = selected
        self.update_background_color()

    def update_background_color(self):
        if self.isEnabled():
            self.background_color = 'lightgreen'
            if self.selected:
                self.background_color = 'orange'
        else:
            self.background_color = 'lightgrey'
            if self.selected:
                self.background_color = 'lime'
        self.setStyleSheet("background-color: " + self.background_color)

    def __str__(self) -> str:
        r = super().__str__() + ':\n'
        r = r + '{\n'
        r = r + '\ttext = ' + self.text() + '\n'
        r = r + '\trow, column = ' + str(self.row) + ',' + str(self.column) + '\n'
        r = r + '\tposition in array = ' + str(self.position_in_array) + '\n'
        r = r + '\twidth, height = ' + str(self.width()) + ',' + str(self.height()) + '\n'
        r = (r + '\tenable, selected = ' +
             str(self.isEnabled()) + ', ' + str(self.selected) + ', ' + '\n')
        r = r + '\tbackground_color = ' + self.background_color + '\n'
        r = r + '}'
        return r


class Buttons2DArrayWidget(QWidget):
    ALL_NEIGHBOURS = 'ALL'
    COLUMN_NEIGHBOURS = 'COLUMN_NEIGHBOURS'
    ROW_NEIGHBOURS = 'ROW_NEIGHBOURS'
    RISING_DIAGONAL_NEIGHBOURS = 'RISING_DIAGONAL_NEIGHBOURS'
    FALLING_DIAGONAL_NEIGHBOURS = 'FALLING_DIAGONAL_NEIGHBOURS'
    valid_cell_neighbours = [ALL_NEIGHBOURS,
                             COLUMN_NEIGHBOURS,
                             ROW_NEIGHBOURS,
                             RISING_DIAGONAL_NEIGHBOURS,
                             FALLING_DIAGONAL_NEIGHBOURS]

    def __init__(self, parent=None, n_rows=15, n_columns=15, buttons_w=30, buttons_h=30):

        super().__init__(parent)
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.selected_buttons = SortedList()
        self.layout = QtWidgets.QGridLayout(self)
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                button = CellIn2DArray(self, r, c, buttons_w, buttons_h, '')
                button.clicked.connect(lambda foo_param, x=button: self.clicked_event_handler(x))
                self.layout.addWidget(button, r, c)
        self.setLayout(self.layout)
        self.random_populate_all_buttons(overwrite=False)

    def enable_all_buttons(self, enable):
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                self.layout.itemAtPosition(r, c).widget().set_enable(enable)

    def select_all_buttons(self, select):
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                self.layout.itemAtPosition(r, c).widget().set_selected(select)

    def get_button_neighbours(self, button: CellIn2DArray, which_neighbours: str):
        # logging.info('looking for the neighbours of the button: %s', str(cell))
        nbs = which_neighbours.upper()
        if which_neighbours not in self.valid_cell_neighbours:
            raise Exception("Not valid value for neighbours\n. Valid types are:  %s", self.valid_cell_neighbours)
        item = self.layout.itemAtPosition(button.row, button.column).widget()
        # logging.debug('cell getted in layout at pos (%s,%s) = %s ', cell.row, cell.column, str(item))
        if button != item:
            raise Exception("Cell not found in GridLayout.\n")
        neighbours = SortedList()
        if which_neighbours == self.ROW_NEIGHBOURS:
            if button.column > 0:
                neighbours.add(self.layout.itemAtPosition(button.row, button.column - 1).widget())
            if button.column < self.n_columns - 1:
                neighbours.add(self.layout.itemAtPosition(button.row, button.column + 1).widget())
        if which_neighbours == self.COLUMN_NEIGHBOURS:
            if button.row > 0:
                neighbours.add(self.layout.itemAtPosition(button.row - 1, button.column).widget())
            if button.row < self.n_rows - 1:
                neighbours.add(self.layout.itemAtPosition(button.row + 1, button.column).widget())
        if which_neighbours == self.RISING_DIAGONAL_NEIGHBOURS:
            if (button.row + 1) < self.n_rows and (button.column - 1) >= 0:
                neighbours.add(self.layout.itemAtPosition(button.row + 1, button.column - 1).widget())
            if (button.row - 1) >= 0 and (button.column + 1) < self.n_columns:
                neighbours.add(self.layout.itemAtPosition(button.row - 1, button.column + 1).widget())
        if which_neighbours == self.FALLING_DIAGONAL_NEIGHBOURS:
            if (button.row - 1) >= 0 and (button.column - 1) >= 0:
                neighbours.add(self.layout.itemAtPosition(button.row - 1, button.column - 1).widget())
            if (button.row + 1) < self.n_rows and (button.column + 1) < self.n_columns:
                neighbours.add(self.layout.itemAtPosition(button.row + 1, button.column + 1).widget())
        if which_neighbours == self.ALL_NEIGHBOURS:
            for n in self.get_button_neighbours(button, self.ROW_NEIGHBOURS):
                neighbours.add(n)
            for n in self.get_button_neighbours(button, self.COLUMN_NEIGHBOURS):
                neighbours.add(n)
            for n in self.get_button_neighbours(button, self.RISING_DIAGONAL_NEIGHBOURS):
                neighbours.add(n)
            for n in self.get_button_neighbours(button, self.FALLING_DIAGONAL_NEIGHBOURS):
                neighbours.add(n)
        return neighbours

    def clicked_event_handler(self, clicked_button):
        if clicked_button.selected:
            self.selected_buttons.remove(clicked_button)
        else:
            self.selected_buttons.add(clicked_button)
        self.show_next_selectable_buttons()

    def show_next_selectable_buttons(self):
        """
        Show possible next selectable buttons in function of which pattern define the selected buttons.
        Patterns:\n
        0. no buttons selected
        1. single button selected
        2. selected buttons defining a row
        3. selected buttons defining a column
        4. selected buttons defining a diagonal which can be rising or falling
        :return: None
        """
        # no buttons selected
        if len(self.selected_buttons) == 0:
            # enable all buttons and set all unselected
            self.enable_all_buttons(True)
            self.select_all_buttons(False)
        # single button pattern
        if len(self.selected_buttons) == 1:
            # disable a deselect all buttons
            self.enable_all_buttons(False)
            self.select_all_buttons(False)
            self.selected_buttons[0].set_enable(True)
            self.selected_buttons[0].set_selected(True)
            nbs = self.get_button_neighbours(self.selected_buttons[0], self.ALL_NEIGHBOURS)
            for n in nbs:
                n.set_enable(True)
        # two buttons selected than can define: row, column or diagonal
        if len(self.selected_buttons) >= 2:
            self.enable_all_buttons(False)
            self.select_all_buttons(False)
            # disable all buttons except the first and the last selected
            for i, b in enumerate(self.selected_buttons):
                if i == 0 or i == (len(self.selected_buttons) - 1):
                    b.set_selected(True)
                    b.set_enable(True)
                else:
                    b.set_selected(True)
                    b.set_enable(False)
            delta_r = self.selected_buttons[0].row - self.selected_buttons[-1].row
            delta_c = self.selected_buttons[0].column - self.selected_buttons[-1].column
            logging.debug('delta_r, delta_c = %s, %s', delta_r, delta_c)
            extrem_neighbours_to_enable = None
            if delta_r == 0:
                # row pattern
                extrem_neighbours_to_enable = self.ROW_NEIGHBOURS
            elif delta_c == 0:
                # column pattern
                extrem_neighbours_to_enable = self.COLUMN_NEIGHBOURS
            elif delta_c > 0:
                # rising diagonal pattern
                extrem_neighbours_to_enable = self.RISING_DIAGONAL_NEIGHBOURS
            elif delta_c < 0:
                # falling diagonal pattern
                extrem_neighbours_to_enable = self.FALLING_DIAGONAL_NEIGHBOURS
            self.get_button_neighbours(self.selected_buttons[0], extrem_neighbours_to_enable)[0].set_enable(True)
            self.get_button_neighbours(self.selected_buttons[-1], extrem_neighbours_to_enable)[1].set_enable(True)

    def random_populate_all_buttons(self,
                                    alphabet=[s.upper() for s in string.ascii_lowercase],
                                    overwrite=True):
        logging.info('Populating the 2D array')
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                button = self.layout.itemAtPosition(r, c).widget()
                if len(button.text()) == 0 or overwrite:
                    self.layout.itemAtPosition(r, c).widget().setText(random.sample(alphabet, 1)[0])

    def hide_word(self, word_to_hide, enable_collisions=True):
        reverse = random.sample([True, False], 1)
        if reverse:
            word_to_hide = word_to_hide[::-1]
        orientation = random.sample(['ROW', 'COLUMN', 'R_DIAGONAL', 'F_DIAGONAL'], 1)
        starting_row = random.randint(0, self.n_rows - len(word_to_hide) + 1)
        starting_column = random.randint(0, self.n_columns - len(word_to_hide) + 1)


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
    w = Buttons2DArrayWidget(None, 15, 15)
    sys.exit(app.exec_())
