from django.urls import path

from manager_shop import views

urlpatterns = [
    path('', views.mobile_index),
    path('memory/', views.memory_index),
    path('producer/', views.producer_index),

    path('<int:id>/change', views.mobile_change),
    path('memory/<int:id>/change', views.change_memory),
    path('producer/<int:id>/change', views.change_producer),

    path('add/', views.mobile_add),
    path('memory/add/', views.add_memory),
    path('producer/add/', views.add_producer),

]
