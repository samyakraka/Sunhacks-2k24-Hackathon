document.getElementById('hrForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const role = document.getElementById('role').value;
    const experience = document.getElementById('experience').value;
    const resume = document.getElementById('resume').files[0];

    if (!role || !experience || !resume) {
        alert('Please fill in all fields and upload a resume.');
        return;
    }

    // Here you can handle the form data, e.g., send it to a server
    console.log(`Role: ${role}, Experience: ${experience}, Resume: ${resume.name}`);
    alert('Your request has been submitted successfully!');
});
