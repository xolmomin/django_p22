from django.db.models import Model, CharField, DecimalField, IntegerField, ImageField


class Product(Model):
    title = CharField(max_length=255)
    discount_price = IntegerField(default=0)
    price = IntegerField(default=0)
    image = ImageField(upload_to='products/', default="products/default.jpeg")
