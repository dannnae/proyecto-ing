from . import views
from django.urls import path


urlpatterns = [
   path('completo/', views.completo, name='completo'),
   path('register/', views.register, name='register'),
   path('index/', views.index, name='index'),
   path('logout/', views.exit, name='exit'),
] 