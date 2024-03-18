from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model  
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    name = models.CharField(_('name'), blank=True, db_index=True, max_length=100)
    biography = models.TextField(_('biography'), blank=True, max_length=10000)
    photo = models.ImageField(_('photo'), upload_to='authors/', null=True, blank=True)

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    

class Genre(models.Model):
    name = models.CharField(_('name'), max_length=50, db_index=True)

    class Meta:
        verbose_name = _("genre")
        verbose_name_plural = _("genres")
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"pk": self.pk})
    

class Book(models.Model):
    name = models.CharField(_('name'), max_length=100)
    publication_year = models.PositiveIntegerField(blank=True)
    description = models.TextField(_('description'), blank=True, max_length=10000)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name=_("author"),
        related_name='books',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name=_("genre"),
    )
    cover_image = models.ImageField(_('cover image'), upload_to='book_covers/', blank=True)

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")
        ordering = ['genre']

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.TextField(_('comment'), max_length=500, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True)
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name='reviews'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name=_("book")
    )

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ['rating']

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})


   