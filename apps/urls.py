from django.urls import path

from apps.views import index_view

urlpatterns = [
   path('', index_view, name='index')
]
