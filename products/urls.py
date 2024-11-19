from django.urls import path
from . import views  # Імпортуємо наші функції з views.py

urlpatterns = [
    path('products/<int:productId>/', views.get_product, name='product_detail'),  # Додаємо маршрут для ендпоінта
]