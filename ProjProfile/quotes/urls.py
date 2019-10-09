from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('earning.html', views.earning, name='earning'),
    path('trending.html', views.trending, name='trending')
]
