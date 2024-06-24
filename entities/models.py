from django.db import models

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_ckeditor_5.fields import CKEditor5Field


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Origin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Entity(models.Model):
    class Gender(models.TextChoices):
        GENDER_MALE = 'male', "Male"
        GENDER_FEMALE = 'female', "Female"

    name = models.EmailField(max_length=100)
    alternative_name = models.CharField(max_length=100, null=True, blank=True)

    category = models.ForeignKey(Category, models.CASCADE)
    origin = models.ForeignKey(Origin, models.CASCADE)
    gender = models.CharField(max_length=100, choices=Gender.choices)
    description = CKEditor5Field()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Hero(Entity):
    class Meta:
        verbose_name_plural = "Heroes"

    is_immortal = models.BooleanField(default=True)

    benevolence_factor = models.PositiveSmallIntegerField(
        help_text="How benevolent this hero is?"
    )
    arbitrariness_factor = models.PositiveSmallIntegerField(
        help_text="How arbitrary this hero is?"
    )
    # relationships
    father = models.ForeignKey(
        "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )
    mother = models.ForeignKey(
        "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )
    spouse = models.ForeignKey(
        "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )


class Villain(Entity):
    is_immortal = models.BooleanField(default=False)

    malevolence_factor = models.PositiveSmallIntegerField(
        help_text="How malevolent this villain is?"
    )
    power_factor = models.PositiveSmallIntegerField(
        help_text="How powerful this villain is?"
    )
    is_unique = models.BooleanField(default=True)
    count = models.PositiveSmallIntegerField(default=1)
