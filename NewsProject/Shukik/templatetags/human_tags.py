from Shukik.models import Profession
from django import template

register = template.Library()

# @register.simple_tag(name='get_list_professions')
# def get_categoryes():
#     return Profession.objects.all()

@register.inclusion_tag('shukik/list_profession.html')
def show_list():
    professions = Profession.objects.all()
    return {'professions': professions}
