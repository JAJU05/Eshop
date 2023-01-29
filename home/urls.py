from django.urls import path

from home.views.products_hanbook import CartListView, CartAddView, CheckoutView
from home.views.pruduct import IndexListView, ShopView, CategoryListView, DetailsView
from home.views.templateView import ContactView, AuthView

urlpatterns = [
    # product
    path("", IndexListView.as_view(), name="index"),
    path("category/", CategoryListView.as_view(), name="category"),
    path('detail/<int:pk>/', DetailsView.as_view(), name='detail'),
    path('shop/', ShopView.as_view(), name='shop'),

    # handbook
    path('cart/', CartListView.as_view(), name='cart'),
    path('add-cart/<int:pk>/', CartAddView.as_view(), name='add-cart'),
    # path('favourite', FavouriteListView.as_view(), name='favourite'),
    # path('add-favourite/<int:pk>', AddFavouriteView.as_view(), name='add-favourite'),

    # temlate
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('auth/', AuthView.as_view(), name='auth'),

]
