from django.urls import path

from home.views.products_hanbook import CartListView, CartAddView, FavouriteListView, AddFavouriteView, CheckoutView, \
    CartDeleteView
from home.views.pruduct import IndexListView, ShopListView, CategoryListView, DetailsView
from home.views.templateView import ContactView, AuthView

urlpatterns = [
    # product
    path("", IndexListView.as_view(), name="index"),
    path("category/", CategoryListView.as_view(), name="category"),
    path('detail/<int:pk>/', DetailsView.as_view(), name='detail'),
    path('shop/', ShopListView.as_view(), name='shop'),

    # cart
    path('cart/', CartListView.as_view(), name='cart'),
    path('add-cart/<int:pk>/', CartAddView.as_view(), name='add-cart'),
    path('delete-cart/<int:pk>', CartDeleteView.as_view(), name='delete-cart'),

    # favourite
    path('favourite', FavouriteListView.as_view(), name='favourite'),
    path('add-favourite/<int:pk>', AddFavouriteView.as_view(), name='add-favourite'),

    # temlate
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('auth/', AuthView.as_view(), name='auth'),

]
