from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Human
from .models import Profession

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'name', 'surname', 'created_at', 'get_photo', 'is_admin')
    list_display_links = ('id', 'name')
    list_editable = ('profession', 'is_admin')
    fields = ('profession', 'name', 'surname', 'info', 'created_at', 'photo', 'get_photo', 'is_admin')
    readonly_fields = ('created_at', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="90px">')
        else:
            return 'Фото нет'
        
    get_photo.short_description = 'Минитюра'

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'