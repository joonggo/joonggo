from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$', auth_views.login,name='login',kwargs={
            'template_name':'accounts/login_form.html',
        }),
    url(r'^logout/$',auth_views.logout,name='logout',kwargs={
            'next_page' : reverse_lazy('home'),
        }),

]