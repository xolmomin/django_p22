from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from events.admin import event_admin_site
from root import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('event-admin/', event_admin_site.urls),
                  path('', include('events.urls')),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "UMSRA Events Admin"
admin.site.site_title = "UMSRA Events Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Events Portal"
