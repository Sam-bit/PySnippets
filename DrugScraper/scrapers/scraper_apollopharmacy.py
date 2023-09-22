from re import sub
from DrugScraper.csv_utils import csvAppendDictToCsv
from DrugScraper.htmlreader import getRequestSoup,getChromeSoup
def scrape_ApolloPharmacy(med_url_list):
    start_url = 'https://www.apollopharmacy.in/brands'
    soup = getRequestSoup(start_url)
    all_brands = soup.find_all("div", class_=lambda value: value and value.startswith ("SitemapDirectories_listedItemsRow__"))
    for brand in all_brands:
        if brand.find('div', class_=lambda value: value and value.startswith ("SitemapDirectories_productsList__")) is not None:
            all_brands_sub = brand.find('div', class_=lambda value: value and value.startswith ("SitemapDirectories_productsList__")).find('ul').find_all('li')
            for brand_sub in all_brands_sub[3:]:
                a = brand_sub.find('a')
                if not str(a['href']).endswith('null'):
                    brand_url = 'https://www.apollopharmacy.in' + a['href']
                    soup = getChromeSoup(brand_url)
                    if soup.find('div',class_=lambda value: value and value.startswith ("ProductCard_pcContainer__")) is not None:
                        all_meds = soup.find('div',class_=lambda value: value and value.startswith ("ProductCard_pcContainer__")).find('div').find('div').find('div').find_all('div',recursive=False)
                        for med in set(all_meds):
                            if med.find('div',class_=lambda value: value and value.startswith ("ProductCard_priceGroup__")) is not None and med.find('div',class_=lambda value: value and value.startswith ("ProductCard_pdHeader__")) is not None:
                                #med_lists.append('https://www.apollopharmacy.in' + str(med.find('div',class_=lambda value: value and value.startswith ("ProductCard_pdHeader__")).find('a')['href']).replace("?doNotTrack=true",""))
                                price_text=med.find('div', class_=lambda value: value and value.startswith(
                                    "ProductCard_priceGroup__")).text
                                if "(" in price_text:
                                    discounted_price = price_text.split(")",1)[1]
                                    mrp_price = price_text.split(')')[0]
                                else:
                                    mrp_price= price_text
                                    discounted_price= price_text
                                mrp_price_final = float(
                                    sub(r'[^0-9.]', '', mrp_price if mrp_price is not None else 0))
                                discount_price_final = float(
                                    sub(r'[^0-9.]', '', discounted_price if discounted_price is not None else 0))

                                med_url ='https://www.apollopharmacy.in' + str(med.find('div',class_=lambda value: value and value.startswith ("ProductCard_pdHeader__")).find('a')['href']).replace("?doNotTrack=true","")
                                print(med_url)
                                soup = getRequestSoup(med_url)
                                detaildiv = soup.find('div', class_=lambda value: value and value.startswith(
                                    "PdpWeb_productDetails__")).find_all('div')[0]
                                med_title = detaildiv.find('h1').text
                                consume_type=detaildiv.find_all('div')[-1].find('p').text
                                how_to_use = ''
                                if soup.find('div',class_=lambda value: value and value.startswith('MuiTypography-root PdpWeb_compositionUrl__')) is not None:
                                    salt_comp_name = soup.find('div',class_=lambda value: value and value.startswith('MuiTypography-root PdpWeb_compositionUrl__')).text
                                elif soup.find('div', class_=lambda value: value and value.startswith("ProductDetailsGeneric_descMain__")) is not None:
                                    alldesclist = soup.find('div', class_=lambda value: value and value.startswith(
                                    "ProductDetailsGeneric_descMain__")).find_all('div', class_=lambda
                                    value: value and value.startswith("ProductDetailsGeneric_descListing__"))
                                    for desc in alldesclist:
                                        if desc.find('h2').text == 'Key Ingredients':
                                            salt_comp_name = desc.find('div').text
                                        if desc.find('h2').text == 'Directions for Use':
                                            how_to_use = desc.find('div').text
                                else:
                                    salt_comp_name = ''
                                manufacture_name = detaildiv.find('div',
                                                                  class_=lambda value: value and value.startswith(
                                                                      "PdpWeb_manufacturerWrapper__")).find('p',
                                                                                                            class_="MuiTypography-root MuiTypography-body1").text
                                num_of_units = soup.find('p', class_=lambda value: value and value.startswith(
                                    "MultiVariantInfo_multiVariantLabel__"))
                                quantity  = soup.find('div',class_=lambda value: value and value.startswith("MedicineInfoWeb_priceWrap__")).find('div',class_=lambda value: value and value.startswith("MedicineInfoWeb_leftGroup__")).find('p').text
                                num_of_units_final = num_of_units.find('span').text if num_of_units is not None else 1
                                data = {
                                    'MED_NAME': med_title,
                                    'MED_URL': med_url,
                                    'MANUFACTURE_NAME': manufacture_name,
                                    'SALT_COMP_NAME': ' '.join(salt_comp_name.replace("Abzorb Contains ","").replace(" and ","").replace("Each tube contains : ","").split(None)),
                                    'CONSUME_TYPE':' '.join(consume_type.split()),
                                    'HOW_TO_USE' : ' '.join(how_to_use.split()),
                                    'NUM_OF_UNITS_OR_VARIANTS': ' '.join(num_of_units_final.split()),
                                    'QUANTITY': ' '.join(quantity.split()),
                                    'MRP_PRICE': mrp_price_final,
                                    'DISCOUNT_PRICE': discount_price_final
                                }

                                print(data)
                                csvAppendDictToCsv(data,med_url_list)
