from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime


def home(request):
    count = Article.objects.count()
    return render(request, "home.html", {"count": count, "year": datetime.now().year})
