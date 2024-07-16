from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, 
    QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy,
    QSpacerItem, QLineEdit, QButtonGroup, QGridLayout, QLabel, QRadioButton
)

# import ffmpeg, datetime, subprocess, time

class AddMacroWindow(QMainWindow):
    TIMER = 0
    INDEX = 1
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Macro")
        self.parentLayout = QVBoxLayout()
        self.init_name_editline()

        self.init_start_widget()
        self.init_stop_widget()
        


        central_widget = QWidget()
        central_widget.setLayout(self.parentLayout)
        self.setCentralWidget(central_widget)

    def init_name_editline(self):
        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText("Macro Name")
        
        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_line_edit)
        
        name_widget = QWidget()
        name_widget.setLayout(name_layout)

        self.parentLayout.addWidget(name_widget)

    def init_start_widget(self):
        start_widget = QWidget()
        start_layout = QVBoxLayout()
        start_widget.setLayout(start_layout)

        start_label = QLabel("Start Recording")
        start_layout.addWidget(start_label)

        start_options_layout = QHBoxLayout()
        start_option_button_group = QButtonGroup()

        # start options buttons
        timer_button = QRadioButton("Timer")
        keybind_button = QRadioButton("Keybind: NULL")

        start_option_button_group.addButton(timer_button)
        start_option_button_group.addButton(keybind_button)
        start_option_button_group.buttonClicked.connect(self.start_widget_option_listener)

        start_option_button_layout = QVBoxLayout()
        start_option_button_layout.addWidget(timer_button)
        start_option_button_layout.addWidget(keybind_button)

        start_option_button_widget = QWidget()
        start_option_button_widget.setLayout(start_option_button_layout)

        start_options_layout.addWidget(start_option_button_widget)

        placeholder = QLabel("Placeholder")
        start_options_layout.addWidget(placeholder)

        start_option_widget = QWidget()
        start_option_widget.setLayout(start_options_layout)

        start_layout.addWidget(start_option_widget)
        self.parentLayout.addWidget(start_widget)

    def start_widget_option_listener(self, button):
        pass



    def init_stop_widget(self):
        stop_widget = QWidget()
        stop_layout = QVBoxLayout()
        stop_widget.setLayout(stop_layout)

        stop_label = QLabel("Stop Recording")
        stop_layout.addWidget(stop_label)

        stop_options_layout = QHBoxLayout()
        stop_option_button_group = QButtonGroup()

        # stop options buttons
        timer_button = QRadioButton("Timer")
        keybind_button = QRadioButton("Keybind: NULL")

        stop_option_button_group.addButton(timer_button)
        stop_option_button_group.addButton(keybind_button)

        stop_option_button_layout = QVBoxLayout()
        stop_option_button_layout.addWidget(timer_button)
        stop_option_button_layout.addWidget(keybind_button)

        stop_option_button_widget = QWidget()
        stop_option_button_widget.setLayout(stop_option_button_layout)

        stop_options_layout.addWidget(stop_option_button_widget)

        placeholder = QLabel("Placeholder")
        stop_options_layout.addWidget(placeholder)

        stop_option_widget = QWidget()
        stop_option_widget.setLayout(stop_options_layout)

        stop_layout.addWidget(stop_option_widget)
        self.parentLayout.addWidget(stop_widget)


def main():
    app = QApplication([])
    main_window = AddMacroWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()


    

