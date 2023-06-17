# from django.shortcuts import render
# from products.models import *
# from accounts.models import Cart, CartItems
# from django.http import HttpResponseRedirect, HttpResponse
# import razorpay
# from django.conf import settings

# def add_to_cart(request, uid):
#     product = Product.objects.get(uid = uid) 
#     user = request.user
#     cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
#     cart_item = CartItems.objects.create(cart=cart, product=product)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def cart(request):

#     cart_items = CartItems.objects.all()
#     price=[1]
#     for cart_item in cart_items:
#         price.append(cart_item.product.price)

#     total = sum(price)

#     cart_obj = None
#     try:
#         cart_obj = Cart.objects.get(is_paid=False, user=request.user)
#     except Exception as e:
#         print(e)

#     if cart_obj:
#         client = razorpay.Client(auth = (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
#         payment = client.order.create({'amount': total*100, 'currency': 'INR', 'payment_capture': 1})
#         cart_obj.razor_pay_order_id = payment['id']
#         cart_obj.save()

#     else:
#         payment = None

#     context = {'cart_items': cart_items, 'total': total, 'payment': payment}
#     return render(request, 'accounts/cart.html', context)

# def remove_cart(request, cart_item_uid):
#     cart_item = CartItems.objects.get(uid=cart_item_uid)
#     cart_item.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def success(request):
#     order_id = request.GET.get('order_id')
#     cart = Cart.objects.get(razor_pay_order_id = order_id)
#     cart.is_paid = True
#     cart.save()
#     CartItems.objects.filter(cart=cart).delete()
#     new_cart = Cart.objects.create(user=request.user)
#     new_cart.save()
#     return HttpResponse('Payment Success')

from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import Cart, CartItems
from django.http import HttpResponseRedirect
import razorpay
from django.conf import settings
from django.contrib import messages

def add_to_cart(request, uid):
    product = get_object_or_404(Product, uid=uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item = CartItems.objects.create(cart=cart, product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart(request):

    cart_obj = get_object_or_404(Cart, is_paid=False, user=request.user)
    cart_items = cart_obj.cart_items.select_related('product').all()

    prices = [cart_item.product.price for cart_item in cart_items]
    prices.append(1)
    total = sum(prices)

    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    payment = client.order.create({'amount': total * 100, 'currency': 'INR', 'payment_capture': 1})
    cart_obj.razor_pay_order_id = payment['id']
    cart_obj.save()

    context = {'cart_items': cart_items, 'total': total, 'payment': payment}
    return render(request, 'accounts/cart.html', context)

def remove_cart(request, cart_item_uid):
    cart_item = get_object_or_404(CartItems, uid=cart_item_uid)
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def success(request):
    order_id = request.GET.get('order_id')
    cart = get_object_or_404(Cart, razor_pay_order_id=order_id)
    cart.is_paid = True
    cart.save()
    CartItems.objects.filter(cart=cart).delete()
    new_cart = Cart.objects.create(user=request.user)
    new_cart.save()
    messages.success(request, 'Order has been placed successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

