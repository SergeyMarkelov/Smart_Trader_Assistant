import talib
import pandas as pd


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

        normalized_atr = (atr_value / price) * 100  # Normalize ATR to price changes
        formatted_atr = round(normalized_atr, 4)
        print(f"{formatted_atr} %")
        self.label.setText(f"{formatted_atr} %")

class Indicators:

    def calculate_and_display_macd(df, label):
        close_prices = df['Close']

        macd_line, signal_line, histogram = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)

        # Short signal when MACD is less than 0
        # Long signal when MACD is greater than 0
        if macd_line.iloc[-1] > 0:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif macd_line.iloc[-1] < 0:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(f"MACD Signal: {signal}")
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_supertrend(df, label, period=7, multiplier=3.0):

        # Calculate ATR (Average True Range) using the talib library
        atr = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=period)

        # Calculate the Supertrend baseline
        basic_upper = (df['High'] + df['Low']) / 2 + multiplier * atr
        basic_lower = (df['High'] + df['Low']) / 2 - multiplier * atr

        # Initialize Supertrend depending on trend direction
        is_up_trend = True
        supertrend_line = pd.Series(index=df.index)
        signal = "None"

        for i in range(period, len(df)):
            if is_up_trend:
                supertrend_line.iloc[i] = basic_upper.iloc[i]
                if df['Close'].iloc[i] < basic_upper.iloc[i]:
                    is_up_trend = False
                    signal = " Sell"
                    label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
                    label.setText(signal)
            else:
                supertrend_line.iloc[i] = basic_lower.iloc[i]
                if df['Close'].iloc[i] > basic_lower.iloc[i]:
                    is_up_trend = True
                    signal = " Buy"
                    label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
                    label.setText(signal)

        return signal

    def calculate_and_display_rsi(df, label, period=14, overbought=70, oversold=30):

        # Calculate RSI (Relative Strength Index) using the talib library
        rsi = talib.RSI(df['Close'], timeperiod=period)

        # Calculate the signal based on the “overbought” and “oversold” levels
        if rsi.iloc[-1] > overbought:
            signal = " Overbought"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif rsi.iloc[-1] < oversold:
            signal = " Oversold"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_parabolic_sar(df, label, acceleration=0.02, maximum=0.2):

        # Calculate Parabolic SAR using the talib library
        parabolic_sar = talib.SAR(df['High'], df['Low'], acceleration=acceleration, maximum=maximum)

        if df['Close'].iloc[-1] > parabolic_sar.iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['Close'].iloc[-1] < parabolic_sar.iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_obv(df, label):

        # Calculate On-Balance Volume (OBV)
        obv = talib.OBV(df['Close'], df['Volume'])

        signal = None
        if obv.iloc[-1] > obv.iloc[-2]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif obv.iloc[-1] < obv.iloc[-2]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal


    def calculate_and_display_stoch(df, label, k_period=14, d_period=3, slowing=3):

        # Calculate Stochastic Oscillator (Stoch)
        slowk, slowd = talib.STOCH(df['High'], df['Low'], df['Close'], fastk_period=k_period, slowk_period=d_period,
                                   slowd_period=slowing)

        signal = None
        if slowk.iloc[-1] >= 50 and slowd.iloc[-1] >= 50:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif slowk.iloc[-1] < 50 and slowk.iloc[-1] <= 50:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif slowk.iloc[-1] >= 80 and slowk.iloc[-1] >= 80:
            signal = " Overbought"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif slowk.iloc[-1] < 30 and slowk.iloc[-1] <= 30:
            signal = " Oversold"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_enhanced_volume(df, label):

        average_volume = df['Volume'].mean()

        # Checking the condition for Long
        if df['Volume'].iloc[-1] > average_volume:
            signal = " Above average"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        # Checking the condition for Short
        elif df['Volume'].iloc[-1] < average_volume:
            signal = " Below average"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_vwap(df, label):
        # Calculating Volume-Weighted Average Price (VWAP)
        df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()

        #VWAP based recommendation
        signal = None
        if df['Close'].iloc[-1] > df['VWAP'].iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['Close'].iloc[-1] < df['VWAP'].iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_vap(df, label):

        # Calculate the total volume for each price level
        df['TotalVolumeAtPrice'] = df.groupby('Close')['Volume'].transform('sum')

        # VAP based recommendation
        signal = None
        if df['Volume'].iloc[-1] > df['TotalVolumeAtPrice'].iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['Volume'].iloc[-1] < df['TotalVolumeAtPrice'].iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_vpt(df, label):
        # Calculate the percentage change in price
        df['Price Change'] = df['Close'].pct_change()

        # Calculate the amount of money moved with price changes
        df['Money Flow'] = df['Volume'] * df['Price Change']

        # Calculate the cumulative sum of money volumes to get the Volume Price Trend (VPT) indicator
        df['VPT'] = df['Money Flow'].cumsum()

        # buy or sell
        signal = None
        if df['VPT'].iloc[-1] > df['VPT'].iloc[-2]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['VPT'].iloc[-1] < df['VPT'].iloc[-2]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_cmf(df, label, period=20):
        # Calculate Multiplier
        multiplier = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'])
        # Limit values from 0 to 1
        multiplier = multiplier.clip(lower=0, upper=1)

        # Calculating Money Flow Volume
        money_flow_volume = multiplier * df['Volume']

        # Calculating the 20-period average of Chaikin Money Flow
        cmf = money_flow_volume.rolling(window=period).sum() / df['Volume'].rolling(window=period).sum()

        # buy or sell
        signal = None
        if cmf.iloc[-1] > 0:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif cmf.iloc[-1] < 0:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_emv(df, label, period=14):
        # Calculating Midpoint Move (MM)
        df['MM'] = ((df['High'] + df['Low']) / 2 - (df['High'].shift(1) + df['Low'].shift(1)) / 2) / 2

        # Calculating Box Ratio (BR)
        df['BR'] = df['Volume'] / (df['High'] - df['Low'])

        # Calculating Ease of Movement (EMV)
        df['EMV'] = df['MM'] / df['BR']

        # Calculate 14-period average EMV
        df['EMV_SMA'] = df['EMV'].rolling(window=period).mean()

        signal = None
        if df['EMV'].iloc[-1] > df['EMV_SMA'].iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['EMV'].iloc[-1] < df['EMV_SMA'].iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")


        return signal

    def calculate_and_display_ma_6(df, label):
        #Simple MA
        ma_6 = talib.SMA(df['Close'], timeperiod=6)

        signal = None
        if df['Close'].iloc[-1] > ma_6.iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['Close'].iloc[-1] < ma_6.iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " No Trend"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_ma_24(df, label):
        # Simple MA
        ma_24 = talib.SMA(df['Close'], timeperiod=24)

        signal = None
        if df['Close'].iloc[-1] > ma_24.iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['Close'].iloc[-1] < ma_24.iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " No Trend"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_ma_72(df, label):
        # Simple MA
        ma_72 = talib.SMA(df['Close'], timeperiod=72)

        signal = None
        if df['Close'].iloc[-1] > ma_72.iloc[-1]:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        elif df['Close'].iloc[-1] < ma_72.iloc[-1]:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " No Trend"
            label.setText(signal)
            label.setStyleSheet("color: white; font-size: 10pt; background-color: rgba(200, 200, 255, 100);")

        return signal

    def calculate_and_display_all_signals(df, label):
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


        # take signals from all functions
        for signal_func in signal_funcs:
            signal = signal_func(df, label)
            if signal == " Buy":
                buy_count += 1
                print ("Buy")

            elif signal == " Sell":
                sell_count += 1
                print("Sell")

            elif signal == " Neutral":
                print("Neutral")
                None

            elif signal == " Oversold":
                buy_count += 1

            elif signal == " Overbought":
                sell_count += 1

            elif signal == " Below average":
                buy_count += 1

            elif signal == " Above average":
                sell_count += 1

        print(buy_count)
        print(sell_count)
        buy_signal = buy_count > sell_count
        sell_signal = sell_count > buy_count

        # make a decision based on our signals
        if buy_signal:
            signal = " Buy"
            label.setText(signal)
            label.setStyleSheet("color: #90E039; font-family: MS Shell Dlg 2; font-size: 14pt; background-color: rgba(200, 200, 255, 100);")

        elif sell_signal:
            signal = " Sell"
            label.setText(signal)
            label.setStyleSheet("color: #960000; font-family: MS Shell Dlg 2; font-size: 14pt; background-color: rgba(200, 200, 255, 100);")
        else:
            signal = " Neutral"
            label.setText(signal)
            label.setStyleSheet("color: white; font-family: MS Shell Dlg 2; font-size: 14pt; background-color: rgba(200, 200, 255, 100);")

        return buy_signal, sell_signal, signal, buy_count, sell_count

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

    def quick_resume(df, label):

        price = df['Close'].iloc[-1]
        price = round(price, 2)
        previous_close = df['Close'].iloc[-2]

        price_change = price - previous_close
        percent_change = (price_change / previous_close) * 100

        temp1, temp2, signal, buy_count, sell_count = Indicators.calculate_and_display_all_signals(df, label)


        label.setStyleSheet("color: white; font-size: 18px; background-color: #1e1f22;")
        label.setText(
            f"Last closed price: {price}\n"
            f"Price change: {price_change:.2f}\n"
            f"Percent change: {percent_change:.2f}%\n"
            f"Buy: {buy_count} indicators, Sell : {sell_count} indicators\n"
            f"General recommendation: {signal}"
        )

















