import logging
import random
from enum import IntEnum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from ejercicios_realizados.sudoku.mi_solucion.sudoku2_ui import UiSudokuForm
from utils.timer_workers_etc.timers_workers_etc import TimerTickerWorker
import sys


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
        self.ui = UiSudokuForm()
        self.ui.setupUi(self)
        # # Signals and Slots
        # self.ui.start_pause_pushButton.clicked.connect(self.start_pause_handler)
        # self.ui.reset_game_pushButton.clicked.connect(self.reset)
        # self.ui.sudoku_table.table_updated_signal.connect(self.updated_ui_sudoku_table_handler)

        self.ui.sudoku_table.ui_sudoku_table_updated.connect(self.on_ui_sudoku_table_updated)

        self.timerTickerWorker = None
        self.timer_worker_thread = None

        self.status = GameState.INITIATED
        self._update_ui()

        # QtCore.QMetaObject.connectSlotsByName(self)

        logging.info("Sudoku    : Initiated.")

        self.reset_sudoku_table()
        self.sudoku_table_updated_signal.emit(self.sudoku_table)
        self._insert_random_numbers_in_sudoku_table_in_random_positions(self.sudoku_table,20)
        self.sudoku_table_updated_signal.emit(self.sudoku_table)
        self.solve_the_sudoku_using_backtracking(0, 0, self.sudoku_table.copy())

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
    def reset_sudoku_table(self):
        for row in range(0, self.N_ROWS):
            for column in range(0, self.N_COLUMNS):
                self.sudoku_table[row][column] = None

    def _insert_random_numbers_in_sudoku_table_in_random_positions(self, sudoku_table, n_numbers):
        for _ in range(0, n_numbers, 1):
            while True:
                random_row = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_column = random.choice(self.ONE_DIGIT_INT_NUMBERS[:-1])
                random_number = random.choice(self.ONE_DIGIT_INT_NUMBERS[1:])
                if (self.test_if_number_match_rules_of_sudoku(sudoku_table, random_number, random_row, random_column) and
                        (not self.sudoku_table[random_row][random_column])):
                    self.sudoku_table[random_row][random_column] = random_number
                    break

    def test_if_number_match_rules_of_sudoku(self, sudoku_table, number, row, column):
        match = True
        nonet_row, nonet_column = self._get_nonet_indexes(row, column)
        if (number in sudoku_table[row] or
                number in [r[column] for r in sudoku_table] or
                number in self._get_numbers_in_sudoku_table_nonet(sudoku_table, nonet_row, nonet_column)):
            match = False
        return match

    def solve_the_sudoku_using_backtracking(self, row, column, sudoku_table_copy):
        possible_solution = list()
        if not sudoku_table_copy[row][column] or isinstance(sudoku_table_copy[row][column], str):
            if not sudoku_table_copy[row][column]:
                # if you are here is because the cell contains None
                sudoku_table_copy[row][column] = str(1)

             # or a temporal number as str
            # for number in self.ONE_DIGIT_INT_NUMBERS[1:]:
            #     possible_solution.append(100*row+10*column+number)
        else:
            # if you are here is because the cell already contains a number
            next_row, next_column = _get_next_position(row. column)

    def _get_previous_position(self, actual_row, actual_column):
        previous_row= 0
        previous_column = 0
        if actual_row > 0:
            if actual_column == 0:
                previous_row = actual_row - 1
                next_column = self.N_COLUMNS - 1
            else:
                previous_row = actual_row 
                next_column = actual_column - 1
        else:
            previous_row = actual_row
            if actual_column == 0:
                next_column = actual_column
            else:
                next_column = actual_column - 1
    
    def _get_next_position(self, actual_row, actual_column):
        next_row = 0
        next_column = 0
        if actual_row < self.N_ROWS - 1:
            if actual_column == self.N_COLUMNS - 1:
                next_row = actual_row + 1
                next_column = 0
            else:
                next_row = actual_row
                next_column = actual_column + 1
        else:
            next_row = actual_row
            if actual_column < self.N_COLUMS - 1:
                next_column = actual_column + 1
            else:
                next_column = actual_column
                
            


    #########################################################################################################

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
    _format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    play_time = 240  # seconds
    interval = 1000  # ms

    logging.info("Main    : creating main....")
    app = QApplication(sys.argv)
    myapp = SudokuForm(play_time,
                       interval,
                       None)
    myapp.show()
    sys.exit(app.exec_())
