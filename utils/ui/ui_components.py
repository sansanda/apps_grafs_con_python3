import random
import string
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt, QObject
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from sortedcontainers import SortedList

import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class CellIn2DArray(QPushButton):
    EMPTY_CELL_CHARACTER = '*'

    def __init__(self, parent=None, row=0, column=0, width=30, height=30, text=EMPTY_CELL_CHARACTER) -> None:
        super().__init__(parent)
        self.setText(text)
        # zero based position inside a 2D array
        self.row = row
        self.column = column
        self.position_in_array = self.row * 100 + self.column
        self.setFixedSize(width, height)
        self.background_color = ''
        self.text_color = ''
        self.marked = None
        self.selected = None
        self.blocked = None
        self.set_blocked(False)
        self.set_enable(True)
        self.set_selected(False)

    def __lt__(self, other):
        comp = False
        if self.position_in_array < other.position_in_array:
            comp = True
        return comp

    def set_marked(self, marked):
        self.marked = marked
        self.update_style()

    def set_blocked(self, blocked):
        self.blocked = blocked
        self.update_style()

    def set_enable(self, enable):
        if not self.blocked:
            self.setEnabled(enable)
            self.update_style()

    def set_selected(self, selected):
        self.selected = selected
        self.update_style()

    def update_style(self):
        if self.isEnabled():
            self.background_color = 'lightgreen'  # lightgrey
            if self.marked:
                self.background_color = 'orange'
            if self.selected:
                self.background_color = 'lightgrey'
                self.text_color = 'black'
                if self.marked:
                    self.background_color = 'red'
        else:
            self.background_color = 'darkgrey'
            self.text_color = 'black'
            if self.selected:
                self.background_color = 'lightgrey'
                self.text_color = 'black'
                if self.marked:
                    self.background_color = 'red'

        self.setStyleSheet(
            "font-weight: bold; background-color: " + self.background_color + "; color: " + self.text_color)

    def __str__(self) -> str:
        r = super().__str__() + ':\n'
        r = r + '{\n'
        r = r + '\ttext = ' + self.text() + '\n'
        r = r + '\trow, column = ' + str(self.row) + ',' + str(self.column) + '\n'
        r = r + '\tposition in array = ' + str(self.position_in_array) + '\n'
        r = r + '\twidth, height = ' + str(self.width()) + ',' + str(self.height()) + '\n'
        r = (r + '\tenable = ' + str(self.isEnabled()) + ', selected = ' + str(self.selected) +
             ', blocked = ' + str(self.blocked) + ', marked = ' + str(self.marked))
        r = r + '\tbackground_color = ' + self.background_color + '\n'
        r = r + '\ttext = ' + self.text() + '\n'

        r = r + '}'
        return r


