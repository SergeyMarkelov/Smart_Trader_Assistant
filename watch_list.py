from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

class WatchListWidget(QWidget):
    def add_asset(self):
        # Получение данных из QLineEdit
        asset_name = self.line_edit.text()

        # Добавление элемента в ListWidget
        item = QListWidgetItem(asset_name)
        remove_button = QPushButton('Remove')
        remove_button.clicked.connect(lambda: self.remove_item(item))
        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, remove_button)

        # Очистка QLineEdit после добавления
        self.line_edit.clear()

    def remove_item(self, item):
        # Удаление элемента из ListWidget
        row = self.list_widget.row(item)
        self.list_widget.takeItem(row)