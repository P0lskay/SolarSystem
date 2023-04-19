from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication
from SolarSystem import SolarSystem
from Planet import Planet


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        planets_list = [
            ['Sun', 15, 0, 0, Qt.yellow],
            ['Mercury', 10, 50, 0, Qt.darkYellow],
            ['Venus', 10, 100, 0, Qt.yellow],
            ['Earth', 10, 150, 0, Qt.blue],
            ['Mars', 10, 200, 0, Qt.red],
            ['Jupiter', 10, 250, 0, Qt.darkRed],
            ['Saturn', 10, 300, 0, Qt.darkYellow],
            ['Uranus', 10, 350, 0, Qt.darkGreen],
            ['Neptune', 10, 400, 0, Qt.darkBlue]
        ]

        self.solar_system = SolarSystem(planets_list)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
