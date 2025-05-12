
// this is for to match the new password and confirm password

document.querySelector('form').onsubmit = function(event) {
  const newPassword = document.getElementById('newPassword').value;
  const confirmNewPassword = document.getElementById('confirmNewPassword').value;

  if (newPassword !== confirmNewPassword) {
      event.preventDefault();  // Prevent form submission
      alert("New password and confirmation do not match.");
  }
};