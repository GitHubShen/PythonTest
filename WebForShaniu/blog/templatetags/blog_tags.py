from ..models import Post
from django import template
from ..models import Category
from ..models import Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num = 5):
    #posts = Post.objects.all()
    #num = num if num < len(posts) else len(posts)
    return Post.objects.all().order_by("-create_time")

@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).all()