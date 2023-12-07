import logging
import re
import sys
from enum import IntEnum

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread, QObject, pyqtSignal

from ejercicios_realizados.acierta_palabras.mi_solucion.words_matching_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QMessageBox

from ejercicios_realizados.sopa_letras.mi_solucion.words_search_ui import Ui_Words_Search_Form
from utils.languages.language_words_etc import getRandomWordAndDefinitions
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
    LOADING_DATA = 5


class WordsLoaderWorker(QObject):
    word_available = pyqtSignal(str, list)
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, n_words, min_letters_per_word, max_letters_per_word):
        QObject.__init__(self)
        self.status = None
        logging.info("WordsLoaderWorker    : Initiating....")
        self.n_words = n_words
        self.min_letters_per_word = min_letters_per_word
        self.max_letters_per_word = max_letters_per_word
        self.status = State.INITIATED
        logging.info("WordsLoaderWorker    : Initiated.")

    def run(self):
        logging.disable(level=logging.NOTSET)
        if self.status == State.INITIATED:
            self.status = State.RUNNING
            logging.info("WordsLoaderWorker    : Started.")
            words_getted = 0
            while words_getted < self.n_words:
                word, word_definitions_list = getRandomWordAndDefinitions(self.min_letters_per_word,
                                                                          self.max_letters_per_word)
                words_getted = words_getted + 1
                self.word_available.emit(word, word_definitions_list)
                self.progress.emit(int(100 * words_getted / self.n_words))  # emit the percent
            self.finished.emit()
            self.status = State.INITIATED
        logging.disable(level=logging.NOTSET)

    def _quit(self):
        logging.info("WordsLoaderWorker    : Quitting....")
        self.deleteLater()


class WordsSearchWidget(QtWidgets.QWidget):
    """
    interval: interval in msseconds
    """

    def __init__(self,
                 play_time=60,
                 interval=1000,
                 words_to_find = 5,
                 parent=None):

        QtWidgets.QWidget.__init__(self)
        logging.info("WordsMatchingWidget    : Initiating....")
        self.ui = Ui_Words_Search_Form()
        self.ui.setupUi(self)
        self.words_to_find = words_to_find
        self.found_words = 0
        self.play_time = play_time
        self.interval = interval
        self.words = list()

        # # Ui config
        # self.ui.progressBar.setMaximum(self.play_time)
        # self.ui.progressBar.setValue(self.play_time)
        #
        # # Signals and Slots
        # self.ui.startPushButton.clicked.connect(self.start)
        # self.ui.pausePushButton.clicked.connect(self.pause)
        # self.ui.resetPushButton.clicked.connect(self.reset)
        # self.ui.progressBar.valueChanged.connect(self._checkFinishTimeGame)
        # self.ui.lineEdit.returnPressed.connect(self._checkAnswer)
        #
        # self.timerTickerWorker = None
        # self.timer_worker_thread = None
        # self.wordsLoaderWorker = None
        # self.loading_words_thread = None
        #
        # self.status = State.INITIATED
        # self._updateUi()
        logging.info("WordsSearchWidget    : Initiated.")

    def start(self):
        # game running
        if self.status == State.INITIATED:
            self.status = State.LOADING_DATA
            self._updateUi()

            # # Step 2: Create a QThread object for managing timer
            # logging.info("WordsMatchingWidget    : Creating the timer thread...")
            # self.timer_worker_thread = QThread()
            # # Step 3: Create a worker object
            # self.timerTickerWorker = TimerTickerWorker(self.interval, self.updateProgressBar)
            # # Step 4: Move worker to the thread
            # self.timerTickerWorker.moveToThread(self.timer_worker_thread)
            # # Step 5: Connect signals and slots
            # # QObject::startTimer: Timers cannot be started from another thread
            # # self.timer_worker_thread.started.connect(self.timerTickerWorker.run)
            # self.timer_worker_thread.finished.connect(self.timerTickerWorker._quit)
            # self.timer_worker_thread.finished.connect(self.timer_worker_thread.deleteLater)
            # self.timer_worker_thread.start()
            # logging.info("WordsMatchingWidget    : Timer thread created.")
            #
            # # Step 2: Create a QThread object for loading the words
            # logging.info("WordsMatchingWidget    : Creating the thread for loading the words...")
            # self.loading_words_thread = QThread()
            # # Step 3: Create a worker object
            # self.wordsLoaderWorker = WordsLoaderWorker(self.n_words - len(self.words),
            #                                            self.min_letters_per_word,
            #                                            self.max_letters_per_word)
            # # Step 4: Move worker to the threads
            # self.wordsLoaderWorker.moveToThread(self.loading_words_thread)
            # # Step 5: Connect signals and slots
            # self.loading_words_thread.started.connect(self.wordsLoaderWorker.run)
            # self.wordsLoaderWorker.word_available.connect(self.wordAvailableHandler)
            # self.wordsLoaderWorker.progress.connect(self.loadingWordsProgressHandler)
            # self.wordsLoaderWorker.finished.connect(self.finishLoadingWordsHandler)
            # self.loading_words_thread.finished.connect(self.wordsLoaderWorker._quit)
            # self.loading_words_thread.finished.connect(self.loading_words_thread.deleteLater)
            # logging.info("WordsMatchingWidget    : Thread for loading words has been created.")
            #
            # self.ui.WordsHintLineEdit.setText(f'Loading words....{0}%')
            # # Step 6: Start the threads
            # logging.info("WordsMatchingWidget    : Starting the timer...")
            # self.timerTickerWorker.run()
            # logging.info("WordsMatchingWidget    : Loading Words...")
            # self.loading_words_thread.start()
            # self.successes = 0

        if self.status == State.PAUSED:
            self.status = State.RUNNING
            self._updateUi()
            self.timerTickerWorker.run()


    def pause(self):
        # game paused
        logging.info("WordsMatchingWidget    : Pausing.")
        self.status = State.PAUSED
        self._updateUi()
        # self.timerTickerWorker.pause()
        logging.info("WordsMatchingWidget    : Paused.")

    def reset(self):
        logging.info("WordsMatchingWidget    : Initiating.")
        self.status = State.INITIATED
        self._updateUi()
        # self.timer_worker_thread.quit()
        # self.loading_words_thread.quit()
        # self.timerTickerWorker = None
        # self.wordsLoaderWorker = None
        # self.ui.progressBar.setMaximum(self.play_time)
        # self.ui.progressBar.setValue(self.play_time)
        logging.info("WordsMatchingWidget    : Initiated.")

    def over(self):
        self.status = State.OVER
        self._updateUi()

    def _checkFinishTimeGame(self):
        pass
