from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, 
    QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy,
    QSpacerItem, QLineEdit, QButtonGroup
)

# import ffmpeg, datetime, subprocess, time

class AddMacroWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Macro")
        self.parentLayout = QVBoxLayout()
        self.init_name_editline()


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
        QButto

def main():
    app = QApplication([])
    main_window = AddMacroWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()


    

