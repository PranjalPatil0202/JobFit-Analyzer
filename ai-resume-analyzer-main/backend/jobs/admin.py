# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'required_skills')
    list_filter = ('created_at',)
