from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL
import sys

class HelloWorldOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(HelloWorldOpenGLWidget, self).__init__(parent)
        self.rotation_angle = 0.0

    def initializeGL(self):
        pass

    def resizeGL(self, w, h):
        pass

    def paintGL(self):
        # Clear the background
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        # Draw a red triangle with southeast shadow
        GL.glPushMatrix()
        GL.glRotatef(self.rotation_angle, 0.0, 0.0, 1.0)
        GL.glBegin(GL.GL_TRIANGLES)

        GL.glColor3f(1.0, 0.0, 0.0)  # Red

        # Bottom-left with shadow
        GL.glVertex3f(-0.6, -0.6, 0.0)

        # Bottom-right with shadow
        GL.glColor3f(0.5, 0.0, 0.0)  # Darker red for shadow
        GL.glVertex3f(0.6, -0.6, 0.0)

        # Top
        GL.glColor3f(1.0, 0.0, 0.0)  # Red for the rest
        GL.glVertex3f(0.0, 0.6, 0.0)

        GL.glEnd()
        GL.glPopMatrix()

    def setRotationAngle(self, angle):
        self.rotation_angle = angle
        self.update()

class HelloWorldApp(QWidget):
    def __init__(self):
        super(HelloWorldApp, self).__init__()

        self.setWindowTitle("Hello World with PySide and OpenGL")
        self.setGeometry(100, 100, 400, 350)  # Increased height to accommodate buttons

        # Set up OpenGL widget
        self.opengl_widget = HelloWorldOpenGLWidget(self)

        # Create layout and add OpenGL widget to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.opengl_widget)

        # Create clockwise and anticlockwise rotation buttons
        self.btn_clockwise = QPushButton("Rotate Clockwise", self)
        self.btn_anticlockwise = QPushButton("Rotate Anticlockwise", self)

        # Connect buttons to rotation methods
        self.btn_clockwise.clicked.connect(self.rotate_clockwise)
        self.btn_anticlockwise.clicked.connect(self.rotate_anticlockwise)

        # Add buttons to layout
        layout.addWidget(self.btn_clockwise)
        layout.addWidget(self.btn_anticlockwise)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def rotate_clockwise(self):
        current_angle = self.opengl_widget.rotation_angle
        new_angle = current_angle + 1.0
        self.opengl_widget.setRotationAngle(new_angle)

    def rotate_anticlockwise(self):
        current_angle = self.opengl_widget.rotation_angle
        new_angle = current_angle - 1.0
        self.opengl_widget.setRotationAngle(new_angle)

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create the main window
    hello_world_app = HelloWorldApp()
    hello_world_app.show()

    # Start event loop
    sys.exit(app.exec())
