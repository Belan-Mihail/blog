from .models import Comment
from django import forms
from .models import RecipePost

# 69 import from .models import RecipePost
# 55 import and add class
# 56 view

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# 69
# 70 views
class RecipePostCreateForm(forms.ModelForm):
    """
    Form for posts  to the site
    """
    class Meta:
        model = RecipePost
        fields = ('recipe_title', 'recipe_image', 'excerpt', 'recipe_body')

# 75
# 76 views
class RecipePostUpdateForm(forms.ModelForm):
    """
    Form for posts  to the site
    """
    class Meta:
        model = RecipePost
        fields = ('recipe_title', 'recipe_image', 'excerpt', 'recipe_body')