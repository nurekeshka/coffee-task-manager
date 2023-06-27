from django.contrib import admin
from apps.accounts import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name')
    fields = ('username', 'first_name', 'last_name', 'email',
              'is_staff', 'is_active')
