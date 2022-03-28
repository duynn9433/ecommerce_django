import patterns as patterns
from django.urls import re_path, path

import catalog

# urlpatterns = patterns('catalog.views',
#     (r'^$','index', {'template_name': 'catalog/index.html'}, 'catalog_home'),
#     (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
#        {'template_name': 'catalog/category.html'}, 'catalog_category'),
#     (r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',
#        {'template_name': 'catalog/product.html'}, 'catalog_product'),
#     (r'^tag_cloud/$', 'tag_cloud',
#        {'template_name': 'catalog/tag_cloud.html'}, 'tag_cloud'),
#     (r'^tag/(?P<tag>[-\w]+)/$', 'tag',
#        {'template_name': 'catalog/tag.html'}, 'tag'),
#     (r'^review/product/add/$', 'add_review', {}, 'add_product_review'),
#     (r'^tag/product/add/$', 'add_tag'),
# )
from catalog import views

urlpatterns =[
    path('', views.index, name='catalog_home'),
    # re_path(r'^category/(?P<category_slug>[-\w]+)/$',
    #         views.show_category({'template_name': 'catalog/category.html'}), name='catalog_category'),
    # re_path(r'^product/(?P<product_slug>[-\w]+)/$',
    #         views.show_product({'template_name': 'catalog/product.html'}), name='catalog_product'),
    path('category/<slug:category_slug>/', views.show_category, name='catalog_category'),
    path('product/<slug:product_slug>/', views.show_product, name='catalog_product'),

]
