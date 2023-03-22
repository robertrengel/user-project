from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name','last_name','date_joined','gender', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff',)

admin.site.register(User, UserAdmin)