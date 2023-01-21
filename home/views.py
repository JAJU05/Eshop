from django.views.generic import ListView, DetailView, TemplateView

from home.models import Product, Category


class IndexListView(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'index.html'
    context_object_name = 'categories'

class CartView(TemplateView):
    template_name = 'cart.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class DetaillView(TemplateView):
    template_name = 'detail.html'


class ShopView(TemplateView):
    template_name = 'shop.html'
