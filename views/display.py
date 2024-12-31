from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QLineEdit

from utils import formatted_number
from .stylesheets import DISPLAY


class Display(QWidget):
    OPERATORS = "+-×÷.%^"

    def __init__(self):
        """Создает виджет дисплея калькулятора с двумя полями для текста (верхнее и нижнее)."""
        super().__init__()
        self.setStyleSheet(DISPLAY)

        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.top_display = QLineEdit()
        self.top_display.setReadOnly(True)
        self.top_display.setObjectName('topDisplay')
        self.top_display.setSizePolicy(size_policy)
        self.top_display.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.bottom_display = QLineEdit()
        self.bottom_display.setPlaceholderText("0")
        self.bottom_display.setReadOnly(True)
        self.bottom_display.setObjectName('bottomDisplay')
        self.bottom_display.setSizePolicy(size_policy)
        self.bottom_display.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.top_display)
        layout.addWidget(self.bottom_display)
        self.setLayout(layout)

        self.last_result = None

    def set_top_text(self, text: str) -> None:
        """Устанавливает текст верхнего дисплея."""
        self.top_display.setText(text)

    def set_bottom_text(self, text: str) -> None:
        """Устанавливает текст нижнего дисплея."""
        self.bottom_display.setText(text)

    def get_text(self) -> str:
        """Возвращает текущий текст нижнего дисплея."""
        return self.bottom_display.text()

    def append_text(self, text: str) -> None:
        """Добавляет текст к текущему выражению, обновляя верхний дисплей."""
        self._update_top_display(text)
        current_text = self.bottom_display.text()

        if self._is_last_char_operator(text):
            self.bottom_display.setText(current_text[:-1] + text)
        else:
            self.bottom_display.setText(formatted_number(current_text + text))

    def clear_displays(self) -> None:
        """Очищает оба дисплея и сбрасывает сохраненный результат."""
        self.top_display.clear()
        self.bottom_display.clear()
        self.last_result = ""

    def backspace(self) -> None:
        """Удаляет последний символ из текста нижнего дисплея."""
        self._update_top_display()
        current_text = self.bottom_display.text()
        self.bottom_display.setText(formatted_number(current_text[:-1]))

    def _update_top_display(self, text: str="") -> None:
        """Обновляет верхний дисплей на основе результата."""
        if not self.last_result: return

        if self.last_result.startswith("Ошибка"):
            self.top_display.clear()
            self.bottom_display.clear()
            self.last_result = ""
            return

        self.top_display.setText(f"→ {self.last_result}")
        if text not in self.OPERATORS:
            self.bottom_display.clear()
        self.last_result = ""

    def _is_last_char_operator(self, text: str) -> bool:
        """Проверяет, является ли последний символ в тексте оператором."""
        return self.bottom_display.text()[-1:] in self.OPERATORS and text in self.OPERATORS
