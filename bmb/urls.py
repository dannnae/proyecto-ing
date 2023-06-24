from . import views
from django.urls import path


urlpatterns = [
   path('register/', views.register, name='register'),
   path('', views.index, name='index'),
   path('login/', views.login, name='login'),
   path('arriendos/', views.arriendos, name='arriendos'),
   path('reparaciones/', views.reparaciones, name='reparaciones'),
   path('accesorios/', views.accesorios, name='accesorios'),
   path('nosotros/', views.nosotros, name='nosotros'),
   path('formarriendo/', views.formarriendo, name='formarriendo'),
   path('logout/', views.logout_view, name='logout'),
   path('listar_solicitudes/', views.listar_solicitudes, name='listar_solicitudes'),
   
]