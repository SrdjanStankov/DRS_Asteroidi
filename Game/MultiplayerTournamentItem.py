from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QButtonGroup

class MultplayerTournamentItem():
    def __init__(self, y_pos, x_pos, startCheck:int):
        tb_x_pos = x_pos
        cb_x_pos = x_pos + 300
        cb_x_step = 75

        self.textbox = QLineEdit()
        self.textbox.move(tb_x_pos, y_pos)
        self.textbox.resize(280, 40)
        font1 = self.textbox.font()
        font1.setPointSize(20)
        self.textbox.setFont(font1)

        self.buttonGroup = QButtonGroup()
        self.radiobutton1 = QRadioButton("Gray")
        self.radiobutton2 = QRadioButton("Red")
        self.radiobutton3 = QRadioButton("Yellow")
        self.radiobutton4 = QRadioButton("Green")
        font = QFont()
        font.setStyleHint(QFont.Helvetica)
        font.setPointSize(13)
        font.setBold(True)
        self.radiobutton1.setFont(font)
        self.radiobutton2.setFont(font)
        self.radiobutton3.setFont(font)
        self.radiobutton4.setFont(font)

        self.buttonGroup.addButton(self.radiobutton1)
        self.buttonGroup.addButton(self.radiobutton2)
        self.buttonGroup.addButton(self.radiobutton3)
        self.buttonGroup.addButton(self.radiobutton4)

        self.buttonGroup.setId(self.radiobutton1, 1)
        self.buttonGroup.setId(self.radiobutton2, 2)
        self.buttonGroup.setId(self.radiobutton3, 3)
        self.buttonGroup.setId(self.radiobutton4, 4)

        if startCheck is 1:
            self.radiobutton1.setChecked(True)
        elif startCheck is 2:
            self.radiobutton2.setChecked(True)
        elif startCheck is 3:
            self.radiobutton3.setChecked(True)
        else:
            self.radiobutton4.setChecked(True)


        y_plus = 7
        self.radiobutton1.move(cb_x_pos, y_pos + y_plus)
        self.radiobutton2.move(cb_x_pos + cb_x_step, y_pos + y_plus)
        self.radiobutton3.move(cb_x_pos + cb_x_step * 2, y_pos + y_plus)
        self.radiobutton4.move(cb_x_pos + cb_x_step * 3, y_pos + y_plus)

    def hideAllWidgets(self):
        self.textbox.hide()
        self.radiobutton1.hide()
        self.radiobutton2.hide()
        self.radiobutton3.hide()
        self.radiobutton4.hide()

    def showAllWidgets(self):
        self.textbox.show()
        # self.radiobutton1.show()
        # self.radiobutton2.show()
        # self.radiobutton3.show()
        # self.radiobutton4.show()
