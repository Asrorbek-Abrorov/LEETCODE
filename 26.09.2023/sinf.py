from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import system
import sys
from datetime import datetime


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel("Calculator")
        self.lbl.setFont(QFont("Arial", 24))
        self.num1_line = QLineEdit()
        self.num2_line = QLineEdit()
        self.pushButton = QPushButton("Submit")
        self.setWindowTitle("Calculator")

        self.h_box0 = QHBoxLayout()
        self.h_box0.addWidget(self.lbl)
        self.h_box0.addStretch()

        self.h_box1 = QHBoxLayout()
        self.h_box1.addWidget(self.num1_line)

        self.h_box2 = QHBoxLayout()
        self.h_box2.addWidget(self.num2_line)

        self.h_box3 = QHBoxLayout()
        self.h_box3.addStretch()
        self.h_box3.addWidget(self.pushButton)
        self.h_box3.addStretch()

        self.v_box = QVBoxLayout()

        self.v_box.addLayout(self.h_box0)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.setLayout(self.v_box)

        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        msg = QMessageBox()
        msg.setDetailedText(f"""        {self.num1_line.text()} + {self.num2_line.text()} = {int(self.num1_line.text()) + int(self.num2_line.text())}
        {self.num1_line.text()} - {self.num2_line.text()} = {int(self.num1_line.text()) - int(self.num2_line.text())}
        {self.num1_line.text()} * {self.num2_line.text()} = {int(self.num1_line.text()) * int(self.num2_line.text())}
        {self.num1_line.text()} / {self.num2_line.text()} = {int(self.num1_line.text()) / int(self.num2_line.text())}""")
        msg.setText(f"kiritilgan uzgaruvchilar {self.num1_line.text()} va {self.num2_line.text()} ")
        msg.exec_()




if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
