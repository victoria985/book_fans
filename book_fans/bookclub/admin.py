from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'publication_year']
    list_display_links = ['name']
    list_filter = ['author', 'genre', 'publication_year']
    search_fields = ['name', 'author__name']  


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'biography']
    list_display_links = ['name']
    search_fields = ['name']  


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name'] 


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating']
    list_display_links = ['book']
    list_filter = ['book', 'user', 'rating']
    search_fields = ['book__name', 'user__username']  


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Review, ReviewAdmin)



