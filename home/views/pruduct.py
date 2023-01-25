from django.views.generic import ListView, TemplateView

from home.models import Product, Category


class IndexListView(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'index.html'
    context_object_name = 'categories'


class DetailsView(TemplateView):
    template_name = 'detail.html'