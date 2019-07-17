from django.shortcuts import render, redirect
from .models import Pets
from .forms	import PetForm

# Create your views here.

def pet_list(request):
    context = {
        "petlist":Pets.objects.filter(available=True)
    }
    return render(request, 'list.html', context)


def pet_detail(request, pet_id):
    context = {
        "pets": Pets.objects.get(id=pet_id)
    }
    return render(request, 'detail.html', context)

def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pet_update(request, pet_id):
    pet_obj = Pets.objects.get(id=pet_id)
    form = RestaurantForm(instance=pet_obj)
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            return redirect('pet-detail')
    context = {
        "pet_obj": pet_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def pet_delete(request, pet_id):
    pet_obj = Pets.objects.get(id=pet_id)
    pet_obj.delete()
    return redirect('petlist')