from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('sellers/', views.SellerList.as_view(), name = "seller_list"),
    path('sellers/new/', views.SellerCreate.as_view(), name = "seller_create"),
    path('sellers/<slug:the_slug>/', views.SellerDetail.as_view(), name = "seller_detail"),
    path('products/', views.ProductList.as_view(), name="product_list"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name = "product_detail"),
    
]