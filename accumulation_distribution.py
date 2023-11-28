import pandas as pd

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Calculate_Dist:

    def calculate_open_to_open_and_high_to_low(df):
        # calculate open_to_open and high_to_low
        # this function was created only for test!!!
        df['open_to_open'] = df['Open'].pct_change() * 100  # (day 1 - day 2) / day 1
        df['high_to_low'] = (df['High'] - df['Low']) / df['Low'] * 100  # (max. price - min. price) / min. price

        # We remove NaN values that could appear after calculations
        df = df.dropna()

        return df['open_to_open'].values, df['high_to_low'].values

    def calculate_open_to_open_probabilities(df, label):
        # Calculate percentage changes in opening prices
        df['open_to_open'] = df['Open'].pct_change() * 100

        # Define bins
        bins = [-float('inf'), -3, -2.7, -2.4, -2.1, -1.8, -1.5, -1.2, -0.9, -0.6, -0.3, 0, 0.3, 0.6, 0.9, 1.2, 1.5,
                1.8, 2.1, 2.4, 2.7, 3, float('inf')]

        # Create categories and count the number of days in each category
        df['open_to_open_category'] = pd.cut(df['open_to_open'], bins=bins, labels=False, right=False)
        category_ranges = [
            " Less than -3%",
            " -3% to -2.7%",
            " -2.7% to -2.4%",
            " -2.4% to -2.1%",
            " -2.1% to -1.8%",
            " -1.8% to -1.5%",
            " -1.5% to -1.2%",
            " -1.2% to -0.9%",
            " -0.9% to -0.6%",
            " -0.6% to -0.3%",
            " -0.3% to 0%",
            " 0% to 0.3%",
            " 0.3% to 0.6%",
            " 0.6% to 0.9%",
            " 0.9% to 1.2%",
            " 1.2% to 1.5%",
            " 1.5% to 1.8%",
            " 1.8% to 2.1%",
            " 2.1% to 2.4%",
            " 2.4% to 2.7%",
            " 2.7% to 3%",
            " More than 3%"
        ]

        days_in_category = df['open_to_open_category'].value_counts().sort_index()

        # Calculate total number of days
        total_days = len(df)

        # Calculate probabilities
        probabilities = days_in_category / total_days * 100
        probabilities_formatted = probabilities.round(2).astype(str) + '%'

        # Создаем DataFrame с колонками Ranges, Frequency и Probability
        result_df = pd.DataFrame({'Ranges': category_ranges,
                                  'Frequency': days_in_category.values,
                                  'Probability': probabilities_formatted},
                                 index=range(len(category_ranges)))

        # Форматируем DataFrame для красивого вывода
        formatted_result = result_df.to_string(index=False)

        if label is not None:
            label.setText(formatted_result)
            label.setStyleSheet(
                "color: white; font-size: 8pt; text-align: center; background-color: rgba(200, 200, 255, 100);")

        return result_df


    def calculate_high_to_low_probabilities(df,label):
        # Calculate percentage changes in high to low prices
        df['high_to_low'] = (df['High'] - df['Low']) / df['Low'] * 100

        # bins
        bins = [-float('inf'), 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, float('inf')]

        # Creating categories
        df['high_to_low_category'] = pd.cut(df['high_to_low'], bins=bins, labels=False, right=False)

        # Count the number of days in each category
        days_in_category = df['high_to_low_category'].value_counts().sort_index()

        # Calculate total number of days
        total_days = len(df)
        # Calculate probabilities without NaN values
        probabilities = days_in_category / total_days * 100

        # Define category ranges
        category_ranges = [
            " Less than 0.2%",
            " 0.2% to 0.4%",
            " 0.4% to 0.6%",
            " 0.6% to 0.8%",
            " 0.8% to 1.0%",
            " 1.0% to 1.2%",
            " 1.2% to 1.4%",
            " 1.4% to 1.6%",
            " 1.6% to 1.8%",
            " 1.8% to 2.0%",
            " 2.0% to 2.2%",
            " 2.2% to 2.4%",
            " 2.4% to 2.6%",
            " 2.6% to 2.8%",
            " 2.8% to 3.0%",
            " 3.0% to 3.2%",
            " 3.2% to 3.4%",
            " 3.4% to 3.6%",
            " 3.6% to 3.8%",
            " 3.8% to 4.0%",
            " More than 4.0%"
        ]

        probabilities_formatted = probabilities.round(2).astype(str) + '%'

        # Create a DataFrame with Ranges, Frequency and Probability columns
        result_df = pd.DataFrame({'Ranges': category_ranges,
                                  'Frequency': days_in_category.values,
                                  'Probability': probabilities_formatted},
                                 index=range(len(category_ranges)))

        formatted_result = result_df.to_string(index=False)

        if label is not None:
            label.setText(formatted_result)
            label.setStyleSheet("color: white; font-size: 8pt; background-color: rgba(200, 200, 255, 100);")

        return result_df

    def create_histogram_widget_open_to_open(df):

        fig, ax = plt.subplots(figsize=(8, 4))  # Set the figure size 7, 2.5

        # Plot the data and set the background color
        result_df = Calculate_Dist.calculate_open_to_open_probabilities(df, label=None)
        result_df['Probability'].str.rstrip('%').astype('float').plot(kind='bar', ax=ax, fontsize=8, color='blue')

        # Configure x-axis labels
        ax.set_xticklabels(result_df['Ranges'], rotation=45, ha='right', fontsize=5, color='red')

        # Add labels with the count of days above each bar
        for bar, count in zip(ax.patches, result_df['Frequency']):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{count} days',
                    ha='center', va='bottom', fontsize=5, color='red')

        # Set the background color of the plot
        ax.set_facecolor('white')

        # Set the color of y-axis labels
        ax.yaxis.label.set_color('red')

        # Set the color of x-axis labels
        ax.xaxis.label.set_color('red')

        # Set the color of tick labels on the y-axis
        ax.tick_params(axis='y', colors='red')

        # Set the color of tick labels on the x-axis
        ax.tick_params(axis='x', colors='red')

        # Create a widget to contain the matplotlib figure
        widget = QWidget()
        layout = QVBoxLayout(widget)
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        widget.setFixedSize(canvas.size())
        widget.setStyleSheet("background-color: #282828, border-radius: 0px;")

        return widget

    def create_histogram_widget_high_to_low(df):

        # Create a figure and plot the histogram
        fig, ax = plt.subplots(figsize=(8, 4))
        result1 = Calculate_Dist.calculate_high_to_low_probabilities(df, label=None)

        # Remove '%' sign and convert to numeric
        result1['Probability'] = result1['Probability'].str.rstrip('%').astype('float')

        # Plot the Probability column directly
        result1['Probability'].plot(kind='bar', ax=ax, fontsize=8)

        ax.set_xticklabels(result1['Ranges'], rotation=45, ha='right', fontsize=5, color='red')

        # Add labels with the count of days above each bar
        for bar, count in zip(ax.patches, result1['Frequency']):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{count} days',
                    ha='center', va='bottom', fontsize=5, color='red')

        ax.set_facecolor('white')

        # Set the color of y-axis labels
        ax.yaxis.label.set_color('red')

        # Set the color of x-axis labels
        ax.xaxis.label.set_color('red')

        # Set the color of tick labels on the y-axis
        ax.tick_params(axis='y', colors='red')

        # Set the color of tick labels on the x-axis
        ax.tick_params(axis='x', colors='red')
        # Create a widget to contain the matplotlib figure
        widget = QWidget()
        layout = QVBoxLayout(widget)
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        widget.setFixedSize(canvas.size())
        widget.setStyleSheet("background-color: #282828, border-radius: 0px;")

        return widget





