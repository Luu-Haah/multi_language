import sys

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QHBoxLayout, QDialog

class DialogTest(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        # create label
        self.mylabel = QLabel(self.tr("My Dialog"))
        # center
        self.mylabel.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.tr("Hello world in Dialog"))

        # create layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addWidget(self.mylabel)
        self.layout.addWidget(self.label_2)
        self.setLayout(self.layout)



