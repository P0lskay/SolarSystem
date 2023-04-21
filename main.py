from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication
from SolarSystem import SolarSystem
from Planet import Planet


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        earth_speed = 0.98
        planets_list = [
            ['Sun', 15, 0, 0, Qt.yellow],
            ['Mercury', 1, 25, earth_speed * 4.147, Qt.darkYellow],
            ['Venus', 3, 50, earth_speed * 1.622, Qt.darkCyan],
            ['Earth', 3, 75, earth_speed, Qt.blue],
            ['Mars', 1.5, 110, earth_speed * 0.531, Qt.red],
            ['Jupiter', 33, 190, earth_speed * 0.084, Qt.darkRed],
            ['Saturn', 26, 290, earth_speed * 0.034, Qt.darkYellow],
            ['Uranus', 13, 390, earth_speed * 0.012, Qt.darkGreen],
            ['Neptune', 25, 450, earth_speed * 0.006, Qt.darkBlue]
        ]

        self.solar_system = SolarSystem(planets_list)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    app.exec()
