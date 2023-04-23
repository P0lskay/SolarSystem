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
