from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout ,QWidget, QLabel, QSpinBox, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 500)
        parentLayout = QVBoxLayout()
        self.setWindowTitle("MacroGen")

        # self.spinBox = QSpinBox()
        # self.spinBox.setMinimum(1)
        # self.spinBox.setMaximum(1e5)

        # self.comboBox = QComboBox()

        self.buttonGroup = QButtonGroup()
        self.radioButtonRed = QRadioButton("Red")
        self.radioButtonYellow = QRadioButton("Yellow")
        self.radioButtonBlue = QRadioButton("Blue")

        self.buttonGroup.addButton(self.radioButtonRed)
        self.buttonGroup.addButton(self.radioButtonYellow)
        self.buttonGroup.addButton(self.radioButtonBlue)

        parentLayout.addWidget(self.radioButtonRed)
        parentLayout.addWidget(self.radioButtonYellow)
        parentLayout.addWidget(self.radioButtonBlue)

        

        self.button = QPushButton("Button 1")
        

        # self.comboBox.addItem("Red")
        # self.comboBox.addItem("Yellow")
        # self.comboBox.addItem("Blue")

        # self.comboBox.currentTextChanged.connect(self.textChangeHandler)

        # parentLayout.addWidget(self.lineEdit)
        # parentLayout.addWidget(self.comboBox)
        # parentLayout.addWidget(self.spinBox)
        parentLayout.addWidget(self.button)

        self.button.clicked.connect(self.clickHandler)


        self.label = QLabel("Layout", alignment=Qt.AlignmentFlag.AlignCenter)
        parentLayout.addWidget(self.label) # row col row-span col-span


        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)

        self.setCentralWidget(centerWidget)

    def clickHandler(self):
        print("Button Clicked!")
        self.label.setText("Button has been clicked!")
        print(self.buttonGroup.checkedButton().text())

    def textChangeHandler(self, currentText):
        print(currentText)





app = QApplication([])
window = Window()

window.show()
app.exec()