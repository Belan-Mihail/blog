from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import (UpdateView, DetailView, DeleteView)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
# Internal:
# from .forms import ContactUsForm, ProfileForm
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


# 97 urls