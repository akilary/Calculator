from PyQt6.QtCore import QObject, pyqtSignal

from .number_format import formatted_number, clean_text
from .math_expression import calculate_expression


class CalculatorController(QObject):
    res_ready: pyqtSignal = pyqtSignal(str, str)
    history_item_double_clicked: pyqtSignal = pyqtSignal(str, str)

    def __init__(self):
        """Инициализирует контроллер калькулятора с сигналами."""
        super().__init__()

    def evaluate_math_expression(self, expression) -> None:
        """Оценивает математическое выражение."""
        try:
            cleaned_expression = clean_text(expression, remove_spaces=True, replace_operators=True)
            raw_res = calculate_expression(cleaned_expression)
            formatted_res = formatted_number(str(int(raw_res)) if raw_res == int(raw_res) else str(raw_res))
            self.res_ready.emit(expression, formatted_res)
        except ZeroDivisionError:
            self.res_ready.emit(expression, "Ошибка: деление на ноль")
        except (SyntaxError, ValueError):
            self.res_ready.emit(expression, "Ошибка ввода")
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.res_ready.emit(expression, "Неизвестная ошибка")

    def handle_history_item_click(self, res: str) -> None:
        """Обрабатывает двойной щелчок по элементу истории."""
        if "―" in res: return
        cleaned_res = clean_text(res, remove_equals=True)
        self.history_item_double_clicked.emit("", cleaned_res)
