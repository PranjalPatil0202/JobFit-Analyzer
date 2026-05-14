from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Resume, Skill
from .serializers import ResumeSerializer
from .utils import extract_text_from_pdf, extract_skills

class ResumeListView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user).order_by('-uploaded_at')

class ResumeUploadView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume_file = self.request.data.get('resume_file')
        extracted_text = ""
        extracted_skills_list = []
        
        if resume_file:
            try:
                extracted_text = extract_text_from_pdf(resume_file)
                if not extracted_text.strip():
                    raise ValidationError({"detail": "Could not extract any text from the provided file. Please ensure it is a valid, readable PDF."})
                extracted_skills_list = extract_skills(extracted_text)
            except Exception as e:
                raise ValidationError({"detail": f"Failed to process the resume file: {str(e)}"})
        else:
            raise ValidationError({"detail": "No resume file was provided."})
            
        resume = serializer.save(user=self.request.user, extracted_text=extracted_text)
        
        for skill_name in extracted_skills_list:
            skill_obj, _ = Skill.objects.get_or_create(
                user=self.request.user,
                name=skill_name
            )
            resume.skills.add(skill_obj)
