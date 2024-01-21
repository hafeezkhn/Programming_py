from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton

import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.setWindowTitle("App")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)

app = QApplication(sys.argv)


window = ButtonHolder()

window.show()
app.exec()

