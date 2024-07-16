from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.registrar_usuario, name='login' ),
]