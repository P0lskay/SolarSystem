import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication


class Planet(QtWidgets.QWidget):
    x_center_of_window: int
    y_center_of_window: int

    def __init__(self, name: str, object_diameter: int, orbit_radius: float, speed_degrees_earth_day: float, color,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.object_diameter = object_diameter
        self.name = name
        self.orbit_radius = orbit_radius
        self.speed_degrees_earth_day = speed_degrees_earth_day
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        self.current_x = 1000 // 2
        self.current_y = 1000 // 2 - self.orbit_radius
        self.current_degrees = 0
        self.x_center_of_window = 1000 // 2
        self.y_center_of_window = 1000 // 2

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(self.color, 8, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(QPoint(self.current_x, self.current_y),
                            self.object_diameter,
                            self.object_diameter
                            )


    def get_next_coordinates(self):
        self.current_degrees += self.speed_degrees_earth_day
        old_x = self.current_x
        old_y = self.current_y
        self.current_x = self.x_center_of_window + self.orbit_radius * math.cos(math.radians(self.current_degrees))
        self.current_y = self.y_center_of_window + self.orbit_radius * math.sin(math.radians(self.current_degrees))
        result = (old_x - self.current_x, old_y - self.current_y)
        return result
