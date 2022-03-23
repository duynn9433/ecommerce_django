from django.shortcuts import render, redirect
from manager_shop.forms.laptops import AddLaptop, AddRAM, AddCPU
from manager_shop.models import Laptop, RAM, CPU


def laptop_index(request):
    list = Laptop.objects.all()
    links = []
    cpus =[]
    rams = []
    for b in list:
        links.append(str(b.id) + '/change')
        cpus.append(b.str_cpu())
        rams.append(b.str_ram())

    return render(request, 'laptop/index.html', {'list': list, 'links': links,'rams':rams,'cpus':cpus})


def ram_index(request):
    list = RAM.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'laptop/ram_index.html', {'list': list, 'links': links})


def cpu_index(request):
    list = CPU.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'laptop/cpu_index.html', {'list': list, 'links': links})


def laptop_add(request):
    if request.method == 'POST':
        form = AddLaptop(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/laptop/')

    form = AddLaptop()
    return render(request, 'base_form.html', {'form': form})


def ram_add(request):
    if request.method == 'POST':
        form = AddRAM(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/laptop/ram/')

    form = AddRAM()
    return render(request, 'base_form.html', {'form': form})


def cpu_add(request):
    if request.method == 'POST':
        form = AddCPU(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/laptop/cpu/')

    form = AddCPU()
    return render(request, 'base_form.html', {'form': form})


def laptop_change(request, id=None):
    o = Laptop.objects.get(id=id)
    if request.method == 'POST':
        form = AddLaptop(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()

            return redirect('/laptop/')

    form = AddLaptop(instance=o)
    return render(request, 'base_form.html', {'form': form})


def cpu_change(request, id=None):
    o = CPU.objects.get(id=id)
    if request.method == 'POST':
        form = AddCPU(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()

            return redirect('/laptop/cpu')

    form = AddCPU(instance=o)
    return render(request, 'base_form.html', {'form': form})


def ram_change(request, id=None):
    o = RAM.objects.get(id=id)
    if request.method == 'POST':
        form = AddRAM(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()

            return redirect('/laptop/ram')

    form = AddRAM(instance=o)
    return render(request, 'base_form.html', {'form': form})

