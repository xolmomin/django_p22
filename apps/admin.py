from django.contrib import admin

from apps.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass
