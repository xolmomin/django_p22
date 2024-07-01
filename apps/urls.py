from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import ProductListView, ProductDetailView, RegisterCreateView, LogoutView, SettingsUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_page'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail_page'),

    path('settings', SettingsUpdateView.as_view(), name='settings_page'),
    path('register', RegisterCreateView.as_view(), name='register_page'),
    path('login', LoginView.as_view(
        template_name='apps/auth/login.html',
        redirect_authenticated_user=True,
        next_page='product_list_page'
    ), name='login_page'),
    path('logout', LogoutView.as_view(), name='logout_page'),
]
