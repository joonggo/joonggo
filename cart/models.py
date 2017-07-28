from django.db import models
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User


class Cart(models.Model):

    user = models.OneToOneField(User,related_name='user')
    title = models.CharField(max_length=100,blank=True) # 이름
    price = models.CharField(max_length=50,blank=True)  # 물건 가격
    img = models.CharField(max_length=100,blank=True)   # 물건 사진
    now_state = models.CharField(max_length=100,blank=True) # 판매 상태
    url = models.CharField(max_length=400)   # 해당 주소
    html = models.TextField(blank=True)      # html
    created_at = models.DateField(auto_now_add=True) # 장바구니 시점


    def save(self, user):
        html = self.html
        soup = BeautifulSoup(html, 'lxml')
        url = self.url
        self.img=soup.select_one("#tbody > table > tbody > tr > th > div > img")["src"]
        product_info=soup.select_one("#tbody > table > tbody > tr > td > div")
        self.title=product_info.select_one("p.title").text
        self.price=product_info.select_one("div.prod_price").text
        self.now_state=product_info.select_one("em")["aria-label"]
        self.user=user
        super().save()

    def __str__(self):
        return self.title
