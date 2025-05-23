from src.utils.report_formatter import ReportFormatter
from src.config.settings import ASSESSMENT_AREAS

class ReportGenerationAgent:
    def __init__(self):
        self.role = "Report Generation Specialist"
        self.goal = "Generate personalized analytics maturity assessment reports"
        self.backstory = """You are an expert in creating clear, actionable reports
        that help organizations understand their analytics maturity and
        provide a clear path forward."""
        self.report_formatter = ReportFormatter()

    def generate_report(self, analysis):
        """Generate a personalized report for a single analysis result."""
        if not analysis:
            return "No analysis results to generate report from"
        
        # Create report sections
        executive_summary = self._create_executive_summary(analysis)
        detailed_analysis = self._create_detailed_analysis(analysis)
        recommendations = self._create_recommendations(analysis)
        
        # Format the complete report
        report = {
            'company_name': analysis['company_name'],
            'email': analysis['email'],
            'industry': analysis['industry'],
            'sections': {
                'executive_summary': executive_summary,
                'detailed_analysis': detailed_analysis,
                'recommendations': recommendations
            }
        }
        
        # Format the report using the template
        formatted_report = self.report_formatter.format_report(report)
        return formatted_report

    def _create_executive_summary(self, analysis):
        """Create the executive summary section."""
        return {
            'overall_stage': analysis['overall_stage'],
            'key_strengths': [s['area'] for s in analysis['strengths']],
            'key_weaknesses': [w['area'] for w in analysis['weaknesses']],
            'summary': f"""Based on the assessment, {analysis['company_name']} is at the {analysis['overall_stage']} 
            of analytics maturity. The organization shows particular strength in {', '.join([s['area'] for s in analysis['strengths']])} 
            while areas needing attention include {', '.join([w['area'] for w in analysis['weaknesses']])}."""
        }

    def _create_detailed_analysis(self, analysis):
        """Create the detailed analysis section."""
        detailed_analysis = {
            'maturity_scores': analysis['maturity_scores'],
            'area_analyses': []
        }
        
        for area in ASSESSMENT_AREAS:
            rating = analysis.get(f'{area.lower().replace(" ", "_")}_rating')
            explanation = analysis.get(f'{area.lower().replace(" ", "_")}_explanation')
            if rating and explanation:
                area_analysis = {
                    'area': area,
                    'rating': rating,
                    'explanation': explanation,
                    'score': analysis['maturity_scores'].get(area, 0)
                }
                detailed_analysis['area_analyses'].append(area_analysis)
        
        return detailed_analysis

    def _create_recommendations(self, analysis):
        """Create the recommendations section."""
        return {
            'short_term': analysis['recommendations']['short_term'],
            'medium_term': analysis['recommendations']['medium_term'],
            'long_term': analysis['recommendations']['long_term'],
            'implementation_guidance': self._generate_implementation_guidance(
                analysis['overall_stage'],
                analysis['industry']
            )
        }

    def _generate_implementation_guidance(self, stage, industry):
        """Generate implementation guidance based on stage and industry."""
        guidance = {
            'Foundation Stage': {
                'timeline': '3-6 months',
                'key_focus': 'Building basic analytics infrastructure',
                'success_metrics': [
                    'Data collection automation rate',
                    'Report generation time',
                    'Staff training completion'
                ]
            },
            'Progressive Stage': {
                'timeline': '6-12 months',
                'key_focus': 'Integration and automation',
                'success_metrics': [
                    'Data integration coverage',
                    'Automated report adoption',
                    'Decision-making speed'
                ]
            },
            'Leading/AI-Driven Stage': {
                'timeline': '12-24 months',
                'key_focus': 'AI/ML implementation and optimization',
                'success_metrics': [
                    'AI model accuracy',
                    'Predictive analytics adoption',
                    'ROI from analytics initiatives'
                ]
            }
        }
        
        return guidance.get(stage, guidance['Foundation Stage']) 