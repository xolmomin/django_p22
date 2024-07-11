from datetime import timedelta

from django.db.models import Model, CharField, IntegerField, ImageField, PositiveSmallIntegerField, DateTimeField, \
    ForeignKey, CASCADE, CheckConstraint, Q, TextChoices, ManyToManyField
from django.utils.timezone import now
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.models.base import SlugBaseModel, CreatedBaseModel


class Category(SlugBaseModel, MPTTModel):
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(SlugBaseModel):
    pass


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()
    discount_percent = PositiveSmallIntegerField(default=0, db_default=0)
    quantity = PositiveSmallIntegerField(default=0, db_default=0)
    tags = ManyToManyField('apps.Tag', blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(discount_percent__lte=100),
                name="discount_percent__lte__100",
            )
        ]

    @property
    def is_new(self) -> bool:
        return self.created_at >= now() - timedelta(days=7)

    @property
    def in_stock(self) -> bool:
        return self.quantity > 0

    @property
    def current_price(self):
        return self.price - self.price * self.discount_percent // 100


class ProductImage(Model):
    image = ImageField(upload_to='products/%Y/%m/%d/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')


class Order(CreatedBaseModel):
    class PaymentMethod(TextChoices):
        PAYPAL = 'paypal', 'Paypal'
        CREDIT_CARD = 'credit_card', 'Credit Card'

    payment_method = CharField(max_length=25, choices=PaymentMethod.choices)
    address = ForeignKey('apps.Address', CASCADE)
    owner = ForeignKey('apps.User', CASCADE)


class OrderItem(Model):
    product = ForeignKey('apps.Product', CASCADE)
    order = ForeignKey('apps.Order', CASCADE, related_name='items')
    quantity = PositiveSmallIntegerField(default=1, db_default=1)
