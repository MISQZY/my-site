from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'acess_level', 'last_login', 'date_joined')
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('acess_level',)}),
    )



admin.site.register(CustomUser, CustomUserAdmin)
