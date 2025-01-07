from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('products/', include('products.urls')),
    path('categories/', include('categories.urls')),
    path('admin/', admin.site.urls),
]
