from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

class ReportFormatter:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Set up custom paragraph styles."""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=30
        ))
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading1'],
            fontSize=18,
            spaceAfter=12
        ))
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=12
        ))

    def format_report(self, report):
        """Format a report as a PDF."""
        try:
            # Create output directory if it doesn't exist
            output_dir = os.path.join(os.path.dirname(__file__), '../../reports')
            os.makedirs(output_dir, exist_ok=True)
            
            # Create PDF file
            filename = f"analytics_maturity_report_{report['company_name'].lower().replace(' ', '_')}.pdf"
            filepath = os.path.join(output_dir, filename)
            doc = SimpleDocTemplate(filepath, pagesize=letter)
            
            # Build the document content
            story = []
            
            # Title
            story.append(Paragraph(f"Analytics Maturity Assessment Report", self.styles['CustomTitle']))
            story.append(Paragraph(f"Company: {report['company_name']}", self.styles['CustomBody']))
            story.append(Paragraph(f"Industry: {report['industry']}", self.styles['CustomBody']))
            story.append(Spacer(1, 20))
            
            # Executive Summary
            story.append(Paragraph("Executive Summary", self.styles['CustomHeading']))
            summary = report['sections']['executive_summary']
            story.append(Paragraph(summary['summary'], self.styles['CustomBody']))
            story.append(Spacer(1, 20))
            
            # Detailed Analysis
            story.append(Paragraph("Detailed Analysis", self.styles['CustomHeading']))
            analysis = report['sections']['detailed_analysis']
            
            # Maturity Scores Table
            data = [['Area', 'Maturity Level', 'Score']]
            for area_analysis in analysis['area_analyses']:
                data.append([
                    area_analysis['area'],
                    area_analysis['rating'],
                    str(area_analysis['score'])
                ])
            
            table = Table(data, colWidths=[2*inch, 2*inch, 1*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            story.append(Spacer(1, 20))
            
            # Recommendations
            story.append(Paragraph("Recommendations", self.styles['CustomHeading']))
            recommendations = report['sections']['recommendations']
            
            # Short-term recommendations
            story.append(Paragraph("Short-term Recommendations", self.styles['CustomBody']))
            for rec in recommendations['short_term']:
                story.append(Paragraph(f"• {rec}", self.styles['CustomBody']))
            story.append(Spacer(1, 12))
            
            # Medium-term recommendations
            story.append(Paragraph("Medium-term Recommendations", self.styles['CustomBody']))
            for rec in recommendations['medium_term']:
                story.append(Paragraph(f"• {rec}", self.styles['CustomBody']))
            story.append(Spacer(1, 12))
            
            # Long-term recommendations
            story.append(Paragraph("Long-term Recommendations", self.styles['CustomBody']))
            for rec in recommendations['long_term']:
                story.append(Paragraph(f"• {rec}", self.styles['CustomBody']))
            story.append(Spacer(1, 20))
            
            # Implementation Guidance
            guidance = recommendations['implementation_guidance']
            story.append(Paragraph("Implementation Guidance", self.styles['CustomHeading']))
            story.append(Paragraph(f"Timeline: {guidance['timeline']}", self.styles['CustomBody']))
            story.append(Paragraph(f"Key Focus: {guidance['key_focus']}", self.styles['CustomBody']))
            story.append(Paragraph("Success Metrics:", self.styles['CustomBody']))
            for metric in guidance['success_metrics']:
                story.append(Paragraph(f"• {metric}", self.styles['CustomBody']))
            
            # Build the PDF
            doc.build(story)
            
            return filepath
            
        except Exception as e:
            print(f"Error formatting report: {str(e)}")
            return None

    def _format_maturity_score(self, score):
        """Format a maturity score for display."""
        if score <= 1.5:
            return "Basic"
        elif score <= 2.5:
            return "Developing"
        else:
            return "Advanced"

    def _format_recommendations(self, recommendations):
        """Format recommendations for display."""
        formatted = {
            'short_term': [],
            'medium_term': [],
            'long_term': []
        }
        
        for timeframe, items in recommendations.items():
            for item in items:
                formatted[timeframe].append({
                    'text': item,
                    'priority': self._determine_priority(item)
                })
        
        return formatted

    def _determine_priority(self, recommendation):
        """Determine the priority of a recommendation."""
        high_priority_keywords = ['critical', 'urgent', 'immediate', 'essential']
        medium_priority_keywords = ['important', 'significant', 'valuable']
        
        recommendation_lower = recommendation.lower()
        
        if any(keyword in recommendation_lower for keyword in high_priority_keywords):
            return 'high'
        elif any(keyword in recommendation_lower for keyword in medium_priority_keywords):
            return 'medium'
        else:
            return 'normal' 