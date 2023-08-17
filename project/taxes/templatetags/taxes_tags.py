from ..models import Accruals_and_taxes
from django.db.models import Sum
from django import template

register = template.Library()

@register.simple_tag
def get_most_summ():
    return Accruals_and_taxes.objects.aggregate(Sum('accrued'))
    # return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]