from django.urls import path
from accounts.views import add_to_cart, cart, remove_cart, success

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('add-to-cart/<uid>/', add_to_cart, name="add_to_cart"),
    path('remove-cart/<cart_item_uid>/', remove_cart, name="remove_cart"),
    path('success/', success, name="success")
]

