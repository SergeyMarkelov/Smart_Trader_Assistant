from PyQt5.QtWidgets import QWidget, QPushButton, QListWidgetItem, QVBoxLayout, QMessageBox
class WatchListWidget(QWidget):
    try:
        def add_asset(self, Asset_input_window_2):
            # Getting data from QLineEdit
            get_asset_name = Asset_input_window_2.text()
            print(get_asset_name)
            if not get_asset_name:
                QMessageBox.warning(None, "Warning", "The form must be filled out.")
                return
            else:
                item = QListWidgetItem(get_asset_name)
                print(item)
                remove_button = QPushButton('Remove')
                print(remove_button)
                remove_button.clicked.connect(lambda: WatchListWidget.remove_item(self, item))

                widget = QWidget()
                print(widget)
                layout = QVBoxLayout(widget)
                print((layout))
                layout.addWidget(remove_button)

                # Installing a widget for a list item
                item.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, widget)

                # Cleaning up QLineEdit after adding
                self.Asset_input_window_2.clear()


        def remove_item(self, item):
            # Removing an item from a ListWidget
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)


    except Exception as e:
        print(f"An error occurred: {e}")

