from django.urls import path, include
from apps.views import product_list, product_detail, product_delete, product_update, product_create

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('product/delete/<int:pk>', product_delete, name='product_delete'),
    path('product/update/<int:pk>', product_update, name='product_update'),
    path('product/create', product_create, name='product_create'),
]
