// Assessment data structure
const assessmentData = {
    currentSection: 0,
    sections: [
        {
            title: "Basic Information",
            fields: [
                {
                    type: "email",
                    name: "email",
                    label: "What is your email address?",
                    required: true,
                    placeholder: "Enter your email address"
                },
                {
                    type: "text",
                    name: "company_name",
                    label: "What is your company name?",
                    required: true,
                    placeholder: "Enter your company name"
                },
                {
                    type: "select",
                    name: "industry",
                    label: "Which industry best describes your business?",
                    required: true,
                    options: [
                        "Recycling",
                        "Manufacturing",
                        "Services",
                        "Healthcare",
                        "Technology",
                        "Agriculture",
                        "Other"
                    ]
                },
                {
                    type: "select",
                    name: "company_size",
                    label: "What is the size of your company?",
                    required: true,
                    options: [
                        "1–9 employees",
                        "10–49 employees",
                        "50–99 employees",
                        "100–249 employees",
                        "250–499 employees",
                        "500+ employees"
                    ]
                }
            ]
        },
        {
            title: "Data Collection",
            fields: [
                {
                    type: "rating",
                    name: "data_collection_rating",
                    label: "How would you rate your data collection process?",
                    required: true,
                    options: [
                        {
                            value: "Basic",
                            description: "Mostly manual (e.g., paper, spreadsheets)"
                        },
                        {
                            value: "Developing",
                            description: "Some automation, partial integration"
                        },
                        {
                            value: "Advanced",
                            description: "Automated, integrated across systems"
                        }
                    ]
                },
                {
                    type: "textarea",
                    name: "data_collection_explanation",
                    label: "Please explain your data collection process.",
                    required: true,
                    placeholder: "Describe tools, frequency, challenges, or recent improvements"
                }
            ]
        },
        {
            title: "Reporting",
            fields: [
                {
                    type: "rating",
                    name: "reporting_rating",
                    label: "How would you rate your reporting capabilities?",
                    required: true,
                    options: [
                        {
                            value: "Basic",
                            description: "Static reports, limited sharing"
                        },
                        {
                            value: "Developing",
                            description: "Dashboards, some automation, regular updates"
                        },
                        {
                            value: "Advanced",
                            description: "Real-time, interactive, self-service dashboards"
                        }
                    ]
                },
                {
                    type: "textarea",
                    name: "reporting_explanation",
                    label: "Please explain your reporting approach.",
                    required: true,
                    placeholder: "What tools do you use? Who creates and uses reports?"
                }
            ]
        },
        {
            title: "Analytics Type",
            fields: [
                {
                    type: "rating",
                    name: "analytics_type_rating",
                    label: "What best describes the type of analytics you use?",
                    required: true,
                    options: [
                        {
                            value: "Basic",
                            description: "Descriptive only (what happened)"
                        },
                        {
                            value: "Developing",
                            description: "Diagnostic (why it happened), some trend analysis"
                        },
                        {
                            value: "Advanced",
                            description: "Predictive/prescriptive (what will/might happen, what to do next)"
                        }
                    ]
                },
                {
                    type: "textarea",
                    name: "analytics_type_explanation",
                    label: "Please explain your analytics use.",
                    required: true,
                    placeholder: "Give examples—trend analysis, forecasting, scenario planning, etc."
                }
            ]
        },
        {
            title: "Tool Usage",
            fields: [
                {
                    type: "rating",
                    name: "tool_usage_rating",
                    label: "How would you rate your analytics tool usage?",
                    required: true,
                    options: [
                        {
                            value: "Basic",
                            description: "Spreadsheets only (Excel, Google Sheets)"
                        },
                        {
                            value: "Developing",
                            description: "BI tools (Power BI, Tableau, Google Data Studio)"
                        },
                        {
                            value: "Advanced",
                            description: "AI/ML tools (AutoML, DataRobot, custom AI, chatbots)"
                        }
                    ]
                },
                {
                    type: "textarea",
                    name: "tool_usage_explanation",
                    label: "Please explain your analytics toolset.",
                    required: true,
                    placeholder: "List main tools, recent upgrades, integration level, etc."
                }
            ]
        },
        {
            title: "Decision-Making",
            fields: [
                {
                    type: "rating",
                    name: "decision_making_rating",
                    label: "How would you describe your decision-making process?",
                    required: true,
                    options: [
                        {
                            value: "Basic",
                            description: "Mostly intuition/gut feeling"
                        },
                        {
                            value: "Developing",
                            description: "Data-informed, some data-driven decisions"
                        },
                        {
                            value: "Advanced",
                            description: "Data-driven, automated or AI-assisted decisions"
                        }
                    ]
                },
                {
                    type: "textarea",
                    name: "decision_making_explanation",
                    label: "Please explain how data influences your decisions.",
                    required: true,
                    placeholder: "Examples of recent data-driven decisions, or where data is underused"
                }
            ]
        },
        {
            title: "Skills",
            fields: [
                {
                    type: "rating",
                    name: "skills_rating",
                    label: "How would you rate your team's analytics skills?",
                    required: true,
                    options: [
                        {
                            value: "Basic",
                            description: "One or few data-savvy people, limited training"
                        },
                        {
                            value: "Developing",
                            description: "Some trained staff, ongoing upskilling"
                        },
                        {
                            value: "Advanced",
                            description: "Cross-team data literacy, analytics champions, regular training"
                        }
                    ]
                },
                {
                    type: "textarea",
                    name: "skills_explanation",
                    label: "Please explain your team's analytics skills and training.",
                    required: true,
                    placeholder: "Mention certifications, training programs, or skill gaps"
                }
            ]
        },
        {
            title: "Additional Comments",
            fields: [
                {
                    type: "textarea",
                    name: "additional_comments",
                    label: "Is there anything else you'd like to share about your analytics journey, challenges, or goals?",
                    required: false,
                    placeholder: "Share any additional thoughts or concerns"
                }
            ]
        }
    ],
    responses: {}
};

