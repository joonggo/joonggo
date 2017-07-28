from django.db import models
import requests
from bs4 import BeautifulSoup

class Cart(models.Model):
    title = models.CharField(max_length=100,blank=True)
    price = models.CharField(max_length=50,blank=True)
    photo = models.CharField(max_length=100,blank=True)
    now_state = models.CharField(max_length=100,blank=True)
    info = models.TextField(blank=True)
    howtodeliver = models.CharField(max_length=100,blank=True)
    howtodeal = models.CharField(max_length=100,blank=True)
    date = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.title

class URL(models.Model):
    url = models.CharField(max_length=400)
    html = models.TextField(blank=True)

    def crawling(self):

        html = self.html
        soup = BeautifulSoup(html, 'lxml')
        url = self.url
        img=soup.select_one("#tbody > table > tbody > tr > th > div > img")["src"]
        product_info=soup.select_one("#tbody > table > tbody > tr > td > div")
        title=product_info.select_one("p.title").text
        price=product_info.select_one("div.prod_price").text
        now_state=product_info.select_one("em")["aria-label"]

        Cart.objects.create(title=title,url=url,photo=img,price=price,now_state=now_state)

    def __str__(self):
        return self.url
