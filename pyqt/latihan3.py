import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 Perulangan')
window.setGeometry(10, 10, 400, 400)
window.move(110, 85)

layout = QVBoxLayout()
i = 0
while i < 10:
    layout.addWidget(QPushButton('HELLO WORLD'))
    i += 1
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
