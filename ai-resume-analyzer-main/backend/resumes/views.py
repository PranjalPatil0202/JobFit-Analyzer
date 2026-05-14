from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .models import Resume, Skill
from .serializers import ResumeSerializer

from .utils import (

    extract_text_from_pdf,

    extract_skills,

    extract_experience_level,

    calculate_resume_score,

    generate_ai_resume_suggestions,

    recommend_career_paths,

    is_valid_resume
)


class ResumeListView(generics.ListAPIView):

    serializer_class = ResumeSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):

        return Resume.objects.filter(
            user=self.request.user
        ).order_by('-uploaded_at')


class ResumeUploadView(generics.CreateAPIView):

    queryset = Resume.objects.all()

    serializer_class = ResumeSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):

        resume_file = self.request.data.get(
            'resume_file'
        )

        extracted_text = ""

        extracted_skills_list = []

        experience_level = "Fresher"

        if resume_file:

            try:

                # Extract PDF text
                extracted_text = (
                    extract_text_from_pdf(
                        resume_file
                    )
                )

                # Empty PDF check
                if not extracted_text.strip():

                    raise ValidationError({

                        "detail":
                        "Could not extract text from PDF."
                    })

                # Resume validation
                if not is_valid_resume(
                    extracted_text
                ):

                    raise ValidationError({

                        "detail":
                        "Uploaded PDF does not appear to be a valid resume."
                    })

                # Extract skills
                extracted_skills_list = (
                    extract_skills(
                        extracted_text
                    )
                )

                # Detect experience level
                experience_level = (
                    extract_experience_level(
                        extracted_text
                    )
                )

                # Calculate ATS score
                score_data = (
                    calculate_resume_score(

                        extracted_skills_list,

                        experience_level,

                        extracted_text
                    )
                )

                # Generate AI suggestions
                ai_suggestions = (
                    generate_ai_resume_suggestions(

                        extracted_skills_list,

                        experience_level,

                        extracted_text
                    )
                )

                # Recommend career paths
                career_paths = (
                    recommend_career_paths(
                        extracted_skills_list
                    )
                )

                print(
                    "Experience Level:",
                    experience_level
                )

                print(
                    "Resume Score:",
                    score_data["score"]
                )

                print(
                    "Career Paths:",
                    career_paths
                )

            except Exception as e:

                raise ValidationError({

                    "detail":
                    f"Failed to process resume: {str(e)}"
                })

        else:

            raise ValidationError({

                "detail":
                "No resume file provided."
            })

        # Save resume
        resume = serializer.save(

            user=self.request.user,

            extracted_text=extracted_text,

            experience_level=experience_level,

            resume_score=score_data["score"],

            strengths=score_data["strengths"],

            improvements=score_data["improvements"],

            ai_suggestions=ai_suggestions,

            career_paths=career_paths
        )

        # Save extracted skills
        for skill_name in extracted_skills_list:

            skill_obj, _ = Skill.objects.get_or_create(

                user=self.request.user,

                name=skill_name
            )

            resume.skills.add(skill_obj)