from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products, name='products_list'),   # example view
    path('<int:id>/', views.Products_show, name='product_detail'),  # example detail view
]
