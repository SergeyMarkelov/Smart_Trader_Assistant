import yfinance as yf
import talib
from PyQt5.QtWidgets import QLabel

tempObj = yf.Ticker('^IXIC')

df = tempObj.history(period='100y')  # Загружаем данные за последние 100 лет

class ATRCalculator:
    def __init__(self, df, label):
        self.df = df
        self.label = label

    def calculate_atr(self, period):
        atr = talib.ATR(self.df['High'], self.df['Low'], self.df['Close'], timeperiod=period)
        self.df['ATR'] = atr
        self.print_atr_info(period)

    def print_atr_info(self, period):
        atr_value = self.df['ATR'].iloc[-1]
        price = self.df['Close'].iloc[-1]
        previous_close = self.df['Close'].iloc[-2]  # Закрытие предыдущего дня

        #price_change = price - previous_close  # Абсолютное изменение цены
        normalized_atr = (atr_value / price) * 100  # Нормализация ATR к изменению цены
        formatted_atr = round(normalized_atr, 4)
        print(f"{formatted_atr} %")


# Создаем QLabel
x = QLabel

# Создаем объект ATRCalculator и вызываем calculate_atr
ATRCalculator(df, x).calculate_atr(6)
""""

class ATRCalculator:
    def __init__(self, df, label):
        self.df = df
        self.label = label

    def calculate_atr(self, period):
        atr = talib.ATR(self.df['High'], self.df['Low'], self.df['Close'], timeperiod=period)
        self.df['ATR'] = atr
        self.print_atr_info(period)

    def print_atr_info(self, period):
        atr_value = self.df['ATR'].iloc[-1]
        formatted_atr = round(atr_value, 5)  # 2 знака после запятой
        self.label.setText(f"{formatted_atr} %")
