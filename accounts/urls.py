import django.contrib.auth.views
from django.urls import path

from accounts import views
from ecommerce_django import settings

urlpatterns = [
    path('register/', views.register, {'template_name': 'registration/register.html', 'SSL': settings.ENABLE_SSL}, name='register'),
    path('my_account/', views.my_account, {'template_name': 'registration/my_account.html'}, name='my_account'),
    path('order_details/', views.order_details, {'template_name': 'registration/order_detail.html'}, name='order_details'),
    path('order_info/', views.order_info, {'template_name': 'registration/order_info.html'}, name='order_info'),
    path('login/', django.contrib.auth.views.LoginView.as_view(template_name='registration/login.html'), {'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL}, name='login'),
    # path('logout/', django.contrib.auth.views.logout_then_login, name='logout'),

]
