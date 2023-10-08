from django.shortcuts import render
from django.views import generic
from .models import RecipePost

# 15 import RecipePost and generic
class RecipesPostList(generic.ListView):
    model = RecipePost
    queryset = RecipePost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    context_object_name = 'recipes_post_list'

# 16 index.html, base.html, css/style.css, js
# 17 urls.py blog