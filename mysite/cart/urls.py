from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_user_cart', views.fetchUserCart, name='fetch_user_cart'),
    path('add_to_cart', views.addtoCart, name='add_to_cart'),
    path('remove_from_cart', views.removefromCart, name='remove_from_cart'),
]
