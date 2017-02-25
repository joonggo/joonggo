from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, resolve_url
from cart.models import Cart, URL
from cart.forms import URLForm
from django.views.decorators.csrf import csrf_exempt

def cartlist(request):
    carts = Cart.objects.all()
    context = {
        'carts': carts,
    }
    return render(request, 'cart/cartlist.html', context)


def urlsave(request):
    form = URLForm(request.POST or None)
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                instance.crawling()
                instance.save()
                context = {
                    'form': form,
                }
                return render(request, 'cart/urlsave.html', context)
            except IndexError:
                return redirect('fail')

    print(form)
    context = {
        'form': form,
    }
    return render(request, 'cart/urlsave.html', context)


def urlfail(request):
    return render(request, 'cart/urlfail.html',)


def geturl(request):
    if request.method =="GET":
        q= request.GET.get('url','')
        url=URL.objects.create(url=q)
        url.crawling()
        return redirect('home')
    return render(request, 'cart/geturl.html',)

@csrf_exempt
def htmlsave(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                instance.crawling()
                instance.save()
                context = {
                    'form': form,
                }
                return redirect('home')
            except IndexError:
                return redirect('fail')
        return redirect('fail')

def cart_delete(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('home')


