import sys

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QTabWidget

from screen_one import ScreenOne
from src.screen_two import ScreenTwo
from src.tab_one import TabOne
from src.tab_two import TabTwo


class HomeScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        self.central_layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        self.screen_one = ScreenOne()
        # self.screen_one.click_signal.connect(self.change_language)
        self.screen_two = ScreenTwo()
        self.tab_one = TabOne()
        self.tab_two = TabTwo()

        # Add tabs to the tab widget
        self.tab_widget.addTab(self.screen_one, "Tab 1")
        self.tab_widget.addTab(self.screen_two, "Tab 2")
        self.tab_widget.addTab(self.tab_one, "Tab 3")
        self.tab_widget.addTab(self.tab_two, "Tab 4")
        # self.tab_widget.currentChanged.connect(self.retranslateUi)

        self.central_layout.addWidget(self.tab_widget)
        self.setLayout(self.central_layout)

