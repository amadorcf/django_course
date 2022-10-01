from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry


# Create your views here.
def queries(request):
    # Obtener todos los elementos
    all_authors = Author.objects.all()

    # Obtener datos filtrados por condicion
    filtered = Author.objects.filter(email="eddie59@example.net")

    # Obtener un unico objeto (filtrado)
    author = Author.objects.get(id=1)

    # Obtener los 10 primero elementos
    limits = Author.objects.all()[:10]

    # Obtener todos los elementos
    orders = Author.objects.all().order_by('email')

    # https://docs.djangoproject.com/en/4.1/topics/db/queries/
    # Obtener elementos cuyo id sea menor a 15
    filtered2 = Author.objects.filter(id__lte=15) # IMPORTANTE!!  >= es __gte, contiene es __contains

    # Obtener elementos cuyo id sea menor a 15
    filtered3 = Author.objects.filter(name__contains="yes")

    return render(request, 'post/queries.html', {'authors': all_authors,
                                                 'filtered': filtered,
                                                 'author': author,
                                                 'limits': limits,
                                                 'orders': orders,
                                                 'filtered2': filtered2,
                                                 'filtered3': filtered3}
                  )

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Finidi"
    author.email = "fin@gmail.com"
    author.save()
    return HttpResponse("Dato modificado")