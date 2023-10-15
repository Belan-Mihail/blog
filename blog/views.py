from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import RecipePost
from .forms import CommentForm

# 56 import CommentForm and go to RecipePostDetail


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
                # 60
                "commented": False,
                "liked": liked,
                # 56
                "comment_form": CommentForm()
                # 57 details.html
            },
        )


    # 60 (and add "commented": False to get method and True to post method)
    # 61 post_setail
    def post(self, request, slug, *args, **kwargs):
        queryset = RecipePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                # 60
                "commented": True,
                "liked": liked,
                # 56
                "comment_form": CommentForm()
                # 57 details.html
            },
        )

# 62 and import HttpResponseRedirect and reverse
# 63 post detail
class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(RecipePost, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_post_detail', args=[slug]))
