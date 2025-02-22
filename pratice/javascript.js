// Form Submission Handling
document.getElementById('contact-form').addEventListener('submit', function (e) {
  e.preventDefault();
  alert('Your message has been sent. Thank you!');
  this.reset();
});