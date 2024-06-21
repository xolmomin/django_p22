from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Origin(models.Model):
    name = models.JSONField(verbose_name="shokir", max_length=100)
    name = models.CharField(verbose_name="shokir", max_length=100)

    def __str__(self):
        return self.name

# entities_entity
class Entity(models.Model):
    class Gender(models.TextChoices):
        GENDER_MALE = 'male', "Male"
        GENDER_FEMALE = 'female', "Female"

    name = models.EmailField(max_length=100)
    alternative_name = models.CharField(
        max_length=100, null=True, blank=True
    )

    category = models.ForeignKey(Category, models.CASCADE)
    origin = models.ForeignKey(Origin, models.CASCADE)
    gender = models.CharField(max_length=100, choices=Gender.choices)
    description = models.TextField()

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