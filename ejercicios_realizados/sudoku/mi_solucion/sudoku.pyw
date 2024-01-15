import logging
import random
import time
from enum import IntEnum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from ejercicios_realizados.sudoku.mi_solucion.sudoku2_ui import UiSudokuForm
from utils.timer_workers_etc.timers_workers_etc import TimerTickerWorker
import sys

_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=_format, level=logging.DEBUG, datefmt="%H:%M:%S")


class GameState(IntEnum):
    """
    Auxiliary class create for translating the instance states string into
    an Enum_IntEnum that will help to the app to manage such states.
    """
    #  TIMER STATUS
    INITIATED = 1
    RUNNING = 2
    PAUSED = 3
    OVER = 4


class SudokuForm(QtWidgets.QWidget):
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
        logging.info("Sudoku    : Initiating....")
        self.sudoku_table = [[None for _ in range(0, self.N_COLUMNS, 1)] for _ in range(0, self.N_ROWS, 1)]
        self.play_time = play_time
        self.interval = interval
        self.remaining_time = self.play_time
        self.difficulty_level = 1
        self.N_CELLS_HIDE_INCREMENT = 10
        self.N_OF_TOTAL_CELLS = self.N_ROWS * self.N_COLUMNS
        self.n_cells_to_show = 60 - self.N_CELLS_HIDE_INCREMENT * (self.difficulty_level - 1)
        self.n_cells_to_hide = self.N_OF_TOTAL_CELLS - self.n_cells_to_show
        self.ui = UiSudokuForm()
        self.ui.setupUi(self)

        # # Signals and Slots
        n = 0
        while True:
            item = self.ui.difficulty_h_layout.itemAt(n)
            if item is None:
                break
            else:
                rb = item.widget()
                rb.clicked.connect(lambda foo_param, x=rb: self.on_ui_radio_button_clicked(x))
                n = n + 1


        # self.ui.start_pause_pushButton.clicked.connect(self.start_pause_handler)
        # self.ui.reset_game_pushButton.clicked.connect(self.reset)
        # self.ui.sudoku_table.table_updated_signal.connect(self.updated_ui_sudoku_table_handler)

        self.ui.sudoku_table.ui_sudoku_table_updated.connect(self.on_ui_sudoku_table_updated)

        self.timerTickerWorker = None
        self.timer_worker_thread = None

        self.status = GameState.INITIATED
        self._update_ui()

        self.sudoku_table = self.reset_sudoku_table(self.sudoku_table.copy())
        self.sudoku_table_updated_signal.emit(self.sudoku_table)
        self.sudoku_table = self._insert_random_numbers_in_random_positions(self.sudoku_table.copy(), 20)
        self.sudoku_table_updated_signal.emit(self.sudoku_table)
        self.sudoku_table_solved = self._solve_the_sudoku(self.sudoku_table.copy(),
                                                          0,
                                                          0,
                                                          0,
                                                          1000)
        self.sudoku_table = self._hide_cells(self.sudoku_table_solved.copy(), self.n_cells_to_hide)
        self.sudoku_table_updated_signal.emit(self.sudoku_table)

        logging.info("Sudoku    : Initiated.")

    def on_ui_radio_button_clicked(self, radio_button):
        print(radio_button.text())

    def on_ui_sudoku_table_updated(self, updated_sudoku_table):
        self.sudoku_table = updated_sudoku_table

    def start_pause_handler(self):
        pass
        # game running
        # if self.status == GameState.INITIATED:
        #     self.words_to_find = random.sample(self.available_words, self.n_words_to_find)
        #     self.ui.buttons_array.hide_words(self.words_to_find, mark_word=self.mark_words)
        #     self.ui.buttons_array.random_populate_all_buttons(overwrite=False)
        #     self.ui.buttons_array.config_buttons_as(buttons_to_config='all', option='enable', enable=True)
        #     self.ui.list_of_words_to_find.setText(
        #         self.ui.list_of_words_to_find.text() + '\n\n' + ' -- '.join(self.words_to_find)
        #     )
        #     # Step 2: Create a QThread object for managing timer
        #     logging.info("Words_Search    : Creating the timer thread...")
        #     self.timer_worker_thread = QThread()
        #     # Step 3: Create a worker object
        #     self.timerTickerWorker = TimerTickerWorker(self.interval, self.update_remaining_time)
        #     # Step 4: Move worker to the thread
        #     self.timerTickerWorker.moveToThread(self.timer_worker_thread)
        #     # Step 5: Connect signals and slots
        #     # # QObject::startTimer: Timers cannot be started from another thread
        #     # self.timer_worker_thread.started.connect(self.timerTickerWorker.run)
        #     self.timer_worker_thread.finished.connect(self.timerTickerWorker._quit)
        #     self.timer_worker_thread.finished.connect(self.timer_worker_thread.deleteLater)
        #     self.timer_worker_thread.start()
        #     logging.info("WordsMatchingWidget    : Timer thread created.")
        #     self.status = GameState.RUNNING
        #     self._update_ui()
        #     self.timerTickerWorker.run()
        # elif self.status == GameState.RUNNING:
        #     self.status = GameState.PAUSED
        #     self._update_ui()
        #     self.timerTickerWorker.pause()
        # elif self.status == GameState.PAUSED:
        #     self.status = GameState.RUNNING
        #     self._update_ui()
        #     self.timerTickerWorker.run()

    def pause(self):
        # game paused
        logging.info("Sudoku    : Pausing.")
        # self.timerTickerWorker.pause()
        self.status = GameState.PAUSED
        self._update_ui()
        logging.info("Sudoku    : Paused.")

    def reset(self):
        logging.info("Words_Search    : Reseting.")
        # self.timerTickerWorker.pause()
        self.status = GameState.INITIATED
        # self.timer_worker_thread.quit()
        # self.timerTickerWorker = None
        self.remaining_time = self.play_time
        self._update_ui()
        logging.info("Words_Search    : Reset.")

    def over(self):
        logging.info("Words_Search    : Game is over.")
        # self.timerTickerWorker.pause()
        self.status = GameState.OVER
        self._update_ui()

    def _check_finish(self):
        pass
        # if int(self.remaining_time) > 0:
        #     if self.found_words == len(self.words_to_find):
        #         self.over()
        #         while not QMessageBox.question(self,
        #                                        'Finish Game!!!!!',
        #                                        'Congrats!!! You Win!!!',
        #                                        QMessageBox.Yes) == QMessageBox.Yes:
        #             pass
        #         self.reset()
        # else:
        #     self.over()
        #     while not QMessageBox.question(self,
        #                                    'Time is over!!!!!',
        #                                    'Sorry!!! You Lose!!! ',
        #                                    QMessageBox.Yes) == QMessageBox.Yes:
        #         pass
        #     self.reset()

    # UI updating
    def update_remaining_time(self):
        logging.debug("Updating remaining time...")
        # self.remaining_time = self.remaining_time - 1
        # self.ui.remaining_time_label.setText("Remaining Time: " + str(self.remaining_time))
        # self._check_finish()

    def _update_ui(self):
        if self.status == GameState.INITIATED:
            self.ui.ui_init_status(self.remaining_time)
        if self.status == GameState.RUNNING:
            self.ui.ui_running_status()
        if self.status == GameState.PAUSED:
            self.ui.ui_paused_status()
        if self.status == GameState.OVER:
            self.ui.ui_over_status()

    #########################################################################################################
    def reset_sudoku_table(self, sudoku_table_copy):
        for row in range(0, self.N_ROWS):
            for column in range(0, self.N_COLUMNS):
                sudoku_table_copy[row][column] = None
        return sudoku_table_copy

    def _insert_random_numbers_in_random_positions(self, sudoku_table_copy, n_numbers):
        for _ in range(0, n_numbers, 1):
            while True:
                random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                while sudoku_table_copy[random_row][random_column] is not None:
                    random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                    random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_number = random.choice(self.ONE_DIGIT_INT_NUMBERS[1:])
                if (
                        self._appearances_in_row(sudoku_table_copy, random_number, random_row) == 0 and
                        self._appearances_in_column(sudoku_table_copy, random_number, random_column) == 0 and
                        self._appearances_in_nonet(sudoku_table_copy, random_number, random_row, random_column) == 0
                ):
                    sudoku_table_copy[random_row][random_column] = random_number
                    break
        return sudoku_table_copy

    def _hide_cells(self, sudoku_table_solved_copy, n_cells_to_hide):
        for _ in range(0, n_cells_to_hide, 1):
            while True:
                random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                while sudoku_table_solved_copy[random_row][random_column] is None:
                    random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                    random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                sudoku_table_solved_copy[random_row][random_column] = None
                break
        return sudoku_table_solved_copy

    def _appearances_in_row(self, sudoku_table, number, row):
        number_appearances = 0
        for n in sudoku_table[row]:
            if n is None:
                continue
            if int(n) == number:
                number_appearances = number_appearances + 1
        return number_appearances

    def _appearances_in_column(self, sudoku_table, number, column):
        number_appearances = 0
        for n in [r[column] for r in sudoku_table]:
            if n is None:
                continue
            if int(n) == number:
                number_appearances = number_appearances + 1
        return number_appearances

    def _appearances_in_nonet(self, sudoku_table, number, row, column):
        number_appearances = 0
        nonet_row, nonet_column = self._get_nonet_indexes(row, column)
        for n in self._get_numbers_in_sudoku_table_nonet(sudoku_table, nonet_row, nonet_column):
            if n is None:
                continue
            if int(n) == number:
                number_appearances = number_appearances + 1
        return number_appearances

    def _solve_the_sudoku_by_backtracking(self, sudoku_table_copy,
                                          from_row_index,
                                          from_column_index,
                                          recursion_depth,
                                          max_recursion_depth):
        if recursion_depth > max_recursion_depth:
            # we have reached the maximum recursion depth and still there is no solution for the sudoku table
            # we return None. There should be a new call with a better sudoku table proposition
            return None
        else:
            # we haven't reached the max recursion depth, we can still looking for the solution
            if ((sudoku_table_copy[from_row_index][from_column_index] is not None) and
                    (from_row_index == self.N_ROWS - 1) and
                    (from_column_index == self.N_COLUMNS - 1)):
                # if you are here is because the algorithm has reached the end of the table and so it has a solution
                return sudoku_table_copy
            else:
                # if you are here is because the algorithm hasn't reached the end of the table and, for the moment,
                # there is not a solution for the sudoku table copy
                if (sudoku_table_copy[from_row_index][from_column_index] is None or
                        isinstance(sudoku_table_copy[from_row_index][from_column_index], str)):
                    # if you are here is because the sudoku_table cell contains or None or a str int value
                    if sudoku_table_copy[from_row_index][from_column_index] is None:
                        # if you are here is because the sudoku_table cell contains None
                        # we will search for a valid number for the cell in from_row_index, from_column_index coords
                        number = 1
                        while (
                                self._appearances_in_row(sudoku_table_copy, number, from_row_index) > 0 or
                                self._appearances_in_column(sudoku_table_copy, number, from_column_index) > 0 or
                                self._appearances_in_nonet(sudoku_table_copy, number, from_row_index,
                                                           from_column_index) > 0
                        ):
                            number = number + 1
                            if number > 9:
                                break
                        # here the number could be 10 or less
                        if number > 9:
                            # then there is not a good number for this cell, we have to go backwards in the table
                            sudoku_table_copy[from_row_index][from_column_index] = None
                            previous_row_index, previous_column_index = (
                                self._get_sudoku_table_previous_coordinates(from_row_index, from_column_index))
                            return self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                          previous_row_index,
                                                                          previous_column_index,
                                                                          recursion_depth + 1,
                                                                          max_recursion_depth)
                        else:
                            # there is a good number for this cell, then we can go to the next table position
                            sudoku_table_copy[from_row_index][from_column_index] = str(number)
                            next_row_index, next_column_index = (
                                self._get_sudoku_table_next_coordinates(from_row_index, from_column_index))
                            return self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                          next_row_index,
                                                                          next_column_index,
                                                                          recursion_depth + 1,
                                                                          max_recursion_depth)
                    else:
                        # if you are here is because the sudoku_table cell contains a str int value
                        # this occurs because we are going back in the table
                        # then we have to search for another number from the number in the actual cell
                        number = int(sudoku_table_copy[from_row_index][from_column_index])
                        if number == 9:
                            # if the cell contains the max number (9) then we have to set it to None
                            # and try with the previous cell
                            if from_row_index == 0 and from_column_index == 0:
                                # we have reach beginning (0,0) of the table by backwargning and the 0,0 cell contains
                                # the number 9, it means that the algorithm can't find a solution for the sudoku table
                                return None
                            else:
                                # the algorithm hasn't reached the beginning of the table so it still can go backwards
                                sudoku_table_copy[from_row_index][from_column_index] = None
                                previous_row_index, previous_column_index = (
                                    self._get_sudoku_table_previous_coordinates(from_row_index, from_column_index))
                                return self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                              previous_row_index,
                                                                              previous_column_index,
                                                                              recursion_depth + 1,
                                                                              max_recursion_depth)
                        else:
                            # if the cell doesn't contain the max number (9) then we have can increase the cell value
                            # and try to go looking forward for the solution
                            number = number + 1
                            while (
                                    self._appearances_in_row(sudoku_table_copy, number, from_row_index) > 0 or
                                    self._appearances_in_column(sudoku_table_copy, number, from_column_index) > 0 or
                                    self._appearances_in_nonet(sudoku_table_copy, number, from_row_index,
                                                               from_column_index) > 0
                            ):
                                number = number + 1
                                if number > 9:
                                    break
                            # here the number could be 10 or less
                            if number > 9:
                                # there is not a good number for this cell, the algorithm has to go backwards
                                sudoku_table_copy[from_row_index][from_column_index] = None
                                previous_row_index, previous_column_index = (
                                    self._get_sudoku_table_previous_coordinates(from_row_index, from_column_index))
                                return self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                              previous_row_index,
                                                                              previous_column_index,
                                                                              recursion_depth + 1,
                                                                              max_recursion_depth)
                            else:
                                # there is a good number for this cell, then we can go to the next table position
                                sudoku_table_copy[from_row_index][from_column_index] = str(number)
                                next_row_index, next_column_index = (
                                    self._get_sudoku_table_next_coordinates(from_row_index, from_column_index))
                                return self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                              next_row_index,
                                                                              next_column_index,
                                                                              recursion_depth + 1,
                                                                              max_recursion_depth)
                else:
                    # if you are here is because the cell already contains a number and this number is one of the very
                    # first random numbers introduced in the initialization of the sudoku table
                    # the algorithm has to mark the number as modificable (converting to an str number) and go forward
                    # for the solution.
                    sudoku_table_copy[from_row_index][from_column_index] = str(
                        sudoku_table_copy[from_row_index][from_column_index])
                    next_row_index, next_column_index = (
                        self._get_sudoku_table_next_coordinates(from_row_index, from_column_index))
                    return self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                  next_row_index,
                                                                  next_column_index,
                                                                  recursion_depth + 1,
                                                                  max_recursion_depth)

    def _solve_the_sudoku(self, sudoku_table_copy,
                          from_row_index,
                          from_column_index,
                          recursion_depth,
                          max_recursion_depth):

        sudoku_table_solved = None
        while sudoku_table_solved is None:
            sudoku_table_solved = self._solve_the_sudoku_by_backtracking(sudoku_table_copy,
                                                                         from_row_index,
                                                                         from_column_index,
                                                                         recursion_depth,
                                                                         max_recursion_depth)
            if sudoku_table_solved is None:
                self.sudoku_table = self.reset_sudoku_table(self.sudoku_table.copy())
                self.sudoku_table = self._insert_random_numbers_in_random_positions(self.sudoku_table.copy(),
                                                                                    20)

        return sudoku_table_solved

    def _get_sudoku_table_previous_coordinates(self, actual_row_index, actual_column_index):
        # logging.debug(f"Invoking {self._get_sudoku_table_previous_coordinates.__name__}")
        # logging.debug(f"args: actual_row_index, actual_column_index =  "
        #               f"{actual_row_index, actual_column_index}")
        if actual_column_index == 0 and actual_row_index == 0:
            return actual_row_index, actual_column_index
        elif ((actual_column_index > 0 and actual_row_index == 0) or
              (actual_column_index > 0 and actual_row_index > 0)):
            return actual_row_index, actual_column_index - 1
        else:
            # case actual_column_index == 0 and actual_row_index > 0
            return actual_row_index - 1, self.N_COLUMNS - 1

    def _get_sudoku_table_next_coordinates(self, actual_row_index, actual_column_index):
        # logging.debug(f"Invoking {self._get_sudoku_table_next_coordinates.__name__}")
        # logging.debug(f"args: actual_row_index, actual_column_index =  "
        #               f"{actual_row_index, actual_column_index}")
        if actual_column_index == self.N_COLUMNS - 1 and actual_row_index == self.N_ROWS - 1:
            return actual_row_index, actual_column_index
        elif ((actual_column_index < self.N_COLUMNS - 1 and actual_row_index == self.N_ROWS - 1) or
              (actual_column_index < self.N_COLUMNS - 1 and actual_row_index < self.N_ROWS - 1)):
            return actual_row_index, actual_column_index + 1
        else:
            # case actual_column_index == self.N_COLUMNS - 1 and actual_row_index < self.N_ROWS - 1
            return actual_row_index + 1, 0

    def _get_nonet_indexes(self, row, column):
        nonet_row = nonet_column = None
        for row_index in range(0, len(self.SUDOKU_TABLE_NONETS_ROWS)):
            if row in self.SUDOKU_TABLE_NONETS_ROWS[row_index]:
                nonet_row = row_index
                break
        for column_index in range(0, len(self.SUDOKU_TABLE_NONETS_COLUMNS)):
            if column in self.SUDOKU_TABLE_NONETS_COLUMNS[column_index]:
                nonet_column = column_index
                break
        return nonet_row, nonet_column

    def _get_numbers_in_sudoku_table_nonet(self, sudoku_table, nonet_row, nonet_column):
        nonet_numbers = []
        if (nonet_column in self.ONE_DIGIT_INT_NUMBERS[0:3] and
                nonet_row in self.ONE_DIGIT_INT_NUMBERS[0:3]):
            for row in self.SUDOKU_TABLE_NONETS_ROWS[nonet_row]:
                for column in self.SUDOKU_TABLE_NONETS_COLUMNS[nonet_column]:
                    nonet_numbers.append(
                        sudoku_table[row][column]
                    )
        return nonet_numbers

    #########################################################################################################

    #########################################################################################################
    # Events management
    def closeEvent(self, event):
        logging.info("Words_Search: Closing.")
        logging.info("Words_Search: Closed.")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    play_time = 240  # seconds
    interval = 1000  # ms

    logging.info("Main    : creating main....")
    app = QApplication(sys.argv)
    myapp = SudokuForm(play_time,
                       interval,
                       None)
    myapp.show()
    sys.exit(app.exec_())
