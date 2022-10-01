# from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


# Create your views here.
def test(request):
    return HttpResponse("Esto es un test y funciona correctamente")


def create(request):
    # comment = Comment(name="Amador", score=5, comment="Este es un comentario")
    # comment.save()
    comment = Comment.objects.create(name="Alex")
    return HttpResponse("Ruta para probar modelos")


def delete(request):
    # comment = Comment.objects.get(id=1)
    # comment.delete()
    Comment.objects.filter(id=7).delete()
    return HttpResponse("Ruta para borrar modelos")
