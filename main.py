import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import uic, QtGui
import random


class MyWidget(QMainWindow):
    def __init__(self):
        self.all_circle = []
        self.draw = False
        super().__init__()
        uic.loadUi('form_for_window.ui', self)
        self.button_create_circle.clicked.connect(self.create_circles)

    def create_circles(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawfigure(qp)
            qp.end()

    def drawfigure(self, qp):
        pen = QtGui.QPen(QtGui.QColor('yellow'), 3)
        qp.setPen(pen)
        x = random.choice(range(50, 650))
        y = random.choice(range(50, 550))
        r = random.choice(range(20, 250))
        qp.drawEllipse(x, y, r, r)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())