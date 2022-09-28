from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {})


def dinamico(request, name):
    categories = ['code', 'design', 'HTML']
    context = {'name': name, 'categories': categories}
    return render(request, 'dinamico.html', context)