from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication
from Planet import Planet

class SolarSystem(QtWidgets.QWidget):
    space_objects: list[Planet]

    def __init__(self, space_objects: list[list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.space_objects = []
        for planet in space_objects:
            new_space_objects = Planet(*planet)
            self.space_objects.append(new_space_objects)

    def move_planets(self, eatrth_days: int) -> list[(int, int)]:
        pass
