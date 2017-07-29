from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, resolve_url,get_object_or_404
from cart.models import Cart
from cart.forms import CartForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def cartlist(request):
    user=request.user
    if user.is_authenticated():
        carts = user.carts.all()
        if carts:
            context = {
                'carts': carts,
            }
            return render(request, 'cart/cartlist.html', context)
        else:
            return HttpResponse("None cart")
    return HttpResponse("good")

def urlfail(request):
    return render(request, 'cart/urlfail.html',)

@login_required(login_url='/accounts/login/')
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

    return HttpResponse("good")

@login_required(login_url='/accounts/login/')
def cart_delete(request,cart_id):
    cart = get_object_or_404(Cart,id=cart_id)
    if request.user==cart.user:
        cart.delete()
        return redirect('home')
    else:
        return redirect('fail')



