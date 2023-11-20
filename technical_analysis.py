import yfinance as yf
import talib
from PyQt5.QtWidgets import QLabel
import pandas as pd

# Создание объекта для пары USD/JPY
usd_jpy = yf.Ticker('SI=F')

# Загрузка исторических данных

df = usd_jpy.history(period='100y')  # Загружаем данные за последние 100 лет


# Периоды для ATR
# periods = [6, 24, 72, 288, 576, 1440, 2880]


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


class Indicators:
    import talib

    import talib

    def calculate_and_display_macd(df, label):
        close_prices = df['Close']

        macd_line, signal_line, histogram = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)

        # Сигнал Short, когда MACD меньше 0
        # Сигнал Long, когда MACD больше 0
        if macd_line.iloc[-1] > 0:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif macd_line.iloc[-1] < 0:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "None"
            label.setText(f"MACD Signal: {signal}")
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_supertrend(df, label, period=7, multiplier=3.0):

        # Рассчитываем ATR (Average True Range) с использованием библиотеки talib
        atr = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=period)

        # Рассчитываем базовую линию Supertrend
        basic_upper = (df['High'] + df['Low']) / 2 + multiplier * atr
        basic_lower = (df['High'] + df['Low']) / 2 - multiplier * atr

        # Инициализация Supertrend в зависимости от направления тренда
        is_up_trend = True
        supertrend_line = pd.Series(index=df.index)
        signal = "None"

        for i in range(period, len(df)):
            if is_up_trend:
                supertrend_line.iloc[i] = basic_upper.iloc[i]
                if df['Close'].iloc[i] < basic_upper.iloc[i]:
                    is_up_trend = False
                    signal = "Sell"
                    label.setStyleSheet("color: red; font-size: 10pt;")
                    label.setText(signal)
            else:
                supertrend_line.iloc[i] = basic_lower.iloc[i]
                if df['Close'].iloc[i] > basic_lower.iloc[i]:
                    is_up_trend = True
                    signal = "Buy"
                    label.setStyleSheet("color: green; font-size: 10pt;")
                    label.setText(signal)

        return signal

    def calculate_and_display_rsi(df, label, period=14, overbought=70, oversold=30):

        # Рассчитываем RSI (Relative Strength Index) с использованием библиотеки talib
        rsi = talib.RSI(df['Close'], timeperiod=period)

        # Вычисляем сигнал на основе уровней "перекупленности" и "перепроданности"
        if rsi.iloc[-1] > overbought:
            signal = "Overbought"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        elif rsi.iloc[-1] < oversold:
            signal = "Oversold"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        else:
            signal = "Neutral"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_parabolic_sar(df, label, acceleration=0.02, maximum=0.2):

        # Рассчитываем Parabolic SAR с использованием библиотеки talib
        parabolic_sar = talib.SAR(df['High'], df['Low'], acceleration=acceleration, maximum=maximum)

        if df['Close'].iloc[-1] > parabolic_sar.iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['Close'].iloc[-1] < parabolic_sar.iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    import talib
    import pandas as pd

    def calculate_and_display_obv(df, label):
        # Рассчитываем On-Balance Volume (OBV)
        obv = talib.OBV(df['Close'], df['Volume'])

        signal = None
        if obv.iloc[-1] > obv.iloc[-2]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif obv.iloc[-1] < obv.iloc[-2]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal


    def calculate_and_display_stoch(df, label, k_period=14, d_period=3, slowing=3):
        # Рассчитываем Stochastic Oscillator (Stoch)
        slowk, slowd = talib.STOCH(df['High'], df['Low'], df['Close'], fastk_period=k_period, slowk_period=d_period,
                                   slowd_period=slowing)

        signal = None
        if slowk.iloc[-1] >= 50 and slowd.iloc[-1] >= 50:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif slowk.iloc[-1] < 50 and slowk.iloc[-1] <= 50:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        elif slowk.iloc[-1] >= 80 and slowk.iloc[-1] >= 80:
            signal = "Overbought"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        elif slowk.iloc[-1] < 30 and slowk.iloc[-1] <= 30:
            signal = "Oversold"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_enhanced_volume(df, label):

        average_volume = df['Volume'].mean()

        # Проверяем условие для Long
        if df['Volume'].iloc[-1] > average_volume:
            signal = "Above average"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        # Проверяем условие для Short
        elif df['Volume'].iloc[-1] < average_volume:
            signal = "Below average"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_vwap(df, label):
        # Рассчитываем Volume-Weighted Average Price (VWAP)
        df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()

        # Рекомендация на основе VWAP
        signal = None
        if df['Close'].iloc[-1] > df['VWAP'].iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['Close'].iloc[-1] < df['VWAP'].iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_vap(df, label):
        # Предполагаем, что в вашем DataFrame есть столбцы 'Price' и 'Volume'
        # Рассчитываем общий объем для каждого уровня цены
        df['TotalVolumeAtPrice'] = df.groupby('Close')['Volume'].transform('sum')

        # Рекомендация на основе VAP
        signal = None
        if df['Volume'].iloc[-1] > df['TotalVolumeAtPrice'].iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['Volume'].iloc[-1] < df['TotalVolumeAtPrice'].iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_vpt(df, label):
        # Рассчитываем процентное изменение цены
        df['Price Change'] = df['Close'].pct_change()

        # Рассчитываем объем денег, перемещаемый с изменением цены
        df['Money Flow'] = df['Volume'] * df['Price Change']

        # Рассчитываем кумулятивную сумму объемов денег, чтобы получить индикатор Volume Price Trend (VPT)
        df['VPT'] = df['Money Flow'].cumsum()

        # Решаем, купить или продать
        signal = None
        if df['VPT'].iloc[-1] > df['VPT'].iloc[-2]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['VPT'].iloc[-1] < df['VPT'].iloc[-2]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_cmf(df, label, period=20):
        # Рассчитываем Multiplier
        multiplier = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'])
        # Ограничиваем значения от 0 до 1
        multiplier = multiplier.clip(lower=0, upper=1)

        # Рассчитываем Money Flow Volume
        money_flow_volume = multiplier * df['Volume']

        # Рассчитываем 20-периодное среднее Chaikin Money Flow
        cmf = money_flow_volume.rolling(window=period).sum() / df['Volume'].rolling(window=period).sum()

        # Решаем, купить или продать
        signal = None
        if cmf.iloc[-1] > 0:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif cmf.iloc[-1] < 0:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        # Возвращаем значения, если они нужны
        return signal

    import pandas as pd

    def calculate_and_display_emv(df, label, period=14):
        # Рассчитываем Midpoint Move (MM)
        df['MM'] = ((df['High'] + df['Low']) / 2 - (df['High'].shift(1) + df['Low'].shift(1)) / 2) / 2

        # Рассчитываем Box Ratio (BR)
        df['BR'] = df['Volume'] / (df['High'] - df['Low'])

        # Рассчитываем Ease of Movement (EMV)
        df['EMV'] = df['MM'] / df['BR']

        # Рассчитываем 14-периодное среднее EMV
        df['EMV_SMA'] = df['EMV'].rolling(window=period).mean()

        signal = None
        if df['EMV'].iloc[-1] > df['EMV_SMA'].iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['EMV'].iloc[-1] < df['EMV_SMA'].iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")


        return signal

    def calculate_and_display_ma_6(df, label):
        ma_6 = talib.SMA(df['Close'], timeperiod=6)

        signal = None
        if df['Close'].iloc[-1] > ma_6.iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['Close'].iloc[-1] < ma_6.iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "No Trend"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_ma_24(df, label):
        ma_24 = talib.SMA(df['Close'], timeperiod=24)

        signal = None
        if df['Close'].iloc[-1] > ma_24.iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['Close'].iloc[-1] < ma_24.iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "No Trend"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_ma_72(df, label):
        ma_72 = talib.SMA(df['Close'], timeperiod=72)

        signal = None
        if df['Close'].iloc[-1] > ma_72.iloc[-1]:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-size: 10pt;")
        elif df['Close'].iloc[-1] < ma_72.iloc[-1]:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: red; font-size: 10pt;")
        else:
            signal = "No Trend"
            label.setText(signal)
            label.setStyleSheet("color: black; font-size: 10pt;")

        return signal

    def calculate_and_display_all_signals(label):
        buy_count = 0
        sell_count = 0

        signal_funcs = [Indicators.calculate_and_display_macd, Indicators.calculate_and_display_supertrend,
                                                     Indicators.calculate_and_display_rsi, Indicators.calculate_and_display_parabolic_sar,
                                                     Indicators.calculate_and_display_obv,
                                                     Indicators.calculate_and_display_stoch,
                                                     Indicators.calculate_and_display_enhanced_volume,
                                                     Indicators.calculate_and_display_vwap,
                                                     Indicators.calculate_and_display_vap,
                                                     Indicators.calculate_and_display_vpt,
                                                     Indicators.calculate_and_display_cmf,
                                                     Indicators.calculate_and_display_emv,
                                                     Indicators.calculate_and_display_ma_6,
                                                     Indicators.calculate_and_display_ma_24,
                                                     Indicators.calculate_and_display_ma_72]


        # Проходимся по всем функциям и считаем сигналы
        for signal_func in signal_funcs:
            signal = signal_func(df, label)
            if signal == "Buy":
                buy_count += 1
                #print ("Buy")
            elif signal == "Sell":
                sell_count += 1
                #print("Sell")
            elif signal == "Oversold":
                buy_count += 1
                #print("Oversold")
            elif signal == "Overbought":
                sell_count += 1
                #print("Overbought")
            elif signal == "Below average":
                buy_count += 1
                #print("Below average")
            elif signal == "Above average":
                sell_count += 1
                #print("Above average")

        buy_signal = buy_count > sell_count
        sell_signal = sell_count > buy_count

        # Принимаем решение на основе комбинированных сигналов
        if buy_signal:
            signal = "Buy"
            label.setText(signal)
            label.setStyleSheet("color: green; font-family: MS Shell Dlg 2; font-size: 14pt;")

        elif sell_signal:
            signal = "Sell"
            label.setText(signal)
            label.setStyleSheet("color: green; font-family: MS Shell Dlg 2; font-size: 14pt;")
        else:
            signal = "Hold"
            label.setText(signal)
            label.setStyleSheet("color: green; font-family: MS Shell Dlg 2; font-size: 14pt;")

        return buy_signal, sell_signal, signal

    def calculate_and_display_growth_days(df, label):
        df['Price Change'] = df['Close'].pct_change()
        df['Direction'] = df['Price Change'].apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'No Change')
        count_days = df.groupby('Direction').size().to_dict()

        growth_days = count_days.get('Up', 0)
        decline_days = count_days.get('Down', 0)

        total_days = growth_days + decline_days
        growth_percentage = (growth_days / total_days) * 100 if total_days > 0 else 0

        label.setText(f"Days of Growth: {growth_days} ({growth_percentage:.2f}%)")

    def calculate_and_display_decline_days(df, label):

        df['Price Change'] = df['Close'].pct_change()
        df['Direction'] = df['Price Change'].apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'No Change')
        count_days = df.groupby('Direction').size().to_dict()

        growth_days = count_days.get('Up', 0)
        decline_days = count_days.get('Down', 0)

        total_days = growth_days + decline_days
        decline_percentage = (decline_days / total_days) * 100 if total_days > 0 else 0

        label.setText(f"Days of Decline: {decline_days} ({decline_percentage:.2f}%)")



















