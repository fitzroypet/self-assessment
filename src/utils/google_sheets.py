import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import GOOGLE_SHEETS_CREDENTIALS, SPREADSHEET_ID, SPREADSHEET_COLUMNS

class GoogleSheetsClient:
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            GOOGLE_SHEETS_CREDENTIALS, self.scope)
        self.client = gspread.authorize(self.credentials)
        self.spreadsheet = self.client.open_by_key(SPREADSHEET_ID)
        self.worksheet = self.spreadsheet.sheet1

    def get_new_entries(self):
        """Get new entries from the Google Sheet."""
        try:
            # Get all data from the sheet
            data = self.worksheet.get_all_records()
            
            # Filter for new entries (not processed)
            new_entries = []
            for row in data:
                if not row.get('processed', False):
                    formatted_entry = self._format_entry(row)
                    if formatted_entry:  # Only add if formatting was successful
                        new_entries.append(formatted_entry)
            
            return new_entries
            
        except Exception as e:
            print(f"Error getting new entries: {str(e)}")
            return []

    def mark_as_processed(self, row_index):
        """Mark an entry as processed."""
        try:
            # Add a 'processed' column if it doesn't exist
            headers = self.worksheet.row_values(1)
            if 'processed' not in headers:
                self.worksheet.update_cell(1, len(headers) + 1, 'processed')
            
            # Mark the row as processed
            self.worksheet.update_cell(row_index + 1, len(headers) + 1, 'TRUE')
            
        except Exception as e:
            print(f"Error marking entry as processed: {str(e)}")

    def _format_entry(self, row):
        """Format a row from the sheet into a standardized structure."""
        try:
            # Basic validation
            required_fields = ['email', 'company_name', 'industry']
            for field in required_fields:
                if not row.get(SPREADSHEET_COLUMNS[field]):
                    print(f"Missing required field: {field}")
                    return None

            # Format the entry
            formatted_entry = {
                'submission_id': row.get(SPREADSHEET_COLUMNS['submission_id']),
                'respondent_id': row.get(SPREADSHEET_COLUMNS['respondent_id']),
                'submitted_at': row.get(SPREADSHEET_COLUMNS['submitted_at']),
                'email': row.get(SPREADSHEET_COLUMNS['email']),
                'company_name': row.get(SPREADSHEET_COLUMNS['company_name']),
                'industry': row.get(SPREADSHEET_COLUMNS['industry']),
                'company_size': row.get(SPREADSHEET_COLUMNS['company_size']),
                'business_description': row.get(SPREADSHEET_COLUMNS['business_description']),
                'assessments': {
                    'Reporting': {
                        'rating': row.get(SPREADSHEET_COLUMNS['reporting_rating']),
                        'explanation': row.get(SPREADSHEET_COLUMNS['reporting_explanation'])
                    },
                    'Analytics Type': {
                        'rating': row.get(SPREADSHEET_COLUMNS['analytics_type_rating']),
                        'explanation': row.get(SPREADSHEET_COLUMNS['analytics_type_explanation'])
                    },
                    'Tool Usage': {
                        'rating': row.get(SPREADSHEET_COLUMNS['tool_usage_rating']),
                        'explanation': row.get(SPREADSHEET_COLUMNS['tool_usage_explanation'])
                    },
                    'Decision-Making': {
                        'rating': row.get(SPREADSHEET_COLUMNS['decision_making_rating']),
                        'explanation': row.get(SPREADSHEET_COLUMNS['decision_making_explanation'])
                    },
                    'Skills': {
                        'rating': row.get(SPREADSHEET_COLUMNS['skills_rating']),
                        'explanation': row.get(SPREADSHEET_COLUMNS['skills_explanation'])
                    }
                },
                'additional_comments': row.get(SPREADSHEET_COLUMNS['additional_comments'])
            }
            
            return formatted_entry
            
        except Exception as e:
            print(f"Error formatting entry: {str(e)}")
            return None 