from django import template
from ..models import Document

register = template.Library()
@register.simple_tag
def total_docs():
    return Document.count()