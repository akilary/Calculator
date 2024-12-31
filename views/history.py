from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QIcon, QKeySequence
from PyQt6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QPushButton, QLabel, QMessageBox, QGridLayout

from utils import read_json, write_json
from .stylesheets import HISTORY


class HistoryView(QWidget):
    FILE_PATH = "src/history.json"

    def __init__(self, controller):
        """Создает виджет истории вычислений и читает сохраненные данные."""
        super().__init__()
        self.setStyleSheet(HISTORY)

        self.controller = controller
        self.controller.res_ready.connect(self.add_entry)

        title = QLabel("История")
        self.remove_history: QPushButton = QPushButton()
        self.remove_history.setShortcut(QKeySequence("delete"))
        self.remove_history.setIcon(QIcon("src/img/trash.svg"))
        self.remove_history.setIconSize(QSize(24, 24))
        self.remove_history.clicked.connect(self.clear_history)
        self.history_list: QListWidget = QListWidget()
        self.history_list.itemDoubleClicked.connect(lambda item: self.controller.handle_history_item_click(item.text()))

        layout = QGridLayout()
        layout.addWidget(title, 0, 0)
        layout.addWidget(self.remove_history, 0, 1)
        layout.addWidget(self.history_list, 1, 0, 1, 2)
        layout.setColumnStretch(0, 90)
        layout.setColumnStretch(1, 1)
        self.setLayout(layout)

        self.history_data = read_json(self.FILE_PATH)
        self._populate_history_list()

    def add_entry(self, expression: str, res: str) -> None:
        """Добавляет новую запись в историю и сохраняет данные."""
        if res.startswith("Ошибка"): return
        self._add_to_list_widget(expression, res)
        self.history_data[expression] = res
        write_json(self.FILE_PATH, self.history_data)

    def clear_history(self) -> None:
        """Очищает список истории после подтверждения."""
        replay = QMessageBox.question(QWidget(),
                                      "Подтверждение удаления",
                                      "Вы уверены, что хотите очистить историю?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if replay == QMessageBox.StandardButton.Yes:
            self.history_data = {}
            self.history_list.clear()
            write_json(self.FILE_PATH, self.history_data)

    def _populate_history_list(self) -> None:
        """Заполняет виджет списка историей из сохраненных данных."""
        for e, r in self.history_data.items():
            self._add_to_list_widget(e, r)

    def _add_to_list_widget(self, expression: str, res: str) -> None:
        """Добавляет запись в виджет истории."""
        expression_item = QListWidgetItem(f"{expression} =")
        expression_item.setFont(QFont("Segoe UI", 13, QFont.Weight.Normal))

        res_item = QListWidgetItem(res)
        res_item.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))

        separator = QListWidgetItem(len(res) * "―")
        separator.setFont(QFont("Segoe UI", 10))

        self.history_list.insertItem(0, separator)
        self.history_list.insertItem(0, res_item)
        self.history_list.insertItem(0, expression_item)
