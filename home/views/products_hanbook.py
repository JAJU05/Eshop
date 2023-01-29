from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, View

from home.models.products_handbook import Cart, Favourite


# class FavouriteListView(LoginRequiredMixin, ListView):
#     template_name = 'favourite.html'
#     queryset = Favourite.objects.all()
#     # context_object_name = 'favourites'
#
#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)


class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    queryset = Cart.objects.annotate(
        real_price=F('product__price') - F('product__price') * F('product__discount') / 100
    )
    context_object_name = 'carts'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        # price - price * discount / 100
        summa = sum(Cart.objects.filter(
            user=self.request.user
        ).annotate(
            real_price=F('product__price') - F('product__price') * F('product__discount') / 100
        ).values_list(
            'real_price', flat=True)
        )
        context['total_price'] = summa
        return context


class CartAddView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            cart.delete()
        return redirect(request.GET.get('url', 'index'))


# class AddFavouriteView(View):
#     def get(self, request, pk, *args, **kwargs):
#         favourite, created = Favourite.objects.get_or_create(user=request.user, product_id=pk)
#         if not created:
#             favourite.delete()
#         return redirect(request.GET.get('url', 'product_list'))


class CheckoutView(TemplateView):
    template_name = 'checkout.html'
