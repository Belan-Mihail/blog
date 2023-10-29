from django.urls import path
from . import views
# Internal:
from .views import CreateProfileView, UserProfilePageView, UserUpdateProfile, contact


urlpatterns = [
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile_page/', views.UserProfilePageView.as_view(), name='profile_page'),
    path('update_profile/', UserUpdateProfile.as_view(), name='update_profile'),
    path('contact/', contact, name='contact'),
    
]

# 98 urls project