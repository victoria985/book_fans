# Generated by Django 5.0.2 on 2024-03-20 07:30

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0005_remove_customuser_read_books_delete_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=tinymce.models.HTMLField(blank=True, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='description'),
        ),
    ]
