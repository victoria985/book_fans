from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(_("picture"), upload_to='user_pictures/', blank=True, null=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("user_detail_current", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.picture:
            image = Image.open(self.picture.path)
            if image.size[0] > 400 or image.size[1] > 300:
                image.thumbnail((400, 300))  #pakeista resize i thumbnail del paveikslelio formos issaugojimo kad nesikeistu formatas
                image.save(self.picture.path)


class Comment(models.Model):
    text = models.TextField(_('text'), max_length=1000)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("user"))
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey('bookclub.Book', on_delete=models.CASCADE, verbose_name=_("book"), null=True, blank=True)
    review = models.ForeignKey('bookclub.Review', on_delete=models.CASCADE, verbose_name=_("review"), null=True, blank=True, related_name='user_comments')

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ['-created_at']

    def __str__(self):
        return self.text[:100]  