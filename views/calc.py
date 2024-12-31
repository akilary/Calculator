from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from .display import Display
from .stylesheets import CALC


class CalculatorView(QWidget):
    def __init__(self, controller):
        """Создает виджет калькулятора с дисплеем и кнопками."""
        super().__init__()
        self.setStyleSheet(CALC)

        self.display = Display()
        self.controller = controller

        self.controller.res_ready.connect(self.update_display)
        self.controller.history_item_double_clicked.connect(self.update_display)

        self.layout = QGridLayout()
        self.layout.addWidget(self.display, 0, 0, 1, 4)
        self._initialize_buttons()
        self.setLayout(self.layout)

    def _initialize_buttons(self) -> None:
        """Создает кнопки калькулятора и добавляет их в макет."""
        buttons = [
            {"text": "1", "row": 4, "col": 0},
            {"text": "2", "row": 4, "col": 1},
            {"text": "3", "row": 4, "col": 2},
            {"text": "4", "row": 3, "col": 0},
            {"text": "5", "row": 3, "col": 1},
            {"text": "6", "row": 3, "col": 2},
            {"text": "7", "row": 2, "col": 0},
            {"text": "8", "row": 2, "col": 1},
            {"text": "9", "row": 2, "col": 2},
            {"text": "0", "row": 5, "col": 1},
            {"text": ".", "row": 5, "col": 0},

            {"text": "(", "row": 1, "col": 0, "object_name": "openParen"},
            {"text": ")", "row": 1, "col": 1, "object_name": "closeParen"},
            {"text": "^", "row": 2, "col": 3, "object_name": "power"},
            {"text": "%", "row": 1, "col": 2, "object_name": "percent"},

            {"text": "÷", "row": 5, "col": 2, "object_name": "div", "shortcut": "/"},
            {"text": "×", "row": 5, "col": 3, "object_name": "mult", "shortcut": "*"},
            {"text": "-", "row": 4, "col": 3, "object_name": "minus"},
            {"text": "+", "row": 3, "col": 3, "object_name": "plus"},

            {"text": "⌫", "row": 1, "col": 3, "object_name": "backspace", "shortcut": "backspace"},
            {"text": "Очистить", "row": 6, "col": 0, "row_span": 1, "col_span": 2, "object_name": "cleerAll", "shortcut": "c"},
            {"text": "=", "row": 6, "col": 2, "row_span": 1, "col_span": 2, "object_name": "equal", "shortcut": "enter"},
        ]
        size_policy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        for button in buttons:
            self._add_button(button, size_policy)

    def _add_button(self, button: dict, size_policy: QSizePolicy) -> None:
        """Добавляет кнопку с заданными параметрами."""
        row_span = button.get("row_span", 1)
        col_span = button.get("col_span", 1)
        object_name = button.get("object_name", "")
        shortcut = button.get("shortcut", button["text"])

        btn: QPushButton = QPushButton(button["text"])
        self._configure_button_actions(button["text"], btn)
        btn.setSizePolicy(size_policy)
        btn.setObjectName(object_name)
        btn.setShortcut(QKeySequence(shortcut))

        self.layout.addWidget(btn, button["row"], button["col"], row_span, col_span)

    def _configure_button_actions(self, button_text: str, btn: QPushButton) -> None:
        """Определяет действия для кнопок."""
        match button_text:
            case "⌫":
                btn.clicked.connect(self.display.backspace)
            case "Очистить":
                btn.clicked.connect(self.display.clear_displays)
            case "=":
                btn.clicked.connect(lambda: self.controller.evaluate_math_expression(self.display.get_text()))
            case _:
                btn.clicked.connect(lambda checked, char=button_text: self.display.append_text(char))

    def update_display(self, expression: str, res: str) -> None:
        """Обновляет текст на дисплее на основе текущего выражения и результата."""
        self.display.set_top_text(expression)
        self.display.set_bottom_text(res)
        self.display.last_result = res