// Initialize the assessment
function startAssessment() {
    // Hide welcome page
    document.querySelector('.container').innerHTML = '';
    
    // Create assessment form
    createAssessmentForm();
    
    // Show first section
    showSection(0);
}

// Create the assessment form structure
function createAssessmentForm() {
    const container = document.createElement('div');
    container.className = 'container py-5';
    
    // Add progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'progress mb-4';
    progressBar.innerHTML = `
        <div class="progress-bar" role="progressbar" style="width: 0%"></div>
    `;
    container.appendChild(progressBar);
    
    // Create sections
    assessmentData.sections.forEach((section, index) => {
        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'assessment-section';
        sectionDiv.id = `section-${index}`;
        
        const card = document.createElement('div');
        card.className = 'card shadow-sm';
        
        const cardBody = document.createElement('div');
        cardBody.className = 'card-body';
        
        // Add section title
        const title = document.createElement('h2');
        title.className = 'mb-4';
        title.textContent = section.title;
        cardBody.appendChild(title);
        
        // Add form fields
        section.fields.forEach(field => {
            const fieldDiv = document.createElement('div');
            fieldDiv.className = 'mb-4';
            
            const label = document.createElement('label');
            label.className = 'form-label';
            label.textContent = field.label;
            fieldDiv.appendChild(label);
            
            // Create appropriate input based on field type
            let input;
            switch (field.type) {
                case 'select':
                    input = document.createElement('select');
                    input.className = 'form-select';
                    field.options.forEach(option => {
                        const optionElement = document.createElement('option');
                        optionElement.value = option;
                        optionElement.textContent = option;
                        input.appendChild(optionElement);
                    });
                    break;
                    
                case 'rating':
                    field.options.forEach(option => {
                        const ratingDiv = document.createElement('div');
                        ratingDiv.className = 'rating-option';
                        ratingDiv.innerHTML = `
                            <h5>${option.value}</h5>
                            <p>${option.description}</p>
                        `;
                        ratingDiv.onclick = () => selectRating(field.name, option.value, ratingDiv);
                        fieldDiv.appendChild(ratingDiv);
                    });
                    break;
                    
                case 'textarea':
                    input = document.createElement('textarea');
                    input.className = 'form-control';
                    input.rows = 4;
                    input.placeholder = field.placeholder;
                    break;
                    
                default:
                    input = document.createElement('input');
                    input.type = field.type;
                    input.className = 'form-control';
                    input.placeholder = field.placeholder;
            }
            
            if (input) {
                input.name = field.name;
                input.required = field.required;
                fieldDiv.appendChild(input);
            }
            
            cardBody.appendChild(fieldDiv);
        });
        
        // Add navigation buttons
        const buttonDiv = document.createElement('div');
        buttonDiv.className = 'd-flex justify-content-between mt-4';
        
        if (index > 0) {
            const prevButton = document.createElement('button');
            prevButton.className = 'btn btn-secondary';
            prevButton.textContent = 'Previous';
            prevButton.onclick = () => showSection(index - 1);
            buttonDiv.appendChild(prevButton);
        }
        
        const nextButton = document.createElement('button');
        nextButton.className = 'btn btn-primary';
        nextButton.textContent = index === assessmentData.sections.length - 1 ? 'Submit' : 'Next';
        nextButton.onclick = () => handleNavigation(index);
        buttonDiv.appendChild(nextButton);
        
        cardBody.appendChild(buttonDiv);
        card.appendChild(cardBody);
        sectionDiv.appendChild(card);
        container.appendChild(sectionDiv);
    });
    
    document.body.appendChild(container);
}

