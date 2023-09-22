from DrugScraper.csv_utils import csvColumnToList
from DrugScraper.scrapers.scraper_1mg import scrape_1mg
#1MG, AskApollo, Medlife, MedPlus, Netmeds, NowRx, OptumRx, PharmEasy, PillPack, Practo, RiteAid, and Saydl

from re import sub
from DrugScraper.csv_utils import csvAppendDictToCsv
from DrugScraper.htmlreader import getRequestSoup,getChromeSoup
from DrugScraper.scrapers.scraper_apollopharmacy import scrape_ApolloPharmacy

if __name__ == '__main__':
    med_url = csvColumnToList()
    scrape_1mg(med_url)
    scrape_ApolloPharmacy(med_url)
