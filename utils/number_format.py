import re


def formatted_number(text: str) -> str:
    """Форматирует числа, добавляя пробелы между разрядами."""
    text = text.replace(" ", "")
    numbers = re.findall(r"\d+\.\d+|\d+", text)
    for number in numbers:
        if "." in number:
            int_part, frac_part = number.split(".")
            formated_number = f"{int(int_part):,}".replace(",", " ") + "." + frac_part
        else:
            formated_number = f"{int(number):,}".replace(",", " ")
        text = text.replace(number, formated_number)
    return text


def clean_text(
        text: str,
        remove_spaces: bool = False,
        replace_operators: bool = False,
        remove_equals: bool = False,
    ) -> str:
    """Очищает текст математического выражения."""
    if remove_spaces:
        text = text.replace(" ", "")
    if replace_operators:
        text = text.replace("×", "*").replace("÷", "/").replace("^", "**")
    if remove_equals:
        text = text.replace(" =", "")
    return text
