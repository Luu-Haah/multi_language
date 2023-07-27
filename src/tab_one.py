import sys

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QHBoxLayout

class TabOne(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        # create label
        self.mylabel_one = QLabel()
        self.mylabel_one.setText(self.tr("Tab One"))
        # center
        self.mylabel_one.setAlignment(Qt.AlignCenter)

        self.label_one = QLabel()
        self.label_one.setText(self.tr("Hello world one"))
        # create layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addWidget(self.mylabel_one)
        self.layout.addWidget(self.label_one)
        self.setLayout(self.layout)

    def retranslateUi_tabone(self):
        print("HanhLT: translate ui tab 1")
        self.mylabel_one.setText(QCoreApplication.translate("TabOne", u"Tab One", None))
        self.label_one.setText(QCoreApplication.translate("TabOne", u"Hello world one", None))

