from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtCore import Qt

app = QApplication([])

window = QMainWindow()

window.setMinimumSize(400, 500)
window.setWindowTitle("MacroGen")

label = QLabel("Text goes here", alignment=Qt.AlignmentFlag.AlignCenter)
font = window.font()
font.setPointSize(17)
font.setBold(True)
label.setFont(font)

button = QPushButton("Click Me")
window.setCentralWidget(button)





window.show()
app.exec()