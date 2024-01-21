from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QHBoxLayout
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPainter, QColor
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtGui import QFont
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

        # Draw circular static scale
        self.drawCircularScale()

        # Draw a simple representation of an aircraft
        GL.glBegin(GL.GL_TRIANGLES)
        GL.glColor3f(1.0, 1.0, 1.0)  # White
        GL.glVertex3f(0.0, 1.0, 0.0)
        GL.glVertex3f(-0.5, -1.0, 0.0)
        GL.glVertex3f(0.5, -1.0, 0.0)
        GL.glEnd()

        # Draw pitch and roll values
        self.drawPitchRollValues()

    def drawCircularScale(self):
        num_circles = 5  # Number of concentric circles
        circle_colors = [(0.5, 0.5, 0.5), (0.4, 0.4, 0.4), (0.3, 0.3, 0.3), (0.2, 0.2, 0.2), (0.1, 0.1, 0.1)]

        num_points = 360
        max_radius = 1.5

        for i in range(num_circles):
            current_radius = max_radius * (i + 1) / num_circles
            current_color = circle_colors[i]

            GL.glColor3f(*current_color)

            # Draw each circle
            GL.glBegin(GL.GL_LINE_LOOP)
            for j in range(num_points):
                angle = math.radians(j)
                x = current_radius * math.cos(angle)
                z = current_radius * math.sin(angle)
                GL.glVertex3f(x, 0.0, z)
            GL.glEnd()

    def drawPitchRollValues(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        font = QFont("Arial", 12)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))  # White color for text

        # Draw pitch value
        pitch_text = f"Pitch: {self.pitch_angle:.2f} degrees"
        painter.drawText(self.width() - 200, 20, pitch_text)

        # Draw roll value
        roll_text = f"Roll: {self.roll_angle:.2f} degrees"
        painter.drawText(self.width() - 200, 40, roll_text)

        painter.end()

    def setPitchAngle(self, angle):
        self.pitch_angle = angle
        self.update()

    def setRollAngle(self, angle):
        self.roll_angle = angle
        self.update()

class FlightDisplayApp(QWidget):
    # Define signals for pitch and roll updates
    pitch_updated = Signal(int)
    roll_updated = Signal(int)
    def __init__(self):
        super(FlightDisplayApp, self).__init__()

        self.setWindowTitle("Flight Display System")
        self.setGeometry(100, 100, 800, 600)

        # Set up OpenGL widget
        self.flight_display_widget = FlightDisplayOpenGLWidget(self)

        # Create sliders for pitch and roll control
        self.pitch_slider = QSlider(Qt.Vertical)
        self.pitch_slider.setMinimum(-90)
        self.pitch_slider.setMaximum(90)
        self.pitch_slider.setValue(0)
        self.pitch_slider.valueChanged.connect(self.on_pitch_slider_value_changed)

        self.roll_slider = QSlider(Qt.Vertical)
        self.roll_slider.setMinimum(-90)
        self.roll_slider.setMaximum(90)
        self.roll_slider.setValue(0)
        self.roll_slider.valueChanged.connect(self.on_roll_slider_value_changed)

        # Create layout
        main_layout = QHBoxLayout(self)

        # Add the OpenGL display and sliders to the main layout
        main_layout.addWidget(self.flight_display_widget)
        main_layout.addWidget(self.pitch_slider)
        main_layout.addWidget(self.roll_slider)

        self.setLayout(main_layout)
        
    def on_pitch_slider_value_changed(self, value):
        self.flight_display_widget.setPitchAngle(value)
        # Emit the signal when the pitch slider is changed
        self.pitch_updated.emit(value)

    def on_roll_slider_value_changed(self, value):
        self.flight_display_widget.setRollAngle(value)
        # Emit the signal when the roll slider is changed
        self.roll_updated.emit(value)

    # Method to update sliders externally
    def updateSliders(self, pitch_value, roll_value):
        self.pitch_slider.setValue(pitch_value)
        self.roll_slider.setValue(roll_value)
        self.flight_display_widget.setPitchAngle(pitch_value)
        self.flight_display_widget.setRollAngle(roll_value)

    def on_pitch_slider_value_changed(self, value):
        self.flight_display_widget.setPitchAngle(value)

    def on_roll_slider_value_changed(self, value):
        self.flight_display_widget.setRollAngle(value)

    def setPitchRollFromSimulink(self, pitch_value, roll_value):
        self.pitch_slider.setValue(pitch_value)
        self.roll_slider.setValue(roll_value)
        self.flight_display_widget.setPitchAngle(pitch_value)
        self.flight_display_widget.setRollAngle(roll_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    flight_display_app = FlightDisplayApp()
    flight_display_app.show()
    sys.exit(app.exec())