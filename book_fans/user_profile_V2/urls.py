from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/user_profile/', views.user_profile, name='user_profile'), 
    path('profile/update/', views.user_update, name='user_update'),
    path('profile/delete/', views.user_delete, name='user_delete'),
    path('comment/create/<int:review_id>/', views.comment_create, name='comment_create'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]
