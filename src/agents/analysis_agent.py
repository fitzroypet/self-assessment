from src.config.settings import ASSESSMENT_AREAS, MATURITY_LEVELS

class AnalysisAgent:
    def __init__(self):
        self.role = "Analytics Maturity Analyst"
        self.goal = "Analyze assessment data and determine maturity stage"
        self.backstory = """You are an expert in analytics maturity assessment.
        Your specialty is in analyzing organizations' analytics capabilities
        and providing detailed insights about their current state and potential improvements."""

    def process_assessment(self, assessment_data):
        """Process a single assessment entry."""
        if not assessment_data:
            return "No assessment data to analyze"
        
        # Calculate overall maturity score
        maturity_scores = self._calculate_maturity_scores(assessment_data)
        overall_stage = self._determine_overall_stage(maturity_scores)
        
        # Analyze strengths and weaknesses
        strengths = self._identify_strengths(assessment_data)
        weaknesses = self._identify_weaknesses(assessment_data)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            overall_stage,
            strengths,
            weaknesses,
            assessment_data.get('industry', '')
        )
        
        return {
            'company_name': assessment_data.get('company_name', ''),
            'email': assessment_data.get('email', ''),
            'industry': assessment_data.get('industry', ''),
            'overall_stage': overall_stage,
            'maturity_scores': maturity_scores,
            'strengths': strengths,
            'weaknesses': weaknesses,
            'recommendations': recommendations
        }

    def _calculate_maturity_scores(self, assessment_data):
        """Calculate maturity scores for each area."""
        scores = {}
        for area in ASSESSMENT_AREAS:
            rating = assessment_data.get(f'{area.lower().replace(" ", "_")}_rating')
            if rating:
                scores[area] = MATURITY_LEVELS.index(rating) + 1
        return scores

    def _determine_overall_stage(self, maturity_scores):
        """Determine the overall maturity stage based on scores."""
        if not maturity_scores:
            return "Foundation Stage"
            
        avg_score = sum(maturity_scores.values()) / len(maturity_scores)
        if avg_score <= 1.5:
            return "Foundation Stage"
        elif avg_score <= 2.5:
            return "Progressive Stage"
        else:
            return "Leading/AI-Driven Stage"

    def _identify_strengths(self, assessment_data):
        """Identify areas of strength (Advanced ratings)."""
        strengths = []
        for area in ASSESSMENT_AREAS:
            rating = assessment_data.get(f'{area.lower().replace(" ", "_")}_rating')
            explanation = assessment_data.get(f'{area.lower().replace(" ", "_")}_explanation')
            if rating == "Advanced" and explanation:
                strengths.append({
                    'area': area,
                    'explanation': explanation
                })
        return strengths

    def _identify_weaknesses(self, assessment_data):
        """Identify areas of weakness (Basic ratings)."""
        weaknesses = []
        for area in ASSESSMENT_AREAS:
            rating = assessment_data.get(f'{area.lower().replace(" ", "_")}_rating')
            explanation = assessment_data.get(f'{area.lower().replace(" ", "_")}_explanation')
            if rating == "Basic" and explanation:
                weaknesses.append({
                    'area': area,
                    'explanation': explanation
                })
        return weaknesses

    def _generate_recommendations(self, overall_stage, strengths, weaknesses, industry):
        """Generate recommendations based on the analysis."""
        recommendations = {
            'short_term': [],
            'medium_term': [],
            'long_term': []
        }
        
        # Add stage-specific recommendations
        if overall_stage == "Foundation Stage":
            recommendations['short_term'].extend([
                "Digitize data collection processes",
                "Implement basic reporting tools",
                "Train key staff on data fundamentals"
            ])
        elif overall_stage == "Progressive Stage":
            recommendations['short_term'].extend([
                "Integrate data sources",
                "Implement automated reporting",
                "Develop data governance framework"
            ])
        else:
            recommendations['short_term'].extend([
                "Pilot AI/ML initiatives",
                "Implement predictive analytics",
                "Develop data-driven decision frameworks"
            ])
        
        # Add industry-specific recommendations
        if industry.lower() in ['retail', 'ecommerce']:
            recommendations['medium_term'].append(
                "Implement customer analytics and segmentation"
            )
        elif industry.lower() in ['manufacturing', 'production']:
            recommendations['medium_term'].append(
                "Implement predictive maintenance analytics"
            )
        
        return recommendations 