from crewai import Agent
from src.utils.google_sheets import GoogleSheetsClient
from config.settings import ASSESSMENT_AREAS

class DataCollectionAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Data Collection Specialist",
            goal="Collect and validate assessment data from Google Sheets",
            backstory="""You are an expert at collecting and validating data from various sources.
            Your specialty is in processing assessment data and ensuring its completeness and accuracy."""
        )
        self.sheets_client = GoogleSheetsClient()

    def execute(self, task):
        # Get new entries from Google Sheets
        new_entries = self.sheets_client.get_new_entries()
        
        if not new_entries:
            return "No new entries found"
        
        processed_data = []
        for entry in new_entries:
            # Validate the entry
            if self._validate_entry(entry):
                processed_data.append(self._format_entry(entry))
        
        return processed_data

    def _validate_entry(self, entry):
        """Validate that all required fields are present and properly formatted."""
        required_fields = ['email', 'company_name', 'industry']
        for field in required_fields:
            if field not in entry or not entry[field]:
                return False
        
        # Validate assessment areas
        for area in ASSESSMENT_AREAS:
            rating_key = f"{area.lower().replace(' ', '_')}_rating"
            explanation_key = f"{area.lower().replace(' ', '_')}_explanation"
            
            if rating_key not in entry or explanation_key not in entry:
                return False
            
            if not entry[rating_key] or not entry[explanation_key]:
                return False
        
        return True

    def _format_entry(self, entry):
        """Format the entry into a standardized structure."""
        formatted_entry = {
            'email': entry['email'],
            'company_name': entry['company_name'],
            'industry': entry['industry'],
            'assessments': {}
        }
        
        for area in ASSESSMENT_AREAS:
            rating_key = f"{area.lower().replace(' ', '_')}_rating"
            explanation_key = f"{area.lower().replace(' ', '_')}_explanation"
            
            formatted_entry['assessments'][area] = {
                'rating': entry[rating_key],
                'explanation': entry[explanation_key]
            }
        
        return formatted_entry 