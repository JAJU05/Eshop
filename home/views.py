from django.views.generic import TemplateView



class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ShopView(TemplateView):
    template_name = 'shop.html'
