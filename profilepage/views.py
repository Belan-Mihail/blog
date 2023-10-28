from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import (ListView, UpdateView, DetailView, DeleteView)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
# Internal:
from .forms import ProfileForm
from .models import Profile
from blog.models import RecipePost
from django.contrib.auth.decorators import login_required


class UserProfilePageView(DetailView):
    """
    A class view to see detail
    of user profile
    """
    model = Profile
    template_name = 'profilepage/profile_page.html'
    

    def get_object(self, *args, **kwargs):
        return self.request.user
    

    def get_context_data(self,**kwargs):
        context = super(UserProfilePageView, self).get_context_data(**kwargs)
        context['recipes_post'] = RecipePost.objects.filter(status=1).order_by("-created_on")
        return context


# 97 urls

class UserUpdateProfile(SuccessMessageMixin, UpdateView):
    """
    A class view to update
    user profile
    """
    model = Profile
    form_class = ProfileForm
    success_url = '/profile_page/profile_page'
    template_name = 'profilepage/update_profile.html'
    success_message = 'Your profile has been updated successfully!'

    def get_object(self, *args, **kwargs):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)