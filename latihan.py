import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class App(QWidget):

    def __init__(self, t):
        super().__init__()
        self.title = 'PyQt5 button'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 200
        self.initUI(t)
        self.move(110, 85)

    def initUI(self, t):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton(t, self)
        button.setStyleSheet('QPushButton { font-size: 20px; color : blue; } ')
        button.setToolTip('This is an example button')
        button.move(50, 50)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Tombol Ditekan')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App("Tombol Biru Ukuran 20px")

    sys.exit(app.exec_())
