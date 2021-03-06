
from django.conf.urls import url, include
from django.contrib import admin
from cart import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.cartlist, name='home'),
    # url(r'^urlsave$',views.urlsave),
    url(r'^urlfail$',views.urlfail, name='fail'),
    # url(r'^geturl$',views.geturl, name='geturl'),
    url(r'^htmlsave$',views.htmlsave, name='htmlsave'),
    url(r'^cart/(?P<cart_id>\d+)/delete$',views.cart_delete),
    url(r'^accounts/',include('authentication.urls')),
]
