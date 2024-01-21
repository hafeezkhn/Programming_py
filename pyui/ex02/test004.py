from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor, QImage, QPixmap
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL
import sys
import os
print("Current working directory:", os.getcwd())

class HelloWorldOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(HelloWorldOpenGLWidget, self).__init__(parent)
        self.rotation_angle = 0.0
        self.arrow_texture = self.loadTexture("arrow.png")  # Replace 'arrow.png' with your arrow image file
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # Update every 16 milliseconds (about 60 FPS)

    def initializeGL(self):
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

    def resizeGL(self, w, h):
        GL.glViewport(0, 0, w, h)

    def paintGL(self):
        # Clear the background
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        # Draw the rotating arrow icon
        GL.glPushMatrix()
        GL.glTranslatef(0.0, 0.0, 0.0)  # Set the initial position
        GL.glRotatef(self.rotation_angle, 0.0, 0.0, 1.0)
        
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.arrow_texture)
        GL.glBegin(GL.GL_QUADS)
        GL.glTexCoord2f(0.0, 0.0); GL.glVertex2f(-0.5, -0.5)
        GL.glTexCoord2f(1.0, 0.0); GL.glVertex2f(0.5, -0.5)
        GL.glTexCoord2f(1.0, 1.0); GL.glVertex2f(0.5, 0.5)
        GL.glTexCoord2f(0.0, 1.0); GL.glVertex2f(-0.5, 0.5)
        GL.glEnd()
        GL.glBindTexture(GL.GL_TEXTURE_2D, 0)

        GL.glPopMatrix()

    def animate(self):
        # Update rotation angle for animation
        self.rotation_angle += 1.0
        if self.rotation_angle >= 360.0:
            self.rotation_angle -= 360.0

        # Trigger a repaint
        self.update()

    def loadTexture(self, filename):
        image = QImage(filename)
        if image.isNull():
            print(f"Failed to load texture: {filename}")
            return 0

        texture = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, texture)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

        # Convert QImage to bytes format
        image = image.convertToFormat(QImage.Format_RGBA8888)
        image_data = image.bits().tobytes()

        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, image.width(), image.height(), 0,
            GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, image_data
        )

        GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
        return texture

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
