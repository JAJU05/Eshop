from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import DecimalField, TextField, ImageField, ForeignKey, CASCADE, IntegerField, \
    TextChoices, CharField

from shared import ChoiceArrayField
from shared.models import SlugBaseModel, Base


class Category(SlugBaseModel):

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Categories"


class Product(SlugBaseModel, Base):
    class SizesChoices(TextChoices):
        XS = 'XS', 'XS'
        S = 'S', 'S'
        M = 'M', 'M'
        L = 'L', 'L'
        XL = 'XL', 'XL'

    class ColorsChoices(TextChoices):
        Black = 'Black', 'Black'
        White = 'White', 'White'
        Red = 'Red', 'Red'
        Blue = 'Blue', 'Blue'
        Green = 'Green', 'Green'
        Yellow = 'Yellow', 'Yellow'

    description = TextField(null=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    image = ImageField(upload_to='products/default-image/')
    size = ChoiceArrayField(CharField(max_length=20, choices=SizesChoices.choices, default=list))
    colors = ChoiceArrayField(CharField(max_length=20, choices=ColorsChoices.choices, default=list))
    category = ForeignKey('home.Category', CASCADE)
    sale = IntegerField(default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if self.sale > 0:
            return self.price - self.price * self.sale / 100
        return self.price

    class Meta:
        ordering = ('-created_at',)
        db_table = 'product'
