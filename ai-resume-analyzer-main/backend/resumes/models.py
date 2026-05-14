from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


class Skill(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='skills'
    )

    name = models.CharField(
        max_length=100
    )

    class Meta:

        unique_together = (
            'user',
            'name'
        )

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.user.username})"
        )


class Resume(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resumes'
    )

    resume_file = models.FileField(
        upload_to='resumes/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf']
            )
        ]
    )

    extracted_text = models.TextField(
        blank=True,
        null=True
    )

    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name='resumes'
    )

    # Experience level
    experience_level = models.CharField(
        max_length=50,
        default='Fresher'
    )

    # Resume ATS score
    resume_score = models.IntegerField(
        default=0
    )

    # Resume strengths
    strengths = models.JSONField(
        default=list
    )

    # Improvement suggestions
    improvements = models.JSONField(
        default=list
    )

    # AI resume suggestions
    ai_suggestions = models.JSONField(
        default=list
    )

    # Career recommendations
    career_paths = models.JSONField(
        default=list
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.user.username}'s "
            f"Resume ({self.id})"
        )