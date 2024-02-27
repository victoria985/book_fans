from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("userprofile")
        verbose_name_plural = _("userprofiles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("userprofile_detail", kwargs={"pk": self.pk})
