from django.db.models import DecimalField, TextField, ImageField, PositiveSmallIntegerField, \
    ForeignKey, CASCADE

from shared.models import SlugBaseModel, Base


class Product(SlugBaseModel,Base):
    description = TextField(null=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    image = ImageField(upload_to='products/')
    discount = PositiveSmallIntegerField(default=0)
    category = ForeignKey('home.Category', CASCADE)

    def __str__(self):
        return self.name




