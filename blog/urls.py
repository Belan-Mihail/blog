from . import views
from django.urls import path

# 17 import and path
urlpatterns = [
    path("", views.RecipesPostList.as_view(), name="home"),
]
# 18 urls.py project