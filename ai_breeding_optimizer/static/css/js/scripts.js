// Form Validation for Upload Data
document.querySelector('form').addEventListener('submit', function(event) {
    let name = document.getElementById('name').value;
    let genetic_traits = document.getElementById('genetic_traits').value;
    let health_status = document.getElementById('health_status').value;
    let productivity = document.getElementById('productivity').value;

    if (!name || !genetic_traits || !health_status || !productivity) {
        alert("All fields are required!");
        event.preventDefault();
    }
});

// Table Row Hover Effect
const tableRows = document.querySelectorAll('tr');
tableRows.forEach(row => {
    row.addEventListener('mouseenter', function() {
        row.style.backgroundColor = '#f2f2f2';
    });
    row.addEventListener('mouseleave', function() {
        row.style.backgroundColor = '';
    });
});

// Smooth Scroll for Recommendations Link
document.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        targetElement.scrollIntoView({ behavior: 'smooth' });
    });
});