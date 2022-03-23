from django.urls import path

from manager_shop import views

urlpatterns = [
    path('', views.book_index),
    path('author/', views.author_index),
    path('publisher/', views.publisher_index),

    path('<int:id>/change', views.book_change),
    path('author/<int:id>/change', views.change_author),
    path('publisher/<int:id>/change', views.change_publisher),

    path('add/', views.book_add),
    path('author/add/', views.add_author),
    path('publisher/add/', views.add_publisher),

]