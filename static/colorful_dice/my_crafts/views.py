from django.shortcuts import render, redirect

# Create your views here.
from colorful_dice.my_crafts.models import Craft


def show_home(request):
    return render(request, 'home_page.html')


def show_profile(request):
    return render(request, 'profile_page.html')


def create_profile(request):
    return render(request, 'create_profile.html')


def show_craft_details(request, pk):
    return render(request, 'craft_details.html')


def show_wire_page(request):
    return render(request, 'wire_page.html')


def show_crochet_page(request):
    return render(request, 'crochet_page.html')


def show_origami_page(request):
    return render(request, 'origami_page.html')


def show_decoupage_page(request):
    return render(request, 'decoupage_page.html')


def like_craft(request, pk):
    craft_photo = Craft.objects.get(pk=pk)
    craft_photo += 1
    craft_photo.save()
    return redirect('craft_details', pk)
