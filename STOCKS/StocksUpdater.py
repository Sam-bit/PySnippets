import os
import time as t
import xlwings as xw
from datetime import datetime,time

def is_time_between(begin_time, end_time):
    # If check time is not given, default to current UTC time
    check_time =  datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

print('Closing Opened Excel File')
xlfilename = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\MY PORTFOLIO.xlsx"
try:
    book = xw.Book(xlfilename)
    book.close()
except Exception as e:
    print(e)
print('Sleeping for 10 secs')
t.sleep(10)
already_updated = (datetime.fromtimestamp(os.path.getmtime(xlfilename))>datetime(datetime.now().year,datetime.now().month,datetime.now().day,16,0))
reUpdate = False
print(already_updated)
# if ((not is_time_between(time(9,0), time(16,0))) and (not already_updated)) or reUpdate:
#     os.system(".\StockCloseUpdater.py")
#     os.system(".\StockWatchlistUpdater.py")
#     os.system(".\MFPriceUpdater.py")
# else:
#     os.system(".\MFPriceUpdater.py")
os.system(".\StockCloseUpdater.py")
os.system(".\StockWatchlistUpdater.py")
os.system(".\MFPriceUpdater.py")
# os.system(".\StockBonusSplitUpdater.py")