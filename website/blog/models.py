from django.db import models
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    entry = models.TextField()
    file_location = models.CharField(max_length=1000)

    # tags = models.ForeignKey() because we want different types of artistic

    def __str__(self):
        return self.title


admin.site.register(Post)