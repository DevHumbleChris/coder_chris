from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    project_info = models.TextField(max_length=500)
    technologies_used = models.TextField()
    github_link = models.URLField()
    website = models.URLField()
    project_image = models.ImageField(upload_to="uploads/")
    primary_language = models.CharField(max_length=50, default="Python")
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def img_path(self):
        return self.project_image.url
    
    def get_absolute_url(self):
        return f"/{self.slug}"

    def __str__(self):
        return self.name
