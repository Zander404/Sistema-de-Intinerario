from django.urls import path
from . import views
urlpatterns = [
    path('', views.painel, name='painel'),
    path('login/', views.registrar_usuario, name='login' ),
]