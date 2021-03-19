from django.contrib import admin
from main.models import Todo_list , Tasks
# Register your models here.
# admin.site.register(Todo_list)
# admin.site.register(Tasks)

@admin.register(Todo_list)
class Todo_list_Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['task', 'created_date', 'due_on', 'owner', 'mark']
    ordering = ['id']
    search_fields = ['task', 'owner', 'mark']
    list_filter = ['created_date', 'due_on', 'owner', 'mark']