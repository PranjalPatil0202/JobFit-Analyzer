# pyrefly: ignore [missing-import]
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.TextField(help_text="Comma separated skills")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
