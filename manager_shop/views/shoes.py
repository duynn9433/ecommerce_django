from django.shortcuts import render, redirect
from manager_shop.forms.shoes import AddShoe, AddBrand
from manager_shop.models import Shoe, Brand


def shoe_index(request):
    list = Shoe.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'shoe/index.html', {'list': list, 'links': links})


def brand_index(request):
    list = Brand.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'shoe/brand_index.html', {'list': list, 'links': links})


def shoe_change(request, id=None):
    o = Shoe.objects.get(id=id)
    if request.method == 'POST':
        form = AddShoe(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/shoe')

    form = AddShoe(instance=o)
    return render(request, 'base_form.html', {'form': form})


def brand_change(request, id=None):
    o = Brand.objects.get(id=id)
    if request.method == 'POST':
        form = AddBrand(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/shoe/brand')

    form = AddBrand(instance=o)
    return render(request, 'base_form.html', {'form': form})


def shoe_add(request):
    if request.method == 'POST':
        form = AddShoe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shoe')

    form = AddShoe()
    return render(request, 'base_form.html', {'form': form})


def add_brand(request):
    if request.method == 'POST':
        form = AddBrand(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shoe/brand')

    form = AddBrand()
    return render(request, 'base_form.html', {'form': form})

