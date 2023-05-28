from django.urls import path
from . import views 

urlpatterns = [
    path('acceuil/', views.acceuil, name='acceuil'),
    path('about/', views.about, name='about'),
   path('contact/',views.contact,name='contact'),
    path('Portfolio/', views.Portfolio, name='Portfolio'),
   path('service/',views.service, name = 'service'),
    path('register/',views.register, name = 'register'), 
    path('navbar/',views.navbar, name = 'navbar'), 
     path('ajouter_projet/',views.ajouter_projet, name = 'ajouter_projet'), 
      path('group/',views.listGroup,name='group'),
       path('listRequest/',views.listRequest, name = 'listRequest'), 
         path('lisprojet/<str:libellai>',views.listdetail,name='listdetail'),
           path('ajoutDetail/<int:projet_id>',views.ajoutDetail,name='ajoutDetail'),
      
]
