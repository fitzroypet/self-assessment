import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4"  # or your preferred model

# Google Sheets settings (optional, for storing responses)
GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

# Application settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Assessment areas and their corresponding spreadsheet columns
SPREADSHEET_COLUMNS = {
    'submission_id': 'Submission ID',
    'respondent_id': 'Respondent ID',
    'submitted_at': 'Submitted at',
    'email': 'What is your email address?',
    'company_name': 'What is your company name?',
    'industry': 'Which industry best describes your business?',
    'company_size': 'What is the size of your company?',
    'business_description': 'Please briefly describe your business and what you do.',
    'reporting_rating': 'How would you rate your reporting capabilities?',
    'reporting_explanation': 'Please explain your data collection process.',
    'analytics_type_rating': 'What best describes the type of analytics you use?',
    'analytics_type_explanation': 'Please explain your analytics use.',
    'tool_usage_rating': 'How would you rate your analytics tool usage?',
    'tool_usage_explanation': 'Please explain your analytics toolset.',
    'decision_making_rating': 'How would you describe your decision-making process?',
    'decision_making_explanation': 'Please explain how data influences your decisions.',
    'skills_rating': 'How would you rate your team\'s analytics skills?',
    'skills_explanation': 'Please explain your team\'s analytics skills and training.',
    'additional_comments': 'Is there anything else you\'d like to share about your analytics journey, challenges, or goals?'
}

# Assessment areas for processing
ASSESSMENT_AREAS = [
    "Reporting",
    "Analytics Type",
    "Tool Usage",
    "Decision-Making",
    "Skills"
]

# Maturity levels
MATURITY_LEVELS = ["Basic", "Developing", "Advanced"] 