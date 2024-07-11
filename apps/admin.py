import import_export
from django.contrib import admin
from django.db.models import F
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Product, ProductImage, Category


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 2
    min_num = 0


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'get_in_stock', 'price'
    inlines = [ProductImageStackedInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            # kwargs["queryset"] = Category.objects.filter(children__isnull=True)
            kwargs["queryset"] = Category.objects.filter(lft=F('rght') - 1)
            # kwargs["queryset"] = Category.objects.filter(rght=F('lft') + 1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @admin.action(description='Sotuvda bormi?')
    def get_in_stock(self, obj: Product):
        return obj.in_stock

    get_in_stock.boolean = True


@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin, ImportExportModelAdmin):
    pass
