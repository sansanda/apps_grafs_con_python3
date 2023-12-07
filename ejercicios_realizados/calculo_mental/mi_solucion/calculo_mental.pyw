import logging
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, QTimer

from ejercicios_realizados.calculo_mental.mi_solucion.calculo_mental_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QMessageBox
from utils.numbers_operands_operators_etc.numbers_operators_operands import \
    get_random_operator_and_operands
from utils.timer_workers_etc.timers_workers_etc import TimerTickerWorker
from utils.states.status import State


class CalculoMentalWidget(QtWidgets.QWidget):
    """
    interval: interval in msseconds
    """

    def __init__(self,
                 operand1_range,
                 operators,
                 operand2_range,
                 play_time=60,
                 interval=1000,
                 parent=None):

        QtWidgets.QWidget.__init__(self)
        logging.info("CalculoMentalWidget    : Initiating....")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.attempts = 0
        self.successes = 0
        self.play_time = play_time
        self.interval = interval
        self.operand1_range = operand1_range
        self.operators = operators
        self.operand2_range = operand2_range

        self.op1 = None
        self.op = None
        self.op2 = None
        self.expected_result = None

        # Ui config
        self.ui.tiempo_restante_progressBar.setMaximum(self.play_time)
        self.ui.tiempo_restante_progressBar.setValue(self.play_time)

        # Signals and Slots
        self.ui.start_pushButton.clicked.connect(self.start)
        self.ui.stop_pushButton.clicked.connect(self.pause)
        self.ui.reset_pushButton.clicked.connect(self.reset)
        self.ui.tiempo_restante_progressBar.valueChanged.connect(self._checkFinish)
        self.ui.result_lineEdit.returnPressed.connect(self._checkAnswer)

        # Thread control objects
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.timerTickerWorker = TimerTickerWorker(self.interval, self.updateProgressBar)
        # Step 4: Move worker to the thread
        self.timerTickerWorker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.finished.connect(self.timerTickerWorker._quit)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()

        self.status = State.INITIATED
        self._updateUi()
        logging.info("CalculoMentalWidget    : Initiated.")

    def start(self):
        # game running
        if self.timerTickerWorker.status == State.INITIATED or \
                self.timerTickerWorker.status == State.PAUSED:
            self.attempts = 0
            self.successes = 0
            self.status = State.RUNNING
            self._updateUi()
            self.timerTickerWorker.run()
            logging.info("CalculoMentalWidget    : Started.")
        self.ui.result_lineEdit.setFocus()
        self._updateQuestion()

    def pause(self):
        # game paused
        self.status = State.PAUSED
        self._updateUi()
        self.timerTickerWorker.pause()
        logging.info("CalculoMentalWidget    : Paused.")

    def reset(self):
        self.status = State.INITIATED
        self._updateUi()
        self.timerTickerWorker.pause()
        self.ui.tiempo_restante_progressBar.setMaximum(self.play_time)
        self.ui.tiempo_restante_progressBar.setValue(self.play_time)
        logging.info("CalculoMentalWidget    : Initiated.")

    def over(self):
        self.status = State.OVER
        self._updateUi()

    def _checkAnswer(self):
        self.attempts = self.attempts + 1
        # check if answer is a number
        try:
            int(self.ui.result_lineEdit.text())
        except ValueError:
            self.start()
            return
        # if you are here is because answer is a number
        if int(self.ui.result_lineEdit.text()) == self.expected_result:
            self._update_feedback(1)
            self.successes = self.successes + 1
            self._updateQuestion()
        else:
            self._update_feedback(0)
        self.ui.result_lineEdit.setText("")
        self._update_score_progressBar()

    def _checkFinish(self):
        if self.ui.tiempo_restante_progressBar.value() == 0:
            self.over()
            while not QMessageBox.question(self,
                                           'Finish Game!!!!!',
                                           'Congrats!!! You score is ' + str(
                                               self.ui.aciertos_progressBar.text()),
                                           QMessageBox.Yes) == QMessageBox.Yes:
                pass
            self.reset()

    # UI updating

    def _update_score_progressBar(self):
        self.ui.aciertos_progressBar.setValue(int((self.successes / self.attempts) * 100))

    def updateProgressBar(self):
        if self.status == State.RUNNING:
            self.ui.tiempo_restante_progressBar.setValue(self.ui.tiempo_restante_progressBar.value()
                                                         - int(self.interval / 1000))

    def _updateUi(self):
        if self.status == State.INITIATED:
            self.ui.ui_init_status()
            self.ui.tiempo_restante_progressBar.setMaximum(self.play_time)
            self.ui.tiempo_restante_progressBar.setValue(self.play_time)
            self.ui.aciertos_progressBar.setValue(0)
        if self.status == State.RUNNING:
            self.ui.ui_running_status()
        if self.status == State.PAUSED:
            self.ui.ui_paused_status()
        if self.status == State.OVER:
            self.ui.ui_over_status()

    def _update_feedback(self, result):
        if result:
            self.ui.feedback.setStyleSheet("QLabel { color : green; }")
            self.ui.feedback2.setStyleSheet("QLabel { color : green; }")
            self.ui.feedback.setText("OK!!")
            self.ui.feedback2.setText("OK!!")
        else:
            self.ui.feedback.setStyleSheet("QLabel { color : red; }")
            self.ui.feedback2.setStyleSheet("QLabel { color : red; }")
            self.ui.feedback.setText("KO!!")
            self.ui.feedback2.setText("KO!!")

    # Events management
    def closeEvent(self, event):
        logging.info("CalculoMentalWidget    : Closing.")
        self.thread.quit()

    # Auxiliary methods
    def _updateQuestion(self):
        self.op1, self.op, self.op2, self.expected_result = \
            get_random_operator_and_operands(self.operand1_range,
                                             self.operators,
                                             self.operand2_range)
        self.ui.operand1_label.setText(str(self.op1))
        self.ui.operator_label.setText(self.op)
        self.ui.operand2_label.setText(str(self.op2))


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    play_time = 30  # seconds
    interval = 1000  # ms
    game_operators = ["+", "-", "*", "/"]
    game_operand1_range = [-50, 50]
    game_operand2_range = [-10, 10]

    logging.info("Main    : creating main....")
    app = QApplication(sys.argv)
    myapp = CalculoMentalWidget(game_operand1_range,
                                game_operators,
                                game_operand2_range,
                                play_time,
                                interval,
                                None)
    myapp.show()
    sys.exit(app.exec_())
