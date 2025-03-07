from django.urls import path
from App.views import *
urlpatterns = [
    path('',homePage,name = 'homePage'),
    path('home/<slug>', home,name = 'home'),
    path('productDetails/<slug>',productDetails,name= 'productDetails'),
    path('register-user',register_user,name = 'register_user'),
    path('login-user',login_user,name = 'login_user'),
    path('cart',cart_data,name = 'cart'),
    path('add_to_cart/<id>',add_to_cart,name = 'add_to_cart'),
    path('remove_cart/<id>',remove_cart,name = 'remove_cart'),
    path('logout',logout_user,name = 'logout'),
]
