from PyQt5.QtCore import QSize
from PyQt5.QtGui import QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView


class View(QGraphicsView):
    def __init__(self, scene: QGraphicsScene, parent=None):
        super(View, self).__init__(scene, parent)


class GameView(QGraphicsView):
    def __init__(self, scene: QGraphicsScene, parent=None):
        super(GameView, self).__init__(scene, parent)

        self.setSceneRect(70, 0, 1280, 680)
        self.setViewportUpdateMode(QGraphicsView.NoViewportUpdate)
        self.setInteractive(False)