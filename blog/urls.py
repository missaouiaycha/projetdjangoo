from django.urls import path
from blog import views

urlpatterns = [
    path('', views.liste_article, name='liste_article'),
    path('ajouter_article/',views.ajouter_article,name='ajouter_article'),
]
