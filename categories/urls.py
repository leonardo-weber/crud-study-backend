from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='product-list'),
    path('<int:id>', CategoryDetailView.as_view(), name='product-detail'),
]