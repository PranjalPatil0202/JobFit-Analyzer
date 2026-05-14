import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Get dataset path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_path = os.path.join(
    BASE_DIR,
    "datasets",
    "jobs.csv"
)

# Load dataset
jobs_df = pd.read_csv(csv_path)

# Debug columns
print(jobs_df.columns)

# Fill missing values
jobs_df['Job Title'] = jobs_df[
    'Job Title'
].fillna('')

jobs_df['Job Description'] = jobs_df[
    'Job Description'
].fillna('')

# Combine title + description
jobs_df['combined_text'] = (

    jobs_df['Job Title'] + ' ' +

    jobs_df['Job Description']
)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    stop_words='english'
)

# Create vectors
job_vectors = vectorizer.fit_transform(
    jobs_df['combined_text']
)

# Common technical skills
TECH_SKILLS = [

    "python",
    "java",
    "javascript",
    "react",
    "django",
    "flask",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "aws",
    "docker",
    "kubernetes",
    "tensorflow",
    "pytorch",
    "machine learning",
    "nlp",
    "git",
    "linux",
    "rest api",
    "graphql",
    "pandas",
    "numpy"
]


def extract_job_skills(text):
    """
    Extract technical skills
    from job description.
    """

    text = text.lower()

    found_skills = []

    for skill in TECH_SKILLS:

        if skill in text:

            found_skills.append(
                skill.title()
            )

    return found_skills


def detect_job_level(job_text):
    """
    Detect job seniority level.
    """

    text = job_text.lower()

    # Senior jobs
    senior_keywords = [

        'senior',
        'lead',
        'architect',
        'manager',
        '5+ years',
        '7+ years'
    ]

    # Mid-level jobs
    mid_keywords = [

        'mid',
        '3+ years',
        'experienced'
    ]

    # Fresher jobs
    fresher_keywords = [

        'intern',
        'internship',
        'fresher',
        'entry level',
        'junior',
        '0-1 year'
    ]

    if any(
        word in text
        for word in senior_keywords
    ):
        return "Senior"

    elif any(
        word in text
        for word in mid_keywords
    ):
        return "Mid-Level"

    elif any(
        word in text
        for word in fresher_keywords
    ):
        return "Fresher"

    return "Junior"


def recommend_jobs_ml(
    resume_skills,
    experience_level="Fresher"
):
    """
    Recommend jobs using:
    - TF-IDF similarity
    - Experience filtering
    - Missing skill analysis
    """

    # Convert resume skills into vector
    resume_vector = vectorizer.transform(
        [resume_skills]
    )

    # Similarity scores
    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )

    # Top matches
    top_indices = similarities[0].argsort()[-30:][::-1]

    recommendations = []

    seen_titles = set()

    # Resume skill set
    resume_skill_set = set(

        skill.strip().lower()

        for skill in resume_skills.split()
    )

    for idx in top_indices:

        title = jobs_df.iloc[idx][
            'Job Title'
        ]

        description = jobs_df.iloc[idx][
            'Job Description'
        ]

        # Skip duplicates
        if title in seen_titles:
            continue

        seen_titles.add(title)

        # Detect job level
        job_level = detect_job_level(

            title + " " + description
        )

        # Experience filtering
        allowed = False

        if experience_level == "Fresher":

            allowed = job_level in [
                "Fresher",
                "Junior"
            ]

        elif experience_level == "Junior":

            allowed = job_level in [
                "Junior",
                "Mid-Level"
            ]

        elif experience_level == "Mid-Level":

            allowed = job_level in [
                "Mid-Level",
                "Senior"
            ]

        else:

            allowed = True

        # Skip disallowed jobs
        if not allowed:
            continue

        # Extract job skills
        job_skills = extract_job_skills(
            description
        )

        # Missing skills
        missing_skills = [

            skill

            for skill in job_skills

            if skill.lower()
            not in resume_skill_set
        ]

        recommendations.append({

            "title": title,

            "description":
            description[:200],

            "match_score":
            round(
                similarities[0][idx] * 100,
                2
            ),

            "experience_level":
            job_level,

            "missing_skills":
            missing_skills[:5]
        })

        # Top 5 jobs
        if len(recommendations) == 5:
            break

    return recommendations