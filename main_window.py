from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
from db_connection import DatabaseConnection
import json

# we are going to use sqlite3 and json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.conn = DatabaseConnection.get_connection()
        self.temp_data()
        
        self.setWindowTitle("MacroGen")
        self.parentLayout = QVBoxLayout()
        self.buttonsLayout = QHBoxLayout()

        self.init_macro_table()

        self.init_action_buttons()
        buttonWidget = QWidget()
        buttonWidget.setLayout(self.buttonsLayout)
        self.parentLayout.addWidget(buttonWidget)

        container = QWidget()
        container.setLayout(self.parentLayout)
        self.setCentralWidget(container)

    def temp_data(self):
        query = "INSERT INTO macros (name, date, date_modified, macro) VALUES (?, ?, ?, ?)"
        params = ('Example Macro', '20204-07-12', '2024-07-12', 'print("Hello, World!")')
        self.conn.execute_query(query, params)

        

    def init_macro_table(self):
        pass

    def init_action_buttons(self):
        add_macro_btn = QPushButton("Add Macro")
        delete_macro_btn = QPushButton("Delete Macro")
        exec_macro_btn = QPushButton("Execute Macro")

        add_macro_btn.clicked.connect(self.add_macro_handler)
        delete_macro_btn.clicked.connect(self.delete_macro_handler)
        exec_macro_btn.clicked.connect(self.exec_macro_handler)

        self.buttonsLayout.addWidget(add_macro_btn)
        self.buttonsLayout.addWidget(delete_macro_btn)
        self.buttonsLayout.addWidget(exec_macro_btn)


    def add_macro_handler(self):
        pass

    def delete_macro_handler(self):
        pass 

    def exec_macro_handler(self):
        pass

def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()