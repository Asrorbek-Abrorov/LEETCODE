from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import system
import sys


class Dastur(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        oyna = QWidget()
        question1 = QLabel(" Question 1", oyna)
        question1.resize(250, 60)
        var1 = QRadioButton("variant1")
        var2 = QRadioButton("variant2")
        var3 = QRadioButton("variant3")
        qh = QHBoxLayout()
        qh.addWidget(var1)
        qh.addWidget(var2)
        qh.addWidget(var3)
        oyna.setLayout(qh)
        self.setCentralWidget(oyna)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dastur()
    window.show()
    sys.exit(app.exec_())
