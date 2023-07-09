from Shukik.models import Profession
from django import template
from django.db.models import Count

register = template.Library()

# @register.simple_tag(name='get_list_professions')
# def get_categoryes():
#     return Profession.objects.all()

@register.inclusion_tag('shukik/list_profession.html')
def show_list():
    professions = Profession.objects.annotate(cnt=Count('human')).filter(cnt__gt=0)
    return {'professions': professions}
