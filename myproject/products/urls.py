from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:productId>/', views.get_product),
    path('products/', views.get_product_list)
]