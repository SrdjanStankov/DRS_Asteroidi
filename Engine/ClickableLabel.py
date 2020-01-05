
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal

class ClickableQLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, text, parent=None):
        QLabel.__init__(self, parent)
        self.setText(text)


    def mousePressEvent(self, ev):
        self.clicked.emit()

    def connect(self, method):
        self.clicked.connect(method)

    def enterEvent(self, event):
        self.setStyleSheet("color: yellow; font-size: 40px; background-color: rgba(0,0,0,0%)")

    def leaveEvent(self, event):
        self.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")


