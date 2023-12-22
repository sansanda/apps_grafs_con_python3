import logging
import random
from enum import IntEnum
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMessageBox

from ejercicios_realizados.sopa_letras.mi_solucion.words_search_ui import Ui_Words_Search_Form
from utils.timer_workers_etc.timers_workers_etc import TimerTickerWorker


class State(IntEnum):
    """
    Auxiliary class create for translating the instance states string into
    an Enum_IntEnum that will help to the app to manage such states.
    """
    #  TIMER STATUS
    INITIATED = 1
    RUNNING = 2
    PAUSED = 3
    OVER = 4


class WordsSearchForm(QtWidgets.QWidget):
    word_matched = pyqtSignal()

    def __init__(self,
                 words_to_find,
                 play_time=60,
                 interval=1000,
                 n_rows=15,
                 n_columns=15,
                 parent=None):

        QtWidgets.QWidget.__init__(self)
        logging.info("Words_Search    : Initiating....")
        self.words_to_find = words_to_find
        self.found_words = 0
        self.play_time = play_time
        self.interval = interval
        self.remaining_time = self.play_time
        self.ui = Ui_Words_Search_Form()
        self.ui.setupUi(self, n_rows, n_columns)
        self.ui.buttons_array.enable_buttons(buttons='all', enable=False)
        # # Signals and Slots
        self.ui.start_pause_pushButton.clicked.connect(self.start_pause_handler)
        self.ui.reset_game_pushButton.clicked.connect(self.reset)
        self.ui.buttons_array.text_available.connect(self.text_available_handler)

        self.timerTickerWorker = None
        self.timer_worker_thread = None

        self.status = State.INITIATED
        self._update_ui()
        logging.info("Words_Search    : Initiated.")

    def text_available_handler(self, text):
        logging.info("text received: %s", text)
        if text in self.words_to_find or text[::-1] in self.words_to_find:
            self.found_words = self.found_words + 1
            self.ui.found_words_label.setText('Words Found: ' + str(self.found_words))
            self.ui.words_to_find_label.setText('Words to Find: ' + str(len(self.words_to_find) - self.found_words))
            logging.info("emitting signal word matched: %s", text)
            self.word_matched.emit()
            self._check_finish()

    def start_pause_handler(self):
        # game running
        if self.status == State.INITIATED:
            self.ui.buttons_array.hide_words(words_to_find, mark_word=False)
            self.ui.buttons_array.random_populate_all_buttons(overwrite=False)
            self.ui.buttons_array.enable_buttons(buttons='all', enable=True)
            # Step 2: Create a QThread object for managing timer
            logging.info("Words_Search    : Creating the timer thread...")
            self.timer_worker_thread = QThread()
            # Step 3: Create a worker object
            self.timerTickerWorker = TimerTickerWorker(self.interval, self.update_ramaining_time)
            # Step 4: Move worker to the thread
            self.timerTickerWorker.moveToThread(self.timer_worker_thread)
            # Step 5: Connect signals and slots
            # # QObject::startTimer: Timers cannot be started from another thread
            # self.timer_worker_thread.started.connect(self.timerTickerWorker.run)
            self.timer_worker_thread.finished.connect(self.timerTickerWorker._quit)
            self.timer_worker_thread.finished.connect(self.timer_worker_thread.deleteLater)
            self.timer_worker_thread.start()
            logging.info("WordsMatchingWidget    : Timer thread created.")
            self.status = State.RUNNING
            self._update_ui()
            self.timerTickerWorker.run()
        elif self.status == State.RUNNING:
            self.status = State.PAUSED
            self._update_ui()
            self.timerTickerWorker.pause()
        elif self.status == State.PAUSED:
            self.status = State.RUNNING
            self._update_ui()
            self.timerTickerWorker.run()

    def pause(self):
        # game paused
        logging.info("Words_Search    : Pausing.")
        self.timerTickerWorker.pause()
        self.status = State.PAUSED
        self._update_ui()
        logging.info("Words_Search    : Paused.")

    def reset(self):
        logging.info("Words_Search    : Initiating.")
        self.timerTickerWorker.pause()
        self.status = State.INITIATED
        self.timer_worker_thread.quit()
        self.timerTickerWorker = None
        self.found_words = 0
        self.remaining_time = self.play_time
        self._update_ui()
        logging.info("Words_Search    : Initiated.")

    def over(self):
        logging.info("Words_Search    : Game is over.")
        self.timerTickerWorker.pause()
        self.status = State.OVER
        self._update_ui()

    def _check_finish(self):
        if int(self.remaining_time) > 0:
            if self.found_words == len(self.words_to_find):
                self.over()
                while not QMessageBox.question(self,
                                               'Finish Game!!!!!',
                                               'Congrats!!! You Win!!!',
                                               QMessageBox.Yes) == QMessageBox.Yes:
                    pass
                self.reset()
        else:
            self.over()
            while not QMessageBox.question(self,
                                           'Time is over!!!!!',
                                           'Sorry!!! You Lose!!! ',
                                           QMessageBox.Yes) == QMessageBox.Yes:
                pass
            self.reset()

    # UI updating
    def update_ramaining_time(self):
        logging.debug("Updating remaining time...")
        self.remaining_time = self.remaining_time - 1
        self.ui.remaining_time_label.setText("Remaining Time: " + str(self.remaining_time))
        self._check_finish()

    def _update_ui(self):
        if self.status == State.INITIATED:
            self.ui.ui_init_status(self.remaining_time, len(self.words_to_find), self.found_words)
        if self.status == State.RUNNING:
            self.ui.ui_running_status()
        if self.status == State.PAUSED:
            self.ui.ui_paused_status()
        if self.status == State.OVER:
            self.ui.ui_over_status()

    # Events management
    def closeEvent(self, event):
        logging.info("Words_Search: Closing.")
        logging.info("Words_Search: Closed.")


if __name__ == "__main__":
    import sys

    _format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    play_time = 240  # seconds
    interval = 1000  # ms
    words = ['MANGO', 'GRAPE', 'APRICOT', 'AVOCADO', 'BLACKBERRY',
              'BANANA', 'APPLE', 'STRAWBERRY', 'ORANGE', 'CHERRY',
              'WATERMELON', 'COCONOUT', 'KIWI', 'LEMON', 'PINEAPPLE',
              'FIG', 'PAPAYA', 'DATE', 'LIME', 'PEACH']
    words_to_find = random.sample(words, 8)
    n_columns = 15
    n_rows = 15

    logging.info("Main    : creating main....")
    app = QApplication(sys.argv)
    myapp = WordsSearchForm(words_to_find,
                            play_time,
                            interval,
                            n_rows,
                            n_columns,
                            None)
    myapp.show()
    sys.exit(app.exec_())
