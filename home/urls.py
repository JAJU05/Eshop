from django.urls import path

from home.views import IndexListView, DetaillView, ShopView, CartView, CheckoutView, ContactView, CategoryListView

urlpatterns = [

    path("", IndexListView.as_view(), name="index"),
    path("category", CategoryListView.as_view(), name="category"),
    path('cart', CartView.as_view(), name='cart'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('contact', ContactView.as_view(), name='contact'),
    path('detail', DetaillView.as_view(), name='detail'),
    path('shop', ShopView.as_view(), name='shop'),

    ]

