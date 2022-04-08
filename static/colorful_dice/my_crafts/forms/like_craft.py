from django.shortcuts import redirect

from colorful_dice.my_crafts.models import Craft


def like_craft(request, pk):
    craft_photo = Craft.objects.get(pk=pk)
    craft_photo += 1
    craft_photo.save()
    return redirect('craft_details', pk)

