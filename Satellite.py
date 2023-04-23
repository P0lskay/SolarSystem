import math

from PyQt5.QtCore import QPointF, QPoint

from SpaceObject import SpaceObject


class Satellite(SpaceObject):

    def __init__(self, name: str, object_diameter: float, orbit_radius: float, speed_degrees_earth_day: float, color,
                 center_of_planet, *args, **kwargs):
        super(Satellite, self).__init__(name, object_diameter, orbit_radius, speed_degrees_earth_day, color, *args,
                                        **kwargs)
        self.current_x = center_of_planet[0] + self.orbit_radius
        self.current_y = center_of_planet[1]
        self.x_center_of_gravity = center_of_planet[0]
        self.y_center_of_gravity = center_of_planet[1]

    def get_next_coordinates(self, new_center_of_gravity: QPoint):
        self.x_center_of_gravity = new_center_of_gravity.x()
        self.y_center_of_gravity = new_center_of_gravity.y()

        self.current_degrees += self.speed_degrees_earth_day

        old_x = self.current_x
        old_y = self.current_y
        self.current_x = self.x_center_of_gravity + self.orbit_radius * math.cos(math.radians(self.current_degrees))
        self.current_y = self.y_center_of_gravity + self.orbit_radius * math.sin(math.radians(self.current_degrees))
        result = QPointF(old_x - self.current_x, old_y - self.current_y)
        return result.toPoint()
