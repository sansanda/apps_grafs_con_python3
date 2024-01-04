import logging
from enum import IntEnum
from PyQt5 import QtWidgets, QtGui
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

    def __init__(self,
                 play_time=60,
                 interval=1000,
                 parent=None):

        QtWidgets.QWidget.__init__(self)
        logging.info("Sudoku    : Initiating....")
        self.play_time = play_time
        self.interval = interval
        self.remaining_time = self.play_time
        self.ui = UiSudokuForm()
        self.ui.setupUi(self)
        # # Signals and Slots
        # self.ui.start_pause_pushButton.clicked.connect(self.start_pause_handler)
        # self.ui.reset_game_pushButton.clicked.connect(self.reset)
        # self.ui.buttons_array.text_available.connect(self.text_available_handler)

        self.timerTickerWorker = None
        self.timer_worker_thread = None

        self.status = GameState.INITIATED
        self._update_ui()
        logging.info("Sudoku    : Initiated.")

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
