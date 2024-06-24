import csv
import io

from django.contrib import admin
from django.db.models import Count
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from mptt.admin import DraggableMPTTAdmin

from entities.models import Origin, Hero, Category


class ExportCsvMixin:

    @admin.action(description='Export Selected')
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]

    # def get_queryset(self, request):
    #     return super().get_queryset(request).filter(parent__isnull=True)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count=Count("hero", distinct=True),
            _villain_count=Count("villain", distinct=True),
        )
        return queryset

    @admin.action(description='botirjon')
    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count

    @admin.action(description='123')
    def get_name(self, obj):
        return obj.name

    list_display = ("get_name", "hero_count", "villain_count")

    hero_count.admin_order_field = '_hero_count'
    villain_count.admin_order_field = '_villain_count'


class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = 'is_very_benevolent'
    parameter_name = 'is_very_benevolent'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(benevolence_factor__gt=75)
        elif value == 'No':
            return queryset.filter(benevolence_factor__lte=75)
        return queryset


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/heroes_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":

            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8") as text_file:
                reader = csv.DictReader(text_file)
                heros_list = []
                for row in reader:
                    heros_list.append(Hero(**row))
                Hero.objects.bulk_create(heros_list)

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        context = {"form": form}
        return render(request, "admin/csv_form.html", context)

    list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)

    def is_very_benevolent(self, obj):
        return obj.benevolence_factor > 75

    is_very_benevolent.boolean = True

    actions = ["mark_immortal_false", "mark_immortal_true"]

    def mark_immortal_false(self, request, queryset):
        queryset.update(is_immortal=False)

    def mark_immortal_true(self, request, queryset):
        queryset.update(is_immortal=True)