// Show a specific section
function showSection(index) {
    document.querySelectorAll('.assessment-section').forEach(section => {
        section.classList.remove('active');
    });
    
    document.querySelector(`#section-${index}`).classList.add('active');
    
    // Update progress bar
    const progress = ((index + 1) / assessmentData.sections.length) * 100;
    document.querySelector('.progress-bar').style.width = `${progress}%`;
}

// Handle navigation between sections
function handleNavigation(index) {
    const currentSection = assessmentData.sections[index];
    const sectionElement = document.querySelector(`#section-${index}`);
    
    // Validate current section
    const inputs = sectionElement.querySelectorAll('input, select, textarea');
    let isValid = true;
    
    inputs.forEach(input => {
        if (input.required && !input.value) {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    if (!isValid) {
        return;
    }
    
    // Save responses
    inputs.forEach(input => {
        assessmentData.responses[input.name] = input.value;
    });
    
    // Navigate to next section or submit
    if (index === assessmentData.sections.length - 1) {
        submitAssessment();
    } else {
        showSection(index + 1);
    }
}

// Handle rating selection
function selectRating(fieldName, value, element) {
    const section = element.closest('.assessment-section');
    section.querySelectorAll('.rating-option').forEach(option => {
        option.classList.remove('selected');
    });
    element.classList.add('selected');
    
    // Create or update hidden input
    let input = section.querySelector(`input[name="${fieldName}"]`);
    if (!input) {
        input = document.createElement('input');
        input.type = 'hidden';
        input.name = fieldName;
        section.appendChild(input);
    }
    input.value = value;
}

// Submit the assessment
async function submitAssessment() {
    try {
        // Show loading state
        const submitButton = document.querySelector('.btn-primary');
        const originalText = submitButton.textContent;
        submitButton.disabled = true;
        submitButton.textContent = 'Processing...';
        
        // Send data to backend
        const response = await fetch('/api/submit-assessment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(assessmentData.responses)
        });
        
        const result = await response.json();
        
        if (!result.success) {
            throw new Error(result.message);
        }
        
        // Store report path for download
        window.reportPath = result.report_path;
        
        // Show thank you page
        document.querySelector('.container').innerHTML = `
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="text-center mb-5">
                        <h1 class="display-4 mb-4">Thank You!</h1>
                        <p class="lead">Your responses have been submitted successfully.</p>
                    </div>
                    
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <h5 class="mb-3">What's next?</h5>
                            <ul class="mb-4">
                                <li>We've analyzed your answers and created a personalized report.</li>
                                <li>Review your results and use the insights to guide your next steps.</li>
                                <li>Your report is ready for download.</li>
                            </ul>
                            
                            <div class="text-center">
                                <button class="btn btn-primary" onclick="downloadReport()">Download Report</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
    } catch (error) {
        console.error('Error submitting assessment:', error);
        alert('There was an error processing your assessment. Please try again.');
        
        // Reset button state
        submitButton.disabled = false;
        submitButton.textContent = originalText;
    }
}

// Download the assessment report
async function downloadReport() {
    try {
        if (!window.reportPath) {
            throw new Error('Report path not found');
        }
        
        // Show loading state
        const downloadButton = document.querySelector('.btn-primary');
        const originalText = downloadButton.textContent;
        downloadButton.disabled = true;
        downloadButton.textContent = 'Downloading...';
        
        // Download the report
        window.location.href = `/api/download-report/${window.reportPath}`;
        
        // Reset button state after a delay
        setTimeout(() => {
            downloadButton.disabled = false;
            downloadButton.textContent = originalText;
        }, 2000);
        
    } catch (error) {
        console.error('Error downloading report:', error);
        alert('There was an error downloading your report. Please try again.');
        
        // Reset button state
        downloadButton.disabled = false;
        downloadButton.textContent = originalText;
    }
} 