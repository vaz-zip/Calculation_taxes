from django import template
from ..models import Document

register = template.Library()
@register.simple_tag
def total_docs():
    return Document.count()

from django.utils.safestring import mark_safe
import markdown

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))