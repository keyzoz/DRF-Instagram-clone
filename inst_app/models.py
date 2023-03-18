from django.db import models
from django.contrib.auth.models import AbstractUser
from inst_app.manager import UserManager




class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=20)
    about_me = models.CharField(max_length=150,null=True,blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    
    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class PostLike(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post','user')

class PostComment(models.Model):
    text = models.CharField(max_length=265)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

