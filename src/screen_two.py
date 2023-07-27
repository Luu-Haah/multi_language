import sys

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QPushButton

from src.dialog_test import DialogTest


class ScreenTwo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        # create label
        self.mylabel = QLabel(self.tr("This is screen 2"))
        # center
        self.mylabel.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.tr("Hello 2"))

        self.btn_show_dialog = QPushButton(self.tr("Show Dialog"))
        self.btn_show_dialog.clicked.connect(self.showDialog)

        # create layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addWidget(self.mylabel)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.btn_show_dialog)
        self.setLayout(self.layout)

    def showDialog(self):
        self.dialog = DialogTest()
        self.dialog.show()

    def retranslateUi_sreentwo(self):
        print("HanhLT: translate Ui 2")
        self.mylabel.setText(QCoreApplication.translate("ScreenTwo", u"This is screen 2", None))
        self.label_2.setText(QCoreApplication.translate("ScreenTwo", u"Hello 2", None))
        self.btn_show_dialog.setText(QCoreApplication.translate("ScreenTwo", u"Show Dialog", None))

        self.update()

