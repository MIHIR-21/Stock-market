from django.urls import path
from . import views as v

app_name = 'stocks'

urlpatterns = [

    path('register/', v.register_page , name = 'register_page'),

    path('login/', v.login_page, name='login_page'),

    path('', v.home , name= 'home'),

    path('add-stock/', v.add_stock, name ='add_stock'),
]