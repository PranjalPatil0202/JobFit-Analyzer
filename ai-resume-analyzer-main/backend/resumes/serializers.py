from rest_framework import serializers
from .models import Resume, Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')

class ResumeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ('id', 'user', 'resume_file', 'extracted_text', 'skills', 'uploaded_at')
        read_only_fields = ('user', 'extracted_text', 'uploaded_at')
