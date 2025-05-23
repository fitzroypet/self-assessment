// Default assessment areas
const ASSESSMENT_AREAS = [
    'Strategy',
    'Data',
    'Technology',
    'People',
    'Process'
];

// Dynamically render assessment area fields
const areasContainer = document.getElementById('areas-container');
ASSESSMENT_AREAS.forEach(area => {
    const div = document.createElement('div');
    div.className = 'area-block';
    div.innerHTML = `
        <h3>${area}</h3>
        <label>Rating:
            <select name="${area.toLowerCase()}_rating" required>
                <option value="">Select...</option>
                <option value="Basic">Basic</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
            </select>
        </label>
        <label>Explanation:
            <textarea name="${area.toLowerCase()}_explanation" rows="2" required></textarea>
        </label>
    `;
    areasContainer.appendChild(div);
});

// Handle form submission
const form = document.getElementById('assessment-form');
const resultsDiv = document.getElementById('results');
const resultsJson = document.getElementById('results-json');
const downloadBtn = document.getElementById('download-report');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // POST to Flask API (adjust URL for production)
    const apiUrl = 'http://localhost:5000/api/analyze';
    resultsJson.textContent = 'Loading...';
    resultsDiv.classList.remove('hidden');
    downloadBtn.classList.add('hidden');

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (result.analysis) {
            resultsJson.textContent = JSON.stringify(result.analysis, null, 2);
            if (result.report_path) {
                downloadBtn.classList.remove('hidden');
                downloadBtn.onclick = () => {
                    window.open('http://localhost:5000' + result.report_path, '_blank');
                };
            }
        } else {
            resultsJson.textContent = result.error || 'Unexpected error.';
        }
    } catch (err) {
        resultsJson.textContent = 'Error: ' + err.message;
    }
}); 