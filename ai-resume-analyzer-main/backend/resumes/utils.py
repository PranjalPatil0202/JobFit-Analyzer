import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file):
    """
    Extracts text from a given PDF file object.
    """
    text = ""
    try:
        # Open the PDF directly from the file stream using PyMuPDF
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    finally:
        # Reset the file pointer so Django can save it properly later
        file.seek(0)
    return text.strip()

# A basic predefined list of common tech skills
PREDEFINED_SKILLS = [
    "python", "java", "c++", "c#", "javascript", "typescript", "ruby", "php",
    "html", "css", "react", "angular", "vue", "node.js", "django", "flask",
    "spring", "sql", "mysql", "postgresql", "mongodb", "aws", "azure", "gcp",
    "docker", "kubernetes", "git", "linux", "machine learning", "nlp",
    "data analysis", "agile", "scrum", "rest api", "graphql", "tensorflow",
    "pytorch", "pandas", "numpy"
]

def extract_skills(text):
    """
    Extracts skills from a given text using a predefined skill list and regex keyword matching.
    """
    if not text:
        return []
        
    extracted_skills = set()
    text_lower = text.lower()
    
    for skill in PREDEFINED_SKILLS:
        # Create a regex pattern with word boundaries.
        # re.escape is used to handle skills with special characters like C++ or Node.js
        pattern = r'\b' + re.escape(skill) + r'\b'
        
        # Search for the pattern in the lowercased text
        if re.search(pattern, text_lower):
            extracted_skills.add(skill.title() if len(skill) > 3 else skill.upper())
            
    return list(extracted_skills)
