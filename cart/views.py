from django.shortcuts import render
from cart.models import Cart

def cartlist(request):
    carts = Cart.objects.all()
    context = {
        'carts' : carts,
    }
    return render(request, 'cart/cartlist.html',context)

def urlsave(request):
    return render(request,'cart/urlsave.html')
