from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, resolve_url
from cart.models import Cart
from cart.forms import CartForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def cartlist(request):
    carts = Cart.objects.all()
    context = {
        'carts': carts,
    }
    return render(request, 'cart/cartlist.html', context)


def urlfail(request):
    return render(request, 'cart/urlfail.html',)


@csrf_exempt
def htmlsave(request):
    form = CartForm(request.POST or None)
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                instance.save(request.user)
                context = {
                    'form': form,
                }
                return HttpResponse("good")
            except IndexError:
                return redirect('fail')
        print("여기")
        return redirect('fail')

def cart_delete(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('home')


