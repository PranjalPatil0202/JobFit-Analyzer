from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from .utils import calculate_skill_overlap

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def recommendations(self, request):
        user = request.user
        # Fetch user's skills
        user_skills = user.skills.values_list('name', flat=True)
        
        jobs = Job.objects.all()
        job_recommendations = []
        
        for job in jobs:
            score = calculate_skill_overlap(user_skills, job.required_skills)
            
            # Serialize the job and inject the match score
            job_data = self.get_serializer(job).data
            job_data['match_score'] = score
            job_recommendations.append(job_data)
            
        # Sort jobs by match_score descending
        job_recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        return Response(job_recommendations)
