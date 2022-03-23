from django.urls import path

from manager_shop import views

urlpatterns = [
    path('', views.shoe_index),
    path('brand/', views.brand_index),

    path('<int:id>/change', views.shoe_change),
    path('brand/<int:id>/change', views.brand_change),

    path('add/', views.shoe_add),
    path('brand/add/', views.add_brand),

]