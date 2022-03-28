from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product


def index(request):
    template_name = "catalog/index.html"
    """ site home page """
    page_title = 'Modern Musician | Musical Instruments and Sheet Music for Musicians'
    return render(request, template_name, locals())


def show_category(request, category_slug):
    template_name = "catalog/category.html"
    """ view for each individual category page """
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, template_name, locals())


def show_product(request, product_slug):
    template_name = "catalog/product.html"
    """ view for each product page """
    p = get_object_or_404(Product, slug=product_slug)

    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(request, template_name, locals())
