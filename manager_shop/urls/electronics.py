from django.urls import path
from manager_shop import views

urlpatterns = [
    path('', views.electronic_index),
    path('size/', views.size_index),

    path('<int:id>/change', views.electronic_change),
    path('size/<int:id>/change', views.size_change),

    path('add/', views.electronic_add),
    path('size/add/', views.add_size),

]