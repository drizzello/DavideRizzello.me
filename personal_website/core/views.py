from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime


def home(request):
    """
    Home page view for the personal blog and portfolio landing page.
    Provides context data for the landing page including article count and current year.
    """
    count = Article.objects.count()
    current_year = datetime.now().year
    
    # Additional context for the landing page
    context = {
        'count': count,
        'year': current_year,
        'page_title': 'Davide Rizzello - Developer & Writer',
        'meta_description': 'Developer, Writer & Digital Craftsman. Building things with code and sharing thoughts through writing.',
    }
    
    return render(request, "home.html", context)
