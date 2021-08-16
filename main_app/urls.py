from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('sellers', views.SellerList.as_view(), name = "seller_list"),
    path('sellers', views.SellerCreate.as_view(), name = "seller_create"),
]