class WordsSearch_2DArrayOfButtons_Widget(QWidget):
    text_available = pyqtSignal(str)

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
    COLUMN_ORIENTATION = 'COLUMN_ORIENTATION'
    ROW_ORIENTATION = 'ROW_ORIENTATION'
    RISING_DIAGONAL_ORIENTATION = 'RISING_DIAGONAL_ORIENTATION'
    FALLING_DIAGONAL_ORIENTATION = 'FALLING_DIAGONAL_ORIENTATION'

    def __init__(self, parent=None, n_rows=15, n_columns=15, buttons_w=30, buttons_h=30):
        super().__init__(parent)
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.selected_buttons = SortedList()
        self.selectable_buttons = list()
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setSpacing(0)
        parent.word_matched.connect(self.word_matched)
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                button = CellIn2DArray(self, r, c, buttons_w, buttons_h,
                                       CellIn2DArray.EMPTY_CELL_CHARACTER)
                button.clicked.connect(lambda foo_param, x=button: self.clicked_event_handler(x))
                self.layout.addWidget(button, r, c)
        self.setLayout(self.layout)
        # QtCore.QMetaObject.connectSlotsByName(parent)

    def word_matched(self):
        logging.info('Received signal word_matched from WordsSearchForm')
        # feedback for the gamer

        # continue game
        self.config_buttons_as(buttons_to_config=self.selected_buttons[:],
                               option='enable', enable=False)
        self.config_buttons_as(buttons_to_config=self.selected_buttons[:],
                               option='select', enable=False)
        self.config_buttons_as(buttons_to_config=self.selected_buttons[:],
                               option='block', enable=True)
        self.selected_buttons = SortedList()

    def clicked_event_handler(self, clicked_button):
        logging.debug("clicked_event_handler(self, clicked_button): clicked_button = %s", clicked_button)
        if clicked_button.selected:
            clicked_button.set_selected(False)
            self.selected_buttons.remove(clicked_button)
            if len(self.selected_buttons) > 0:
                self.config_buttons_as(buttons_to_config=[self.selected_buttons[0], self.selected_buttons[-1]],
                                       option='enable', enable=True)
                self.config_buttons_as(buttons_to_config=self.selected_buttons[1:-1],
                                       option='enable', enable=False)
                self.config_buttons_as(buttons_to_config=self.get_next_selectable_buttons(),
                                       option='enable', enable=True)
        else:
            if len(self.selected_buttons) == 0:
                clicked_button.set_selected(True)
                self.selected_buttons.add(clicked_button)
                self.config_buttons_as(buttons_to_config=[self.selected_buttons[0], self.selected_buttons[-1]],
                                       option='enable', enable=True)
                self.config_buttons_as(buttons_to_config=self.selected_buttons[1:-1],
                                       option='enable', enable=False)
                self.config_buttons_as(buttons_to_config=self.get_next_selectable_buttons(),
                                       option='enable', enable=True)
            else:
                if clicked_button not in self.get_next_selectable_buttons():
                    self.config_buttons_as(buttons_to_config=self.selected_buttons[:],
                                           option='select', enable=False)
                    self.config_buttons_as(buttons_to_config=self.selected_buttons[:],
                                           option='enable', enable=True)
                    self.selected_buttons = SortedList()
                    clicked_button.set_selected(True)
                    self.selected_buttons.add(clicked_button)
                    self.config_buttons_as(buttons_to_config=[self.selected_buttons[0], self.selected_buttons[-1]],
                                           option='enable', enable=True)
                    self.config_buttons_as(buttons_to_config=self.selected_buttons[1:-1],
                                           option='enable', enable=False)
                    self.config_buttons_as(buttons_to_config=self.get_next_selectable_buttons(),
                                           option='enable', enable=True)
                else:
                    clicked_button.set_selected(True)
                    self.selected_buttons.add(clicked_button)
                    self.config_buttons_as(buttons_to_config=[self.selected_buttons[0], self.selected_buttons[-1]],
                                           option='enable', enable=True)
                    self.config_buttons_as(buttons_to_config=self.selected_buttons[1:-1],
                                           option='enable', enable=False)
                    self.config_buttons_as(buttons_to_config=self.get_next_selectable_buttons(),
                                           option='enable', enable=True)
        txt = self.get_buttons_text(self.selected_buttons)
        logging.debug("clicked_event_handler(self, clicked_button): "
                      "emitting text available signal('%s')", txt)
        self.text_available.emit(txt)

    def init_array(self):
        self.selected_buttons = SortedList()
        self.selectable_buttons = list()
        self.config_buttons_as(buttons_to_config='all', option='block', enable=False)
        self.config_buttons_as(buttons_to_config='all', option='enable', enable=False)
        self.config_buttons_as(buttons_to_config='all', option='select', enable=False)
        self.config_buttons_as(buttons_to_config='all', option='mark', enable=False)
        self.initialize_buttons_text(text=CellIn2DArray.EMPTY_CELL_CHARACTER)

    def config_buttons_as(self, buttons_to_config='all', option='select', enable=True):
        _buttons_to_config = list()
        if buttons_to_config is None:
            return
        if type(buttons_to_config) is not list and type(buttons_to_config) is not str:
            return
        if type(buttons_to_config) is list and len(buttons_to_config) == 0:
            return
        if type(buttons_to_config) is str and buttons_to_config.upper() == 'ALL':
            for button in self.get_all_buttons():
                _buttons_to_config.append(button)
        else:
            for button in buttons_to_config:
                _buttons_to_config.append(button)

        if option == 'mark':
            for button in _buttons_to_config:
                button.set_marked(enable)
        elif option == 'select':
            for button in _buttons_to_config:
                button.set_selected(enable)
        elif option == 'block':
            for button in _buttons_to_config:
                button.set_blocked(enable)
        elif option == 'enable':
            for button in _buttons_to_config:
                button.set_enable(enable)

    def get_all_buttons(self):
        buttons = list()
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                buttons.append(self.layout.itemAtPosition(r, c).widget())
        return buttons

    def get_button_neighbours(self, button: CellIn2DArray, which_neighbours: str):
        # logging.info('looking for the neighbours of the button: %s', str(cell))
        nbs = which_neighbours.upper()
        if which_neighbours not in self.valid_cell_neighbours:
            raise Exception("Not valid value for neighbours\n. Valid types are:  %s", self.valid_cell_neighbours)
        item = self.layout.itemAtPosition(button.row, button.column).widget()
        # logging.debug('cell got in layout at pos (%s,%s) = %s ', cell.row, cell.column, str(item))
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

    def get_next_selectable_buttons(self):
        """
        return a list with the possible next selectable buttons in function of which pattern define the selected buttons.
        Patterns:\n
        0. no buttons selected
        1. single button selected
        2. selected buttons defining a row
        3. selected buttons defining a column
        4. selected buttons defining a diagonal which can be rising or falling
        :return: list with the possible selectable buttons
        """
        selectable_buttons = list()
        if len(self.selected_buttons) == 0:
            # no buttons selected pattern
            for r in range(self.n_rows):
                for c in range(self.n_columns):
                    selectable_buttons.append(self.layout.itemAtPosition(r, c).widget())
        if len(self.selected_buttons) == 1:
            # single button selected pattern
            # disable a deselect all buttons
            nbs = self.get_button_neighbours(self.selected_buttons[0], self.ALL_NEIGHBOURS)
            for n in nbs:
                selectable_buttons.append(n)
        if len(self.selected_buttons) >= 2:
            # two buttons selected pattern than can define: row, column or diagonal
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
            first_button_neighbours = self.get_button_neighbours(self.selected_buttons[0], extrem_neighbours_to_enable)
            if len(first_button_neighbours) > 1:
                selectable_buttons.append(first_button_neighbours[0])
            last_button_neighbours = self.get_button_neighbours(self.selected_buttons[-1], extrem_neighbours_to_enable)
            if len(last_button_neighbours) > 1:
                selectable_buttons.append(last_button_neighbours[1])
        return selectable_buttons

    def random_populate_all_buttons(self,
                                    alphabet=[s.upper() for s in string.ascii_lowercase],
                                    overwrite=True):
        logging.info('Populating the 2D array')
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                button = self.layout.itemAtPosition(r, c).widget()
                if button.text() == CellIn2DArray.EMPTY_CELL_CHARACTER or overwrite:
                    self.layout.itemAtPosition(r, c).widget().setText(random.choice(alphabet))

    def get_buttons_line(self, starting_row, starting_column, orientation, n_buttons):
        logging.debug('getting buttons giving parameters: n_buttons = %s, '
                      'orientation = %s, '
                      'starting_row = %s, '
                      'starting_column = %s, ', n_buttons, orientation, starting_row, starting_column)
        buttons = []
        if orientation == self.ROW_ORIENTATION:
            if (starting_column + n_buttons) < self.n_columns:
                for c in range(starting_column, starting_column + n_buttons):
                    buttons.append(self.layout.itemAtPosition(starting_row, c).widget())
        elif orientation == self.COLUMN_ORIENTATION:
            if (starting_row + n_buttons) < self.n_rows:
                for r in range(starting_row, starting_row + n_buttons):
                    buttons.append(self.layout.itemAtPosition(r, starting_column).widget())
        elif orientation == self.FALLING_DIAGONAL_ORIENTATION:
            if (starting_row + n_buttons) < self.n_rows and (starting_column + n_buttons) < self.n_columns:
                for i, r in enumerate(range(starting_row, starting_row + n_buttons)):
                    buttons.append(self.layout.itemAtPosition(r, starting_column + i).widget())
        elif orientation == self.RISING_DIAGONAL_ORIENTATION:
            if (starting_row - n_buttons) >= 0 and (starting_column + n_buttons) < self.n_columns:
                for i, c in enumerate(range(starting_column, starting_column + n_buttons)):
                    buttons.append(self.layout.itemAtPosition(starting_row - i, c).widget())
        return buttons

    def get_buttons_text(self, buttons):
        logging.debug('getting buttons text done the buttons....')
        if len(buttons) == 0:
            return None
        s = ''
        for button in buttons:
            s = s + button.text()
        return s

    def insert_text_in_buttons(self, text, buttons, mark_button=False):
        for i, button in enumerate(buttons):
            if mark_button:
                button.set_marked(True)
            button.setText(text[i])

    def initialize_buttons_text(self, text=CellIn2DArray.EMPTY_CELL_CHARACTER, buttons='all', mark_button=False):
        if buttons is None:
            return
        if type(buttons) is not list and type(buttons) is not str:
            return
        if type(buttons) is list and len(buttons) == 0:
            return
        if type(buttons) is str and buttons.upper() == 'ALL':
            for r in range(self.n_rows):
                for c in range(self.n_columns):
                    if mark_button:
                        self.layout.itemAtPosition(r, c).widget().set_marked(True)
                    self.layout.itemAtPosition(r, c).widget().setText(text)
        else:
            for button in buttons:
                if mark_button:
                    button.set_marked(True)
                button.setText(text)

    def hide_words(self, words, mark_word=False, enable_collisions=True):
        for word in words:
            self.hide_word(word, mark_word, enable_collisions)

    def hide_word(self, word_to_hide, mark_word=False, enable_collisions=True):
        if len(word_to_hide) > self.n_rows or len(word_to_hide) > self.n_rows:
            raise Exception("Word too much long!!!")
        collision = True
        while collision:
            collision = False
            bad_parameters = True
            # get correct parameters for hiding the word
            while bad_parameters:
                bad_parameters = False
                # randomly get parameters for hiding the word
                reverse = random.choice([True, False])
                if reverse:
                    word_to_hide = word_to_hide[::-1]
                orientation = random.sample([self.ROW_ORIENTATION,
                                             self.COLUMN_ORIENTATION,
                                             self.RISING_DIAGONAL_ORIENTATION,
                                             self.FALLING_DIAGONAL_ORIENTATION], 1)[0]
                starting_row = random.randint(0, self.n_rows - len(word_to_hide))
                starting_column = random.randint(0, self.n_columns - len(word_to_hide))
                logging.debug('reverse = %s, '
                              'orientation = %s, '
                              'starting_row = %s, '
                              'starting_column = %s, ', reverse, orientation, starting_row, starting_column)
                buttons = self.get_buttons_line(starting_row, starting_column, orientation, len(word_to_hide))
                if len(buttons) == 0:
                    bad_parameters = True
            # detect collision
            bs_text = self.get_buttons_text(buttons)
            # If the buttons cells where we want to hide our word contains letters then there is a collision.
            # If there is a collision we have, again, to get the parameters for hiding the word
            for c in bs_text[:]:
                if c in string.ascii_letters:
                    collision = True
                    break
        # if we are here is because there is not collision,
        # then we can hide the word in the place indicated by the parameters.
        self.insert_text_in_buttons(word_to_hide, buttons, mark_word)

    def __str__(self):
        r = ''
        r = r + super().__str__() + ':\n'
        r = r + '{\n'

        r = r + '}'


