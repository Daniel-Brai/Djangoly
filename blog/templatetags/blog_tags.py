from django import template
from django.db.models import Count
from django.template import Library
from django.utils.safestring import mark_safe
import markdown
from ..models import Post, PublishedManager

register: Library = template.Library()

@register.simple_tag
def total_posts() -> int:
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5) -> dict[str, PublishedManager]:
    latest_posts: PublishedManager = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5) -> PublishedManager:
    return Post.published.annotate(total_comments=Count('comments'))\
                        .order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))                        