import import_export
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.models import Product, ProductImage, Category


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 2
    min_num = 0


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'get_in_stock', 'price'
    inlines = [ProductImageStackedInline]

    @admin.action(description='Sotuvda bormi?')
    def get_in_stock(self, obj: Product):
        return obj.in_stock

    get_in_stock.boolean = True


@admin.register(Category)
class CategoryModelAdmin(ImportExportModelAdmin):
    pass
