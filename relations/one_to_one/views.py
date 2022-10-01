from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Place, Restaurant

# Create your views h
# ere.
def create(request):
    place = Place(name="Baeza", adress="Calle Libertad")
    place.save()

    restaurant = Restaurant(place=place, employees=5)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
