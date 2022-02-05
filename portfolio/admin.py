from django.contrib import admin
from .models import Project, Images

class ProjectImagesInline(admin.StackedInline):
    model = Images
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Information', {'fields': ['name', 'project_info', 'technologies_used', 'github_link', 'website', 'project_image', 'primary_language', 'primary_framework']}, ),
    ]
    inlines = [ProjectImagesInline]

admin.site.register(Project, ProjectAdmin)
