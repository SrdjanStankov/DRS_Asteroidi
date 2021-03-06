from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QBrush, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel, QLineEdit

from ClickableLabel import ClickableQLabel
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class MultiplayerThreePlayerScene(QGraphicsScene):
    def __init__(self, startMethod, backMethod, parent=None):
        super(MultiplayerThreePlayerScene, self).__init__(parent)

        screenWidth = 1370
        screenHeight = 730

        oImage = QPixmap("asteroids.jpg")
        sImage = oImage.scaled(QSize(screenWidth, screenHeight))  # resize Image to widgets size

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeight)

        self.y_start = 220
        self.y_step = 150

        player1 = QLabel('PLAYER 1')
        player2 = QLabel('PLAYER 2')
        player3 = QLabel('PLAYER 3')
        back = ClickableQLabel('BACK')
        start = ClickableQLabel('START')
        player1.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        player2.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        player3.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        start.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        back.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        player1.setGeometry(QRect(270, self.y_start, 300, 40))  # (x, y, width, height)
        player2.setGeometry(QRect(270, self.y_start + self.y_step, 300, 40))
        player3.setGeometry(QRect(270, self.y_start + self.y_step * 2, 300, 40))
        start.setGeometry(QRect(screenWidth - 200, screenHeight - 100, 300, 40))
        back.setGeometry(QRect(100, 100, 300, 40))

        commands1 = QLabel("left => left, right => right,\n up => up, down => down,\n shoot => ctrl")
        commands2 = QLabel("left => a,    right => d,    \n up => w,  down => s,   \n shoot => shift")
        commands3 = QLabel("left => g,    right => j,    \n up => y,  down => h,   \n shoot => v")
        commands1.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0,0,0,0%)")
        commands2.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0,0,0,0%)")
        commands3.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0,0,0,0%)")
        y_comm_start = self.y_start - 20
        commands1.setGeometry(QRect(1050, y_comm_start, 300, 64))
        commands2.setGeometry(QRect(1050, y_comm_start + self.y_step, 300, 64))
        commands3.setGeometry(QRect(1050, y_comm_start + self.y_step * 2, 300, 64))

        self.textbox1 = QLineEdit()
        self.textbox1.move(500, self.y_start)
        self.textbox1.resize(280, 40)
        font1 = self.textbox1.font()
        font1.setPointSize(20)
        self.textbox1.setFont(font1)

        self.textbox2 = QLineEdit()
        self.textbox2.move(500, self.y_start + self.y_step)
        self.textbox2.resize(280, 40)
        font2 = self.textbox2.font()
        font2.setPointSize(20)
        self.textbox2.setFont(font2)

        self.textbox3 = QLineEdit()
        self.textbox3.move(500, self.y_start + self.y_step * 2)
        self.textbox3.resize(280, 40)
        font3 = self.textbox3.font()
        font3.setPointSize(20)
        self.textbox3.setFont(font3)

        start.connect(startMethod)
        back.connect(backMethod)

        oImageSpaceshipGray = QPixmap("spaceship2.jpg")
        sImageSpaceshipGray = oImageSpaceshipGray.scaled(QSize(100, 100))  # resize Image to widgets size
        self.graphicsPixmapItem1 = QGraphicsPixmapItem(sImageSpaceshipGray)

        oImageSpaceshipYellow = QPixmap("spaceshipRed.jpg")
        sImageSpaceshipYellow = oImageSpaceshipYellow.scaled(QSize(100, 100))  # resize Image to widgets size
        self.graphicsPixmapItem2 = QGraphicsPixmapItem(sImageSpaceshipYellow)

        oImageSpaceshipRed = QPixmap("spaceshipYellow.jpg")
        sImageSpaceshipRed = oImageSpaceshipRed.scaled(QSize(100, 100))  # resize Image to widgets size
        self.graphicsPixmapItem3 = QGraphicsPixmapItem(sImageSpaceshipRed)


        self.graphicsPixmapItem1.setPos(900, self.y_start - 30)
        self.graphicsPixmapItem2.setPos(900, self.y_start + self.y_step - 30)
        self.graphicsPixmapItem3.setPos(900, self.y_start + self.y_step * 2 - 30)


        self.addItem(self.graphicsPixmapItem1)
        self.addItem(self.graphicsPixmapItem2)
        self.addItem(self.graphicsPixmapItem3)
        self.addWidget(player1)
        self.addWidget(player2)
        self.addWidget(player3)
        self.addWidget(start)
        self.addWidget(commands1)
        self.addWidget(commands2)
        self.addWidget(commands3)
        self.addWidget(back)
        self.addWidget(self.textbox1)
        self.addWidget(self.textbox2)
        self.addWidget(self.textbox3)
