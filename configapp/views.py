from django.shortcuts import render
from .models import News, Category

def search_by_form(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = News.objects.filter(title__icontains=query)

    category = Category.objects.all()
    news = News.objects.all()

    context = {
        'category': category,
        'news': news if not query else results,
        'keyword': query
    }
    return render(request, 'index.html', context=context)

def home_view(request):
    category = Category.objects.all()
    news = News.objects.all()

    context = {
        'category': category,
        'news': news
    }
    return render(request, 'index.html', context=context)
