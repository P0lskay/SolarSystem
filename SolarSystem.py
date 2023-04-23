import threading
from time import sleep
from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QDate
from PyQt5.QtGui import QPainter, QPen, QBrush, QPainterPath
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QDateEdit
from Planet import Planet


class SolarSystem(QtWidgets.QWidget):
    space_objects: list[Planet]

    def __init__(self, space_objects: list[list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_time = QDateEdit(QDate(1982, 3, 10))
        self.timer = QtCore.QTimer(self)
        self.stop_button = QPushButton("||", self)
        self.start_button = QPushButton("|>", self)
        self.fast_start_button = QPushButton("|>|>|>", self)
        self.space_objects = []
        for planet in space_objects:
            new_space_objects = Planet(*planet, self)
            self.space_objects.append(new_space_objects)

        self.initUi()
        self.show()

    def initUi(self):
        self.setGeometry(50, 50, 1000, 1000)

        time_control_widget = QWidget(self)

        self.start_button.clicked.connect(self.clicked_start_btn)

        self.fast_start_button.clicked.connect(self.clicked_fast_start_btn)

        self.stop_button.clicked.connect(self.clicked_stop_btn)

        time_control_layout = QHBoxLayout()
        time_control_layout.addWidget(self.start_button)
        time_control_layout.addWidget(self.fast_start_button)
        time_control_layout.addWidget(self.stop_button)
        time_control_layout.addWidget(self.current_time)
        time_control_widget.setLayout(time_control_layout)
        time_control_widget.show()

        for planet in self.space_objects:
            planet.setGeometry(0, 0, 1000, 1000)
            planet.show()
            for satellite in planet.satellites:
                satellite.setGeometry(0, 0, 1000, 1000)
                satellite.show()


    def move_planets(self):
        for planet in self.space_objects:
            planet.move(planet.get_next_coordinates())
            for satellite in planet.satellites:
                satellite.move(satellite.get_next_coordinates(QPoint(planet.current_x, planet.current_y)))

        self.current_time.setDate(self.current_time.date().addDays(1))


    def clicked_stop_btn(self):
        self.timer.stop()
        self.timer = QtCore.QTimer(self)

    def clicked_start_btn(self):
        self.timer.stop()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.move_planets)
        self.timer.start(20)

    def clicked_fast_start_btn(self):
        self.timer.stop()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.move_planets)
        self.timer.start(5)

    def paintEvent(self, event):
        painter = QPainter(self)
        for planet in self.space_objects:
            painter.setPen(QPen(Qt.black,  1, Qt.DotLine))
            painter.drawEllipse(1000 // 2-planet.orbit_radius, 1000 // 2 - planet.orbit_radius, planet.orbit_radius*2, planet.orbit_radius*2)
        painter.end()