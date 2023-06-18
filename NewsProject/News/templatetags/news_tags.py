from News.models import Category
from django import template

register = template.Library()

# @register.simple_tag(name='get_list_categoryes')
# def get_categoryes():
#     return Category.objects.all()

@register.inclusion_tag('news/list_categoryes.html')
def show_categoryes():
    categoryes = Category.objects.all()
    return {'categoryes': categoryes}
