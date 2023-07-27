import sys

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QCoreApplication, Signal
from PySide6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QHBoxLayout, QPushButton


class ScreenOne(QWidget):
    click_signal = Signal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        # create label
        self.mylabel = QLabel(self.tr("This is screen 1"))
        # center
        self.mylabel.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.tr("Hello 1"))

        # center
        self.mylabel.setAlignment(Qt.AlignCenter)

        self.label_1 = QLabel(self.tr("This is a QLabel 1"))
        self.button_1 = QPushButton(self.tr("Press me 1"))

        self.button_2 = QPushButton(self.tr("Press me 2"))
        self.button_3 = QPushButton(self.tr("Press me 3"))
        self.button_change_language = QPushButton(self.tr("Change Language"))
        self.button_change_language.clicked.connect(self.change_language)

        # create layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.mylabel)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.button_1)
        self.layout.addWidget(self.button_2)
        self.layout.addWidget(self.button_3)
        self.layout.addWidget(self.button_change_language)

        self.setLayout(self.layout)

    def change_language(self):
        self.click_signal.emit(True)

    def retranslateUi_screenone(self):

        self.mylabel.setText(QCoreApplication.translate("ScreenOne", u"This is screen 1", None))
        self.label_2.setText(QCoreApplication.translate("ScreenOne", u"Hello 1", None))
        self.label_1.setText(QCoreApplication.translate("ScreenOne", u"This is a QLabel 1", None))
        self.button_1.setText(QCoreApplication.translate("ScreenOne", "Press me 1", None))
        self.button_2.setText(QCoreApplication.translate("ScreenOne", "Press me 2", None))
        self.button_3.setText(QCoreApplication.translate("ScreenOne", "Press me 3", None))
        self.button_change_language.setText(QCoreApplication.translate("", "Change Language", None))

