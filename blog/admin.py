from django.contrib import admin
from .models import RecipePost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#1 create superuser admin 123456

# 6 import and registrate
# admin.site.register(RecipePost)

# 7 install Summernote pip3 install django-summernote \\ freeze
# 8 setting.py


# 10 import summernote and delete admin.site.register(RecipePost) and add below
@admin.register(RecipePost)
class RecipePostAdmin(SummernoteModelAdmin):
    summernote_fields = ('recipe_body')

# 11 migrate (without makemigrations)
# 12 add test recipe post