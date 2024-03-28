from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'publication_year', 'description', 'author', 'genre', 'cover_image']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'biography', 'photo']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['comment', 'rating', 'user', 'book']

class BookDeleteForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = []

class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = []

class ReviewDeleteForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = []
