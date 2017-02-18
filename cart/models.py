from django.db import models

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

    cart = Cart.objects.create(title=title, price=price, photo=photo, info=info, photo=photo, date=date)
