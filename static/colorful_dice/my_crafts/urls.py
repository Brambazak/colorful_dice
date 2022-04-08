from django.urls import path

from colorful_dice.my_crafts.views import show_home, show_profile, create_profile, show_craft_details, show_wire_page, \
    show_crochet_page, show_origami_page, show_decoupage_page

urlpatterns = (
    path('', show_home, name='home'),
    path('', show_profile, name='profile'),
    path('', create_profile, name='create profile'),

    path('crafts/craft/<int:pk>/', show_craft_details, name='craft details'),
    path('crafts/wire/<int:pk>/', show_wire_page, name='wire'),
    path('crafts/crochet/<int:pk>/', show_crochet_page, name='crochet'),
    path('crafts/origami/<int:pk>/', show_origami_page, name='origami'),
    path('crafts/decoupage/<int:pk>/', show_decoupage_page, name='decoupage'),

)
