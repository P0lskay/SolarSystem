import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PyQt5.QtWidgets import QApplication

from Satellite import Satellite
from SpaceObject import SpaceObject


class Planet(SpaceObject):

    def __init__(self, name: str, object_diameter: float, orbit_radius: float, speed_degrees_earth_day: float, color,
                 satellites=[], *args, **kwargs):
        super(Planet, self).__init__(name, object_diameter, orbit_radius, speed_degrees_earth_day, color, *args,
                                     **kwargs)

        self.satellites = []
        for satellite in satellites:
            satellite.append((self.current_x, self.current_y))
            new_satellite = Satellite(*satellite, self.parent())
            self.satellites.append(new_satellite)
