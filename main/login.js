// Add this to your existing script.js

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Login logic here
});

document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Registration logic here
});

document.getElementById('switch-to-register').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('login-form-container').style.display = 'none';
    document.getElementById('register-form-container').style.display = 'block';
});

document.getElementById('switch-to-login').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('register-form-container').style.display = 'none';
    document.getElementById('login-form-container').style.display = 'block';
});
