from django.urls import path
from . import views
# Internal:
from .views import UserProfilePageView, UserUpdateProfile


urlpatterns = [
    path('profile_page/', views.UserProfilePageView.as_view(), name='profile_page'),
    path('update_profile/', UserUpdateProfile.as_view(), name='update_profile'),
    
]

# 98 urls project