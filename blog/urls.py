from . import views
from django.urls import path

# 17 import and path
urlpatterns = [
    path("", views.RecipesPostList.as_view(), name="home"),
    # 35 add path to detail.html update index.html add links to the each posts, add check code post-detail
    # 36 index
    path('<slug:slug>/', views.RecipePostDetail.as_view(), name='recipe_post_detail'),
]
# 18 urls.py project