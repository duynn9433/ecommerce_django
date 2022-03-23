from django.urls import path

from manager_shop import views

urlpatterns =[
    path('', views.laptop_index),
    path('ram/', views.ram_index),
    path('cpu/', views.cpu_index),

    path('add/', views.laptop_add),
    path('ram/add/', views.ram_add),
    path('cpu/add/', views.cpu_add),

    path('<int:id>/change', views.laptop_change),
    path('ram/<int:id>/change', views.ram_change),
    path('cpu/<int:id>/change', views.cpu_change),
]