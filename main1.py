import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
import os
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


from time_tracker import topics


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Time Tracker")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignTop)

        self.topics_label = QLabel("Topics:")
        self.layout.addWidget(self.topics_label)

        self.topics_table = QTableWidget()
        self.layout.addWidget(self.topics_table)

        self.date_label = QLabel("Select Date:")
        self.layout.addWidget(self.date_label)

        self.date_button_layout = QHBoxLayout()
        self.layout.addLayout(self.date_button_layout)

        self.date_button_layout.addWidget(QLabel("Date:"))
        self.date_input = QLabel()
        self.date_button_layout.addWidget(self.date_input)

        self.add_date_button = QPushButton("Add Date")
        self.add_date_button.clicked.connect(self.add_date)
        self.date_button_layout.addWidget(self.add_date_button)

        self.select_topics_label = QLabel("Select Topics:")
        self.layout.addWidget(self.select_topics_label)

        self.select_topics_table = QTableWidget()
        self.layout.addWidget(self.select_topics_table)

        self.start_time_button = QPushButton("Start Time")
        self.start_time_button.clicked.connect(self.start_time)
        self.layout.addWidget(self.start_time_button)

        self.end_time_button = QPushButton("End Time")
        self.end_time_button.clicked.connect(self.end_time)
        self.layout.addWidget(self.end_time_button)

        self.save_table_button = QPushButton("Save Table")
        self.save_table_button.clicked.connect(self.save_table)
        self.layout.addWidget(self.save_table_button)

        self.show()

        self.current_date = None
        self.not_null = None

        self.load_topics()

    def load_topics(self):
        try:
            topics_instance = topics()
            topics_list = topics_instance.alltopics()

            self.topics_table.setColumnCount(2)
            self.topics_table.setHorizontalHeaderLabels(["Main Topics", "Sub Topics"])
            self.topics_table.setRowCount(len(topics_list))

            for row, topic in enumerate(topics_list.values):
                for col, value in enumerate(topic):
                    item = QTableWidgetItem(str(value))
                    self.topics_table.setItem(row, col, item)

            self.topics_table.resizeColumnsToContents()

        except Exception as e:
            print(e)

    def add_date(self):
        try:
            current_date = datetime.now().strftime("%Y-%m-%d")
            self.date_input.setText(current_date)

            topics_instance = topics()
            topics_instance.add_date(current_date)

            self.current_date = current_date
            self.not_null = None

            self.load_select_topics()

        except Exception as e:
            print(e)

    def load_select_topics(self):
        try:
            topics_instance = topics()
            not_null_topics = topics_instance.select_topics(0, 1, 2)

            self.select_topics_table.setColumnCount(len(not_null_topics.columns))
            self.select_topics_table.setHorizontalHeaderLabels(not_null_topics.columns)
            self.select_topics_table.setRowCount(len(not_null_topics))

            for row, topic in enumerate(not_null_topics.values):
                for col, value in enumerate(topic):
                    item = QTableWidgetItem(str(value))
                    self.select_topics_table.setItem(row, col, item)

            self.select_topics_table.resizeColumnsToContents()

        except Exception as e:
            print(e)

    def start_time(self):
        try:
            selected_row = self.select_topics_table.currentRow()
            if selected_row >= 0:
                topics_instance = topics()
                not_null_topics = topics_instance.time_start(selected_row, 1)

                self.not_null = not_null_topics

                self.load_select_topics()

        except Exception as e:
            print(e)

    def end_time(self):
        try:
            selected_row = self.select_topics_table.currentRow()
            if selected_row >= 0:
                topics_instance = topics()
                not_null_topics = topics_instance.end_time(selected_row, 1)

                self.not_null = not_null_topics

                self.load_select_topics()

        except Exception as e:
            print(e)

    def save_table(self):
        try:
            if self.current_date and self.not_null is not None:
                topics_instance = topics()
                table_data = topics_instance.table()

                # Create the directory if it doesn't exist
                directory = f'time_slots'
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Save the file into the directory
                file_path = os.path.join(directory, f'time_slots_{self.current_date}_data.csv')
                table_data.to_csv(file_path, index=False)
                print(f"Table saved to {file_path}")

            else:
                print("Please select topics first.")

        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
