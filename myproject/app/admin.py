from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password1', 'password2',
            'first_name', 'last_name', 'phone_number','birthday', 'organization' )
admin.site.register(CustomUser)

