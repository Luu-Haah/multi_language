import os
import sys
from PySide6.QtCore import Qt, QLocale, QTranslator, QCoreApplication
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QLabel, QPushButton, QTabWidget

from screen_one import ScreenOne
from src.home_screen import HomeScreen
from src.screen_two import ScreenTwo
from src.tab_one import TabOne
from src.tab_two import TabTwo


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.current_locale = QLocale.system().name()
        self.load_ui()

    def load_ui(self):
        self.is_en = True
        self.central_widget = HomeScreen()
        self.central_widget.screen_one.click_signal.connect(self.change_language)
        self.setCentralWidget(self.central_widget)

    def change_language(self):
        qtranslator = QTranslator()
        if self.is_en:
            print("HanhLT: tieng viet")
            translator.load("/Users/hanhluu/Documents/Project/Qt/multi_language/language/main_en.qm")
            QCoreApplication.instance().installTranslator(qtranslator)
            self.retranslateUi()
            self.is_en = False
        else:
            print("HanhLT: tieng anh")
            translator.load("/Users/hanhluu/Documents/Project/Qt/multi_language/language/main_vi.qm")
            QCoreApplication.instance().installTranslator(qtranslator)
            self.retranslateUi()
            self.is_en = True

    def retranslateUi(self):
        print("HanhLT: retranslateUi")
        # Update the text of the label and button
        self.central_widget.screen_one.retranslateUi_screenone()
        self.central_widget.screen_two.retranslateUi_sreentwo()
        self.central_widget.tab_one.retranslateUi_tabone()
        self.central_widget.tab_two.retranslateUi_tabtwo()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and install the translator
    translator = QTranslator()
    translator.load("/Users/hanhluu/Documents/Project/Qt/multi_language/language/main_vi.qm")
    app.installTranslator(translator)

    window = MainWindow()

    window.show()
    sys.exit(app.exec())
