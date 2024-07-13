from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

class CreateMacroWindow(QWidget):
    dataSent = pyqtSignal(str)

    def __init__(self):
        super.__init()
        recording = False
        self.setWindowTitle("Create Macro")
        self.layout = QVBoxLayout()
        
        self.startButton = QPushButton("Start Recording Keybind")
        self.startButton.clicked.connect(self.start_recording)

        self.pauseButton = QPushButton("Pause/Unpause Recording Keybind")
        self.pauseButton.clicked.connect(self.pause_recording)

        self.endButton = QPushButton("End Recording Keybind")
        self.endButton.clicked.connect(self.end_recording)

        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.pauseButton)
        self.layout.addWidget(self.endButton)

    def start_recording(self):
        pass

    def pause_recording(self):
        pass

    def end_recording(self):
        pass

    