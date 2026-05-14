from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer
from .recommendation_engine import recommend_jobs_ml


class JobViewSet(viewsets.ModelViewSet):

    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def recommendations(self, request):

        user = request.user

        # Fetch user's extracted skills
        user_skills = user.skills.values_list('name', flat=True)

        # Convert list to text
        skills_text = " ".join(user_skills)

        # Get ML recommendations
        recommendations = recommend_jobs_ml(skills_text)

        return Response(recommendations)