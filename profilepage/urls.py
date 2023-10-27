from django.urls import path
from . import views
# Internal:
from .views import UserProfilePageView


urlpatterns = [
    path('profile_page/', views.UserProfilePageView.as_view(), name='profile_page'),
]

# 98 urls project