import re
import requests
from bs4 import BeautifulSoup
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


price = []
link = []


def find_it(classname, soup):
    try:
        for g in soup.find_all('a', {'class': re.compile(f'{classname}')}):
            stringify = str(g)
            print(stringify)
            price_re = "<span class=\"ListItemPrice_currency_2l0XS\">CHF</span><span>(.*?).–</span><!-- --></span>"
            price_s = re.search(price_re, stringify)
            photo_re = "class=\"ListItemImage_imagesNumber_e43Eo\"><div><span>(.*?)</span></div></div>"
            photo_s = re.search(photo_re, stringify)
            if price_s.group(1) and int(photo_s.group(1)) > 1:
                print(f"price: {price_s.group(1)} with photos {photo_s.group(1)}")
                price.append(price_s.group(1))
                pattern = "href=\"/buy/(.*?)\">"
                substring = re.search(pattern, stringify)
                link.append("https://www.homegate.ch/buy/" + substring.group(1))
    except Exception as e:
        # print(e.args)
        pass


def write_file(name):
    with open(f'{name}.md', 'a+') as table:
        table.write('''|Price| Link |
                |-------|-------|
                 ''')
        results = list(zip(price, link))
        for r in results:
            table.write("|" + str(r[0]) + "|" + str(r[1]) + "\n")
    table.close()


def cook_soup(page, type, min_price, max_price ):
    try:
        url = f'https://www.homegate.ch/buy/plot/{type}/country-switzerland/matching-list?ep={page}&o=resultingSearchablePrice-asc&ai={min_price}&aj={max_price}&avb=12M'
        content = requests.get(url, headers=headers)
        soup = BeautifulSoup(content.text, 'html.parser')
        return soup
    except:
        return None


if __name__ == '__main__':
    min_price = 61000
    max_price = 99000
    plot_land = 'sc-building-plot'
    single_house ='sc-single-house'
    houses = 'houses'
    farm_house= 'sc-farm-house'

    type = plot_land
    for page in range(20):
        soup = cook_soup(page, min_price=min_price,max_price=max_price, type=type)
        if soup == None:
            break
        classes = ['ListItemTopPremium_item', 'ListItem_itemLink_']
        for c in classes:
            find_it(c, soup)
    write_file(f"{type}-{datetime.date.today()} {min_price}-{max_price}")
