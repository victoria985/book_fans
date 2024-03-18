from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from . import models, forms 
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect 
from django.utils.translation import gettext_lazy as _


def index(request):
    books = models.Book.objects.all()  # Gauti visus objektus iš Book modelio

    context = {
        'books': books,  # Perduodame knygų sąrašą į šabloną
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

def review_detail(request, pk:int) -> HttpResponse:
    review = get_object_or_404(models.Review, pk=pk)
    comments = models.Comment.objects.filter(review=review)
    return render(request, 'bookclub/review_detail.html', {
        'review': review,
        'comments': comments,
    })

def read_book(request, book_id):
    user = request.user
    book = get_object_or_404(models.Book, id=book_id)
    
    if user.read_books.filter(id=book_id).exists():
        messages.info(request, f"You have already read the book '{book.name}'. Choose another one from the list.")
    else:
        user.read_books.add(book)
        messages.success(request, f"You have successfully marked '{book.name}' as read.")
    return redirect('book_list')

def book_create(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('The book has been created successfully.'))
            return redirect('book_list')
    else:
        form = forms.BookForm()
    return render(request, 'bookclub/book_create.html', {'form': form})

def author_create(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('The author has been created successfully.'))
            return redirect('author_list')
    else:
        form = forms.AuthorForm()
    return render(request, 'bookclub/author_create.html', {'form': form})

def review_create(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('The review has been created successfully.'))
            return redirect('review_list')
    else:
        form = forms.ReviewForm()
    return render(request, 'bookclub/review_create.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(models.Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, _('The book has been deleted successfully.'))
        return redirect('book_list')
    return render(request, 'bookclub/book_delete.html', {'book': book})

def author_delete(request, pk):
    author = get_object_or_404(models.Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        messages.success(request, _('The author has been deleted successfully.'))
        return redirect('author_list')
    return render(request, 'bookclub/author_delete.html', {'author': author})

def review_delete(request, pk):
    review = get_object_or_404(models.Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.success(request, _('The review has been deleted successfully.'))
        return redirect('review_list')
    return render(request, 'bookclub/review_delete.html', {'review': review})
    
