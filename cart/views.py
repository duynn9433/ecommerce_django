from django.shortcuts import render
from cart import cart


def show_cart(request):
    template_name = "cart/cart.html"
    cart_item_count = cart.cart_distinct_item_count(request)
    # cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    return render(request, template_name, locals())
    # return render(request, template_name, locals(), context_instance=RequestContext(request))

