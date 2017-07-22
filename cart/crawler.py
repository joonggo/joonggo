import requests
from bs4 import BeautifulSoup


def joongo_crawler(url):

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    name = soup.select('.product_name')[0].text
    name = name.replace('\n', '')
    name = name.replace('\t', '')
    name = name.replace('\r', '')
    name = name.replace(' ', '')
    name = name.replace('상품명:', '')
    name = name.replace('[상품거래]', '')

    txt_tag = soup.select('.product_info .txt_desc')

    price = txt_tag[0].text
    description = txt_tag[1].text
    how_method = txt_tag[2].text
    how_deliver = txt_tag[3].text

    price = price.strip()
    description = description.strip()
    how_method = how_method.strip()
    how_deliver = how_deliver.strip()

    date_list = soup.select('.date')
    date = date_list[0].text

    photo_list = soup.select('.img_box img')
    photo = photo_list[0].get('src')
