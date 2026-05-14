def calculate_skill_overlap(user_skills, job_skills_text):
    """
    Calculates the overlap percentage between user's skills and a job's required skills.
    Returns a score between 0 and 100.
    """
    if not user_skills or not job_skills_text:
        return 0.0
        
    # Standardize and parse job skills (assuming comma separated)
    job_skills = set(skill.strip().lower() for skill in job_skills_text.split(',') if skill.strip())
    
    # Standardize user skills
    user_skills_set = set(skill.lower() for skill in user_skills)
    
    if not job_skills:
        return 0.0
        
    # Calculate overlap
    intersection = user_skills_set.intersection(job_skills)
    overlap_percentage = (len(intersection) / len(job_skills)) * 100
    
    return round(overlap_percentage, 2)
