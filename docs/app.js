// Multi-step form navigation and logic

document.addEventListener('DOMContentLoaded', () => {
    // Sections
    const welcomeSection = document.getElementById('welcome-section');
    const form = document.getElementById('assessment-form');
    const step1 = document.getElementById('step-1');
    const step2 = document.getElementById('step-2');
    const thankyouSection = document.getElementById('thankyou-section');

    // Buttons
    const startBtn = document.getElementById('start-btn');
    const toStep2Btn = document.getElementById('to-step-2');
    const backToStep1Btn = document.getElementById('back-to-step-1');

    // Show only the given section
    function showSection(section) {
        [welcomeSection, form, step1, step2, thankyouSection].forEach(s => {
            if (s) s.classList.add('hidden');
        });
        if (section) section.classList.remove('hidden');
    }

    // Start assessment
    startBtn.addEventListener('click', () => {
        showSection(form);
        showSection(step1);
    });

    // Next to Step 2
    toStep2Btn.addEventListener('click', () => {
        // Validate Step 1
        const email = form.elements['email'].value.trim();
        const company = form.elements['company_name'].value.trim();
        const industry = form.elements['industry'].value;
        const size = form.elements['company_size'].value;
        if (!email || !company || !industry || !size) {
            alert('Please fill in all required fields.');
            return;
        }
        showSection(form);
        showSection(step2);
    });

    // Back to Step 1
    backToStep1Btn.addEventListener('click', () => {
        showSection(form);
        showSection(step1);
    });

    // Handle form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        // Validate Step 2 required fields
        const requiredFields = [
            'data_collection_rating', 'data_collection_explanation',
            'reporting_rating', 'reporting_explanation',
            'analytics_type_rating', 'analytics_type_explanation',
            'tool_usage_rating', 'tool_usage_explanation',
            'decision_making_rating', 'decision_making_explanation',
            'skills_rating', 'skills_explanation'
        ];
        for (const name of requiredFields) {
            const el = form.elements[name];
            if (el && !el.value.trim()) {
                alert('Please fill in all required fields.');
                el.focus();
                return;
            }
        }
        // Prepare data
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        // POST to backend (adjust URL as needed)
        // const apiUrl = 'http://localhost:5000/api/analyze';
        // await fetch(apiUrl, { ... });
        // For now, just show thank you
        showSection(thankyouSection);
    });

    // Initial state
    showSection(welcomeSection);
}); 