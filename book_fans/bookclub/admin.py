from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class AuthorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass





admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Review, ReviewAdmin)