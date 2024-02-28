from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookclub/books/', views.book_list, name='book_list'),
    path('bookclub/books/<int:pk>/', views.book_detail, name='book_detail'),
    path('bookclub/genres/', views.genre_list, name='genre_list'),
    path('bookclub/genres/<int:pk>/', views.genre_detail, name='genre_detail'),
    path('bookclub/genres/<int:pk>/books/', views.genre_book_list, name='genre_book_list'),
    path('bookclub/authors/', views.author_list, name='author_list'),
    path('bookclub/authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('bookclub/reviews/', views.review_list, name='review_list'),
    path('bookclub/reviews/<int:pk>/', views.review_detail, name='review_detail'),
]
 
