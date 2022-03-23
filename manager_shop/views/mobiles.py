from django.shortcuts import render, redirect
from manager_shop.forms.mobiles import AddMobile, AddMemory, AddProducer
from manager_shop.models import MobilePhone, Memory, Producer


def mobile_index(request):
    mobiles = MobilePhone.objects.all()
    memories = []
    links = []
    for b in mobiles:
        memories.append(b.str_memories())
        links.append(str(b.id) + '/change')

    return render(request, 'mobile/index.html', {'mobiles': mobiles, 'memories': memories, 'links': links})


def memory_index(request):
    memories = Memory.objects.all()
    links = []
    for a in memories:
        links.append(str(a.id)+'/change')

    return render(request, 'mobile/memory_index.html', {'memories': memories, 'links': links})


def producer_index(request):
    pro = Producer.objects.all()
    links = []
    for a in pro:
        links.append(str(a.id)+'/change')

    return render(request, 'mobile/producer_index.html', {'producers': pro, 'links': links})


def mobile_change(request, id = None):
    o = MobilePhone.objects.get(id=id)
    if request.method == 'POST':
        form = AddMobile(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/mobile')

    form = AddMobile(instance=o)
    return render(request, 'base_form.html', {'form': form})


def change_memory(request, id = None):
    o = Memory.objects.get(id=id)
    if request.method == 'POST':
        form = AddMemory(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/mobile/memory')

    form = AddMemory(instance=o)
    return render(request, 'base_form.html', {'form': form})


def change_producer(request, id = None):
    o = Producer.objects.get(id=id)
    if request.method == 'POST':
        form = AddProducer(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/mobile/producer')

    form = AddProducer(instance=o)
    return render(request, 'base_form.html', {'form': form})


def mobile_add(request):
    if request.method == 'POST':
        form = AddMobile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mobile')

    form = AddMobile()
    return render(request, 'base_form.html', {'form': form})


def add_memory(request):
    if request.method == 'POST':
        form = AddMemory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mobile/memory')

    form = AddMemory()
    return render(request, 'base_form.html', {'form': form})


def add_producer(request):
    if request.method == 'POST':
        form = AddProducer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mobile/producer')

    form = AddProducer()
    return render(request, 'base_form.html', {'form': form})


