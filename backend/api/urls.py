from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('recent', views.recent, name='recent'),
  path('search', views.search, name='search'),
  path('recentcloud', views.recentcloud, name='recentcloud'),
  path('searchcloud', views.searchcloud, name='searchcloud'),
]
