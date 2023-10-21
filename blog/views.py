from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView
from django.views import generic, View 
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from .models import RecipePost, Category
from .forms import Comment, CommentForm, RecipePostCreateForm, RecipePostUpdateForm


# 56 import CommentForm and go to RecipePostDetail 

# 70 import Views and Forms nd from django.contrib.auth.decorators import login_require

# 33 import View, get 404 function

# 15 import RecipePost and generic
# add comments


class RecipesPostList(generic.ListView):
    model = RecipePost
    queryset = RecipePost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 5
    context_object_name = 'recipes_post_list'
    # 90 
    # 91 index.html categories
    def get_context_data(self,**kwargs):
        context = super(RecipesPostList, self).get_context_data(**kwargs)
        context['categor'] = Category.objects.all()
        return context

# def post_list(request):
    """
    Display a list of published and approved posts, paginated.

    Parameters:
        request (HttpRequest): the HTTP request object

    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    # post_list = Post.objects.filter(status="published", approved=True)
    # categories = Category.objects.all()
    # paginator = Paginator(post_list, 3)
    # page = request.GET.get("page")
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)

    # template = ["blog/post/post_list.html"]
    # context = {
    #     "page_title": "Coding Articles",
    #     "posts": posts,
    #     "categories": categories,
    #     "page": page,
    # }
    # return render(request, template, context)

    

# 16 index.html, base.html, css/style.css, js
# 17 urls.py blog


# 34 add class RecipesPostDetail and add post_details
# add comment
# 35 urls
class RecipePostDetail(View):

    model = RecipePost

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
            comment.recipe_post = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "slug": slug,
                "comments": comments,
                # 60
                "commented": True,
                "liked": liked,
                # 56
                "comment_form": CommentForm()
                # 57 details.html
            },
        )


#83 import Comment and Redirect (change name in view urls and templates)
# 84 urls
def deletecomment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    success_message = 'Your comment has been deleted successfully!'
    return redirect(comment.recipe_post.get_absolute_url()) 

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

# 70
# 71 urls.py

class RecipePostCreateView(SuccessMessageMixin, CreateView):
    """
    
    """
    model = RecipePost
    template_name = 'recipe_create.html'
    form_class = RecipePostCreateForm
    success_url = '/'
    success_message = 'Your recipe is is awaiting administrator approval'

    


    def form_valid(self, form):
        form.instance.recipe_author = self.request.user
        form.save()
        return super().form_valid(form)


# 76 and import RecipePostUpdateForm and UserPassesTestMixin
# 77 template
class RecipePostUpdateView(SuccessMessageMixin,
                          UserPassesTestMixin,
                          UpdateView):
    """
    A class view to update the existing story by user
    """
    model = RecipePost
    template_name = 'recipe_update.html'
    form_class = RecipePostUpdateForm
    success_url = '/'
    success_message = 'Your updated recipe is awaiting administrator approval'


    def form_valid(self, form):
        form.instance.recipe_author = self.request.user
        form.instance.status = 0
        return super().form_valid(form)

    def test_func(self):
        if self.request.user != self.get_object().recipe_author:
                messages.info(request, 'Editing an article is available only to the author')
                return False
        return True

# 79
# 80 urls
class RecipePostDeleteView(SuccessMessageMixin,
                          UserPassesTestMixin,
                          DeleteView):
    """
    A class view to delete the story by user
    """
    model = RecipePost
    success_url = '/'
    template_name = 'recipe_delete.html'
    context_object_name = 'recipe'
    success_message = 'Your post has been deleted successfully!'


    def test_func(self):
        if self.request.user != self.get_object().recipe_author:
                messages.info(request, 'Deleting an article is available only to the author')
                return False
        return True

# 93
# 94 urls
class RecipePostCategory(generic.ListView):
    model = RecipePost
    template_name = 'index.html'
    context_object_name = 'recipes_post_list'
    
    def get_context_data(self,**kwargs):
        context = super(RecipePostCategory, self).get_context_data(**kwargs)
        context['categor'] = Category.objects.all()
        return context
 
    def get_queryset(self):
        return RecipePost.objects.filter(cat__slug=self.kwargs['cat_slug'])