from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, PositiveSmallIntegerField, ForeignKey, CASCADE, DateField, OneToOneField, \
    PositiveIntegerField

from apps.models.base import CreatedBaseModel


class User(AbstractUser):
    pass


class CreditCard(CreatedBaseModel):
    order = OneToOneField('apps.Order', CASCADE)
    number = CharField(max_length=16)
    cvv = CharField(max_length=3)
    expire_date = DateField()


class SiteSettings(Model):
    tax = PositiveSmallIntegerField()


class Address(CreatedBaseModel):
    full_name = CharField(max_length=255)
    street = CharField(max_length=255)
    zip_code = PositiveIntegerField()
    city = CharField(max_length=255)
    phone = CharField(max_length=255)
    user = ForeignKey('apps.User', CASCADE, related_name='addresses')
