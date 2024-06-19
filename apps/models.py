from colorfield.fields import ColorField
from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField, DateTimeField, IntegerField, \
    PositiveIntegerField, BooleanField, TextChoices
from django.utils.timezone import now


class BaseStrModel(Model):

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Field(BaseStrModel):
    name = CharField(max_length=255)
    background_color = ColorField(default='#FF0000')
    color = ColorField(default='#FF0000')


class Job(BaseStrModel):
    name = CharField(max_length=255)


class Company(BaseStrModel):
    name = CharField(max_length=255)


class Country(BaseStrModel):
    name = CharField(max_length=255)


class City(BaseStrModel):
    name = CharField(max_length=255)
    country = ForeignKey('apps.Country', CASCADE)


class Employee(Model):
    class WorkingType(TextChoices):
        PART_TIME = 'part-time', 'Part time'
        FULL_TIME = 'full-time', 'Full time'

    working_type = CharField(max_length=25, choices=WorkingType.choices)
    image = ImageField(upload_to='employees/')
    joined_at = DateTimeField(auto_now_add=True)
    salary = PositiveIntegerField(default=0)
    has_star = BooleanField(default=False)
    city = ForeignKey('apps.City', CASCADE)
    job = ForeignKey('apps.Job', CASCADE)
    field = ForeignKey('apps.Field', CASCADE)
    company = ForeignKey('apps.Company', CASCADE)

    def __str__(self):
        return str(self.id)

    @property
    def days_ago(self):
        return now().day - self.joined_at.day