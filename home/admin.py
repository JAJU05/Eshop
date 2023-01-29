from django.contrib import admin
from home.models import Product, Category
from home.models.products_handbook import Cart

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
