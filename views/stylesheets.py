MAIN_WINDOW = """
QWidget {
    background-color: #202020;
    color: #dcdcdc;
    font-family: "Segoe UI", sans-serif;
    font-size: 18px;
}
"""

CALC = """
QPushButton {
    background-color: #2e2e2e;
    color: #c0c0c0;
    border: 1px solid #454545;
    border-radius: 6px;
    padding: 10px;
}

QPushButton:hover {
    background-color: #3b3b3b;
    color: #ffffff;
}

QPushButton:pressed {
    background-color: #454545;
    color: #dcdcdc;
}

QPushButton#equal {
    background-color: #3a3a3a;
    color: #ffffff;
    font-weight: bold;
    font-size: 20px;
}

QPushButton#equal:hover {
    background-color: #4a4a4a;
}

QPushButton#equal:pressed {
    background-color: #2a2a2a;
}

QPushButton#div, QPushButton#mult, QPushButton#minus, QPushButton#plus, QPushButton#openParen, QPushButton#closeParen, 
QPushButton#power,  QPushButton#percent{
    background-color: #3a3a3a;
    color: #f0f0f0;
    font-weight: bold;
}

QPushButton#div:hover, QPushButton#mult:hover, QPushButton#minus:hover, QPushButton#plus:hover, QPushButton#openParen:hover,
QPushButton#closeParen:hover, QPushButton#power:hover, QPushButton#percent:hover{
    background-color: #4a4a4a;
}

QPushButton#div:pressed, QPushButton#mult:pressed, QPushButton#minus:pressed, QPushButton#plus:pressed,
QPushButton#openParen:pressed, QPushButton#closeParen:pressed, QPushButton#power:pressed, QPushButton#percent:pressed{
    background-color: #2a2a2a;
}

QPushButton#cleerAll, QPushButton#backspace {
    background-color: #262626;
    color: #c0c0c0;
    font-size: 18px;
    font-weight: bold;
}

QPushButton#cleerAll:hover, QPushButton#backspace:hover {
    background-color: #4a4a4a;
    color: #ffffff;
}

QPushButton#cleerAll:pressed, QPushButton#backspace:pressed {
    background-color: #2a2a2a;
}
"""

DISPLAY = """
QLineEdit {
    background-color: #181818;
    border-radius: 6px;
    color: #f5f5f5;
    font-size: 22px;
    padding: 6px;
    qproperty-alignment: 'AlignRight | AlignVCenter';
}

QLineEdit#topDisplay {
    color: #c0c0c0;
    font-weight: normal;
}

QLineEdit#bottomDisplay {
    font-weight: bold;
    color: #ffffff;
}
"""

HISTORY = """
QListWidget {
    background-color: #262626;
    color: #dcdcdc;
    border: 1px solid #3c3c3c;
    border-radius: 6px;
    outline: 0px solid #fff;
}

QListWidget QScrollBar:vertical {
    background-color: #262626;
    width: 15px;
}

QListWidget QScrollBar::handle:vertical {
    background-color: #555555; 
    border-radius: 6px;
    min-height: 20px;
}

QListWidget QScrollBar::handle:vertical:hover {
    background-color: #777777;
}

QListWidget QScrollBar::add-line:vertical, QListWidget QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
}

QListWidget QScrollBar::add-page:vertical, QListWidget QScrollBar::sub-page:vertical {
    background: none;
}

QListWidget QScrollBar:horizontal {
    background-color: #262626;
    height: 15px;
}

QListWidget QScrollBar::handle:horizontal {
    background-color: #555555; 
    border-radius: 6px;
    min-width: 20px;
}

QListWidget QScrollBar::handle:horizontal:hover {
    background-color: #777777; 
}

QListWidget QScrollBar::add-line:horizontal, QListWidget QScrollBar::sub-line:horizontal {
    background: none;
    width: 0px;
}

QListWidget QScrollBar::add-page:horizontal, QListWidget QScrollBar::sub-page:horizontal {
    background: none;
}

QListWidget::item {
    padding: 0px;
    border: none;
}

QListWidget::item:selected {
    background-color: #3a3a3a;
    color: #ffffff;
}

QPushButton {
    background-color: transparent;
    border: 0px solid #454545;
    border-radius: 6px;
}

QPushButton:hover {
    background-color: #4a4a4a;
    color: #ffffff;
}

QPushButton:pressed {
    background-color: #2a2a2a;
}
"""
