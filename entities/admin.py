from django.contrib import admin
from django.db.models import Count

from entities.models import Origin, Hero


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


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
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
