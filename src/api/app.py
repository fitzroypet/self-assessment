from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime
from src.agents.assessment_agent import AssessmentAgent
from src.utils.report_generator import ReportGenerator

app = Flask(__name__)
CORS(app)

# Initialize agents and utilities
assessment_agent = AssessmentAgent()
report_generator = ReportGenerator()

@app.route('/api/submit-assessment', methods=['POST'])
def submit_assessment():
    try:
        data = request.json
        
        # Process the assessment using the assessment agent
        assessment_results = assessment_agent.process_assessment(data)
        
        # Generate the report
        report_path = report_generator.generate_report(assessment_results)
        
        return jsonify({
            'success': True,
            'message': 'Assessment processed successfully',
            'report_path': report_path
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/download-report/<path:filename>', methods=['GET'])
def download_report(filename):
    try:
        return send_file(
            filename,
            as_attachment=True,
            download_name=f'analytics_maturity_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        )
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 