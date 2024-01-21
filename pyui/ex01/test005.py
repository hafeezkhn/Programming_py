from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QSlider
from PySide6.QtCore import Qt
import sys

def slider_clicked(data):
    print("moved clicked slider",data)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("APP")

slider = QSlider(window)
slider.setMaximum(100)
slider.setMinimum(0)
slider.setGeometry(50,50,200,20)
slider.setOrientation(Qt.Horizontal)
slider.valueChanged.connect(slider_clicked)


window.show()
app.exec()

