from django.db import models
import requests
from bs4 import BeautifulSoup

class Cart(models.Model):
    title = models.CharField(max_length=100,blank=True)
    price = models.IntegerField(default=1,blank=True)
    photo = models.CharField(max_length=100,blank=True)
    info = models.TextField(blank=True)
    howtodeliver = models.CharField(max_length=100,blank=True)
    howtodeal = models.CharField(max_length=100,blank=True)
    date = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title

class URL(models.Model):
    url = models.CharField(max_length=400)

    def crawling(self):

        response = requests.get(self.url)
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

        Cart.objects.create(title=name, price=price, photo=photo, info=description, howtodeliver=how_deliver, howtodeal=how_method, date=date)

    def __str__(self):
        return self.url
