from django import template
from bots.models import Bots

register = template.Library()

@register.inclusion_tag('bots/tags/bots_list.html')
def show_bots():
    bots = Bots.objects.all().order_by('title')
    return {'bots': bots}
