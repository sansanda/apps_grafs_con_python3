import logging
import random
import time
from enum import IntEnum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMessageBox
from ejercicios_realizados.sudoku.mi_solucion.sudoku2_ui import UiSudokuForm
from utils.data_structures.data_structures import (generate_empty_2D_list,
                                                   value_appearances_in,
                                                   get_nonet_coordinates,
                                                   get_2D_list_position_coordinates, _get_2D_list_sublist_coordinates)
from utils.timer_workers_etc.timers_workers_etc import TimerTickerWorker
import sys
import copy

_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=_format, level=logging.DEBUG, datefmt="%H:%M:%S")


class GameState(IntEnum):
    """
    Auxiliary class create for translating the instance states string into
    an Enum_IntEnum that will help to the app to manage such states.
    """
    GENERATING_SUDOKU = 0
    INITIATING = 1
    RUNNING = 2
    CHECKING_SOLUTION = 3


class SudokuForm(QtWidgets.QWidget):
    """
    SUDOKU GAME MAIN WIDGET
    Main Widget that shows the UI for interacting with the gamer.
    This widget contains the control of the data layer. I mean, all methods retating with the manage of the data
    like: reset tables, update tables, solve tables, check proposed solution, appearances of number in rows, etc...
    of the data layer.
    The data layer basically contains the bidimiensional list for the sudoku table
    and the bidimimensional list for the sovlved sudoku table.
    Also, comunicates with/from the UI layer with signals/slots.
    """
    sudoku_table_updated_signal = pyqtSignal(list)
    N_ROWS = 9
    N_COLUMNS = 9
    ONE_DIGIT_INT_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    SUDOKU_TABLE_NONETS_ROWS = [[0, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8]]
    SUDOKU_TABLE_NONETS_COLUMNS = [[0, 1, 2],
                                   [3, 4, 5],
                                   [6, 7, 8]]

    def __init__(self,
                 play_time=60,
                 interval=1000,
                 parent=None):

        QtWidgets.QWidget.__init__(self)

        self.ui = UiSudokuForm()
        self.ui.setupUi(self)
        self.status = GameState.INITIATING
        self._update_ui()

        self.play_time = play_time
        self.interval = interval
        self.remaining_time = self.play_time
        self.sudoku_table = generate_empty_2D_list()

        self.n_levels_of_difficulty = 6
        self.difficulty_level = 1
        self.N_CELLS_HIDE_INCREMENT = 10
        self.N_OF_TOTAL_CELLS = self.N_ROWS * self.N_COLUMNS
        self.n_cells_to_show = 60 - self.N_CELLS_HIDE_INCREMENT * (self.difficulty_level - 1)
        self.n_cells_to_hide = self.N_OF_TOTAL_CELLS - self.n_cells_to_show

        # Signals and Slots
        radio_buttons = [self.ui.difficulty_h_layout.itemAt(n).widget()
                         for n in range(0, self.n_levels_of_difficulty, 1)]
        for rb in radio_buttons:
            rb.clicked.connect(lambda foo_param, x=rb: self._on_ui_radio_button_clicked(x))
        self.ui.comprobar_solucion_pushButton.clicked.connect(self._on_comprobar_solucion_pushbutton_clicked)
        self.ui.sudoku_table.ui_sudoku_table_updated.connect(self._on_ui_sudoku_table_updated)

        self.status = GameState.GENERATING_SUDOKU
        self._update_ui()

        self.timer = QtCore.QTimer()
        self.timer.singleShot(2000, self._generate_and_show_sudoku_table)

    def _generate_and_show_sudoku_table(self):
        """
        Updates the sudoku_table instance and the sudoku_table_solved attributes.
        Generates a valid sudoku_table with only 20 numbers generated randomly in positions also randomly.
        Also, solves the sudoku table calling the function _solve_the_sudoku.
        Finally, emits the signal sudoku_table_updated_signal indicating that the attribute sudoku_table
        has been updated.
        :return: None
        """
        self.sudoku_table = generate_empty_2D_list()
        self.sudoku_table = self._insert_random_numbers_in_random_positions(self.sudoku_table, 20)
        self.sudoku_table_solved = self._solve_the_sudoku(copy.deepcopy(self.sudoku_table),
                                                          0,
                                                          0,
                                                          0,
                                                          10000)
        self.sudoku_table = self._hide_cells_randomly(copy.deepcopy(self.sudoku_table_solved), self.n_cells_to_hide)
        self.sudoku_table_updated_signal.emit(self.sudoku_table)

        self.status = GameState.RUNNING
        self._update_ui()

    def _on_comprobar_solucion_pushbutton_clicked(self):
        """
        Slot called when the user clicks the button comprobar_solucion_pushButton.
        Basically, checks if the user proposed solution for the sudoku is good or not and generates
        the subsequent feedback.
        :return: None
        """
        self.status = GameState.CHECKING_SOLUTION
        self._update_ui()

        if self.sudoku_table == self.sudoku_table_solved:
            while not QMessageBox.question(self,
                                           'Checking the proposed solution!!!!!',
                                           'Congrats!!! You Win!!!',
                                           QMessageBox.Yes) == QMessageBox.Yes:
                pass
        else:
            while not QMessageBox.question(self,
                                           'Checking the proposed solution!!!!!',
                                           'Sorry!!! There is something wrong with your proposition!!!',
                                           QMessageBox.Yes) == QMessageBox.Yes:
                pass

        self.status = GameState.RUNNING
        self._update_ui()

    def _on_ui_radio_button_clicked(self, radio_button):
        """
        Slot called when the user clicks any of the six radio buttons for changing the level of difficulty of the game.
        If the radio_button clicked is the Solucion radio_button the ui sudoku table will show the sudoku solved.
        If other radio_button is clicked the program will calculate the number of sudoku table cells to hide,
        will update the ui in generating sudoku mode, will call the _generate_and_show_sudoku_table method,
        will update the ui sudoku table with the new sudoku table values and will return the ui running mode.
        :return: None
        """
        try:
            last_char = int(radio_button.text()[-1])
        except ValueError:
            # the difficulty selected is for reveal the solution
            self.sudoku_table_updated_signal.emit(self.sudoku_table_solved)
            return

        # if you are here is because the radio button clicked is for change the difficulty level and not
        # for revealing the solution of the sudoku

        actual_difficulty_level = self.difficulty_level
        self.difficulty_level = last_char

        if not (self.difficulty_level == actual_difficulty_level):
            # the difficulty level has changed
            self.status = GameState.GENERATING_SUDOKU
            self._update_ui()
            self.n_cells_to_show = 60 - self.N_CELLS_HIDE_INCREMENT * (self.difficulty_level - 1)
            self.n_cells_to_hide = self.N_OF_TOTAL_CELLS - self.n_cells_to_show
            self.timer.singleShot(1000, self._generate_and_show_sudoku_table)
        else:
            self.sudoku_table_updated_signal.emit(self.sudoku_table)

    def _on_ui_sudoku_table_updated(self, updated_sudoku_table):
        """
        Slot called when the ui sudoku table is updated.
        Ui sudoku table and sudoku table must contain the same values.
        :return: None
        """
        self.sudoku_table = updated_sudoku_table

    def _update_ui(self):
        """
        Method that modifies the UI according the state of the game.
        For example, if called when the game status is GENERATING_SUDOKU all the buttons, radio_buttons and the
        other widgets of the UI will be disabled.
        :return: None
        """
        if self.status == GameState.GENERATING_SUDOKU:
            self.ui.ui_generating_sudoku_status()
        if self.status == GameState.INITIATING:
            self.ui.ui_initiating_status()
        if self.status == GameState.RUNNING:
            self.ui.ui_running_status()
        if self.status == GameState.CHECKING_SOLUTION:
            self.ui.ui_checking_solution_status()

    #########################################################################################################

    def _insert_random_numbers_in_random_positions(self, sudoku_table, n_numbers):
        for _ in range(0, n_numbers, 1):
            while True:
                random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                while sudoku_table[random_row][random_column] is not None:
                    random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                    random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                initial_coordinates = (random_row, 0)
                final_coordinates = (random_row, len(sudoku_table) - 1)
                random_row_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates, final_coordinates)
                initial_coordinates = (0, random_column)
                final_coordinates = (len(sudoku_table) - 1, random_column)
                random_column_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates, final_coordinates)
                random_nonet_coordinates = get_nonet_coordinates(random_row, random_column)
                initial_coordinates = (random_nonet_coordinates[0] * 3, random_nonet_coordinates[1] * 3)
                final_coordinates = (initial_coordinates[0] + 2, initial_coordinates[1] + 2)
                random_none_area_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates, final_coordinates)

                random_number = random.choice(self.ONE_DIGIT_INT_NUMBERS[1:])
                if (
                        value_appearances_in(sudoku_table, random_row_coordinates, random_number) == 0 and
                        value_appearances_in(sudoku_table, random_column_coordinates, random_number) == 0 and
                        value_appearances_in(sudoku_table, random_none_area_coordinates, random_number) == 0
                ):
                    sudoku_table[random_row][random_column] = random_number
                    break
        return sudoku_table

    def _hide_cells_randomly(self, sudoku_table, n_cells_to_hide):
        for _ in range(0, n_cells_to_hide, 1):
            while True:
                random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                while sudoku_table[random_row][random_column] is None:
                    random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                    random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                sudoku_table[random_row][random_column] = None
                break
        return sudoku_table

    def _appearances_in_nonet(self, sudoku_table, number, row, column):
        number_appearances = 0
        nonet_row, nonet_column = get_nonet_coordinates(row, column)
        for n in self._get_numbers_in_sudoku_table_nonet(sudoku_table, nonet_row, nonet_column):
            if n is None:
                continue
            if int(n) == number:
                number_appearances = number_appearances + 1
        return number_appearances

    def _solve_the_sudoku_by_backtracking(self,
                                          sudoku_table,
                                          from_row,
                                          from_column,
                                          recursion_depth,
                                          max_recursion_depth):
        if recursion_depth > max_recursion_depth:
            # we have reached the maximum recursion depth and still there is no solution for the sudoku table
            # we return None. There should be a new call with a better sudoku table proposition
            return None
        else:
            # we haven't reached the max recursion depth, we can still looking for the solution
            if ((sudoku_table[from_row][from_column] is not None) and
                    (from_row == self.N_ROWS - 1) and
                    (from_column == self.N_COLUMNS - 1)):
                # if you are here is because the algorithm has reached the end of the table and so it has a solution
                return sudoku_table
            else:
                # if you are here is because the algorithm hasn't reached the end of the table and, for the moment,
                # there is not a solution for the sudoku table copy
                if (sudoku_table[from_row][from_column] is None or
                        isinstance(sudoku_table[from_row][from_column], str)):
                    # if you are here is because the sudoku_table cell contains or None or a str int value
                    if sudoku_table[from_row][from_column] is None:
                        # if you are here is because the sudoku_table cell contains None
                        # we will search for a valid number for the cell in from_row_index, from_column_index coords
                        number = 1

                        initial_coordinates = (from_row, 0)
                        final_coordinates = (from_row, len(sudoku_table) - 1)
                        from_row_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates,
                                                                                final_coordinates)
                        initial_coordinates = (0, from_column)
                        final_coordinates = (len(sudoku_table) - 1, from_column)
                        from_column_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates,
                                                                                   final_coordinates)
                        nonet_coordinates = get_nonet_coordinates(from_row, from_column)
                        initial_coordinates = (nonet_coordinates[0] * 3, nonet_coordinates[1] * 3)
                        final_coordinates = (initial_coordinates[0] + 2, initial_coordinates[1] + 2)
                        nonet_area_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates,
                                                                                  final_coordinates)

                        while (
                                value_appearances_in(sudoku_table, from_row_coordinates, number) > 0 or
                                value_appearances_in(sudoku_table, from_column_coordinates, number) > 0 or
                                value_appearances_in(sudoku_table, nonet_area_coordinates, number) > 0
                        ):
                            number = number + 1
                            if number > 9:
                                break
                        # here the number could be 10 or less
                        if number > 9:
                            # then there is not a good number for this cell, we have to go backwards in the table
                            sudoku_table[from_row][from_column] = None
                            previous_row_index, previous_column_index = (
                                get_2D_list_position_coordinates(sudoku_table,
                                                                 (from_row, from_column),
                                                                 next_or_previous='previous_position'))
                            return self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                          previous_row_index,
                                                                          previous_column_index,
                                                                          recursion_depth + 1,
                                                                          max_recursion_depth)
                        else:
                            # there is a good number for this cell, then we can go to the next table position
                            sudoku_table[from_row][from_column] = str(number)
                            next_row_index, next_column_index = (
                                get_2D_list_position_coordinates(sudoku_table,
                                                                 (from_row, from_column),
                                                                 next_or_previous='next_position'))
                            return self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                          next_row_index,
                                                                          next_column_index,
                                                                          recursion_depth + 1,
                                                                          max_recursion_depth)
                    else:
                        # if you are here is because the sudoku_table cell contains a str int value
                        # this occurs because we are going back in the table
                        # then we have to search for another number from the number in the actual cell
                        number = int(sudoku_table[from_row][from_column])
                        if number == 9:
                            # if the cell contains the max number (9) then we have to set it to None
                            # and try with the previous cell
                            if from_row == 0 and from_column == 0:
                                # we have reach beginning (0,0) of the table going backwards and the 0,0 cell contains
                                # the number 9, it means that the algorithm can't find a solution for the sudoku table
                                # for _ in range(0, 30, 1):
                                #     print("NO SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                return None
                            else:
                                # the algorithm hasn't reached the beginning of the table so it still can go backwards
                                sudoku_table[from_row][from_column] = None
                                previous_row_index, previous_column_index = (
                                    get_2D_list_position_coordinates(sudoku_table,
                                                                     (from_row, from_column),
                                                                     next_or_previous='previous_position'))
                                return self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                              previous_row_index,
                                                                              previous_column_index,
                                                                              recursion_depth + 1,
                                                                              max_recursion_depth)
                        else:
                            # if the cell doesn't contain the max number (9) then we have can increase the cell value
                            # and try to go looking forward for the solution
                            number = number + 1

                            initial_coordinates = (from_row, 0)
                            final_coordinates = (from_row, len(sudoku_table) - 1)
                            from_row_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates,
                                                                                    final_coordinates)
                            initial_coordinates = (0, from_column)
                            final_coordinates = (len(sudoku_table) - 1, from_column)
                            from_column_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates,
                                                                                       final_coordinates)
                            nonet_coordinates = get_nonet_coordinates(from_row, from_column)
                            initial_coordinates = (nonet_coordinates[0] * 3, nonet_coordinates[1] * 3)
                            final_coordinates = (initial_coordinates[0] + 2, initial_coordinates[1] + 2)
                            nonet_area_coordinates = _get_2D_list_sublist_coordinates(initial_coordinates,
                                                                                      final_coordinates)

                            while (
                                    value_appearances_in(sudoku_table, from_row_coordinates, number) > 0 or
                                    value_appearances_in(sudoku_table, from_column_coordinates, number) > 0 or
                                    value_appearances_in(sudoku_table, nonet_area_coordinates, number) > 0
                            ):
                                number = number + 1
                                if number > 9:
                                    break
                            # here the number could be 10 or less
                            if number > 9:
                                # there is not a good number for this cell, the algorithm has to go backwards
                                sudoku_table[from_row][from_column] = None
                                previous_row_index, previous_column_index = (
                                    get_2D_list_position_coordinates(sudoku_table,
                                                                     (from_row, from_column),
                                                                     next_or_previous='previous_position'))
                                return self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                              previous_row_index,
                                                                              previous_column_index,
                                                                              recursion_depth + 1,
                                                                              max_recursion_depth)
                            else:
                                # there is a good number for this cell, then we can go to the next table position
                                sudoku_table[from_row][from_column] = str(number)
                                next_row_index, next_column_index = (
                                    get_2D_list_position_coordinates(sudoku_table,
                                                                     (from_row, from_column),
                                                                     next_or_previous='next_position'))
                                return self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                              next_row_index,
                                                                              next_column_index,
                                                                              recursion_depth + 1,
                                                                              max_recursion_depth)
                else:
                    # if you are here is because the cell already contains a number and this number is one of the very
                    # first random numbers introduced in the initialization of the sudoku table
                    # the algorithm has to mark the number as modificable (converting to an str number) and go forward
                    # for the solution.
                    sudoku_table[from_row][from_column] = str(
                        sudoku_table[from_row][from_column])
                    next_row_index, next_column_index = (
                        get_2D_list_position_coordinates(sudoku_table,
                                                         (from_row, from_column),
                                                         next_or_previous='next_position'))
                    return self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                  next_row_index,
                                                                  next_column_index,
                                                                  recursion_depth + 1,
                                                                  max_recursion_depth)

    def _solve_the_sudoku(self, sudoku_table,
                          from_row_index,
                          from_column_index,
                          recursion_depth,
                          max_recursion_depth):

        sudoku_table_solved = None
        while sudoku_table_solved is None:
            sudoku_table_solved = self._solve_the_sudoku_by_backtracking(sudoku_table,
                                                                         from_row_index,
                                                                         from_column_index,
                                                                         recursion_depth,
                                                                         max_recursion_depth)
            if sudoku_table_solved is None:
                sudoku_table = generate_empty_2D_list()
                sudoku_table = self._insert_random_numbers_in_random_positions(sudoku_table, 20)

        return [[int(n) for n in r] for r in sudoku_table_solved]

    def _get_numbers_in_sudoku_table_nonet(self, sudoku_table, nonet_row, nonet_column):
        nonet_numbers = []
        if (nonet_column in self.ONE_DIGIT_INT_NUMBERS[0:3] and
                nonet_row in self.ONE_DIGIT_INT_NUMBERS[0:3]):
            for row in self.SUDOKU_TABLE_NONETS_ROWS[nonet_row]:
                for column in self.SUDOKU_TABLE_NONETS_COLUMNS[nonet_column]:
                    nonet_numbers.append(sudoku_table[row][column])
        return nonet_numbers

    #########################################################################################################

    #########################################################################################################
    # Events management
    def closeEvent(self, event):
        logging.info("SUDOKU: Closing.")
        logging.info("SUDOKU: Closed.")


if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    play_time = 240  # seconds
    interval = 1000  # ms

    logging.info("Main    : creating main....")
    app = QApplication(sys.argv)
    myapp = SudokuForm(play_time,
                       interval,
                       None)
    myapp.show()
    sys.exit(app.exec_())
