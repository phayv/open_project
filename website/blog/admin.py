from django.contrib import admin
from .models import Post, PostTags

admin.site.register(Post)
admin.site.register(PostTags)