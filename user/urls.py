from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login' ),
    path('list_user/', views.user_list, name='user_list'),
    path('update_user/<int:pk>', views.user_update, name='user_update'),
    path('detail_user/<int:pk>', views.user_detail, name ='user_detail'),
    path('delet_user/<int:pk>', views.user_delete, name='user_delete')
]