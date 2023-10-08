from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# 2 import 

# 3 create RecipePost Model

STATUS = ((0, "Draft"), (1, "Published"))


class RecipePost(models.Model):
    """
    RecipePost model 
    """
    recipe_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    recipe_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_blog_posts"
    )
    recipe_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    recipe_body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipepost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "recipe"
        verbose_name_plural = "recipes"

    def __str__(self):
        return self.recipe_title

    def number_of_likes(self):
        return self.likes.count()

# 4 create Comments model
# 5 migrations
# 6 admin

class Comment(models.Model):
    recipe_post = models.ForeignKey(RecipePost, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"Comment {self.body} by {self.name}"