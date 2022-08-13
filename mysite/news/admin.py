from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'get_html_photo', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('title',)
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'content')
    fields = ('title', 'category', 'content', 'photo', 'get_html_photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_html_photo')


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_html_photo.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



admin.site.site_header = 'Админ-панель OnlyGuns'
admin.site.site_title = 'Админ-панель OnlyGuns'
