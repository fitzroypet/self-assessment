import requests
import json

def test_assessment():
    # Test assessment data
    assessment_data = {
        "company_name": "Test Company",
        "industry": "Technology",
        "data_collection_rating": "Advanced",
        "data_collection_explanation": "We have automated data collection processes",
        "data_quality_rating": "Basic",
        "data_quality_explanation": "Need to improve data validation",
        "analytics_tools_rating": "Developing",
        "analytics_tools_explanation": "Using basic BI tools",
        "data_governance_rating": "Basic",
        "data_governance_explanation": "No formal governance framework",
        "team_capabilities_rating": "Developing",
        "team_capabilities_explanation": "Some team members have analytics skills"
    }

    # Send request to analyze endpoint
    response = requests.post(
        'http://localhost:5000/api/analyze',
        json=assessment_data
    )

    if response.status_code == 200:
        result = response.json()
        print("Analysis successful!")
        print("\nAnalysis Results:")
        print(json.dumps(result['analysis'], indent=2))
        print("\nReport generated at:", result['report_path'])
    else:
        print("Error:", response.json()['error'])

if __name__ == '__main__':
    test_assessment() 