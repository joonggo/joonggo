from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, resolve_url
from cart.models import Cart, URL
from cart.forms import URLForm


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
