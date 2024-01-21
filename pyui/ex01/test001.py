from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QOpenGLWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor

import sys

class HelloWorldOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(HelloWorldOpenGLWidget, self).__init__(parent)

    def initializeGL(self):
        pass

    def resizeGL(self, w, h):
        pass

    def paintGL(self):
        # Clear the background
        self.qglClearColor(QColor(0, 0, 0, 255))
        self.glClear(self.GL_COLOR_BUFFER_BIT)

        # Render "Hello, World!" in the center
        painter = QPainter(self)
        painter.begin(self)

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(255, 255, 255))
        painter.setFont(self.font())

        text = "Hello, World!"
        painter.drawText(self.width() // 2 - 50, self.height() // 2, text)

        painter.end()

class HelloWorldApp(QWidget):
    def __init__(self):
        super(HelloWorldApp, self).__init__()

        self.setWindowTitle("Hello World with PySide and OpenGL")
        self.setGeometry(100, 100, 400, 300)

        # Set up OpenGL widget
        self.opengl_widget = HelloWorldOpenGLWidget(self)

        # Create layout and add OpenGL widget to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.opengl_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create the main window
    hello_world_app = HelloWorldApp()
    hello_world_app.show()

    # Start event loop
    sys.exit(app.exec())
