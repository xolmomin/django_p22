from django.contrib.admin import ModelAdmin, register, action

from apps.models import Field, Job, Company, Country, City, Employee


@register(Field)
class FieldModelAdmin(ModelAdmin):
    pass


@register(Employee)
class EmployeeModelAdmin(ModelAdmin):
    list_display = ['id', 'city', 'get_country']

    @action(description='Country')
    def get_country(self, obj: Employee):
        return obj.city.country


@register(Company)
class CompanyModelAdmin(ModelAdmin):
    pass


@register(Job)
class JobModelAdmin(ModelAdmin):
    pass


@register(Country)
class CountryModelAdmin(ModelAdmin):
    pass


@register(City)
class CityModelAdmin(ModelAdmin):
    list_display = ['id', 'name', 'country']
