from . import views
from django.urls import path
from .views import RecipePostCreateView


# 17 import and path
urlpatterns = [
    path("", views.RecipesPostList.as_view(), name="home"),
    # 35 add path to detail.html update index.html add links to the each posts, add check code post-detail
    # 36 index
    path('<slug:slug>/', views.RecipePostDetail.as_view(), name='recipe_post_detail'),
    # 64
    # 65 setting project import
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # 71
    # 72 create template 
    path('recipe/create/', RecipePostCreateView.as_view(), name='recipe_create'),
]
# 18 urls.py project