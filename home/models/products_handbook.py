from django.db.models import Model, CharField, DateTimeField, SlugField


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
