from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request, template_name="registration/register.html"):
    # if request.method == 'POST':
    #     postdata = request.POST.copy()
    #     form = UserCreationForm(postdata)
    #     if form.is_valid():
    #         form.save()
    #         un = postdata.get('username', '')
    #         pw = postdata.get('password1', '')
    #         from django.contrib.auth import login, authenticate
    #         new_user = authenticate(username=un, password=pw)
    #         if new_user and new_user.is_active:
    #             login(request, new_user)
    #             url = reverse('my_account')
    #             return HttpResponseRedirect(url)
    # else:
    #     form = UserCreationForm()
    # page_title = 'User Registration'
    return render(request, template_name, locals())


def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    return render(request, template_name, locals())


def order_details(request, template_name="registration/order_details.html"):
    page_title = 'Order Details'
    return render(request, template_name, locals())


def order_info(request, template_name="registration/order_info.html"):
    page_title = 'Order Information'
    return render(request, template_name, locals())
