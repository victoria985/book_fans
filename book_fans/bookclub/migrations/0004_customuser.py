# Generated by Django 5.0.2 on 2024-03-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0003_alter_author_options_author_photo_book_cover_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('read_books', models.ManyToManyField(blank=True, related_name='read_by', to='bookclub.book')),
            ],
        ),
    ]
