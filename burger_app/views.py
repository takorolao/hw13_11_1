from django.shortcuts import render
from .models import Burger, Ingredient

def burger_list(request):
    burgers = Burger.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'burger_app/burger_list.html', {'burgers': burgers, 'ingredients': ingredients})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'burger_app/ingredient_list.html', {'ingredients': ingredients})