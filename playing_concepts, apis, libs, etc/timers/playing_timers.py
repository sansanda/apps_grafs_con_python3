import threading
import time

import logging

# create logger
logger = logging.getLogger('calculo_mental')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


class RepeatedTimerUntil(object):
    def __init__(self, total_time, interval, function, *args, **kwargs):
        self._timer = threading.Timer(interval, self._run)
        self.total_time = total_time
        self.remaining_time = self.total_time
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.remaining_time = self.remaining_time - self.interval
        if self.remaining_time < 0:
            self.reset()
        else:
            self.start()
            self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def pause(self):
        self._timer.cancel()
        self.is_running = False

    def reset(self):
        self.pause()
        self.remaining_time = self.total_time

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class MyTimer(threading.Thread):
    def __init__(self, interval, execute, name, *args, **kwargs):
        threading.Thread.__init__(self, name=name)
        self.daemon = False
        self.event = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.event.set()

    def run(self):
        if not self.event.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)


def printit():
    threading.Timer(1.0, printit).start()
    print("Hello, World!")


def foo():
    print("hola")


if __name__ == "__main__":
    # printit()
    timer = RepeatedTimerUntil(total_time=10, interval=1, function=foo)
    timer.start()
    while(True):
        print(timer.remaining_time)
        time.sleep(0.5)
