from django.views.generic import ListView, DetailView

from home.models.products import Product


class IndexListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
