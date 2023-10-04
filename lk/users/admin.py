from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'full_name', 'status',]

    fieldsets = UserAdmin.fieldsets + (
        ('Реквизиты 1С', {'fields': ('full_name', 'status',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Реквизиты 1С', {'fields': ('full_name', 'status',)}),
    )

    search_fields = ('full_name', 'username',)
    ordering = ('full_name', 'username',)
    list_filter = ('status',)


admin.site.register(CustomUser, CustomUserAdmin)