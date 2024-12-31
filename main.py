import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from utils import CalculatorController
from views import CalculatorView, HistoryView
from views.stylesheets import MAIN_WINDOW


class MainWindow(QMainWindow):
    def __init__(self):
        """Инициализирует главное окно приложения, размещает виджеты калькулятора и истории."""
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setMinimumSize(700, 500)
        self.setWindowIcon(QIcon("src/img/logo.ico"))
        self.setStyleSheet(MAIN_WINDOW)

        self.controller = CalculatorController()
        self.calc_view = CalculatorView(self.controller)
        self.history_view = HistoryView(self.controller)

        layout = QHBoxLayout()
        layout.addWidget(self.calc_view)
        layout.setStretch(0, 3)

        layout.addWidget(self.history_view)
        layout.setStretch(1, 2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
