from django.urls import path

from apps.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail', ProductDetailView.as_view(), name='product_detail')
]
