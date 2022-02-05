from rest_framework import serializers
from portfolio.models import Project, Images

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name', 'slug', 'project_info', 'technologies_used', 'github_link', 'website', 'primary_language', 'primary_framework', 'get_absolute_url', 'date_posted', 'project_image', 'img_path'
        )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

