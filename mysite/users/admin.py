from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'get_html_photo', 'acess_level', 'last_login', 'date_joined')
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('acess_level', 'photo')}),
    )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src ='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'

admin.site.register(CustomUser, CustomUserAdmin)
