import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QCoreApplication
import healMonster3


class heal2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.back = QLabel(self)
        self.back.setGeometry(0, 0, 852, 1202)
        self.pixmap = QPixmap("image/back_image/heal_2.jpg")
        self.back.setPixmap(self.pixmap)
        #포켓몬1
        self.moster1 = QLabel(self)
        self.moster1.move(100, 150)
        self.moster1.resize(150, 150)
        self.pixmap = QPixmap("image/btn_image/gorapaduck_btn.png")
        self.moster1.setPixmap(self.pixmap)

        monster1btn = QPushButton(self)
        monster1btn.setStyleSheet("background-color:rgb(0,0,0,0);")

        monster1name = QLabel("포켓몬1 이름", self)
        monster1hp = QLabel("포켓몬1생명", self)
        monster1name.resize(100, 50)
        monster1hp.resize(100, 50)
        monster1btn.resize(150, 150)
        monster1name.move(260, 150)
        monster1hp.move(260, 200)
        monster1btn.move(100, 150)
        # 포켓몬2
        self.moster2 = QLabel(self)
        self.moster2.move(450, 150)
        self.moster2.resize(150, 150)
        self.pixmap = QPixmap("image/btn_image/gorapaduck_btn.png")
        self.moster2.setPixmap(self.pixmap)

        monster2btn = QPushButton(self)
        monster2btn.setStyleSheet("background-color:rgb(0,0,0,0);")


        monster2name = QLabel("포켓몬2 이름", self)
        monster2hp = QLabel("포켓몬 2체력", self)
        monster2name.resize(100, 50)
        monster2hp.resize(100, 50)
        monster2btn.resize(150, 150)
        monster2name.move(610, 150)
        monster2hp.move(610, 200)
        monster2btn.move(450, 150)
        # 포켓몬3
        self.moster3 = QLabel(self)
        self.moster3.move(100, 400)
        self.moster3.resize(150, 150)
        self.pixmap = QPixmap("image/btn_image/gorapaduck_btn.png")
        self.moster3.setPixmap(self.pixmap)

        monster3btn = QPushButton(self)
        monster3btn.setStyleSheet("background-color:rgb(0,0,0,0);")


        monster3name = QLabel("포켓몬3 이름", self)
        monster3hp = QLabel("포켓몬3 체력", self)
        monster3name.resize(100, 50)
        monster3hp.resize(100, 50)
        monster3btn.resize(150, 150)
        monster3name.move(260, 400)
        monster3hp.move(260, 450)
        monster3btn.move(100, 400)
        # 포켓몬4
        self.moster4 = QLabel(self)
        self.moster4.move(450, 400)
        self.moster4.resize(150, 150)
        self.pixmap = QPixmap("image/btn_image/gorapaduck_btn.png")
        self.moster4.setPixmap(self.pixmap)

        monster4btn = QPushButton(self)
        monster4btn.setStyleSheet("background-color:rgb(0,0,0,0);")


        monster4name = QLabel("포켓몬4 이름", self)
        monster4hp = QLabel("포켓몬4 체력", self)
        monster4name.resize(100, 50)
        monster4hp.resize(100, 50)
        monster4btn.resize(150, 150)
        monster4name.move(610, 400)
        monster4hp.move(610, 450)
        monster4btn.move(450, 400)
        # 포켓몬5
        self.moster5 = QLabel(self)
        self.moster5.move(100, 650)
        self.moster5.resize(150, 150)
        self.pixmap = QPixmap("image/btn_image/gorapaduck_btn.png")
        self.moster5.setPixmap(self.pixmap)

        monster5btn = QPushButton(self)
        monster5btn.setStyleSheet("background-color:rgb(0,0,0,0);")


        monster5name = QLabel("포켓몬5 이름", self)
        monster5hp = QLabel("포켓몬5 체력", self)
        monster5name.resize(100, 50)
        monster5hp.resize(100, 50)
        monster5btn.resize(150, 150)
        monster5name.move(260, 650)
        monster5hp.move(260, 700)
        monster5btn.move(100, 650)

        noticemsg = QLabel("※ 포켓몬은 한 번에 두 개까지 선택 가능합니다.", self)
        noticemsg.resize(500, 50)
        noticemsg.move(230, 850)

        self.select = QLabel(self)
        self.select.move(250, 950)
        self.select.resize(350, 120)
        self.pixmap = QPixmap("image/btn_image/select.png")
        self.select.setPixmap(self.pixmap)

        selectbtn = QPushButton(self)
        selectbtn.setStyleSheet("background-color:rgb(0,0,0,0);")
        selectbtn.resize(350, 120)
        selectbtn.move(250, 950)
        selectbtn.clicked.connect(self.clickSelect)

        self.resize(850, 1200)
        self.setWindowTitle("포켓몬 치료2")
        self.show()

    def clickSelect(self):
        self.close()
        self.h3 = healMonster3.heal3()



