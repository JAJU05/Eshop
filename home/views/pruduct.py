from django.views.generic import ListView, TemplateView, DetailView

from home.models import Product, Category


class IndexListView(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'index.html'
    context_object_name = 'categories'


class DetailsView(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'


class ShopView(TemplateView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'product'