class SudokuTableQWidget(QWidget):
    ui_sudoku_table_updated = pyqtSignal(list)
    ONE_DIGIT_INT_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, parent=None, column_width=60, row_height=60):
        super().__init__(parent)
        self.setObjectName("SudokuTableWidget")

        self.n_rows = self.n_columns = 9
        self.sudoku_table = [[None for _ in range(0, self.n_columns, 1)] for _ in range(0, self.n_rows, 1)]
        self.ui_table_rows_reserved_for_lines = [3, 7]
        self.ui_table_columns_reserved_for_lines = [3, 7]
        self.ui_table_rows_reserved_for_numbers = [0, 1, 2, 4, 5, 6, 8, 9, 10]
        self.ui_table_columns_reserved_for_numbers = [0, 1, 2, 4, 5, 6, 8, 9, 10]
        self.nonets_table_rows = [[0, 1, 2],
                                  [3, 4, 5],
                                  [6, 7, 8]]
        self.nonets_table_columns = [[0, 1, 2],
                                     [3, 4, 5],
                                     [6, 7, 8]]

        self.column_width = column_width
        self.row_height = row_height

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(0)
        self.gridLayout.setAlignment(Qt.AlignCenter)
        self.gridLayout.setContentsMargins(10, 10, 10, 20)

        # add the horizontal lines
        for r in self.ui_table_rows_reserved_for_lines:
            line = QtWidgets.QFrame(self)
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Plain)
            line.setLineWidth(10)
            line.setMidLineWidth(10)
            line.setObjectName("line_h" + str(r))
            self.gridLayout.addWidget(line, r, 0, 1, self.n_rows + len(self.ui_table_rows_reserved_for_lines),
                                      Qt.AlignTop)
        # add the vertical lines
        for c in self.ui_table_columns_reserved_for_lines:
            line = QtWidgets.QFrame(self)
            line.setFrameShape(QtWidgets.QFrame.VLine)
            line.setFrameShadow(QtWidgets.QFrame.Plain)
            line.setLineWidth(10)
            line.setMidLineWidth(10)
            line.setObjectName("line_v" + str(c))
            self.gridLayout.addWidget(line, 0, c, self.n_columns + len(self.ui_table_columns_reserved_for_lines), 1)

        # add the lineEdit widgets
        for r in self.ui_table_rows_reserved_for_numbers:
            for c in self.ui_table_columns_reserved_for_numbers:
                lineEdit = QtWidgets.QLineEdit(self)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(lineEdit.sizePolicy().hasHeightForWidth())
                lineEdit.setSizePolicy(sizePolicy)
                lineEdit.setAlignment(Qt.AlignCenter)
                lineEdit.setStyleSheet('font-size:12pt; font-weight: bold; color: dodgerblue;')
                lineEdit.setMinimumSize(QtCore.QSize(self.column_width, self.row_height))
                lineEdit.setMaximumSize(QtCore.QSize(self.column_width, self.row_height))
                lineEdit.row = r
                lineEdit.column = c
                lineEdit.setObjectName("cell" + str(r) + str(c))
                lineEdit.textChanged.connect(lambda foo_param, x=lineEdit: self._line_edit_change_handler(x))
                self.gridLayout.addWidget(lineEdit, r, c, 1, 1)

        self.setLayout(self.gridLayout)
        self.reset_ui_table()

    def reset_ui_table(self):
        for row in range(0, self.n_rows):
            for column in range(0, self.n_columns):
                self._insert_number_at_ui_table_pos(row, column, None)

    def _insert_random_numbers_in_ui_table_in_random_positions(self, n_numbers):
        for _ in range(0, n_numbers, 1):
            while True:
                random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_number = random.choice(self.ONE_DIGIT_INT_NUMBERS[1:])
                if (self.test_if_number_match_rules_of_sudoku(random_number, random_row, random_column) and
                        (not self.get_number_at_ui_table_pos(random_row, random_column))):
                    self._insert_number_at_ui_table_pos(random_row, random_column, random_number)
                    break

    def _insert_number_at_ui_table_pos(self, row, column, number):
        """
        Insert a number in the row and column done by ther parameters.
        From the function the sudoku table is a 9x9 numbers table
        :param row: the row where to insert (0 to 8 positions)
        :param column: the column where to insert (0 to 8 positions)
        :param number: the number to insert
        :return: None
        """
        if (number not in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS or
                row not in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1] or
                column not in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1]):
            return
        lineEdit = self.gridLayout.itemAtPosition(self.ui_table_rows_reserved_for_numbers[row],
                                                  self.ui_table_columns_reserved_for_numbers[column]).widget()
        lineEdit.setText(str(number))

    def get_number_at_ui_table_pos(self, row, column):
        """
        Gets the number in the row and column indicated by ther parameters.
        Sudoku table is a 9x9 table with cells (lineEdit widgets) positions that can hold a text (of a number)
        in the range of [1:9] inc.
        :param row: the row where it is the number (0 to 8 positions)
        :param column: the column where it is the number (0 to 8 positions)
        :return: the number at the position given by the row and column parameters or
        None if was impossible to obtain the number
        """
        number = None
        if (row not in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1] or
                column not in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1]):
            pass
        else:
            text = self.gridLayout.itemAtPosition(self.ui_table_rows_reserved_for_numbers[row],
                                                  self.ui_table_columns_reserved_for_numbers[column]).widget().text()
            try:
                number = int(text)
            except ValueError:
                pass
        return number

    def get_numbers_in_ui_table_row(self, row):
        """
        Gets the numbers in the row indicated by the parameter.
        Sudoku table is a 9x9 table with cells (lineEdit widgets) positions that can hold a text (of a number)
        in the range of [1:9] inc.
        :param row: the row where there are the numbers (0 to 8 positions)
        :return: a list containing the numbers of the row.
        The List can be full of None if the row was totally empty --> ""
        """
        row_numbers = []
        if row in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1]:
            for column in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1]:
                row_numbers.append(self.get_number_at_ui_table_pos(row, column))
        return row_numbers

    def get_numbers_in_ui_table_column(self, column):
        """
        Gets the numbers in the column indicated by the parameter.
        Sudoku table is a 9x9 table with cells (lineEdit widgets) positions that can hold a text (of a number)
        in the range of [1:9] inc.
        :param column: the column where there are the numbers (0 to 8 positions)
        :return: a list containing the numbers of the column.
        The List can be full of None if the column was totally empty --> ""
        """
        column_numbers = []
        if column in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1]:
            for row in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[:-1]:
                column_numbers.append(self.get_number_at_ui_table_pos(row, column))
        return column_numbers

    def get_numbers_in_ui_table_nonet(self, nonet_row, nonet_column):
        nonet_numbers = []
        if (nonet_column in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[0:3] and
                nonet_row in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[0:3]):
            for row in self.nonets_table_rows[nonet_row]:
                for column in self.nonets_table_columns[nonet_column]:
                    nonet_numbers.append(
                        self.get_number_at_ui_table_pos(row, column)
                    )
        return nonet_numbers

    def _get_nonet_indexes(self, row, column):
        nonet_row = nonet_column = None
        for row_index in range(0, len(self.nonets_table_rows)):
            if row in self.nonets_table_rows[row_index]:
                nonet_row = row_index
                break
        for column_index in range(0, len(self.nonets_table_columns)):
            if column in self.nonets_table_columns[column_index]:
                nonet_column = column_index
                break
        return nonet_row, nonet_column

    def test_if_number_match_rules_of_sudoku(self, number, row, column):
        match = True
        nonet_row, nonet_column = self._get_nonet_indexes(row, column)
        if (number in self.get_numbers_in_ui_table_row(row) or
                number in self.get_numbers_in_ui_table_column(column) or
                number in self.get_numbers_in_ui_table_nonet(nonet_row, nonet_column)):
            match = False
        return match

    def solve_the_sudoku_using_backtracking(self):
        pass

    # signal handlers
    def _line_edit_change_handler(self, lineEdit):
        """
        Checks the new value text value of the lineEdit Widget.
        Only accepts representations of integers numbers between the range "1" -- "9" inclusives.
        If the text entered is out of range then the "1" default value will be setted.
        :param lineEdit: The widget where the text has been changed.
        :return: None
        """
        # check if the text is a one digit integer between 1 and 9.
        # if yes --> leave it
        # if not --> set 1 as lene edit text
        text = lineEdit.text()
        if (text.isnumeric() and
                int(text) in SudokuTableQWidget.ONE_DIGIT_INT_NUMBERS[1:] and
                len(text) == 1
        ):
            # emit signal with the 2d table representation of the ui table
            pass
        else:
            lineEdit.setText(str(1))
        lineEdit.selectAll()
        self.ui_sudoku_table_updated.emit(self._convert_sudoku_ui_table_to_2D_numbers_list())

    def _update_ui_table_handler(self, sudoku_table):
        # from sudoku table to ui
        for row in range(0, self.n_rows, 1):
            for column in range(0, self.n_columns, 1):
                self._insert_number_at_ui_table_pos(row, column, sudoku_table[row][column])

    def _convert_sudoku_ui_table_to_2D_numbers_list(self):
        # from ui to 2D numbers list
        list = [[None for _ in range(0, self.n_columns, 1)] for _ in range(0, self.n_rows, 1)]
        for row in range(0, self.n_rows, 1):
            for column in range(0, self.n_columns, 1):
                list[row][column] = self.get_number_at_ui_table_pos(row, column)
        return list


import sys


def main():
    app = QApplication(sys.argv)
    parent = QtWidgets.QWidget(None)
    ex = SudokuTableQWidget(parent, 600, 600, 60, 60)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
