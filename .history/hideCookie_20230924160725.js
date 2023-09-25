// Function to hide the cookie consent form
function hideCookieConsent() {
    const cookieConsent = document.getElementById('cookie-consent');
    if (cookieConsent) {
      cookieConsent.style.display = 'none';
    }
  }
  
  // Function to show the cookie consent form
  function showCookieConsent() {
    const cookieConsent = document.getElementById('cookie-consent');
    if (cookieConsent) {
      cookieConsent.style.display = 'block';
    }
  }
  
  // Delay the showing of the cookie consent form (5000 milliseconds = 5 seconds)
  setTimeout(showCookieConsent, 5000);
  
  // Add an event listener to show the cookie consent form when the user clicks "Agree"
  const acceptBtn = document.querySelector('.button button');
  if (acceptBtn) {
    acceptBtn.addEventListener('click', hideCookieConsent);
  }
  