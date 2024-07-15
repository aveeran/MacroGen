from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, 
    QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy,
    QSpacerItem
)

from PyQt6.QtCore import Qt, QEvent

from db_connection import DatabaseConnection

# we are going to use sqlite3 and json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_conn = DatabaseConnection.get_instance()
        self.secondary_windows = []
        
        self.setWindowTitle("MacroGen")
        self.parentLayout = QVBoxLayout()
        self.buttonsLayout = QHBoxLayout()

        self.init_macro_table()

        button_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        buttonWidget = QWidget()
        self.buttonsLayout.addItem(button_spacer)
        self.init_action_buttons()
        buttonWidget.setLayout(self.buttonsLayout)
        
        self.parentLayout.addWidget(buttonWidget)

        container = QWidget()
        container.setLayout(self.parentLayout)
        self.setCentralWidget(container)

    def closeEvent(self, event):
        for x in self.secondary_windows:
            x.close()
        DatabaseConnection.close_connection()
        event.accept()

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
            for col, col_data in enumerate(row_data[0:5]):
                item = QTableWidgetItem(str(col_data)) # QTableWidgetItem accepts a string

                # right-align macro ID
                if col == 0:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        self.tableWidget.cellDoubleClicked.connect(self.on_row_double_clicked)

        self.parentLayout.addWidget(self.tableWidget)
    
    def on_row_double_clicked(self, row, column):
        pass

    def init_action_buttons(self):
        add_macro_btn = QPushButton("Add Macro")
        view_macro_btn = QPushButton("View Macro")
        exec_macro_btn = QPushButton("Execute Macro")

        add_macro_btn.clicked.connect(self.add_macro_handler)
        view_macro_btn.clicked.connect(self.delete_macro_handler)
        exec_macro_btn.clicked.connect(self.exec_macro_handler)

        self.buttonsLayout.addWidget(add_macro_btn)
        self.buttonsLayout.addWidget(view_macro_btn)
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