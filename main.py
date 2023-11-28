
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsScene

import data_taker
from technical_analysis import ATRCalculator, Indicators
from accumulation_distribution import Calculate_Dist




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Skeleton = QtWidgets.QFrame(self.centralwidget)
        self.Skeleton.setGeometry(QtCore.QRect(0, 0, 1920, 1200))
        self.Skeleton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Skeleton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Skeleton.setObjectName("Skeleton")
        self.Background_image = QtWidgets.QLabel(self.Skeleton)
        self.Background_image.setGeometry(QtCore.QRect(0, 0, 1920, 1200))
        self.Background_image.setStyleSheet("background-color: #000000;\n"
"")
        self.Background_image.setText("")
        self.Background_image.setObjectName("Background_image")
        self.label = QtWidgets.QLabel(self.Skeleton)
        self.label.setGeometry(QtCore.QRect(220, 930, 881, 61))
        self.label.setStyleSheet("background-color: rgba(200, 200, 255, 100);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Pager = QtWidgets.QStackedWidget(self.Skeleton)
        self.Pager.setGeometry(QtCore.QRect(20, 20, 1241, 901))
        self.Pager.setStyleSheet("background-color: #121212;\n"
"border-radius: 5px;\n"
"")
        self.Pager.setObjectName("Pager")
        self.Asset_page = QtWidgets.QWidget()
        self.Asset_page.setObjectName("Asset_page")
        self.Asset_windows_title = QtWidgets.QLabel(self.Asset_page)
        self.Asset_windows_title.setGeometry(QtCore.QRect(490, 20, 391, 101))
        self.Asset_windows_title.setStyleSheet("QLabel {\n"
"    background-color:#2b2d30; \n"
"    color: white;\n"
"    border-radius: 5px; \n"
"    font-size: 26pt; \n"
"    padding: 5px; \n"
"}\n"
"")
        self.Asset_windows_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Asset_windows_title.setObjectName("Asset_windows_title")
        self.Asset_components = QtWidgets.QFrame(self.Asset_page)
        self.Asset_components.setGeometry(QtCore.QRect(290, 660, 721, 211))
        self.Asset_components.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Asset_components.setStyleSheet("background-color: #1e1f22;\n"
"")
        self.Asset_components.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Asset_components.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Asset_components.setObjectName("Asset_components")
        self.Choose_the_asset_label = QtWidgets.QLabel(self.Asset_components)
        self.Choose_the_asset_label.setGeometry(QtCore.QRect(220, 20, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Choose_the_asset_label.setFont(font)
        self.Choose_the_asset_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Choose_the_asset_label.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 24pt;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.Choose_the_asset_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Choose_the_asset_label.setObjectName("Choose_the_asset_label")
        self.Asset_input_window = QtWidgets.QLineEdit(self.Asset_components)
        self.Asset_input_window.setGeometry(QtCore.QRect(270, 90, 261, 51))
        self.Asset_input_window.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(200, 200, 255, 255);\n"
"    color: white; \n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
"    font-size: 20pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2b2d30;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit.placeholder {\n"
"    color: #b9babf; \n"
"}\n"
"")
        self.Asset_input_window.setText("")
        self.Asset_input_window.setAlignment(QtCore.Qt.AlignCenter)
        self.Asset_input_window.setObjectName("Asset_input_window")
        self.Find_asset_button = QtWidgets.QPushButton(self.Asset_components)
        self.Find_asset_button.setGeometry(QtCore.QRect(340, 160, 131, 41))
        self.Find_asset_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Find_asset_button.setStyleSheet("QPushButton {\n"
"   background-color: rgba(100, 100, 200, 150);\n"
"    color: White;\n"
"    border-radius: 15px; \n"
"    font-size: 20pt; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 200, 200);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.Find_asset_button.setObjectName("Find_asset_button")
        self.Quick_resume_frame = QtWidgets.QFrame(self.Asset_page)
        self.Quick_resume_frame.setGeometry(QtCore.QRect(270, 170, 751, 461))
        self.Quick_resume_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Quick_resume_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Quick_resume_frame.setObjectName("Quick_resume_frame")
        self.Quick_resume_label = QtWidgets.QLabel(self.Quick_resume_frame)
        self.Quick_resume_label.setGeometry(QtCore.QRect(290, 20, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Quick_resume_label.setFont(font)
        self.Quick_resume_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Quick_resume_label.setStyleSheet("QFrame {\n"
"    background-color:#43454a;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 24pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.Quick_resume_label.setObjectName("Quick_resume_label")
        self.Quick_resume_output = QtWidgets.QLabel(self.Quick_resume_frame)
        self.Quick_resume_output.setGeometry(QtCore.QRect(20, 110, 721, 341))
        self.Quick_resume_output.setStyleSheet("background-color: #1e1f22;")
        self.Quick_resume_output.setText("")
        self.Quick_resume_output.setObjectName("Quick_resume_output")
        self.Pager.addWidget(self.Asset_page)
        self.Technical_analysis_page = QtWidgets.QWidget()
        self.Technical_analysis_page.setObjectName("Technical_analysis_page")
        self.TA_title_label = QtWidgets.QLabel(self.Technical_analysis_page)
        self.TA_title_label.setGeometry(QtCore.QRect(450, 20, 431, 71))
        self.TA_title_label.setStyleSheet("QLabel {\n"
"    background-color:#2b2d30; \n"
"    color: white;\n"
"    border-radius: 5px; \n"
"    font-size: 26pt; \n"
"    padding: 5px; \n"
"}\n"
"")
        self.TA_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TA_title_label.setObjectName("TA_title_label")
        self.scrollArea = QtWidgets.QScrollArea(self.Technical_analysis_page)
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 1241, 801))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1241, 801))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.labeL_LIST = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeL_LIST.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.labeL_LIST.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.labeL_LIST.setObjectName("labeL_LIST")
        self.label_Resume = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Resume.setGeometry(QtCore.QRect(790, 20, 101, 41))
        self.label_Resume.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Resume.setObjectName("label_Resume")
        self.label_Resume_Output = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Resume_Output.setGeometry(QtCore.QRect(1060, 20, 161, 41))
        self.label_Resume_Output.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Resume_Output.setText("")
        self.label_Resume_Output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Resume_Output.setObjectName("label_Resume_Output")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 511, 681))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_MACD = QtWidgets.QLabel(self.layoutWidget)
        self.label_MACD.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MACD.setObjectName("label_MACD")
        self.verticalLayout.addWidget(self.label_MACD)
        self.label_Supertrend = QtWidgets.QLabel(self.layoutWidget)
        self.label_Supertrend.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Supertrend.setObjectName("label_Supertrend")
        self.verticalLayout.addWidget(self.label_Supertrend)
        self.label_Rsi = QtWidgets.QLabel(self.layoutWidget)
        self.label_Rsi.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Rsi.setObjectName("label_Rsi")
        self.verticalLayout.addWidget(self.label_Rsi)
        self.label_Parabolic_SAR = QtWidgets.QLabel(self.layoutWidget)
        self.label_Parabolic_SAR.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Parabolic_SAR.setObjectName("label_Parabolic_SAR")
        self.verticalLayout.addWidget(self.label_Parabolic_SAR)
        self.label_On_balance_ind = QtWidgets.QLabel(self.layoutWidget)
        self.label_On_balance_ind.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_On_balance_ind.setObjectName("label_On_balance_ind")
        self.verticalLayout.addWidget(self.label_On_balance_ind)
        self.label_Stochastic = QtWidgets.QLabel(self.layoutWidget)
        self.label_Stochastic.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Stochastic.setObjectName("label_Stochastic")
        self.verticalLayout.addWidget(self.label_Stochastic)
        self.label_Traders_Lion = QtWidgets.QLabel(self.layoutWidget)
        self.label_Traders_Lion.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Traders_Lion.setObjectName("label_Traders_Lion")
        self.verticalLayout.addWidget(self.label_Traders_Lion)
        self.label_Volume_Weighted = QtWidgets.QLabel(self.layoutWidget)
        self.label_Volume_Weighted.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Volume_Weighted.setObjectName("label_Volume_Weighted")
        self.verticalLayout.addWidget(self.label_Volume_Weighted)
        self.label_Volume_price_trend_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Volume_price_trend_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Volume_price_trend_2.setObjectName("label_Volume_price_trend_2")
        self.verticalLayout.addWidget(self.label_Volume_price_trend_2)
        self.label_Volume_price_trend = QtWidgets.QLabel(self.layoutWidget)
        self.label_Volume_price_trend.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Volume_price_trend.setObjectName("label_Volume_price_trend")
        self.verticalLayout.addWidget(self.label_Volume_price_trend)
        self.label_Chaikin = QtWidgets.QLabel(self.layoutWidget)
        self.label_Chaikin.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Chaikin.setObjectName("label_Chaikin")
        self.verticalLayout.addWidget(self.label_Chaikin)
        self.label_Ease_of_Movement = QtWidgets.QLabel(self.layoutWidget)
        self.label_Ease_of_Movement.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Ease_of_Movement.setObjectName("label_Ease_of_Movement")
        self.verticalLayout.addWidget(self.label_Ease_of_Movement)
        self.label_MA_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MA_6.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MA_6.setObjectName("label_MA_6")
        self.verticalLayout.addWidget(self.label_MA_6)
        self.label_MA_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MA_24.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MA_24.setObjectName("label_MA_24")
        self.verticalLayout.addWidget(self.label_MA_24)
        self.label_MA_72 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MA_72.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MA_72.setObjectName("label_MA_72")
        self.verticalLayout.addWidget(self.label_MA_72)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_MACD_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MACD_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MACD_2.setText("")
        self.label_MACD_2.setObjectName("label_MACD_2")
        self.verticalLayout_2.addWidget(self.label_MACD_2)
        self.label_Supertrend_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Supertrend_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Supertrend_2.setText("")
        self.label_Supertrend_2.setObjectName("label_Supertrend_2")
        self.verticalLayout_2.addWidget(self.label_Supertrend_2)
        self.label_Rsi_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Rsi_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Rsi_2.setText("")
        self.label_Rsi_2.setObjectName("label_Rsi_2")
        self.verticalLayout_2.addWidget(self.label_Rsi_2)
        self.label_Parabolic_SAR_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Parabolic_SAR_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Parabolic_SAR_2.setText("")
        self.label_Parabolic_SAR_2.setObjectName("label_Parabolic_SAR_2")
        self.verticalLayout_2.addWidget(self.label_Parabolic_SAR_2)
        self.label_On_balance_ind_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_On_balance_ind_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_On_balance_ind_2.setText("")
        self.label_On_balance_ind_2.setObjectName("label_On_balance_ind_2")
        self.verticalLayout_2.addWidget(self.label_On_balance_ind_2)
        self.label_Stochastic_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Stochastic_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Stochastic_2.setText("")
        self.label_Stochastic_2.setObjectName("label_Stochastic_2")
        self.verticalLayout_2.addWidget(self.label_Stochastic_2)
        self.label_Traders_Lion_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Traders_Lion_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Traders_Lion_2.setText("")
        self.label_Traders_Lion_2.setObjectName("label_Traders_Lion_2")
        self.verticalLayout_2.addWidget(self.label_Traders_Lion_2)
        self.label_Volume_Weighted_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Volume_Weighted_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Volume_Weighted_2.setText("")
        self.label_Volume_Weighted_2.setObjectName("label_Volume_Weighted_2")
        self.verticalLayout_2.addWidget(self.label_Volume_Weighted_2)
        self.label_Volume_price_trend_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Volume_price_trend_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Volume_price_trend_3.setText("")
        self.label_Volume_price_trend_3.setObjectName("label_Volume_price_trend_3")
        self.verticalLayout_2.addWidget(self.label_Volume_price_trend_3)
        self.label_Volume_price_trend_2_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Volume_price_trend_2_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Volume_price_trend_2_1.setText("")
        self.label_Volume_price_trend_2_1.setObjectName("label_Volume_price_trend_2_1")
        self.verticalLayout_2.addWidget(self.label_Volume_price_trend_2_1)
        self.label_Chaikin_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Chaikin_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Chaikin_2.setText("")
        self.label_Chaikin_2.setObjectName("label_Chaikin_2")
        self.verticalLayout_2.addWidget(self.label_Chaikin_2)
        self.label_Ease_of_Movement_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Ease_of_Movement_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Ease_of_Movement_2.setText("")
        self.label_Ease_of_Movement_2.setObjectName("label_Ease_of_Movement_2")
        self.verticalLayout_2.addWidget(self.label_Ease_of_Movement_2)
        self.label_MA_6_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MA_6_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MA_6_2.setText("")
        self.label_MA_6_2.setObjectName("label_MA_6_2")
        self.verticalLayout_2.addWidget(self.label_MA_6_2)
        self.label_MA_24_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MA_24_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MA_24_2.setText("")
        self.label_MA_24_2.setObjectName("label_MA_24_2")
        self.verticalLayout_2.addWidget(self.label_MA_24_2)
        self.label_MA_72_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_MA_72_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_MA_72_2.setText("")
        self.label_MA_72_2.setObjectName("label_MA_72_2")
        self.verticalLayout_2.addWidget(self.label_MA_72_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1.setGeometry(QtCore.QRect(790, 80, 431, 681))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_ATR_and_Perfomance = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_ATR_and_Perfomance.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_ATR_and_Perfomance.setObjectName("verticalLayout_ATR_and_Perfomance")
        self.label_Trend_Perfomance_title = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Trend_Perfomance_title.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Trend_Perfomance_title.setObjectName("label_Trend_Perfomance_title")
        self.verticalLayout_ATR_and_Perfomance.addWidget(self.label_Trend_Perfomance_title)
        self.label_Grow_Duration = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Grow_Duration.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Grow_Duration.setText("")
        self.label_Grow_Duration.setObjectName("label_Grow_Duration")
        self.verticalLayout_ATR_and_Perfomance.addWidget(self.label_Grow_Duration)
        self.label_Decline_Duration_ = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Decline_Duration_.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Decline_Duration_.setText("")
        self.label_Decline_Duration_.setObjectName("label_Decline_Duration_")
        self.verticalLayout_ATR_and_Perfomance.addWidget(self.label_Decline_Duration_)
        self.label_ATR_title = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_title.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_title.setObjectName("label_ATR_title")
        self.verticalLayout_ATR_and_Perfomance.addWidget(self.label_ATR_title)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_ATR_1_week_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_week_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_week_1.setObjectName("label_ATR_1_week_1")
        self.verticalLayout_6.addWidget(self.label_ATR_1_week_1)
        self.label_ATR_1_month_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_month_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_month_1.setObjectName("label_ATR_1_month_1")
        self.verticalLayout_6.addWidget(self.label_ATR_1_month_1)
        self.label_ATR_3_months_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_3_months_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_3_months_1.setObjectName("label_ATR_3_months_1")
        self.verticalLayout_6.addWidget(self.label_ATR_3_months_1)
        self.label_ATR_1_year_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_year_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_year_1.setObjectName("label_ATR_1_year_1")
        self.verticalLayout_6.addWidget(self.label_ATR_1_year_1)
        self.label_ATR_2_years_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_2_years_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_2_years_1.setObjectName("label_ATR_2_years_1")
        self.verticalLayout_6.addWidget(self.label_ATR_2_years_1)
        self.label_ATR_5_years_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_5_years_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_5_years_1.setObjectName("label_ATR_5_years_1")
        self.verticalLayout_6.addWidget(self.label_ATR_5_years_1)
        self.label_ATR_10_years_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_10_years_1.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_10_years_1.setObjectName("label_ATR_10_years_1")
        self.verticalLayout_6.addWidget(self.label_ATR_10_years_1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_ATR_1_week_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_week_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_week_2.setObjectName("label_ATR_1_week_2")
        self.verticalLayout_7.addWidget(self.label_ATR_1_week_2)
        self.label_ATR_1_month_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_month_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_month_2.setObjectName("label_ATR_1_month_2")
        self.verticalLayout_7.addWidget(self.label_ATR_1_month_2)
        self.label_ATR_3_months_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_3_months_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_3_months_2.setObjectName("label_ATR_3_months_2")
        self.verticalLayout_7.addWidget(self.label_ATR_3_months_2)
        self.label_ATR_1_year_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_year_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_year_2.setObjectName("label_ATR_1_year_2")
        self.verticalLayout_7.addWidget(self.label_ATR_1_year_2)
        self.label_ATR_2_years_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_2_years_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_2_years_2.setObjectName("label_ATR_2_years_2")
        self.verticalLayout_7.addWidget(self.label_ATR_2_years_2)
        self.label_ATR_5_years_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_5_years_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_5_years_2.setObjectName("label_ATR_5_years_2")
        self.verticalLayout_7.addWidget(self.label_ATR_5_years_2)
        self.label_ATR_10_years_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_10_years_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_10_years_2.setObjectName("label_ATR_10_years_2")
        self.verticalLayout_7.addWidget(self.label_ATR_10_years_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_ATR_1_week_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_week_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_week_3.setText("")
        self.label_ATR_1_week_3.setObjectName("label_ATR_1_week_3")
        self.verticalLayout_8.addWidget(self.label_ATR_1_week_3)
        self.label_ATR_1_month_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_month_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_month_3.setText("")
        self.label_ATR_1_month_3.setObjectName("label_ATR_1_month_3")
        self.verticalLayout_8.addWidget(self.label_ATR_1_month_3)
        self.label_ATR_3_months_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_3_months_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_3_months_3.setText("")
        self.label_ATR_3_months_3.setObjectName("label_ATR_3_months_3")
        self.verticalLayout_8.addWidget(self.label_ATR_3_months_3)
        self.label_ATR_1_year_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_1_year_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_1_year_3.setText("")
        self.label_ATR_1_year_3.setObjectName("label_ATR_1_year_3")
        self.verticalLayout_8.addWidget(self.label_ATR_1_year_3)
        self.label_ATR_2_years_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_2_years_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_2_years_3.setText("")
        self.label_ATR_2_years_3.setObjectName("label_ATR_2_years_3")
        self.verticalLayout_8.addWidget(self.label_ATR_2_years_3)
        self.label_ATR_5_years_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_5_years_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_5_years_3.setText("")
        self.label_ATR_5_years_3.setObjectName("label_ATR_5_years_3")
        self.verticalLayout_8.addWidget(self.label_ATR_5_years_3)
        self.label_ATR_10_years_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ATR_10_years_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_ATR_10_years_3.setText("")
        self.label_ATR_10_years_3.setObjectName("label_ATR_10_years_3")
        self.verticalLayout_8.addWidget(self.label_ATR_10_years_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_ATR_and_Perfomance.addLayout(self.horizontalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Pager.addWidget(self.Technical_analysis_page)
        self.A_D_page = QtWidgets.QWidget()
        self.A_D_page.setObjectName("A_D_page")
        self.TA_title_label_2 = QtWidgets.QLabel(self.A_D_page)
        self.TA_title_label_2.setGeometry(QtCore.QRect(440, 20, 441, 71))
        self.TA_title_label_2.setStyleSheet("QLabel {\n"
"    background-color:#2b2d30; \n"
"    color: white;\n"
"    border-radius: 5px; \n"
"    font-size: 26pt; \n"
"    padding: 5px; \n"
"}\n"
"")
        self.TA_title_label_2.setObjectName("TA_title_label_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.A_D_page)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 110, 1241, 791))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1241, 791))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 311, 741))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Ranges_open_to_open = QtWidgets.QLabel(self.layoutWidget2)
        self.label_Ranges_open_to_open.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Ranges_open_to_open.setText("")
        self.label_Ranges_open_to_open.setObjectName("label_Ranges_open_to_open")
        self.verticalLayout_3.addWidget(self.label_Ranges_open_to_open)
        self.label_Ranges_hight_to_low = QtWidgets.QLabel(self.layoutWidget2)
        self.label_Ranges_hight_to_low.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_Ranges_hight_to_low.setText("")
        self.label_Ranges_hight_to_low.setObjectName("label_Ranges_hight_to_low")
        self.verticalLayout_3.addWidget(self.label_Ranges_hight_to_low)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.layoutWidget3 = QtWidgets.QWidget(self.A_D_page)
        self.layoutWidget3.setGeometry(QtCore.QRect(380, 130, 841, 741))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView_open_to_open = QtWidgets.QGraphicsView(self.layoutWidget3)
        self.graphicsView_open_to_open.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.graphicsView_open_to_open.setObjectName("graphicsView_open_to_open")
        self.verticalLayout_4.addWidget(self.graphicsView_open_to_open)
        self.graphicsView_hight_to_low = QtWidgets.QGraphicsView(self.layoutWidget3)
        self.graphicsView_hight_to_low.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.graphicsView_hight_to_low.setObjectName("graphicsView_hight_to_low")
        self.verticalLayout_4.addWidget(self.graphicsView_hight_to_low)
        self.Pager.addWidget(self.A_D_page)
        self.Watch_List_page = QtWidgets.QWidget()
        self.Watch_List_page.setEnabled(False)
        self.Watch_List_page.setObjectName("Watch_List_page")
        #self.Pager.addWidget(self.Watch_List_page)
        self.About_page = QtWidgets.QWidget()
        self.About_page.setObjectName("About_page")
        self.label_3 = QtWidgets.QLabel(self.About_page)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 1171, 841))
        self.label_3.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 16pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.Pager.addWidget(self.About_page)
        self.Contactpage = QtWidgets.QWidget()
        self.Contactpage.setObjectName("Contactpage")
        self.label_4 = QtWidgets.QLabel(self.Contactpage)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 1171, 841))
        self.label_4.setStyleSheet("QFrame {\n"
"    background-color: rgba(200, 200, 255, 100);\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14pt;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.Pager.addWidget(self.Contactpage)
        self.layoutWidget4 = QtWidgets.QWidget(self.Skeleton)
        self.layoutWidget4.setGeometry(QtCore.QRect(250, 930, 811, 61))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Asset = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_Asset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Asset.setStyleSheet("QPushButton {\n"
"   background-color: rgba(100, 100, 200, 150);\n"
"    color: White;\n"
"    border-radius: 15px; \n"
"    font-size: 20pt; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 200, 200);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.pushButton_Asset.setObjectName("pushButton_Asset")
        self.horizontalLayout.addWidget(self.pushButton_Asset)
        self.pushButton_TechAnalysis = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_TechAnalysis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_TechAnalysis.setStyleSheet("QPushButton {\n"
"   background-color: rgba(100, 100, 200, 150);\n"
"    color: White;\n"
"    border-radius: 15px; \n"
"    font-size: 20pt; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 200, 200);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.pushButton_TechAnalysis.setObjectName("pushButton_TechAnalysis")
        self.horizontalLayout.addWidget(self.pushButton_TechAnalysis)
        self.pushButton_A_D = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_A_D.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_A_D.setStyleSheet("QPushButton {\n"
"   background-color: rgba(100, 100, 200, 150);\n"
"    color: White;\n"
"    border-radius: 15px; \n"
"    font-size: 20pt; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 200, 200);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.pushButton_A_D.setObjectName("pushButton_A_D")
        self.horizontalLayout.addWidget(self.pushButton_A_D)
        self.pushButton_About = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_About.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_About.setStyleSheet("QPushButton {\n"
"   background-color: rgba(100, 100, 200, 150);\n"
"    color: White;\n"
"    border-radius: 15px; \n"
"    font-size: 20pt; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 200, 200);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.pushButton_About.setObjectName("pushButton_About")
        self.horizontalLayout.addWidget(self.pushButton_About)
        self.pushButton_Contact = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_Contact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Contact.setStyleSheet("QPushButton {\n"
"   background-color: rgba(100, 100, 200, 150);\n"
"    color: White;\n"
"    border-radius: 15px; \n"
"    font-size: 20pt; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 200, 200);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.pushButton_Contact.setObjectName("pushButton_Contact")
        self.horizontalLayout.addWidget(self.pushButton_Contact)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pager.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart trader Assistant"))
        self.Asset_windows_title.setText(_translate("MainWindow", "Asset selection window"))
        self.Choose_the_asset_label.setText(_translate("MainWindow", "Choose the asset"))
        self.Find_asset_button.setText(_translate("MainWindow", "Find"))
        self.Quick_resume_label.setText(_translate("MainWindow", "Quick Resume"))
        self.TA_title_label.setText(_translate("MainWindow", "Technical Analysis "))
        self.labeL_LIST.setText(_translate("MainWindow", "List of indicators:"))
        self.label_Resume.setText(_translate("MainWindow", "Resume:"))
        self.label_MACD.setText(_translate("MainWindow", "Moving Average Convergence Divergence (MACD)"))
        self.label_Supertrend.setText(_translate("MainWindow", "Supertrend"))
        self.label_Rsi.setText(_translate("MainWindow", "Relative Strength Index (RSI)"))
        self.label_Parabolic_SAR.setText(_translate("MainWindow", "Parabolic SAR"))
        self.label_On_balance_ind.setText(_translate("MainWindow", "On-Balance indicator"))
        self.label_Stochastic.setText(_translate("MainWindow", "Stochastic"))
        self.label_Traders_Lion.setText(_translate("MainWindow", "Trader\'s Lion Enhanced Volume"))
        self.label_Volume_Weighted.setText(_translate("MainWindow", "Volume-Weighted Average Price"))
        self.label_Volume_price_trend_2.setText(_translate("MainWindow", "Volume at Price"))
        self.label_Volume_price_trend.setText(_translate("MainWindow", "Volume Price Trend Indicator"))
        self.label_Chaikin.setText(_translate("MainWindow", "Chaikin Money Flow Indicator"))
        self.label_Ease_of_Movement.setText(_translate("MainWindow", "Ease of Movement"))
        self.label_MA_6.setText(_translate("MainWindow", "Moving Average (6 days)"))
        self.label_MA_24.setText(_translate("MainWindow", "Moving Average (24 days)"))
        self.label_MA_72.setText(_translate("MainWindow", "Moving Average (72 days)"))
        self.label_Trend_Perfomance_title.setText(_translate("MainWindow", "Performance Trend Summary:"))
        self.label_ATR_title.setText(_translate("MainWindow", "Average Average Daily ATR:"))
        self.label_ATR_1_week_1.setText(_translate("MainWindow", "1 Week"))
        self.label_ATR_1_month_1.setText(_translate("MainWindow", "1 Month"))
        self.label_ATR_3_months_1.setText(_translate("MainWindow", "3 Months"))
        self.label_ATR_1_year_1.setText(_translate("MainWindow", "1 Year"))
        self.label_ATR_2_years_1.setText(_translate("MainWindow", "2 Years"))
        self.label_ATR_5_years_1.setText(_translate("MainWindow", "5 years"))
        self.label_ATR_10_years_1.setText(_translate("MainWindow", "10 years"))
        self.label_ATR_1_week_2.setText(_translate("MainWindow", "6 days"))
        self.label_ATR_1_month_2.setText(_translate("MainWindow", "24 days"))
        self.label_ATR_3_months_2.setText(_translate("MainWindow", "72 days"))
        self.label_ATR_1_year_2.setText(_translate("MainWindow", "288 days"))
        self.label_ATR_2_years_2.setText(_translate("MainWindow", "576 days"))
        self.label_ATR_5_years_2.setText(_translate("MainWindow", "1440 days"))
        self.label_ATR_10_years_2.setText(_translate("MainWindow", "2880 days"))
        self.TA_title_label_2.setText(_translate("MainWindow", "Accumulation/Distribution"))
        self.label_3.setText(_translate("MainWindow", "<html><head/>\n"
"<body><p><br/>&quot;Smart Trader Assistant&quot; is an innovative application developed on the PyQt5 framework, aiming to provide investors</p>\n"
" <p> and traders with advanced tools for asset analysis in international financial markets. This application not only offers </p>\n"
"<p>an intuitive and <p> aesthetically pleasing user interface but also incorporates advanced features for technical analysis </p>\n"
"<p>and tools for investment portfolio management.</p>\n"
"<p>\n"
"</p>\n"
"<p>Key features of &quot;Smart Trader Assistant&quot; include:</p>\n"
"<p> \n"
"</p>\n"
"<p>Comprehensive Analysis: The application allows the utilization of advanced technical analysis and statistical tools,</p>\n"
"<p> assisting investors in making more informed investment decisions.</p>\n"
"<p>User-Friendly: Designed with intuitiveness and ease of use in mind, the application enables users to quickly start </p>\n"
"<p>utilizing its features.</p>\n"
"<p> \n"
"</p>\n"
"<p>To find assets, users must use tickers from Yahoo.</p>\n"
"</body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>The program was created as part of a graduation project for non-commercial use.</p><p>Email: sergey.markelov.gd@gmail.com</p><p>LinkedIn: https://www.linkedin.com/in/sergey-markelov-gd/ </p><p/><p/></body></html>"))
        self.pushButton_Asset.setText(_translate("MainWindow", " Asset "))
        self.pushButton_TechAnalysis.setText(_translate("MainWindow", "  Technical Analysis  "))
        self.pushButton_A_D.setText(_translate("MainWindow", "A/D"))
        self.pushButton_About.setText(_translate("MainWindow", "  About  "))
        self.pushButton_Contact.setText(_translate("MainWindow", "  Contact  "))

        # buttons functions

        self.pushButton_Asset.clicked.connect(lambda: self.Pager.setCurrentIndex(0))
        self.pushButton_TechAnalysis.clicked.connect(lambda: self.Pager.setCurrentIndex(1))
        self.pushButton_A_D.clicked.connect(lambda: self.Pager.setCurrentIndex(2))
        self.pushButton_About.clicked.connect(lambda: self.Pager.setCurrentIndex(3))
        self.pushButton_Contact.clicked.connect(lambda: self.Pager.setCurrentIndex(4))

        # buttons name

        self.pushButton_Asset.setText("Asset")
        self.pushButton_TechAnalysis.setText("Technical Analysis")
        self.pushButton_A_D.setText("A/D")
        self.pushButton_About.setText("About")
        self.pushButton_Contact.setText("Contact")

        # asset data
        def take_data():
                print("ok")
                gl_asset_data = data_taker.FindAsset.add_asset(self, self.Asset_input_window)
                print("gl_asset_data: ", type(gl_asset_data))
                if gl_asset_data is not None:

                        if "Empty DataFrame" in gl_asset_data.to_string():
                                print("error has been caught!!!")

                        else:

                                # ATR
                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_1_week_3)
                                ATR_label1_calc.calculate_atr(6)

                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_1_month_3)
                                ATR_label1_calc.calculate_atr(24)

                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_3_months_3)
                                ATR_label1_calc.calculate_atr(72)

                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_1_year_3)
                                ATR_label1_calc.calculate_atr(288)

                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_2_years_3)
                                ATR_label1_calc.calculate_atr(576)

                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_5_years_3)
                                ATR_label1_calc.calculate_atr(1440)

                                ATR_label1_calc = ATRCalculator(gl_asset_data, self.label_ATR_10_years_3)
                                ATR_label1_calc.calculate_atr(2880)

                                # Indicators

                                Indicators.calculate_and_display_macd(gl_asset_data, self.label_MACD_2)
                                Indicators.calculate_and_display_supertrend(gl_asset_data, self.label_Supertrend_2)
                                Indicators.calculate_and_display_rsi(gl_asset_data, self.label_Rsi_2)
                                Indicators.calculate_and_display_parabolic_sar(gl_asset_data,
                                                                               self.label_Parabolic_SAR_2)
                                Indicators.calculate_and_display_obv(gl_asset_data, self.label_On_balance_ind_2)
                                Indicators.calculate_and_display_stoch(gl_asset_data, self.label_Stochastic_2)
                                Indicators.calculate_and_display_enhanced_volume(gl_asset_data,
                                                                                 self.label_Traders_Lion_2)
                                Indicators.calculate_and_display_vwap(gl_asset_data, self.label_Volume_Weighted_2)
                                Indicators.calculate_and_display_vap(gl_asset_data, self.label_Volume_price_trend_3)
                                Indicators.calculate_and_display_vpt(gl_asset_data, self.label_Volume_price_trend_2_1)
                                Indicators.calculate_and_display_cmf(gl_asset_data, self.label_Chaikin_2)
                                Indicators.calculate_and_display_emv(gl_asset_data, self.label_Ease_of_Movement_2)
                                Indicators.calculate_and_display_ma_6(gl_asset_data, self.label_MA_6_2)
                                Indicators.calculate_and_display_ma_24(gl_asset_data, self.label_MA_24_2)
                                Indicators.calculate_and_display_ma_72(gl_asset_data, self.label_MA_72_2)
                                Indicators.calculate_and_display_all_signals(gl_asset_data, self.label_Resume_Output)
                                Indicators.calculate_and_display_growth_days(gl_asset_data, self.label_Grow_Duration)
                                Indicators.calculate_and_display_decline_days(gl_asset_data,
                                                                              self.label_Decline_Duration_)
                                Calculate_Dist.calculate_open_to_open_probabilities(gl_asset_data,
                                                                                    self.label_Ranges_open_to_open)
                                Calculate_Dist.calculate_high_to_low_probabilities(gl_asset_data,
                                                                                   self.label_Ranges_hight_to_low)

                                Indicators.quick_resume(gl_asset_data, self.Quick_resume_output)

                                # histograms
                                histogram_open_to_open = Calculate_Dist.create_histogram_widget_open_to_open(
                                        gl_asset_data)
                                scene_temp = QGraphicsScene()
                                scene_temp.setBackgroundBrush(QColor("#282828"))
                                scene_temp.addWidget(histogram_open_to_open)
                                self.graphicsView_open_to_open.setScene(scene_temp)

                                scene2_temp = QGraphicsScene()
                                scene2_temp.setBackgroundBrush(QColor("#282828"))
                                histogram_high_to_low = Calculate_Dist.create_histogram_widget_high_to_low(gl_asset_data)
                                scene2_temp.addWidget(histogram_high_to_low)
                                self.graphicsView_hight_to_low.setScene(scene2_temp)

        # data serching and running indicators

        try:
                self.Find_asset_button.clicked.connect(take_data)
        except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
