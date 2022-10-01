# from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Reporter, Article
from datetime import date


# Create your views here.
def create(request):
    author = Reporter(first_name="Amador", last_name="Cano", email="ama@dor.es")
    author.save()

    art1 = Article(headline="Creando un titulo",
                   date=date(2022,5,5),
                   reporter=author,
                   )
    art1.save()

    art2 = Article(headline="Creando cositas",
                   date=date(2022,5,15),
                   reporter=author,
                   )
    art2.save()

    art3= Article(headline="Creando",
                   date=date(2022,4,9),
                   reporter=author,
                   )
    art3.save()

    result = art1.reporter.last_name
    result1= author.article_set.all().count()

    return HttpResponse(result1)