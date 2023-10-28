from . import views
from django.urls import path
from .views import RecipePostCreateView, RecipePostUpdateView, RecipePostDeleteView, RecipePostCategory


# 17 import and path
urlpatterns = [
    path("", views.RecipesPostList.as_view(), name="home"),
    
    # 35 add path to detail.html update index.html add links to the each posts, add check code post-detail
    # 36 index
    path('<slug:slug>/', views.RecipePostDetail.as_view(), name='recipe_post_detail'),
    # 84
    # 85 post detail
    path('comment/<int:id>', views.deletecomment, name='blog_comment'),

    # 64
    # 65 setting project import
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # 71
    # 72 create template 
    path('recipe/create/', RecipePostCreateView.as_view(), name='recipe_create'),
    # 77 import
    # 78 add button update to detail.views
    path('recipe/<slug:slug>/update/', RecipePostUpdateView.as_view(), name='recipe_update'),
    # 80 import
    # 81 templatest
    path('recipe/<slug:slug>/delete/', RecipePostDeleteView.as_view(), name='recipe_delete'),
    # 94 import RecipePostCategory and below
    # 95 index html add a href
    path('category/<slug:cat_slug>/', RecipePostCategory.as_view(), name='category'),
    
    

]
# 18 urls.py project