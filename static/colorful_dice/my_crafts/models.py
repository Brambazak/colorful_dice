from random import choices

from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Craft(models.Model):
    CRAFT_NAME_MIN_LEN = 2
    CRAFT_NAME_MAX_LEN = 100
    CATEGORY = (
        ('Wire', 'Wire'),
        ('Origami', 'Origami'),
        ('Crochet', 'Crochet'),
        ('Decoupage', 'Decoupage'),
        ('Others', 'Others'),
    )
    craft_name = models.CharField(
        max_length=CRAFT_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(CRAFT_NAME_MIN_LEN),
        )
    )
    craft_category = models.CharField(
        max_length=1000,
        choices=CATEGORY,
    )

    craft_image = models.ImageField()

    # likes =
    # comments =


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
    )

    category_craft = models.ForeignKey(
        Craft,
        on_delete=models.CASCADE,
    )


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
        )
    )


class Register(models.Model):
    first_name = Profile.first_name
    last_name = Profile.last_name
    profile_name = models.CharField(max_length=10,)
    profile_password = models.CharField(max_length=20)


class Login(models.Model):
    name = Register.profile_name
    password = Register.profile_password
