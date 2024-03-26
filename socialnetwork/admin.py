from django.contrib import admin
from django.contrib.auth.models import User
from rest_auth.models import TokenModel
from rest_framework.authtoken.admin import TokenAdmin


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')


admin.site.register(User, UserAdmin)

TokenAdmin.autocomplete_fields = []

admin.site.register(TokenModel, TokenAdmin)
