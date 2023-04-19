from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication


class Planet(QtWidgets.QWidget):
    def __init__(self, name: str, object_diameter: int, orbit_radius: float, speed_degrees_earth_day: float, color, *args, **kwargs):
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
        self.current_x = self.parent().width()//2
        self.current_y = self.parent().height()//2 - self.orbit_radius


    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(self.color, 8, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(QPoint(self.current_x, self.current_y),
                            self.object_diameter,
                            self.object_diameter
                            )


        self.current_x += 100
        self.current_y += 100


    def trigger_refresh(self):
        self.repaint()
