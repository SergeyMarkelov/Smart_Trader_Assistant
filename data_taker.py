import yfinance as yf
from interface import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class FindAsset:
    def add_asset(self, Asset_input_window):
        # Getting data from QLineEdit
        get_asset_name = Asset_input_window.text()

        if not get_asset_name:
            QMessageBox.warning(None, "Warning", "The form must be filled out.")
            return None  # Return None to indicate no valid asset data
        else:
            ticker = yf.Ticker(get_asset_name)
            df = ticker.history(period='100y')

            if "Empty DataFrame" in df.to_string():
                QMessageBox.warning(None, "Warning",
                                    f"Invalid asset name: {get_asset_name}. No data found, symbol may be delisted.")
                return None  # Return None to indicate no valid asset data

            else:
                return df
