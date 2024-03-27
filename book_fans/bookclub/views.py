from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.http import HttpRequest, HttpResponse
from user_profile_V2.models import Comment
from . import models, forms 
from django.contrib import messages
from django.views import generic


class AuthorListView(generic.ListView):
    model = models.Author
    template_name = 'bookclub/author_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Author.objects.all()

class BookListView(generic.ListView):
    model = models.Book
    template_name = 'bookclub/book_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.all()

class ReviewListView(generic.ListView):
    model = models.Review
    template_name = 'bookclub/review_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Review.objects.all()

def author_list(request: HttpRequest) -> HttpResponse:
    author_list = models.Author.objects.all()
    author_name = request.GET.get('author_name')
    if author_name:
        author_list = author_list.filter(name__icontains=author_name)
    paginator = Paginator(author_list, 6) 
    page_number = request.GET.get('page')
    try:
        authors = paginator.page(page_number)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)
    return render(request, 'bookclub/author_list.html', {'authors': authors})

def book_list(request: HttpRequest) -> HttpResponse:
    book_list = models.Book.objects.all()
    book_name = request.GET.get('book_name')
    if book_name:
        book_list = book_list.filter(name__icontains=book_name)
    paginator = Paginator(book_list, 14)  
    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'bookclub/book_list.html', {'books': books})


def review_list(request: HttpRequest) -> HttpResponse:
    review_list = models.Review.objects.all()
    paginator = Paginator(review_list, 2)  
    page_number = request.GET.get('page')
    try:
        reviews = paginator.page(page_number)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    return render(request, 'bookclub/review_list.html', {'reviews': reviews})

def index(request):
    books = models.Book.objects.all()  
    context = {
        'books': books,  
    }
    return render(request, 'bookclub/index.html', context)

def genre_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'bookclub/genre_list.html', {
        'genre_list': models.Genre.objects.all(),
    })

def genre_book_list(request, pk):
    genre = get_object_or_404(models.Genre, pk=pk)
    books_in_genre = models.Book.objects.filter(genre=genre)
    return render(request, 'bookclub/genre_book_list.html', {'genre': genre, 'books_in_genre': books_in_genre})

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
    from user_profile_V2.models import Comment
    review = get_object_or_404(models.Review, pk=pk)
    comments = Comment.objects.filter(review=review)
    return render(request, 'bookclub/review_detail.html', {
        'review': review,
        'comments': comments,
    })

@login_required
def book_create(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, _('The book has been created successfully.'))
            return redirect('book_list')
    else:
        form = forms.BookForm()
    return render(request, 'bookclub/book_create.html', {'form': form})

@login_required
def author_create(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, _('The author has been created successfully.'))
            return redirect('author_list')
    else:
        form = forms.AuthorForm()
    return render(request, 'bookclub/author_create.html', {'form': form})

@login_required
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

@login_required
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = forms.ReviewForm(instance=review)
    return render(request, 'bookclub/review_edit.html', {'form': form})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(models.Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, _('The book has been deleted successfully.'))
        return redirect('book_list')
    return render(request, 'bookclub/book_delete.html', {'book': book})

@login_required
def author_delete(request, pk):
    author = get_object_or_404(models.Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        messages.success(request, _('The author has been deleted successfully.'))
        return redirect('author_list')
    return render(request, 'bookclub/author_delete.html', {'author': author})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(models.Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.success(request, _('The review has been deleted successfully.'))
        return redirect('review_list')
    return render(request, 'bookclub/review_delete.html', {'review': review})
    