from django.views.generic import ListView, DetailView

from home.models import Product, Category


class IndexListView(ListView):
    queryset = Product.objects.order_by('-created_at')[:8]
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 9


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'base.html'
    context_object_name = 'categories'


class DetailsView(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'


class ShopListView(ListView):
    queryset = Product.objects.all()
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        # search products
        name = self.request.GET.get('name__icontains', None)
        object_list = super(ShopListView, self).get_queryset()
        if name and name != '':
            object_list = object_list.filter(name__icontains=name)
        return object_list
