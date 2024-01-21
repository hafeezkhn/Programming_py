from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
import sys

def button_clicked(data):
    print("you clicked button",data)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("APP")

button = QPushButton("Press ME")
button.setCheckable(True)
button.clicked.connect(button_clicked)

window.setCentralWidget(button)
window.show()

app.exec()

