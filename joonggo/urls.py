
from django.conf.urls import url
from django.contrib import admin
from cart import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.cartlist, name='home'),
    url(r'^urlsave$',views.urlsave),
    url(r'^urlfail$',views.urlfail, name='fail'),
    url(r'^geturl$',views.geturl, name='geturl'),
    url(r'^htmlsave$',views.htmlsave, name='htmlsave'),
]
