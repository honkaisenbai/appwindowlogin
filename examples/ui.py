import sys

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QLineEdit,QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login App")
        self.setWindowIcon(QIcon("./assets/img/logo.png"))
        self.setFixedSize(QSize(400, 300))

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Logo
        logo_label = QLabel()
        logo_path = "./assets/img/logo.png"
        pixmap = QPixmap(logo_path)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        # Username text
        username_label = QLabel("Username")
        username_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(username_label)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMaxLength(10)
        layout.addWidget(self.username_input)

        # Password text
        username_label = QLabel("Password")
        username_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(username_label)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setFixedWidth(120)
        self.login_button.setStyleSheet("""
            QPushButton {
            background-color: #0078d7;
            color: white;
            border-radius: 6px;
            font-size: 16px;
            padding: 8px 0;
            transition: width 0.2s;
            }
        """)
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Animation for hover
        self.anim = QPropertyAnimation(self.login_button, b"minimumWidth")
        self.login_button.installEventFilter(self)

        # Connect button click to show Hello World UI
        def show_hello_world(self):
            hello_widget = QWidget()
            hello_layout = QVBoxLayout()
            hello_label = QLabel("Hello World")
            hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hello_layout.addWidget(hello_label)
            hello_widget.setLayout(hello_layout)

        self.login_button.clicked.connect(show_hello_world)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    

    
        def eventFilter(self, obj, event):
            if obj == self.login_button:
                if event.type() == event.Type.Enter:
                    self.anim.stop()
                    self.anim.setDuration(200)
                    self.anim.setStartValue(self.login_button.width())
                    self.anim.setEndValue(150)
                    self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
                    self.anim.start()
                elif event.type() == event.Type.Leave:
                    self.anim.stop()
                    self.anim.setDuration(200)
                    self.anim.setStartValue(self.login_button.width())
                    self.anim.setEndValue(120)
                    self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
                    self.anim.start()
            return super().eventFilter(obj, event)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()