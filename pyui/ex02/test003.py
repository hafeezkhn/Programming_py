from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QPainter, QColor
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL

import sys

class HelloWorldOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(HelloWorldOpenGLWidget, self).__init__(parent)
        self.rotation_angle = 0.0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # Update every 16 milliseconds (about 60 FPS)

    def initializeGL(self):
        pass

    def resizeGL(self, w, h):
        pass

    def paintGL(self):
        # Clear the background
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        # Draw a rotating colored triangle
        GL.glPushMatrix()
        GL.glRotatef(self.rotation_angle, 0.0, 0.0, 1.0)
        GL.glBegin(GL.GL_TRIANGLES)
        GL.glColor3f(1.0, 0.0, 0.0)  # Red
        GL.glVertex3f(-0.6, -0.6, 0.0)

        GL.glColor3f(0.0, 1.0, 0.0)  # Green
        GL.glVertex3f(0.6, -0.6, 0.0)

        GL.glColor3f(0.0, 0.0, 1.0)  # Blue
        GL.glVertex3f(0.0, 0.6, 0.0)
        GL.glEnd()
        GL.glPopMatrix()

    def animate(self):
        # Update rotation angle for animation
        self.rotation_angle += 1.0
        if self.rotation_angle >= 360.0:
            self.rotation_angle -= 360.0

        # Trigger a repaint
        self.update()

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
    app.exec()
