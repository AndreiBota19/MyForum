from django.contrib import admin
from posts.models import Post
from .models import Profile

admin.site.register(Post)
admin.site.register(Profile)

