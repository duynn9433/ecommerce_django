from django.urls import path

from checkout import views

urlpatterns = [
    path('checkout/', views.index, name='index'),
    path('', views.show_checkout, name='checkout'),
    path('checkout_update/', views.show_checkout_update, name='checkout_update'),
    path('process_order/', views.process_order, name='process_order'),
    # path('show_checkout/', views.show_checkout, name='checkout'),
    path('receipt/', views.receipt, name='checkout_receipt'),
]