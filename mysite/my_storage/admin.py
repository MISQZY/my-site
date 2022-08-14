from django.contrib import admin

from .models import Storage, Category

class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','acess_required' ,'created_at', 'updated_at', 'is_published')
    list_display_links = ('title',)
    list_filter = ('is_published','category', 'acess_required')
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)





admin.site.register(Storage, StorageAdmin)
admin.site.register(Category, CategoryAdmin)
