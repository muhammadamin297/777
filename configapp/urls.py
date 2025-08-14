from django.urls import path
from .views import search_by_url, search_by_form, home_view

urlpatterns = [
    path('search/<str:keyword>/', search_by_url, name='search-by-url'),
    path('search/', search_by_form, name='search-by-form'),
    path('', home_view, name='home'),
]
