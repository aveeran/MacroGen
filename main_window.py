from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
from db_connection import DatabaseConnection
import json

# we are going to use sqlite3 and json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_conn = DatabaseConnection.get_instance()
        
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

    def closeEvent(self, event):
        DatabaseConnection.close_connection()

    def init_macro_table(self):
        query = "SELECT * FROM macros"
        cursor = self.db_conn.execute_query(query)
        rows = cursor.fetchall()
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(5)

        horizontal_header_labels = ["ID", "NAME", "DATE CREATED", "DATE MODIFIED", "CONTENT"]
        self.tableWidget.setHorizontalHeaderLabels(horizontal_header_labels)

        for row, row_data in enumerate(rows):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(col_data)
                self.tableWidget.setItem(row, col, item)
        self.parentLayout.addWidget(self.tableWidget)

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