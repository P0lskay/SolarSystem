from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication


class _Bar(QtWidgets.QWidget):

    def __init__(self, x = 10, y = 10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

    def sizeHint(self):
        return QtCore.QSize(40,120)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawEllipse(self.size().width() // 2, self.size().height() // 2, self.x, self.y)

        painter.end()

    def _trigger_refresh(self):
        self.x += 10
        self.y += 10
        self.update()


class PowerBar(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, steps=10, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QPushButton()
        self._dial.clicked.connect(
           self._bar._trigger_refresh
        )

        layout.addWidget(self._dial)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = PowerBar()
    window.show()
    app.exec()