from django.shortcuts import render, redirect
from manager_shop.models.electronics import Electronic, Size
from manager_shop.forms.electronics import AddElectronic, AddSize


def electronic_index(request):
    list = Electronic.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'electronic/index.html', {'list': list, 'links': links})


def size_index(request):
    list = Size.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'electronic/size_index.html', {'list': list, 'links': links})


def electronic_change(request, id=None):
    o = Electronic.objects.get(id=id)
    if request.method == 'POST':
        form = AddElectronic(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/electronic')

    form = AddElectronic(instance=o)
    return render(request, 'base_form.html', {'form': form})


def size_change(request, id=None):
    o = Size.objects.get(id=id)
    if request.method == 'POST':
        form = AddSize(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/electronic/size')

    form = AddSize(instance=o)
    return render(request, 'base_form.html', {'form': form})


def electronic_add(request):
    if request.method == 'POST':
        form = AddElectronic(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/electronic')

    form = AddElectronic()
    return render(request, 'base_form.html', {'form': form})


def add_size(request):
    if request.method == 'POST':
        form = AddSize(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/electronic/size')

    form = AddSize()
    return render(request, 'base_form.html', {'form': form})

