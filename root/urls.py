from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from events.admin import event_admin_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('event-admin/', event_admin_site.urls),
]
admin.site.site_header = "UMSRA Events Admin"
admin.site.site_title = "UMSRA Events Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Events Portal"
