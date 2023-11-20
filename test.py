from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

class WatchListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Watch List')

        # Создание виджетов
        self.label_list = QVBoxLayout()
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.show_input_form)

        # Создание основного макета
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(self.label_list)
        #main_layout.addWidget(self.add_button)

        # Создание формы ввода
        self.input_label = QLabel('Asset:')
        self.input_line_edit = QLineEdit()
        self.add_input_button = QPushButton('Add')
        self.add_input_button.clicked.connect(self.add_asset)
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input_label)
        self.input_layout.addWidget(self.input_line_edit)
        self.input_layout.addWidget(self.add_input_button)
        self.input_layout.setContentsMargins(0, 0, 0, 0)
        self.input_layout.setSpacing(0)

        # Показать форму ввода
        self.show_input_form()

    def show_input_form(self):
        # Очистка предыдущих данных в форме ввода
        self.input_line_edit.clear()

        # Показать форму ввода
        self.label_list.addLayout(self.input_layout)

    def add_asset(self):
        # Получение данных из формы ввода
        asset_name = self.input_line_edit.text()

        # Создание нового QLabel и QPushButton
        label = QLabel(f'Asset: {asset_name}')
        remove_button = QPushButton('Remove')
        remove_button.clicked.connect(lambda: self.remove_label(label, remove_button))

        # Создание горизонтального макета для QLabel и QPushButton
        label_layout = QHBoxLayout()
        label_layout.addWidget(label)
        label_layout.addWidget(remove_button)

        # Добавление в список горизонтальный макет
        self.label_list.addLayout(label_layout)

    def remove_label(self, label, remove_button):
        # Удаление QLabel и QPushButton
        label.deleteLater()
        remove_button.deleteLater()

if __name__ == '__main__':
    app = QApplication([])
    watch_list_widget = WatchListWidget()
    watch_list_widget.show()
    app.exec_()
