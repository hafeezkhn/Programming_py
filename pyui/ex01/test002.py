from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton

import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("APP")

button = QPushButton()
button.setText("Press")

window.setCentralWidget(button)
window.show()

app.exec()

