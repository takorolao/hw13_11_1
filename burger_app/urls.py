from django.urls import path
from . import views

urlpatterns = [
    path('burgers/', views.burger_list, name='burger_list'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
]
