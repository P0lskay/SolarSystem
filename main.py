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
            ['Mercury', 10, 50, 6, Qt.darkYellow],
            ['Venus', 10, 100, 2, Qt.darkCyan],
            ['Earth', 10, 150, 15, Qt.blue],
            ['Mars', 10, 200, 10, Qt.red],
            ['Jupiter', 10, 250, 17, Qt.darkRed],
            ['Saturn', 10, 300, 32, Qt.darkYellow],
            ['Uranus', 10, 350, 21, Qt.darkGreen],
            ['Neptune', 10, 400, 11, Qt.darkBlue]
        ]

        self.solar_system = SolarSystem(planets_list)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    app.exec()
