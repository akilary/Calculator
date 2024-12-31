from re import sub, search, Match

PATTERN = r"(\d+\.?\d*)%(\d+\.?\d*)"


def calculate_expression(expression: str) -> str:
    """Вычисляет математическое выражение."""

    def evaluate_percentage(match: Match) -> str:
        num1, num2 = match.group(1), match.group(2)
        return str(float(num1) / 100 * float(num2))

    while search(PATTERN, expression):
        expression = sub(PATTERN, evaluate_percentage, expression)

    return eval(expression)
