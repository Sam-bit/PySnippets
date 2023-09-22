from re import sub
from DrugScraper.csv_utils import csvAppendDictToCsv
from DrugScraper.htmlreader import getRequestSoup

def scrape_1mg(med_url_list):
    for i in range(ord('a'), ord('z') + 1):
        start_url = 'https://www.1mg.com/drugs-all-medicines?label=' + chr(i)
        soup = getRequestSoup(start_url)
        max_page = soup.find('ul', class_='list-pagination').find_all('li')[-2].text
        for j in range(1, int(max_page)):
            page_url = 'https://www.1mg.com/drugs-all-medicines?page=' + str(j) + '&label=' + chr(i)
            soup = getRequestSoup(page_url)
            all_meds = soup.find("div", class_=lambda value: value and "style__product-grid___" in value).find_all(
                'div')
            for med in all_meds:
                if med.find('div') is not None:
                    if med.find('div').find('a', href=True) is not None:
                        a = med.find('div').find('a', href=True)
                        med_url = 'https://www.1mg.com' + a['href']
                        print(med_url)
                        soup = getRequestSoup(med_url)
                        med_title = soup.find("h1", class_=lambda value: value and value.startswith(
                            "DrugHeader__title-content___")).text
                        detail1 = soup.find_all("div", class_=lambda value: value and value.startswith(
                            'DrugHeader__meta___'))[0].find_all('div')[1].find('a')
                        detail2 = soup.find_all("div", class_=lambda value: value and value.startswith(
                            'DrugHeader__meta___'))[1].find_all('div')[1].find('a')
                        how_to_use=''
                        if soup.find(id = 'how_to_use') is not None:
                            how_to_use = soup.find(id = 'how_to_use').find('div').find('div').find('div').find('div').text
                        manufacture_name = detail1.text if detail1 is not None else ''
                        salt_comp_name = detail2.text if detail2 is not None else ''

                        if soup.find("div", class_=lambda value: value and value.startswith(
                                'DrugPriceBox__quantity___')) is not None:
                            quantity = soup.find("div", class_=lambda value: value and value.startswith(
                            'DrugPriceBox__quantity___')).text
                            num_of_units = quantity.split(' in ')[0]
                        elif soup.find("div", class_=lambda value: value and value.startswith(
                                "sku-card-item style__slide-parent___")) is not None:
                            quantity =soup.find("div", class_=lambda value: value and value.startswith(
                                "sku-card-item style__slide-parent___")).find("div", class_=lambda value: value and value.startswith(
                                "style__pack-size___")).text
                            num_of_units = quantity.split(" of ",1)[1]
                        else:
                            quantity=""
                            num_of_units =''
                        mrp_price = soup.find("span", class_=lambda value: value and value.startswith(
                            "PriceBoxPlanOption__margin-right-")) or soup.find("span", class_=lambda
                            value: value and value.startswith(
                            "DrugPriceBox__slashed-price___"))
                        mrp_price_final=float(sub(r'[^0-9.]', '', mrp_price.text) if mrp_price is not None else 0)
                        discounted_price = soup.find("span", class_=lambda value: value and value.startswith(
                            "PriceBoxPlanOption__offer-price___")) or soup.find("div", class_=lambda
                            value: value and value.startswith(
                            "DrugPriceBox__best-price___"))
                        discount_price_final = float(sub(r'[^0-9.]', '', discounted_price.text) if discounted_price is not None else 0)
                        data = {
                            'MED_NAME': med_title,
                            'MED_URL': med_url,
                            'MANUFACTURE_NAME': manufacture_name,
                            'SALT_COMP_NAME': salt_comp_name,
                            'CONSUME_TYPE': '',
                            'HOW_TO_USE': ' '.join(how_to_use.split()),
                            'NUM_OF_UNITS_OR_VARIANTS': ' '.join(num_of_units.split()),
                            'QUANTITY' : quantity,
                            'MRP_PRICE': mrp_price_final,
                            'DISCOUNT_PRICE': discount_price_final
                        }
                        print(data)


