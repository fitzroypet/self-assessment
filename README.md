# Self Assessment Tool

A web-based self-assessment tool that helps evaluate different areas of expertise including Strategy, Data, Technology, People, and Process.

## Features

- Interactive assessment form with multiple areas of evaluation
- Rating system (Basic, Intermediate, Advanced)
- Detailed explanation fields for each area
- API integration for analysis
- Report generation and download capability

## Setup

1. Clone the repository:
```bash
git clone https://github.com/fitzroypet/self-assessment.git
cd self-assessment
```

2. Set up the backend (Flask):
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

3. Open the frontend:
- Open `frontend/index.html` in your web browser
- Or serve it using a local web server

## Usage

1. Fill out the assessment form for each area
2. Submit the form to get analysis
3. Download the generated report

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- API: RESTful endpoints for analysis

## Development

- Run tests: `pytest`
- Format code: `black .`
- Lint code: `flake8`

## Project Structure

- `src/`: Main application code
- `config/`: Configuration files
- `templates/`: Email and report templates
- `tests/`: Test files
- `.github/workflows/`: GitHub Actions workflows 