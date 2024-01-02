from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QObject, QPoint
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QLabel, QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1000)
        self.anim.start()

class PopUPBubble(QObject):
    def __init__(self):
        super().__init__()
        e = QGraphicsOpacityEffect(self)
        self.label = QLabel()
        self.label.setGraphicsEffect(e)
        self.label.setStyleSheet("border: 3px solid gray;border-radius:20px;background-color:#ffffff;color:gray")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Notification')
        a = QPropertyAnimation(e, b"opacity")
        a.setDuration(1000)
        a.setStartValue(0)
        a.setEndValue(1)
        a.setEasingCurve(QEasingCurve.InOutCubic)
        a.start(QPropertyAnimation.DeleteWhenStopped)
        self.label.show()

        timer = QTimer(self)
        timer.timeout.connect(self.fadeout)
        timer.start()

    def fadeout(self):
        e = QGraphicsOpacityEffect()
        self.label.setGraphicsEffect(e)
        a = QPropertyAnimation(e, b"opacity")
        a.setDuration(1000)  # it will took 1000 ms to face out
        a.setStartValue(1)
        a.setEndValue(0)
        a.setEasingCurve(QEasingCurve.OutBack)
        a.finished.connect(self.label.hide)
        a.start()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())