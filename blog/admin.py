from django.contrib import admin
from .models import RecipePost, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#1 create superuser admin 123456

# 6 import and registrate
# admin.site.register(RecipePost)

# 7 install Summernote pip3 install django-summernote \\ freeze
# 8 setting.py


# 10 import summernote and delete admin.site.register(RecipePost) and add bsummernote_fields = ('recipe_body')elow
@admin.register(RecipePost)
class RecipePostAdmin(SummernoteModelAdmin):
    # 13 add filters
    prepopulated_fields = {'slug': ('recipe_title',)}
    search_fields = ['recipe_title', 'recipe_body']
    list_filter = ('status', 'created_on')
    list_display=('recipe_title', 'slug', 'status')
    summernote_fields = ('recipe_body')

# 11 migrate (without makemigrations)
# 12 add test recipe post

# 14
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe_post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
# views.py

# 87 and import Category
# 88 migration and create 3 categories and 1 article
# 89 forms
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')
    prepopulated_fields = {"slug": ("name", )}
    