import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, \
    QTableWidgetItem, QDialog, QDialogButtonBox
from PyQt5.QtGui import QFontMetrics, QPainter, QPixmap
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, \
    QTableWidgetItem, QFileDialog

import pandas as pd
import os
import time_tracker
import table_plan


class TimetableApp(QWidget):
    def __init__(self):
        super().__init__()
        self.table_plan = table_plan.Table()  # Create an instance of the Table class
        self.time_tracker = time_tracker.topics()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Timetable App")
        self.setGeometry(100, 100, 600, 400)
        self.showMaximized()

        self.label1 = QLabel("Break Time between Sessions (mins):")
        self.input1 = QLineEdit()

        self.label2 = QLabel("Total Number of Sessions:")
        self.input2 = QLineEdit()

        self.label3 = QLabel("Slot Select (0, 1, 2, or 3):")
        self.input3 = QLineEdit()

        self.generate_btn = QPushButton("Generate Timetable")
        self.generate_btn.clicked.connect(self.generate_timetable)

        self.save_btn = QPushButton("Save Table as Image")
        self.save_btn.setEnabled(False)  # Disable save button initially
        self.save_btn.clicked.connect(self.save_table_as_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.label3)
        layout.addWidget(self.input3)
        layout.addWidget(self.generate_btn)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def generate_timetable(self):
        try:
            self.table_plan.single_break_time = int(self.input1.text())
            self.table_plan.total_sessions = int(self.input2.text())
            self.table_plan.slot_select = int(self.input3.text())

            self.table_plan.table_data()

            self.setup_table()
            self.save_btn.setEnabled(True)  # Enable save button after generating the table

        except Exception as e:
            print(e)

    def setup_table(self):
        self.timetable_table = QTableWidget()
        self.timetable_table.setColumnCount(len(self.table_plan.columns))
        self.timetable_table.setRowCount(1)
        df = self.table_plan.read_csv()

        for i, column_name in enumerate(self.table_plan.columns):
            header_item = QTableWidgetItem(column_name)
            value = str(df.iloc[0, i])
            item = QTableWidgetItem(value)
            self.timetable_table.setHorizontalHeaderItem(i, header_item)
            self.timetable_table.setItem(0, i, item)

        self.timetable_table.resizeColumnsToContents()  # Adjust column widths to fit contents

        layout = QVBoxLayout()
        layout.addWidget(self.timetable_table)
        self.layout().addLayout(layout)

    def save_table_as_image(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Save Table as Image")

        layout = QVBoxLayout(dialog)

        pixmap = QPixmap(self.timetable_table.size())
        self.timetable_table.render(pixmap)

        image_label = QLabel(dialog)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel, dialog)
        button_box.accepted.connect(lambda: self.save_image(pixmap))
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        dialog.exec()

    def save_image(self, pixmap):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Table as Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)")
        if filename:
            pixmap.save(filename)
            print("Table saved as image:", filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimetableApp()
    window.show()
    sys.exit(app.exec_())
