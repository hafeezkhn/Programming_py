from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt
from OpenGL import GL, GLU
import sys
import math

class FlightDisplayOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(FlightDisplayOpenGLWidget, self).__init__(parent)
        self.pitch_angle = 0.0
        self.roll_angle = 0.0

    def initializeGL(self):
        GL.glEnable(GL.GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        GL.glViewport(0, 0, w, h)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(45, w/h, 0.1, 100.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def paintGL(self):
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        GL.glLoadIdentity()
        GL.glTranslatef(0.0, 0.0, -5.0)
        GL.glRotatef(self.pitch_angle, 1.0, 0.0, 0.0)
        GL.glRotatef(self.roll_angle, 0.0, 0.0, 1.0)

        # Draw a simple representation of an aircraft
        GL.glBegin(GL.GL_TRIANGLES)

        GL.glColor3f(1.0, 1.0, 1.0)  # White
        GL.glVertex3f(0.0, 1.0, 0.0)
        GL.glVertex3f(-0.5, -1.0, 0.0)
        GL.glVertex3f(0.5, -1.0, 0.0)

        GL.glEnd()

    def setPitchAngle(self, angle):
        self.pitch_angle = angle
        self.update()

    def setRollAngle(self, angle):
        self.roll_angle = angle
        self.update()

class FlightDisplayApp(QWidget):
    def __init__(self):
        super(FlightDisplayApp, self).__init__()

        self.setWindowTitle("Flight Display System")
        self.setGeometry(100, 100, 800, 600)

        # Set up OpenGL widget
        self.flight_display_widget = FlightDisplayOpenGLWidget(self)

        # Create sliders for pitch and roll control
        self.pitch_slider = QSlider(Qt.Horizontal)
        self.pitch_slider.setMinimum(-90)
        self.pitch_slider.setMaximum(90)
        self.pitch_slider.setValue(0)
        self.pitch_slider.valueChanged.connect(self.on_pitch_slider_value_changed)

        self.roll_slider = QSlider(Qt.Horizontal)
        self.roll_slider.setMinimum(-90)
        self.roll_slider.setMaximum(90)
        self.roll_slider.setValue(0)
        self.roll_slider.valueChanged.connect(self.on_roll_slider_value_changed)

        # Labels to display pitch and roll angles
        self.pitch_label = QLabel("Pitch Angle: 0")
        self.roll_label = QLabel("Roll Angle: 0")

        # Create layout and add components to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.flight_display_widget)
        layout.addWidget(self.pitch_slider)
        layout.addWidget(self.pitch_label)
        layout.addWidget(self.roll_slider)
        layout.addWidget(self.roll_label)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def on_pitch_slider_value_changed(self, value):
        self.pitch_label.setText(f"Pitch Angle: {value}")
        self.flight_display_widget.setPitchAngle(value)

    def on_roll_slider_value_changed(self, value):
        self.roll_label.setText(f"Roll Angle: {value}")
        self.flight_display_widget.setRollAngle(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    flight_display_app = FlightDisplayApp()
    flight_display_app.show()
    sys.exit(app.exec())
