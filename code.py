from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
from PyQt5.QtWidgets import QMenuBar, QStatusBar
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QColor, QPainter
from random import randint
import sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_circle_button = QPushButton(self.centralwidget)
        self.create_circle_button.setGeometry(QRect(160, 120, 271, 91))
        self.create_circle_button.setObjectName("create_circle_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_circle_button.setText(_translate("MainWindow", "Создать окружность"))


class RandomCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.need_to_draw = False
        self.points_data = []
        self.create_circle_button.clicked.connect(self.draw)

    def draw(self):
        self.need_to_draw = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.draw_circle(painter)
        painter.end()

    def draw_circle(self, painter):
        if self.need_to_draw:
            diameter = randint(10, 200)
            coord_x = randint(diameter // 2, 600 - diameter // 2)
            coord_y = randint(diameter // 2, 400 - diameter // 2)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            circle = {
                "x": coord_x - diameter // 2,
                "y": coord_y - diameter // 2,
                "d": diameter,
                "c": color
            }
            self.points_data.append(circle)
            for circle in self.points_data:
                painter.setBrush(circle["c"])
                painter.drawEllipse(circle["x"], circle["y"], circle["d"], circle["d"])
            self.need_to_draw = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    random_circles = RandomCircles()
    random_circles.show()
    sys.exit(app.exec())
