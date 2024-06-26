from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.urls')),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
100ta
13:30 - 14:30
acm.tuit.uz
algo.ubtuit.uz
acmp.ru
timus
binarysearch
codeforces

'''
