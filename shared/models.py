from django.db.models import CharField, SlugField, Model, DateTimeField, IntegerField, FloatField
from django.utils.text import slugify


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True


class Base(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
