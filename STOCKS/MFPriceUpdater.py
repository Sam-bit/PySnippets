from re import sub
import openpyxl
import requests
from bs4 import BeautifulSoup


def getSoup(mf_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 '
                      'Safari/537.36 '
    }
    html = requests.get(mf_url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_current_nav(soup):
    try:
        cur_nav = float(sub(r'[^0-9.]', '', soup.find('td', class_= "fd12Cell contentPrimary bodyLargeHeavy").text.strip()))
    except:
        cur_nav = "N/A"
    return cur_nav

def get_expense_ratio(soup):
    try:
        exp_ratio = soup.find('h3', class_= "ot654subHeading bodyLargeHeavy").text.strip().replace("Expense ratio: ","")
    except:
        exp_ratio = "N/A"
    return exp_ratio
xlfilename = "C:\\Users\\LENOVO\\Desktop\\MY PORTFOLIO.xlsx"
my_wb = openpyxl.load_workbook(xlfilename)
my_sheet_obj = my_wb['ALL INVESTMENTS']
for i in range(19, 24):
    mf_url = my_sheet_obj.cell(row=i, column=7)
    print(str(mf_url.value).strip())
    soup = getSoup(str(mf_url.value).strip())
    current_nav = get_current_nav(soup)
    expense_ratio = get_expense_ratio(soup)

    my_sheet_obj.cell(row=i, column=4).value = current_nav
    my_sheet_obj.cell(row=i, column=2).value = expense_ratio
    my_wb.save(xlfilename)
    print("=========SAVED=========")