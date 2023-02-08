from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = EmailField(max_length=20, unique=True)
    phone = CharField(max_length=25, null=True, blank=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'Users'

    def save(self, *args, **kwargs):
        if self.username is None or self.username == '':
            self.username = f'User000{self.__class__.objects.count()}'
        super().save(*args, **kwargs)

    @property
    def total_price_of_all_products(self):
        total_price = sum(item.total_price_of_products for item in self.cart_set.all())
        return total_price
