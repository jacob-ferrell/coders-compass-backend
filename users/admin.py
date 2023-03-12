from django.contrib import admin
from .models import NewUser

class NewUserAdmin(admin.ModelAdmin):
    list_display=('id', 'email', 'username', 'first_name', 'is_staff')

admin.site.register(NewUser, NewUserAdmin)