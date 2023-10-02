from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import system
import sys
from datetime import datetime


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.label1 = QLabel("Name:   ")
        self.label2 = QLabel("Subject:")
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()

        self.plus = QPushButton("+")
        self.minus = QPushButton("-")
        self.save = QPushButton("Save")
        self.exit = QPushButton("Exit")
        self.number = QLabel(str(self.counter))

        self.qh1 = QHBoxLayout()
        self.qh2 = QHBoxLayout()
        self.qh3 = QHBoxLayout()
        self.qh4 = QHBoxLayout()

        self.qh1.addWidget(self.label1)
        self.qh1.addWidget(self.line1)
        self.qh2.addWidget(self.label2)
        self.qh2.addWidget(self.line2)

        self.qh3.addStretch()
        self.qh3.addWidget(self.plus)
        self.qh3.addStretch()
        self.qh3.addWidget(self.number)
        self.qh3.addStretch()
        self.qh3.addWidget(self.minus)
        self.qh3.addStretch()

        self.qh4.addStretch()
        self.qh4.addWidget(self.save)
        self.qh4.addWidget(self.exit)
        self.qh4.addStretch()

        self.qv = QVBoxLayout()
        self.qv.addLayout(self.qh1)
        self.qv.addLayout(self.qh2)
        self.qv.addLayout(self.qh3)
        self.qv.addLayout(self.qh4)
        self.setLayout(self.qv)

        self.line1.setPlaceholderText("Enter Name...")
        self.line2.setPlaceholderText("Enter Subject... ")

        self.plus.clicked.connect(self.plusClick)
        self.minus.clicked.connect(self.minusClick)
        self.save.clicked.connect(self.saveClick)
        self.exit.clicked.connect(self.exitClick)

        self.save.setStyleSheet("""background-color : Green;""")
        self.exit.setStyleSheet("""background-color : Red;""")

    def plusClick(self):
        self.counter += 1
        self.number.setText(str(self.counter))

    def minusClick(self):
        if self.counter <= 0:
            self.counter = 0
            self.number.setText(str(self.counter))
        else:
            self.counter -= 1
            self.number.setText(str(self.counter))

    def saveClick(self):
        f = open("users.txt", "a")

        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        f.write(f"{self.line1.text().ljust(15)}{self.line2.text().ljust(15)}{self.number.text().ljust(15)}{date_time.ljust(10)}")
        f.write("\n")

        f.close()
        self.line1.setText("")
        self.line2.setText("")
        self.number.setText(str(0))

    def exitClick(self):
        system("clear")
        sys.exit()


if __name__ == "__main__":
    app = QApplication([])
    window = Login()
    window.show()
    sys.exit(app.exec_())
