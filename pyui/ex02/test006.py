from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt
from OpenGL import GL, GLU
import sys

class HelloWorldOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(HelloWorldOpenGLWidget, self).__init__(parent)
        self.rotation_angle = 0.0

    def initializeGL(self):
        GL.glEnable(GL.GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        GL.glViewport(0, 0, w, h)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(45, w/h, 0.1, 100.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def paintGL(self):
        GL.glClearColor(1.0, 1.0, 0.0, 1.0)  # Yellow background
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        GL.glLoadIdentity()
        GL.glTranslatef(0.0, 0.0, -5.0)
        GL.glRotatef(self.rotation_angle, 1.0, 1.0, 1.0)

        # Draw a solid multicolor cube
        GL.glBegin(GL.GL_QUADS)
        
        GL.glColor3f(1.0, 0.0, 0.0)  # Red
        GL.glVertex3f(-0.5, 0.5, 0.5)
        GL.glVertex3f(0.5, 0.5, 0.5)
        GL.glVertex3f(0.5, -0.5, 0.5)
        GL.glVertex3f(-0.5, -0.5, 0.5)
        
        GL.glColor3f(0.0, 1.0, 0.0)  # Green
        GL.glVertex3f(-0.5, 0.5, -0.5)
        GL.glVertex3f(0.5, 0.5, -0.5)
        GL.glVertex3f(0.5, -0.5, -0.5)
        GL.glVertex3f(-0.5, -0.5, -0.5)
        
        GL.glColor3f(0.0, 0.0, 1.0)  # Blue
        GL.glVertex3f(-0.5, 0.5, 0.5)
        GL.glVertex3f(0.5, 0.5, 0.5)
        GL.glVertex3f(0.5, 0.5, -0.5)
        GL.glVertex3f(-0.5, 0.5, -0.5)
        
        GL.glColor3f(1.0, 1.0, 0.0)  # Yellow
        GL.glVertex3f(-0.5, -0.5, 0.5)
        GL.glVertex3f(0.5, -0.5, 0.5)
        GL.glVertex3f(0.5, -0.5, -0.5)
        GL.glVertex3f(-0.5, -0.5, -0.5)
        
        GL.glColor3f(1.0, 0.0, 1.0)  # Magenta
        GL.glVertex3f(0.5, 0.5, 0.5)
        GL.glVertex3f(0.5, -0.5, 0.5)
        GL.glVertex3f(0.5, -0.5, -0.5)
        GL.glVertex3f(0.5, 0.5, -0.5)
        
        GL.glColor3f(0.0, 1.0, 1.0)  # Cyan
        GL.glVertex3f(-0.5, 0.5, 0.5)
        GL.glVertex3f(-0.5, -0.5, 0.5)
        GL.glVertex3f(-0.5, -0.5, -0.5)
        GL.glVertex3f(-0.5, 0.5, -0.5)
        
        GL.glEnd()

    def setRotationAngle(self, angle):
        self.rotation_angle = angle
        self.update()

class HelloWorldApp(QWidget):
    def __init__(self):
        super(HelloWorldApp, self).__init__()

        self.setWindowTitle("Hello World with PySide and OpenGL")
        self.setGeometry(100, 100, 800, 600)

        # Set up OpenGL widget
        self.opengl_widget = HelloWorldOpenGLWidget(self)

        # Create a slider for rotation control
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(360)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.on_slider_value_changed)

        # Label to display the rotation angle
        self.angle_label = QLabel("Rotation Angle: 0")

        # Create layout and add OpenGL widget and slider to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.opengl_widget)
        layout.addWidget(self.slider)
        layout.addWidget(self.angle_label)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def on_slider_value_changed(self, value):
        self.angle_label.setText(f"Rotation Angle: {value}")
        self.opengl_widget.setRotationAngle(value)

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create the main window
    hello_world_app = HelloWorldApp()
    hello_world_app.show()

    # Start event loop
    sys.exit(app.exec())
