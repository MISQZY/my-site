from unicodedata import category
from django import template
from my_storage.models import Category, Storage
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('my_storage/tags/list_of_categories.html')
def show_list_categories():
    #categories = Category.objects.all
    categories = Category.objects.annotate(cnt=Count('storage')).filter(cnt__gt=0)
    return {'categories': categories}

# @register.inclusion_tag('my_storage/tags/list_of_cards.html')
# def show_list_cards():
#     cats = Category.objects.filter()
#     cards = Storage.objects.filter(category__in='category_id')
#     return {'cards': cards}
