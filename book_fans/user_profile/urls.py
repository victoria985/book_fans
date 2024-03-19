from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.user_detail, name='user_detail'),
    path('profile/update/', views.user_update, name='user_update'),
    path('profile/delete/', views.user_delete, name='user_delete'),
]