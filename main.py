from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication
from SolarSystem import SolarSystem
from Planet import Planet


class MainWindow(QtWidgets.QWidget):

    def __init__(self, steps=10, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        planets_list = [
            ['Sun', 50, 10, 0, Qt.yellow],
            ['Mercury', 50, 10, 0, Qt.darkYellow],
            ['Venus', 50, 10, 0, Qt.yellow],
            ['Earth', 50, 10, 0, Qt.blue],
            ['Mars', 50, 10, 0, Qt.red],
            ['Jupiter', 50, 10, 0, Qt.darkRed],
            ['Saturn', 50, 10, 0, Qt.darkYellow],
            ['Uranus', 50, 10, 0, Qt.darkGreen],
            ['Neptune', 50, 10, 0, Qt.darkBlue]
        ]

        layout = QtWidgets.QVBoxLayout()
        self.solar_system = SolarSystem(planets_list)
        p = Planet('Uranus', 100, 210, 0, Qt.darkGreen)
        for space_object in self.solar_system.space_objects:
            layout.addWidget(space_object)

        # _dial = QtWidgets.QPushButton()
        # _dial.clicked.connect(
        # self.solar_system.space_objects[8]._trigger_refresh
        # )

        #layout.addWidget(_dial)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showFullScreen()
    app.exec()
