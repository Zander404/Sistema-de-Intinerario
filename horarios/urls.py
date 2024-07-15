from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:box>/', views.info, name='info'),
]