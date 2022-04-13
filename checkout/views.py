import json
import profile

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from cart import cart
from checkout.forms import CheckoutForm
from checkout.models import Order, OrderItem
from accounts import profile


def index(request):
    return render(request, 'checkout/index.html')


def show_checkout_update(request):
    template_name = 'checkout/checkout_update.html'
    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
    return render(request, template_name, locals())


def show_checkout(request):
    template_name = 'checkout/checkout.html'
    """ checkout form page to collect user shipping and billing information """
    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            pass

            # response = checkout.process(request)
            # order_number = response.get('order_number', 0)
            # error_message = response.get('message', '')
            # if order_number:
            #     request.session['order_number'] = order_number
            #     receipt_url = reverse('checkout_receipt')
            #     return HttpResponseRedirect(receipt_url)
        else:
            error_message = u'Correct the errors below'
    else:
        if request.user.is_authenticated():
            user_profile = profile.retrieve(request)
            form = CheckoutForm(instance=user_profile)
        else:
            form = CheckoutForm()
    page_title = 'Checkout'
    return render(request, template_name, locals())


def receipt(request):
    template_name = 'checkout/receipt.html'
    """ page displayed with order information after an order has been placed successfully """
    order_number = request.session.get('order_number', '')
    transaction_id = request.session.get('transaction_id', '')
    if order_number:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
    else:
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    return render(request, template_name, locals())


def process_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        order = Order()
        order.shipping_name = data['order']['shipping_name']
        order.shipping_address_1 = data['order']['shipping_address_1']
        order.shipping_address_2 = data['order']['shipping_address_2']
        order.shipping_city = data['order']['shipping_city']
        order.shipping_state = data['order']['shipping_state']
        order.shipping_zip = data['order']['shipping_zip']
        order.shipping_country = data['order']['shipping_country']
        order.phone = data['order']['phone']
        order.email = data['order']['email']

        order.transaction_id = data['order']['transaction_id']
        order.ip_address = data['order']['ip']

        order.user = None

        # if request.user.is_authenticated():
        #     order.user = request.user

        order.status = Order.SUBMITTED
        order.save()
        request.session['order_number'] = order.id
        request.session['transaction_id'] = order.transaction_id

        if order.pk:
            """ if the order save succeeded """
            cart_items = cart.get_cart_items(request)
            for ci in cart_items:
                """ create order item for each cart item """
                oi = OrderItem()
                oi.order = order
                oi.quantity = ci.quantity
                oi.price = ci.product.price  # now using @property
                oi.product = ci.product
                oi.save()
            # all set, clear the cart
            cart.empty_cart(request)

            # save profile info for future orders
            # if request.user.is_authenticated():
            #     profile.set(request)

        return JsonResponse('Payment submitted..', safe=False)

