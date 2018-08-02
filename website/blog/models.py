from django.db import models


class PostTags(models.Model):
    tag = models.CharField(max_length=300)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    entry = models.TextField(blank=True)
    entry_snippet = models.TextField(max_length=1000, blank=True)
    file_location = models.CharField(max_length=1000)
    tags = models.ManyToManyField(PostTags)

    def __str__(self):
        return self.title




