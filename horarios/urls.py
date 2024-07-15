from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='index'),
    path('intinerario/', views.intinerario, name='intinerario'),
    path('intinerario/<int:box>/', views.info, name='info_bus'),
    path('institucional/', views.institucional, name='institucional'),
    path('transporte/', views.transporte, name='transporte'),
    path('contato/', views.contato, name='contato'),
]