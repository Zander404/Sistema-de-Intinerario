from django.urls import path
from . import views


urlpatterns = [

    ## ROTAS BASES
    path('', view=views.index, name='index'),
    path('intinerario/', views.intinerario, name='intinerario'),
    path('intineario/search/', views.search_intinerario, name='search_rote'),
    path('intinerario/<int:box>/', views.info, name='info_instinerario'),
    path('institucional/', views.institucional, name='institucional'),
    path('transporte/', views.transporte, name='transporte'),
    path('contato/', views.contato, name='contato'),

    ## ROTAS ADMINS
    
    path('painel/', views.painel, name='painel'),

    path('painel/rote/', views.read_rote, name='list_rotes'),
    path('painel/rote/detail_rote/<int:pk>/', views.detail_rote, name='info_rote'),
    path('painel/rote/add_rote', views.create_rote, name='add_rote'),
    path('painel/rote/update_rote', views.update_rote, name='update_rote'),
    path('painel/rote/delete_rote', views.delete_rote, name='delete_rote'),


    ## ROTAS 
]   