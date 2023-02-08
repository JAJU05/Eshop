from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, View

from home.models import Category
from home.models.products_handbook import Cart, Favourite


class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    queryset = Cart.objects.annotate(
        real_price=F('product__price') - F('product__price') * F('product__sale') / 100
    )
    context_object_name = 'carts'


class CartAddView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            cart.delete()
        return redirect(request.GET.get('url', 'index'))


class FavouriteListView(LoginRequiredMixin, ListView):
    model = Favourite
    template_name = 'favourite.html'
    queryset = Favourite.objects.all()
    context_object_name = 'favourites'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class AddFavouriteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        favourite, created = Favourite.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            favourite.delete()
        return redirect(request.GET.get('url', 'index'))


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class CartDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        cart = Cart.objects.filter(id=pk)
        if cart.exists():
            cart.delete()
        return redirect(request.GET.get('url', 'cart'))
