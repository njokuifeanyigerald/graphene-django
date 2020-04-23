from django.shortcuts import render
from .models import Category, Ingredient
from django.http import JsonResponse
from .serializer import Ingredientserializer
# from django.views.generic import View

def home(req):
    info = Ingredient.objects.all()
    serializer = Ingredientserializer(info, many=True)  
    return JsonResponse(serializer.data, safe=False)