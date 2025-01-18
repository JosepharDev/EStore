from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAccountAdmin(UserAdmin):
    list_display = ("username", 'first_name', 'last_name', "email", 'last_login', "date_joined", "is_active")
    list_display_links = ("email", 'username', 'first_name')
    list_editable = ['is_active']
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()
    readonly_fields  = ['date_joined', 'last_login']
    ordering = ["-date_joined"]

admin.site.register(User, UserAccountAdmin)
