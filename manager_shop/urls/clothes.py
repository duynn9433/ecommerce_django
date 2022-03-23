from django.urls import path

from manager_shop import views

urlpatterns = [
    path('', views.cloth_index),
    path('vendor/', views.vendor_index),

    path('<int:id>/change', views.cloth_change),
    path('vendor/<int:id>/change', views.vendor_change),

    path('add/', views.cloth_add),
    path('vendor/add/', views.add_vendor),

]