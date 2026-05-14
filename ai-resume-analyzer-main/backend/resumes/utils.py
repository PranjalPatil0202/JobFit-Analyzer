import fitz  # PyMuPDF
import re


def extract_text_from_pdf(file):
    """
    Extract text from PDF.
    """

    text = ""

    try:

        doc = fitz.open(
            stream=file.read(),
            filetype="pdf"
        )

        for page in doc:

            text += page.get_text()

    except Exception as e:

        print(
            f"Error extracting PDF text: {e}"
        )

        return ""

    finally:

        file.seek(0)

    return text.strip()


# Predefined technical skills
PREDEFINED_SKILLS = [

    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "ruby",
    "php",

    "html",
    "css",

    "react",
    "angular",
    "vue",

    "node.js",
    "django",
    "flask",
    "spring",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "aws",
    "azure",
    "gcp",

    "docker",
    "kubernetes",

    "git",
    "linux",

    "machine learning",
    "nlp",
    "data analysis",

    "agile",
    "scrum",

    "rest api",
    "graphql",

    "tensorflow",
    "pytorch",

    "pandas",
    "numpy"
]


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    if not text:
        return []

    extracted_skills = set()

    text_lower = text.lower()

    for skill in PREDEFINED_SKILLS:

        pattern = (
            r'\b' +
            re.escape(skill) +
            r'\b'
        )

        if re.search(pattern, text_lower):

            formatted_skill = (

                skill.title()

                if len(skill) > 3

                else skill.upper()
            )

            extracted_skills.add(
                formatted_skill
            )

    return list(extracted_skills)


def extract_experience_level(text):
    """
    Detect experience level.
    """

    if not text:
        return "Fresher"

    text = text.lower()

    # Match years
    match = re.search(
        r'(\d+)\+?\s*(years|year|yrs)',
        text
    )

    if match:

        years = int(match.group(1))

        if years == 0:

            return "Fresher"

        elif years <= 2:

            return "Junior"

        elif years <= 5:

            return "Mid-Level"

        else:

            return "Senior"

    # Fresher keywords
    fresher_keywords = [

        'fresher',
        'internship',
        'student',
        'entry level'
    ]

    if any(
        keyword in text
        for keyword in fresher_keywords
    ):

        return "Fresher"

    return "Junior"


def calculate_resume_score(
    skills,
    experience_level,
    resume_text
):
    """
    Calculate ATS resume score.
    """

    score = 0

    strengths = []

    improvements = []

    # Skill score
    skill_count = len(skills)

    if skill_count >= 10:

        score += 40

        strengths.append(
            "Strong technical skill set"
        )

    elif skill_count >= 5:

        score += 25

        strengths.append(
            "Good technical skills"
        )

    else:

        score += 10

        improvements.append(
            "Add more technical skills"
        )

    # Experience score
    if experience_level == "Senior":

        score += 20

        strengths.append(
            "Strong professional experience"
        )

    elif experience_level == "Mid-Level":

        score += 15

    elif experience_level == "Junior":

        score += 10

    else:

        score += 5

        improvements.append(
            "Gain internship or project experience"
        )

    # Resume quality score
    word_count = len(
        resume_text.split()
    )

    if word_count >= 500:

        score += 20

        strengths.append(
            "Detailed resume content"
        )

    elif word_count >= 250:

        score += 15

    else:

        score += 5

        improvements.append(
            "Add more detailed content"
        )

    # Advanced skills
    advanced_skills = [

        "AWS",
        "Docker",
        "Kubernetes",
        "Tensorflow",
        "Pytorch",
        "Machine Learning"
    ]

    found_advanced = [

        skill for skill in skills

        if skill in advanced_skills
    ]

    if len(found_advanced) >= 3:

        score += 20

        strengths.append(
            "Strong modern technology stack"
        )

    elif len(found_advanced) >= 1:

        score += 10

    else:

        improvements.append(
            "Learn cloud and DevOps technologies"
        )

    # Limit score
    score = min(score, 100)

    return {

        "score": score,

        "strengths": strengths,

        "improvements": improvements
    }


def generate_ai_resume_suggestions(
    skills,
    experience_level,
    resume_text
):
    """
    Generate AI-like resume suggestions.
    """

    suggestions = []

    text = resume_text.lower()

    # Project suggestions
    if 'project' not in text:

        suggestions.append(
            "Add project details to strengthen your resume."
        )

    # Certification suggestions
    if 'certification' not in text:

        suggestions.append(
            "Add certifications to improve credibility."
        )

    # GitHub suggestion
    if 'github' not in text:

        suggestions.append(
            "Include your GitHub profile link."
        )

    # LinkedIn suggestion
    if 'linkedin' not in text:

        suggestions.append(
            "Include your LinkedIn profile."
        )

    # Cloud skills suggestion
    cloud_skills = [

        'AWS',
        'Docker',
        'Kubernetes'
    ]

    if not any(
        skill in skills
        for skill in cloud_skills
    ):

        suggestions.append(
            "Learn cloud and DevOps technologies."
        )

    # Fresher suggestions
    if experience_level == "Fresher":

        suggestions.append(
            "Add internships or freelance work experience."
        )

    return suggestions[:5]


def recommend_career_paths(skills):
    """
    Recommend career paths
    based on extracted skills.
    """

    career_paths = []

    skills_lower = [

        skill.lower()

        for skill in skills
    ]

    # Backend Developer
    backend_skills = [

        'python',
        'django',
        'flask',
        'sql',
        'postgresql',
        'mysql'
    ]

    if any(
        skill in skills_lower
        for skill in backend_skills
    ):

        career_paths.append(
            "Backend Developer"
        )

    # Frontend Developer
    frontend_skills = [

        'javascript',
        'react',
        'html',
        'css',
        'typescript'
    ]

    if any(
        skill in skills_lower
        for skill in frontend_skills
    ):

        career_paths.append(
            "Frontend Developer"
        )

    # Full Stack Developer
    if (

        any(
            skill in skills_lower
            for skill in backend_skills
        )

        and

        any(
            skill in skills_lower
            for skill in frontend_skills
        )
    ):

        career_paths.append(
            "Full Stack Developer"
        )

    # Machine Learning Engineer
    ml_skills = [

        'machine learning',
        'tensorflow',
        'pytorch',
        'numpy',
        'pandas',
        'nlp'
    ]

    if any(
        skill in skills_lower
        for skill in ml_skills
    ):

        career_paths.append(
            "Machine Learning Engineer"
        )

    # Cloud Engineer
    cloud_skills = [

        'aws',
        'docker',
        'kubernetes'
    ]

    if any(
        skill in skills_lower
        for skill in cloud_skills
    ):

        career_paths.append(
            "Cloud Engineer"
        )

    # Data Analyst
    data_skills = [

        'pandas',
        'numpy',
        'sql',
        'data analysis'
    ]

    if any(
        skill in skills_lower
        for skill in data_skills
    ):

        career_paths.append(
            "Data Analyst"
        )

    # Default fallback
    if not career_paths:

        career_paths.append(
            "Software Developer"
        )

    return career_paths[:5]


def is_valid_resume(text):
    """
    Validate whether uploaded PDF
    is actually a resume.
    """

    if not text:
        return False

    text = text.lower()

    # Resume-related keywords
    resume_keywords = [

        'skills',
        'education',
        'experience',
        'projects',
        'internship',
        'summary',
        'certification',
        'technical',
        'profile',
        'objective'
    ]

    # Count matching keywords
    match_count = sum(

        keyword in text

        for keyword in resume_keywords
    )

    # Resume should contain
    # at least 2 keywords
    if match_count >= 2:

        return True

    return False