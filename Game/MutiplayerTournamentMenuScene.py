
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QBrush, QColor, QImage, QPixmap, QFont
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel, QComboBox
from PyQt5.QtWidgets import QLineEdit, QRadioButton
from PyQt5.uic.properties import QtGui

from ClickableLabel import ClickableQLabel
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal
import MultiplayerTournamentItem as mpti

class MutiplayerTournamentMenuScene(QGraphicsScene):
    def __init__(self, startMethod, backMethod, parent=None):
        super(MutiplayerTournamentMenuScene, self).__init__(parent)

        screenWidth = 1370
        screenHeight = 730

        oImage = QPixmap("asteroids.jpg")
        sImage = oImage.scaled(QSize(screenWidth, screenHeight))  # resize Image to widgets size

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeight)


        chooseNumber = QLabel('Chose number of tournament participants :')
        chooseNumber.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0,0,0,0%)")
        chooseNumber.setGeometry(QRect(100, 200, 400, 40))

        back = ClickableQLabel('BACK')
        back.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        back.setGeometry(QRect(100, 100, 300, 40))
        back.connect(backMethod)

        start = ClickableQLabel('START')
        start.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        start.setGeometry(QRect(screenWidth - 200, screenHeight - 200, 300, 40))
        start.connect(startMethod)


        self.comboBox = QComboBox()
        self.comboBox.addItem("2")
        self.comboBox.addItem("4")
        self.comboBox.addItem("6")
        self.comboBox.addItem("8")
        self.comboBox.addItem("10")
        self.comboBox.move(250, 250)
        self.comboBox.resize(100, 40)
        font = QFont()
        font.setStyleHint(QFont.Helvetica)
        font.setPointSize(25)
        font.setBold(True)
        self.comboBox.setFont(font)

        #self.comboBox.currentIndexChanged.connect(self.onChange)
        self.comboBox.activated[str].connect(self.onChange)

        self.item_y_start = 100
        self.item_x_start = 550
        self.item_y_step = 50

        self.mpti1 = mpti.MultplayerTournamentItem(self.item_y_start, self.item_x_start, 1)
        self.mpti2 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step, self.item_x_start, 2)
        self.mpti3 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 2, self.item_x_start, 3)
        self.mpti4 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 3, self.item_x_start, 4)
        self.mpti5 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 4, self.item_x_start, 1)
        self.mpti6 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 5, self.item_x_start, 2)
        self.mpti7 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 6, self.item_x_start, 3)
        self.mpti8 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 7, self.item_x_start, 4)
        self.mpti9 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 8, self.item_x_start, 1)
        self.mpti10 = mpti.MultplayerTournamentItem(self.item_y_start + self.item_y_step * 9, self.item_x_start, 2)


        self.addWidget(chooseNumber)
        self.addWidget(start)
        self.addWidget(back)
        self.addWidget(self.comboBox)
        self.__addItemsToSceneFromMPItem(self.mpti1)
        self.__addItemsToSceneFromMPItem(self.mpti2)
        self.__addItemsToSceneFromMPItem(self.mpti3)
        self.__addItemsToSceneFromMPItem(self.mpti4)
        self.__addItemsToSceneFromMPItem(self.mpti5)
        self.__addItemsToSceneFromMPItem(self.mpti6)
        self.__addItemsToSceneFromMPItem(self.mpti7)
        self.__addItemsToSceneFromMPItem(self.mpti8)
        self.__addItemsToSceneFromMPItem(self.mpti9)
        self.__addItemsToSceneFromMPItem(self.mpti10)
        self.__hideEveryTBandRB()

        self.lastChecked = None


    def onChange(self):
        text = self.comboBox.currentText()

        if self.lastChecked is not None:
            self.__hideEveryTBandRB()

        if text == "2":
            self.mpti1.showAllWidgets()
            self.mpti2.showAllWidgets()
        elif text == "4":
            self.mpti1.showAllWidgets()
            self.mpti2.showAllWidgets()
            self.mpti3.showAllWidgets()
            self.mpti4.showAllWidgets()
        elif text == "6":
            self.mpti1.showAllWidgets()
            self.mpti2.showAllWidgets()
            self.mpti3.showAllWidgets()
            self.mpti4.showAllWidgets()
            self.mpti5.showAllWidgets()
            self.mpti6.showAllWidgets()
        elif text == "8":
            self.mpti1.showAllWidgets()
            self.mpti2.showAllWidgets()
            self.mpti3.showAllWidgets()
            self.mpti4.showAllWidgets()
            self.mpti5.showAllWidgets()
            self.mpti6.showAllWidgets()
            self.mpti7.showAllWidgets()
            self.mpti8.showAllWidgets()
        else:
            self.mpti1.showAllWidgets()
            self.mpti2.showAllWidgets()
            self.mpti3.showAllWidgets()
            self.mpti4.showAllWidgets()
            self.mpti5.showAllWidgets()
            self.mpti6.showAllWidgets()
            self.mpti7.showAllWidgets()
            self.mpti8.showAllWidgets()
            self.mpti9.showAllWidgets()
            self.mpti10.showAllWidgets()

        self.lastChecked = self.comboBox.currentText()

    def __addItemsToSceneFromMPItem(self, mpti):
        self.addWidget(mpti.textbox)
        self.addWidget(mpti.radiobutton1)
        self.addWidget(mpti.radiobutton2)
        self.addWidget(mpti.radiobutton3)
        self.addWidget(mpti.radiobutton4)


    def __hideEveryTBandRB(self):
        self.mpti1.hideAllWidgets()
        self.mpti2.hideAllWidgets()
        self.mpti3.hideAllWidgets()
        self.mpti4.hideAllWidgets()
        self.mpti5.hideAllWidgets()
        self.mpti6.hideAllWidgets()
        self.mpti7.hideAllWidgets()
        self.mpti8.hideAllWidgets()
        self.mpti9.hideAllWidgets()
        self.mpti10.hideAllWidgets()
