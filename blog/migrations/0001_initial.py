# Generated by Django 3.2.22 on 2023-10-08 06:20

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('recipe_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('excerpt', models.TextField(blank=True)),
                ('recipe_body', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('likes', models.ManyToManyField(blank=True, related_name='recipepost_like', to=settings.AUTH_USER_MODEL)),
                ('recipe_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'recipe',
                'verbose_name_plural': 'recipes',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('recipe_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.recipepost')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['created_on'],
            },
        ),
    ]