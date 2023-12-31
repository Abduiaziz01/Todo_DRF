from django.contrib import admin

from apps.todo.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'is_completed', 'created_at', 'image')
    search_fields=('title', 'description')