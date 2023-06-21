from . import views
from django.urls import path


urlpatterns = [
   path('register/', views.register, name='register'),
   path('index/', views.index, name='index'),
   path('logout/', views.exit, name='exit'),
   path('arriendos/', views.arriendos, name='arriendos'),
   path('reparaciones/', views.reparaciones, name='reparaciones'),
   path('accesorios/', views.accesorios, name='accesorios'),
   path('nosotros/', views.nosotros, name='nosotros'),
   path('formarriendo/', views.formarriendo, name='formarriendo')
]