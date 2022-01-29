from rest_framework import serializers
from portfolio.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name', 'slug', 'project_info', 'technologies_used', 'github_link', 'website', 'primary_language', 'get_absolute_url', 'date_posted', 'project_image', 'img_path'
        )

