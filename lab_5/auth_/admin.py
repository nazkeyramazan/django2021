from django.contrib import admin
from .models import MainUser

# Register your models here.

@admin.register(MainUser)
class MainUser_Admin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']