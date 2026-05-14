import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Get dataset path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "datasets", "jobs.csv")

# Load CSV
jobs_df = pd.read_csv(csv_path)

# Print columns for debugging
print(jobs_df.columns)

# Fill missing values
jobs_df['Job Title'] = jobs_df['Job Title'].fillna('')
jobs_df['Job Description'] = jobs_df['Job Description'].fillna('')

# Combine title + description
jobs_df['combined_text'] = (
    jobs_df['Job Title'] + ' ' +
    jobs_df['Job Description']
)

# Create TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')

job_vectors = vectorizer.fit_transform(
    jobs_df['combined_text']
)

def recommend_jobs_ml(resume_skills):

    # Convert resume text into vector
    resume_vector = vectorizer.transform([resume_skills])

    # Calculate similarity
    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )

    # Get top matching jobs
    top_indices = similarities[0].argsort()[-20:][::-1]

    recommendations = []
    seen_titles = set()

    for idx in top_indices:

        title = jobs_df.iloc[idx]['Job Title']

        # Skip duplicate titles
        if title in seen_titles:
            continue

        seen_titles.add(title)

        recommendations.append({
            "title": title,
            "description": jobs_df.iloc[idx]['Job Description'][:200],
            "match_score": round(similarities[0][idx] * 100, 2)
        })

        # Limit to 5 unique jobs
        if len(recommendations) == 5:
            break

    return recommendations