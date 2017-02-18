from django.shortcuts import render
from cart.models import Cart,URL
from cart.forms import URLForm

def cartlist(request):
    carts = Cart.objects.all()
    context = {
        'carts' : carts,
    }
    return render(request, 'cart/cartlist.html',context)

def urlsave(request):
    form = URLForm(request.POST or None)
    if request.method == 'POST':
        form =URLForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print('저장 완료')
            context = {
                'form':form,
            }
            return render(request,'cart/urlsave.html',context)

    print(form)
    context = {
        'form':form,
    }
    return render(request,'cart/urlsave.html',context)
