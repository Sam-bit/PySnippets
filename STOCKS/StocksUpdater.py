import os
import shutil

shutil.copy("C:\\Users\\LENOVO\\Desktop\\MY PORTFOLIO.xlsx", "D:\\ANDROID")
shutil.copy("C:\\Users\\LENOVO\\Desktop\\DIVIDENDS.xlsx", "D:\\ANDROID")
os.system("StockCloseUpdater.py")
os.system("StockWatchlistUpdater.py")
os.system("MFPriceUpdater.py")
os.system("StockBonusSplitUpdater.py")