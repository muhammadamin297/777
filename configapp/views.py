
from django.shortcuts import render
from unicodedata import category

from .models import News,Category

# URL orqali qidiruv
def search_by_url(request, keyword):
    results = News.objects.filter(title__icontains=keyword)
    return render(request, 'index2.html', {'results': results, 'keyword': keyword})

# Forma orqali qidiruv
def search_by_form(request):
    query = request.GET.get('q', '')
    results = News.objects.filter(title__icontains=query) if query else []
    return render(request, 'index.html', {'results': results, 'keyword': query})



def home_view(request):
    category=Category.objects.all()
    news=News.objects.all()
    # query = request.GET.get('q', '')
    # if query:
    #     category=category.filter(title__icontains=query)

    context = {
        'category': category,
        'news' : news
    }
    return  render(request,'index.html',context=context)