import sys

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QLineEdit,QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login App")
        self.setFixedSize(QSize(400, 300))

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMaxLength(10)
        layout.addWidget(self.username_input)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Login button
        login_button = QPushButton("Log In")
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()