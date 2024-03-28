from django.contrib import admin
from . import models


class UserProfileV2Admin(admin.ModelAdmin):
    fields = ['username', 'email']


class CommentAdmin(admin.ModelAdmin):
    fields = ['text', 'user', 'created_at', 'book', 'review'] 





admin.site.register(models.UserProfileV2)
admin.site.register(models.Comment)
