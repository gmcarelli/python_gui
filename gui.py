import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QStackedWidget, QGroupBox, QRadioButton
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("EssayGrader")
        self.setFixedSize(400, 450)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create the first screen (widget)
        self.screen1 = QWidget()
        self.setup_screen1()
        self.stacked_widget.addWidget(self.screen1)

        # Create the second screen (widget)
        self.screen2 = QWidget()
        self.setup_screen2()
        self.stacked_widget.addWidget(self.screen2)

    def setup_screen1(self) -> None:
        layout: QVBoxLayout = QVBoxLayout(self.screen1)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # App name label
        app_name_label = QLabel("EssayGrader")
        font = app_name_label.font()
        font.setPointSize(20)
        font.setBold(True)
        app_name_label.setFont(font)
        app_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(app_name_label)

        # Essay theme label
        theme_label = QLabel("tema da redação")
        layout.addWidget(theme_label)

        # Text input
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Digite o tema aqui...")
        self.text_input.setFixedHeight(150)
        self.text_input.textChanged.connect(self.limit_text)
        layout.addWidget(self.text_input)

        # Character count label
        self.char_count_label = QLabel("0/500")
        self.char_count_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.char_count_label)

        # Buttons
        button_layout = QHBoxLayout()
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.go_to_screen2)

        button_layout.addWidget(quit_button)
        button_layout.addStretch()
        button_layout.addWidget(next_button)
        layout.addLayout(button_layout)

    def limit_text(self) -> None:
        text: str = self.text_input.toPlainText()
        if len(text) > 500:
            self.text_input.setPlainText(text[:500])
            # Move cursor to the end
            cursor = self.text_input.textCursor()
            cursor.setPosition(500)
            self.text_input.setTextCursor(cursor)
        self.char_count_label.setText(f"{len(self.text_input.toPlainText())}/500")

    def setup_screen2(self) -> None:
        layout: QVBoxLayout = QVBoxLayout(self.screen2)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Radio button groups
        for i in range(5):
            group_box = QGroupBox(f"Critério {i+1}")
            group_layout = QVBoxLayout()

            options = ["Insuficiente", "Regular", "Bom", "Excelente"]
            for opt in options:
                radio_button = QRadioButton(opt)
                group_layout.addWidget(radio_button)

            # Set a default selection
            group_layout.itemAt(0).widget().setChecked(True)

            group_box.setLayout(group_layout)
            layout.addWidget(group_box)

        layout.addStretch()

        # Buttons
        button_layout = QHBoxLayout()
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.go_to_screen1)
        grade_now_button = QPushButton("Grade Now")
        # grade_now_button.clicked.connect(self.grade_now) # Placeholder
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)

        button_layout.addWidget(back_button)
        button_layout.addStretch()
        button_layout.addWidget(grade_now_button)
        button_layout.addWidget(quit_button)
        layout.addLayout(button_layout)

    def go_to_screen1(self) -> None:
        self.stacked_widget.setCurrentIndex(0)

    def go_to_screen2(self) -> None:
        self.stacked_widget.setCurrentIndex(1)