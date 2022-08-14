from django.contrib import admin

from .models import Bots

class BotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tg_name', 'status')
    list_display_links = ('title',)
    search_fields = ('title', 'token', 'tg_name')



admin.site.register(Bots, BotsAdmin)
