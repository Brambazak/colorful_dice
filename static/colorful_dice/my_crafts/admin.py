from django.contrib import admin

# Register your models here.
from colorful_dice.my_crafts.models import Craft, Category, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

