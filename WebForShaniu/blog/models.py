# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)

class Tag(models.Model):
    name = models.CharField(max_length = 100)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 800, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    viewnum = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_time', 'title']

    def increase_viewnum(self):
       self.viewnum += 1
       self.save(update_fields=['viewnum'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post, self).save(*args, **kwargs)
