import threading
from time import sleep
from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPainter, QPen, QBrush, QPainterPath
from PyQt5.QtWidgets import QApplication, QPushButton
from Planet import Planet

class SolarSystem(QtWidgets.QWidget):
    space_objects: list[Planet]

    def __init__(self, space_objects: list[list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 50, 1000, 1000)
        self.space_objects = []
        for planet in space_objects:
            new_space_objects = Planet(*planet, self)
            self.space_objects.append(new_space_objects)
        self.initUi()
        self.show()
        #self.mouseReleaseEvent = self.move_planets

    def initUi(self):
        self.start_button = QPushButton(self)
        self.start_button.clicked.connect(self.clicked_btn)
        self.start_button.show()

        for i in self.space_objects:
            self.p = i
            self.p.setGeometry(0, 0, 1000, 1000)
            self.p.show()


    def move_planets(self) -> list[(int, int)]:
        for i in self.space_objects:
            self.p = i

            self.p.move(*self.p.get_next_coordinates())




    def clicked_btn(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.move_planets)
        timer.start(90)
