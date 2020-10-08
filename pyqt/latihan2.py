import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Latihan 2')
window.setGeometry(10, 10, 400, 100)
window.move(110, 85)

layout = QHBoxLayout()
button = QPushButton('p')
button.resize(100, 32)
button.move(50, 50)

layout.addWidget(button)
layout.addWidget(QPushButton('2'))
layout.addWidget(QPushButton('3'))
layout.addWidget(QPushButton('4'))
layout.addWidget(QPushButton('5'))

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
