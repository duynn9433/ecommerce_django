from django.shortcuts import render, redirect
from manager_shop.forms.clothes import AddCloth, AddVendor
from manager_shop.models import Cloth, Vendor


def cloth_index(request):
    list = Cloth.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'cloth/index.html', {'list': list, 'links': links})


def vendor_index(request):
    list = Vendor.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'cloth/vendor_index.html', {'list': list, 'links': links})


def cloth_change(request, id=None):
    o = Cloth.objects.get(id=id)
    if request.method == 'POST':
        form = AddCloth(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/cloth')

    form = AddCloth(instance=o)
    return render(request, 'base_form.html', {'form': form})


def vendor_change(request, id=None):
    o = Vendor.objects.get(id=id)
    if request.method == 'POST':
        form = AddVendor(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/cloth/vendor')

    form = AddCloth(instance=o)
    return render(request, 'base_form.html', {'form': form})


def cloth_add(request):
    if request.method == 'POST':
        form = AddCloth(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cloth')

    form = AddCloth()
    return render(request, 'base_form.html', {'form': form})


def add_vendor(request):
    if request.method == 'POST':
        form = AddVendor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cloth/vendor')

    form = AddVendor()
    return render(request, 'base_form.html', {'form': form})

