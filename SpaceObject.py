import math

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont


class SpaceObject(QtWidgets.QWidget):

    def __init__(self, name: str, object_diameter: float, orbit_radius: float, speed_degrees_earth_day: float, color,
                 *args: object, **kwargs):
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
        self.current_x = 1000 // 2 + self.orbit_radius
        self.current_y = 1000 // 2
        self.current_degrees: float = 0.0
        self.x_center_of_gravity = 1000 // 2
        self.y_center_of_gravity = 1000 // 2

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(self.color, 8, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(QPoint(self.current_x, self.current_y),
                            self.object_diameter,
                            self.object_diameter
                            )
        if self.name != 'Sun':
            painter.setPen(Qt.black)
            painter.setFont(QFont('Decorative', min(10, self.object_diameter * 5)))
            painter.drawText(QPoint(self.current_x - self.object_diameter, self.current_y - 10 - self.object_diameter),
                             self.name)

    def get_next_coordinates(self):
        """
        Вычисляет сдвиг планеты относительно текущей позиции для перехода к ее следующей позиции
        :return: QPoint, где x - сдвиг по Оx, а y - сдвиг по Oy
        """
        self.current_degrees += self.speed_degrees_earth_day

        old_x = self.current_x
        old_y = self.current_y
        self.current_x = self.x_center_of_gravity + self.orbit_radius * math.cos(math.radians(self.current_degrees))
        self.current_y = self.y_center_of_gravity + self.orbit_radius * math.sin(math.radians(self.current_degrees))
        result = QPointF(old_x - self.current_x, old_y - self.current_y)
        return result.toPoint()
