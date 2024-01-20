from django.contrib import admin
from .models import UserTable


@admin.register(UserTable)
class UserTableAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
