from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns=[
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base_bt2.html')),
    path('book/', include('manager_shop.urls.books_urls')),
    path('cloth/', include('manager_shop.urls.clothes')),

    path('mobile/', include('manager_shop.urls.mobiles')),
    path('shoe/', include('manager_shop.urls.shoes')),
    path('electronic/', include('manager_shop.urls.electronics')),
    path('laptop/', include('manager_shop.urls.laptops')),
]