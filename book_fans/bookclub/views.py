from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from . import models 
from django.contrib import messages
from django.shortcuts import redirect 


def index(request: HttpRequest) -> HttpResponse:
    books_count = models.Book.objects.count()
    authors_count = models.Author.objects.count()
    reviews_count = models.Review.objects.count()
    users_count = models.get_user_model().objects.count()
    
    context = {
        'books_count': books_count,
        'authors_count': authors_count,
        'reviews_count': reviews_count,
        'users_count': users_count,
    }
    return render(request, 'bookclub/index.html', context)

def book_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'bookclub/book_list.html', {
        'book_list': models.Book.objects.all(),
    })

def author_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'bookclub/author_list.html', {
        'author_list': models.Author.objects.all(),
    })

def genre_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'bookclub/genre_list.html', {
        'genre_list': models.Genre.objects.all(),
    })

def genre_book_list(request, pk):
    genre = get_object_or_404(models.Genre, pk=pk)
    books_in_genre = models.Book.objects.filter(genre=genre)
    return render(request, 'bookclub/genre_book_list.html', {'genre': genre, 'books_in_genre': books_in_genre})


def review_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'bookclub/review_list.html', {
        'review_list': models.Review.objects.all(),
    })

def book_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'bookclub/book_detail.html', {
        'book': get_object_or_404(models.Book, pk=pk)
    })

def author_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'bookclub/author_detail.html', {
        'author': get_object_or_404(models.Author, pk=pk)
    })

def genre_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'bookclub/genre_detail.html', {
        'genre': get_object_or_404(models.Genre, pk=pk)
    })

def review_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'bookclub/review_detail.html', {
        'review': get_object_or_404(models.Review, pk=pk)
    })

def read_book(request, book_id):
    user = request.user
    book = get_object_or_404('Book', id=book_id)
    
    if user.read_books.filter(id=book_id).exists():
        messages.info(request, f"You have already read the book '{book.title}'. Choose another one from the list.")
    else:
        user.read_books.add(book)
        messages.success(request, f"You have successfully marked '{book.title}' as read.")
    return redirect('book_list')
    
