from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import RecipePost

# 33 import View, get 404 function

# 15 import RecipePost and generic
# add comments
class RecipesPostList(generic.ListView):
    model = RecipePost
    queryset = RecipePost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 5
    context_object_name = 'recipes_post_list'

# 16 index.html, base.html, css/style.css, js
# 17 urls.py blog


# 34 add class RecipesPostDetail and add post_details
# add comment
# 35 urls
class RecipePostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = RecipePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
            },
        )
