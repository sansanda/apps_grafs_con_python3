import logging
from PyQt5.QtCore import QObject, QTimer
from utils.states.status import State


class TimerTickerWorker(QObject):
    """
    interval: interval in msseconds
    """

    def __init__(self, interval, callback_function):
        QObject.__init__(self)
        logging.info("TimerTickerWorker    : Initiating....")
        self.interval = interval
        self.status = State.INITIATED
        self.timer = QTimer()
        self.timer.timeout.connect(callback_function)
        logging.info("TimerTickerWorker    : Initiated.")

    def run(self):
        if self.status != State.RUNNING:
            self.status = State.RUNNING
            self.timer.start(self.interval)
            logging.info("TimerTickerWorker    : Started.")

    def pause(self):
        if self.status == State.RUNNING:
            self.status = State.PAUSED
            self.timer.stop()
            logging.info("TimerTickerWorker    : Paused.")

    def _quit(self):
        logging.info("TimerTickerWorker    : Quitting....")
        self.timer.stop()
        self.timer.deleteLater()
        self.deleteLater()
