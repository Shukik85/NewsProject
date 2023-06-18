from django.contrib import admin
from .models import Human
from .models import Profession

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'name', 'surname', 'created_at', 'photo', 'is_admin')
    list_display_links = ('id', 'name')
    list_editable = ('profession', 'is_admin')

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)