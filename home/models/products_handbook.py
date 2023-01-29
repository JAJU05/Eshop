from django.db.models import Model, CharField, SlugField, ForeignKey, CASCADE, IntegerField, EmailField


class Cart(Model):
    product = ForeignKey('home.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE)
    count = IntegerField(default=1)

    def __str__(self):
        return self.user, self.count

    @property
    def total_price_of_products(self):
        return self.product.total_price * self.count

    class Meta:
        db_table = 'basket'


class Order(Model):
    first_name = CharField(max_length=255, unique=True)
    last_name = CharField(max_length=255, unique=True)
    email = EmailField(max_length=20)
    address_1 = CharField(max_length=255, unique=True)
    address_2 = CharField(max_length=255)
    state = CharField(max_length=255)
    phone = CharField(max_length=15, unique=True)
    zipcode = CharField(max_length=8)
    country = ForeignKey('Country', CASCADE)


class Country(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)


class Favourite(Model):
    user = ForeignKey('users.User', on_delete=CASCADE)
    product = ForeignKey('home.Product', CASCADE)

    class Meta:
        db_table = 'favourite'
