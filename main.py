import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_create_circle = QtWidgets.QPushButton(self.centralwidget)
        self.button_create_circle.setGeometry(QtCore.QRect(260, 500, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_create_circle.setFont(font)
        self.button_create_circle.setObjectName("button_create_circle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "окружности"))
        self.button_create_circle.setText(_translate("MainWindow", "добавить окружность"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.all_circles = []
        super().__init__()
        self.setupUi(self)
        self.button_create_circle.clicked.connect(self.create_circles)

    def create_circles(self):
        x = choice(range(50, 650))
        y = choice(range(50, 550))
        r = choice(range(20, 250))
        color = (choice(range(0, 255)), choice(range(0, 255)),
                 choice(range(0, 255)))
        self.all_circles.append((x, y, r, r, color))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawfigure(qp)
        qp.end()

    def drawfigure(self, qp):
        for circle in self.all_circles:
            pen = QtGui.QPen(QtGui.QColor(*circle[-1]), 10)
            qp.setPen(pen)
            qp.drawEllipse(*circle[0:4])


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
