from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from events.admin import event_admin_site
from events.views import IndexTemplateView
from root import settings

urlpatterns = [
    # path('', index_view)
    path('', IndexTemplateView.as_view())
]