#         if int(self.ui.progressBar.text()) <= 0:
#             self._checkFinish()

    def _checkFinish(self):
        pass
        # if int(self.ui.progressBar.text()) > 0:
        #     if self.successes == self.n_words:
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

    def updateProgressBar(self):
        pass
        # if self.status == State.RUNNING:
        #     logging.debug("WordsMatchingWidget    : Updating Progress Bar.")
        #     self.ui.progressBar.setValue(self.ui.progressBar.value()
        #                                  - int(self.interval / 1000))
        #     self._checkFinish()

    def wordAvailableHandler(self, word, word_definitions_list):
        pass
        # self.words.append(word)
        # self.words_definitions.append(word_definitions_list)
        # logging.debug(self.words)

    def loadingWordsProgressHandler(self, progress):
        pass
        # logging.debug("WordsMatchingWidget    : Progress Received %s.", progress)
        # self.ui.WordsHintLineEdit.setText(f'Loading words....{progress}%')
        # if progress == 100:
        #     self.ui.WordsHintLineEdit.clear()

    def finishLoadingWordsHandler(self):
        pass
        # logging.info("WordsMatchingWidget    : Finished Loading Words.")
        # self.status = State.RUNNING
        # self._updateUi()
        # self.showWords()
        # self.showWordsDefinitions()
        # self.ui.lineEdit.setFocus()
        # logging.info("WordsMatchingWidget    : Started.")

    def showWords(self):
        pass
        # text = ''
        # for i, w in enumerate(self.words):
        #     text = text + str(i + 1) + ':' + w[0:self.letters_to_show].upper() \
        #            + '*' * (len(w) - self.letters_to_show) + '  '
        #
        # fontSize = int(72 / len(self.words)) if len(self.words) != 0 else 24
        # font = QtGui.QFont()
        # font.setPointSize(fontSize)
        # self.ui.WordsHintLineEdit.setFont(font)
        # self.ui.WordsHintLineEdit.setText(text)

    def showWordsDefinitions(self):
        pass
        # text = ''
        # for i, wsd in enumerate(self.words_definitions):
        #     for wd in wsd:
        #         text = text + str(i + 1) + ':' + wd + '\n'
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.ui.wordDefinitionTextEdit.setFont(font)
        # self.ui.wordDefinitionTextEdit.appendPlainText(text)
        # self.ui.wordDefinitionTextEdit.verticalScrollBar().setValue(0)

    def _updateUi(self):
        pass
        # if self.status == State.INITIATED:
        #     self.ui.ui_init_status()
        #     self.ui.progressBar.setMaximum(self.play_time)
        #     self.ui.progressBar.setValue(self.play_time)
        # if self.status == State.RUNNING:
        #     self.ui.ui_running_status()
        # if self.status == State.PAUSED:
        #     self.ui.ui_paused_status()
        # if self.status == State.OVER:
        #     self.ui.ui_over_status()
        # if self.status == State.LOADING_DATA:
        #     self.ui.ui_loading_data_status()

    # Events management
    def closeEvent(self, event):
        logging.info("WordsMatchingWidget    : Closing.")
        # self.timer_worker_thread.quit()
        # self.loading_words_thread.quit()
        logging.info("WordsMatchingWidget    : Closed.")


if __name__ == "__main__":
    _format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=_format, level=logging.CRITICAL,
                        datefmt="%H:%M:%S")
    play_time = 120  # seconds
    interval = 1000  # ms
    min_n_letters_per_word = 6
    max_n_letters_per_word = 9
    words_to_find = 5
    letters_to_show = 5

    logging.info("Main    : creating main....")
    app = QApplication(sys.argv)
    myapp = WordsSearchWidget(play_time,
                              interval,
                              words_to_find,)
    myapp.show()
    sys.exit(app.exec_())
