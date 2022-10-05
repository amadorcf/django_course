from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm


def index(request):
    if request.method == 'POST':
        # Guardar la informacion
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
    else:
        form = ProductForm()
        return render(request, 'index.html', {'form': form})

