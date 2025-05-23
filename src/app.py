from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
from src.agents.analysis_agent import AnalysisAgent
from src.agents.report_generation_agent import ReportGenerationAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize agents
analysis_agent = AnalysisAgent()
report_agent = ReportGenerationAgent()

@app.route('/')
def home():
    return render_template_string('''
        <h1>Analytics Maturity Assessment API</h1>
        <p>This is the backend API. The user interface is hosted on <a href="https://your-github-username.github.io/your-repo-name/" target="_blank">GitHub Pages</a>.</p>
    ''')

@app.route('/api/analyze', methods=['POST'])
def analyze_assessment():
    """Endpoint to analyze assessment data and generate a report."""
    try:
        # Get assessment data from request
        assessment_data = request.json
        
        # Validate required fields
        required_fields = ['company_name', 'industry']
        for field in required_fields:
            if field not in assessment_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Process assessment
        analysis_result = analysis_agent.process_assessment(assessment_data)
        
        # Generate report
        report_path = report_agent.generate_report(analysis_result)
        
        if not report_path:
            return jsonify({'error': 'Failed to generate report'}), 500
        
        # Return analysis results and report path
        return jsonify({
            'analysis': analysis_result,
            'report_path': report_path
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/report/<filename>', methods=['GET'])
def get_report(filename):
    """Endpoint to download generated reports."""
    try:
        reports_dir = os.path.join(os.path.dirname(__file__), '../reports')
        file_path = os.path.join(reports_dir, filename)
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'Report not found'}), 404
            
        return send_file(file_path, as_attachment=True)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create reports directory if it doesn't exist
    reports_dir = os.path.join(os.path.dirname(__file__), '../reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    # Run the Flask application
    app.run(debug=True, port=5000) 