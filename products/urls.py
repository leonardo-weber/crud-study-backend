from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='get_all_products'),
    path('products/<int:id>', views.get_product_by_id, name='get_product_by_id'),
    path('products/create', views.create_product, name='create_product'),
    path('products/update/<int:id>', views.create_product, name='update_product'),
]