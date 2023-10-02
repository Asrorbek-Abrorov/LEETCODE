import sys
from os import system

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

system("clear")


class Dastur(QMainWindow):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.label = None
        self.setWindowTitle("Iphone 15 Pro Max")
        self.setGeometry(1455, 30, 360, 670)
        self.UiComponents()
        self.show()

        self.setStyleSheet("""background-color: black;
                            color: azure;
                            font-size: 20pt;
                            """)

    def UiComponents(self):

        self.label = QLabel(self)

        self.label.setGeometry(5, 180, 325, 70)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("""
                                  background : black;
                                  font-size: 60px""")

        self.label.setAlignment(Qt.AlignRight)

        ac = QPushButton("AC", self)
        ac.setGeometry(25, 260, 70, 70)
        ac.setStyleSheet("""background-color : rgb(147, 145, 141);
                        color: azure;
                        border-radius : 35px;""")

        ishora = QPushButton("+/-", self)
        ishora.setGeometry(105, 260, 70, 70)
        ishora.setStyleSheet("""background-color : rgb(147, 145, 141);
                        color: azure;
                        border-radius : 35px;""")

        foiz = QPushButton("%", self)
        foiz.setGeometry(185, 260, 70, 70)
        foiz.setStyleSheet("""background-color : rgb(147, 145, 141);
                            color: azure;
                            border-radius : 35px;""")

        bolish = QPushButton("/", self)
        bolish.setGeometry(265, 260, 70, 70)
        bolish.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        yetti = QPushButton("7", self)
        yetti.setGeometry(25, 340, 70, 70)
        yetti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        sakiz = QPushButton("8", self)
        sakiz.setGeometry(105, 340, 70, 70)
        sakiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        toqqiz = QPushButton("9", self)
        toqqiz.setGeometry(185, 340, 70, 70)
        toqqiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        kopaytirma = QPushButton("x", self)
        kopaytirma.setGeometry(265, 340, 70, 70)
        kopaytirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        tort = QPushButton("4", self)
        tort.setGeometry(25, 415, 70, 70)
        tort.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        besh = QPushButton("5", self)
        besh.setGeometry(105, 415, 70, 70)
        besh.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        olti = QPushButton("6", self)
        olti.setGeometry(185, 415, 70, 70)
        olti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        ayirma = QPushButton("-", self)
        ayirma.setGeometry(265, 415, 70, 70)
        ayirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        bir = QPushButton("1", self)
        bir.setGeometry(25, 490, 70, 70)
        bir.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        ikki = QPushButton("2", self)
        ikki.setGeometry(105, 490, 70, 70)
        ikki.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        uch = QPushButton("3", self)
        uch.setGeometry(185, 490, 70, 70)
        uch.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        qoshish = QPushButton("+", self)
        qoshish.setGeometry(265, 490, 70, 70)
        qoshish.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        nol = QPushButton("0          ", self)
        nol.setGeometry(25, 565, 150, 70)
        nol.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        nuqta = QPushButton(".", self)
        nuqta.setGeometry(185, 565, 70, 70)
        nuqta.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        teng = QPushButton("=", self)
        teng.setGeometry(265, 565, 70, 70)
        teng.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        ayirma.clicked.connect(self.action_ayirish)
        teng.clicked.connect(self.action_teng)
        bolish.clicked.connect(self.action_bolish)
        kopaytirma.clicked.connect(self.action_kopaytirish)
        qoshish.clicked.connect(self.action_qoshish)
        ac.clicked.connect(self.action_ac)
        ishora.clicked.connect(self.action_belgi)
        foiz.clicked.connect(self.action_foiz)
        nuqta.clicked.connect(self.action_nuqta)
        nol.clicked.connect(self.action0)
        bir.clicked.connect(self.action1)
        ikki.clicked.connect(self.action2)
        uch.clicked.connect(self.action3)
        tort.clicked.connect(self.action4)
        besh.clicked.connect(self.action5)
        olti.clicked.connect(self.action6)
        yetti.clicked.connect(self.action7)
        sakiz.clicked.connect(self.action8)
        toqqiz.clicked.connect(self.action9)

    def action_teng(forma):
        tenglik = forma.label.text()

        try:
            ans = eval(tenglik)

            forma.label.setText(str(ans))

        except:
            forma.label.setText("Wrong Input")

    def action_qoshish(forma):
        text = forma.label.text()
        forma.label.setText(text + " + ")

    def action_ayirish(forma):
        text = forma.label.text()
        forma.label.setText(text + " - ")

    def action_bolish(forma):
        text = forma.label.text()
        forma.label.setText(text + " / ")

    def action_kopaytirish(forma):
        text = forma.label.text()
        forma.label.setText(text + " * ")

    def action_foiz(forma):
        text = forma.label.text()
        forma.label.setText(text + " //100 ")

    def action_belgi(forma):
        text = forma.label.text()
        forma.label.setText(text + " +/- ")

    def action_nuqta(forma):
        text = forma.label.text()
        forma.label.setText(text + ".")

    def action0(forma):
        text = forma.label.text()
        forma.label.setText(text + "0")

    def action1(forma):
        text = forma.label.text()
        forma.label.setText(text + "1")

    def action2(forma):
        text = forma.label.text()
        forma.label.setText(text + "2")

    def action3(forma):
        text = forma.label.text()
        forma.label.setText(text + "3")

    def action4(forma):
        text = forma.label.text()
        forma.label.setText(text + "4")

    def action5(forma):
        text = forma.label.text()
        forma.label.setText(text + "5")

    def action6(forma):
        text = forma.label.text()
        forma.label.setText(text + "6")

    def action7(forma):
        text = forma.label.text()
        forma.label.setText(text + "7")

    def action8(forma):
        text = forma.label.text()
        forma.label.setText(text + "8")

    def action9(forma):
        text = forma.label.text()
        forma.label.setText(text + "9")

    def action_ac(forma):
        forma.label.setText("")


app = QApplication([])
dastur = Dastur()
sys.exit(app.exec_())
