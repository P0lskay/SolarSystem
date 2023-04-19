from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication
from Planet import Planet

class SolarSystem(QtWidgets.QWidget):
    space_objects: list[Planet]

    def __init__(self, space_objects: list[list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumHeight(1000)
        self.setMinimumWidth(1000)
        self.space_objects = []
        for planet in space_objects:
            new_space_objects = Planet(*planet, self)
            self.space_objects.append(new_space_objects)
        self.initUi()
        self.show()
        self.move_planets(10)

    def initUi(self):
        for i in self.space_objects:
            self.p = i
            self.p.setGeometry(0, 0, 1000, 1000)
            anim = QPropertyAnimation(self.p, b'pos', self)
            anim.setDuration(1)
            anim.setStartValue(QPoint(0, 0))
            anim.setEndValue(QPoint(100, 250))
            anim.start()
            self.p.show()

    def move_planets(self, eatrth_days: int) -> list[(int, int)]:
        pass


    def _trigger_refresh(self):
        self.update()
