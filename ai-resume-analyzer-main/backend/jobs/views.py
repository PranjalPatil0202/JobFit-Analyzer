from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer
from .recommendation_engine import recommend_jobs_ml

# Import Resume model
from resumes.models import Resume


class JobViewSet(viewsets.ModelViewSet):

    queryset = Job.objects.all().order_by(
        '-created_at'
    )

    serializer_class = JobSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[
            permissions.IsAuthenticated
        ]
    )
    def recommendations(self, request):

        user = request.user

        # Fetch extracted skills
        user_skills = user.skills.values_list(
            'name',
            flat=True
        )

        # Convert skills list to text
        skills_text = " ".join(user_skills)

        # Get latest uploaded resume
        latest_resume = Resume.objects.filter(
            user=user
        ).order_by(
            '-uploaded_at'
        ).first()

        # Default level
        experience_level = "Fresher"

        # Get detected experience level
        if latest_resume:

            experience_level = (
                latest_resume.experience_level
            )

        # ML recommendations with
        # experience filtering
        recommendations = recommend_jobs_ml(

            skills_text,

            experience_level
        )

        return Response(recommendations)