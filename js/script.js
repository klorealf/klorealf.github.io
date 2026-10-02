/* =========================================================
   script.js — small bits of interactivity
   ========================================================= */

// 1. MOBILE MENU ------------------------------------------------
// Find the hamburger button and the list of links on the page
const menuButton = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

// When the button is tapped, open or close the menu
menuButton.addEventListener('click', () => {
  // classList.toggle adds "open" if it's missing, removes it if present.
  // It returns true when the class was added (menu now open).
  const isOpen = navLinks.classList.toggle('open');
  // Update aria-expanded so screen readers know the menu state
  menuButton.setAttribute('aria-expanded', isOpen);
});

// Close the menu after a link is tapped (otherwise it stays covering the page)
navLinks.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
  });
});

// 2. HIGHLIGHT THE CURRENT SECTION IN THE MENU -------------------
// Grab every <section> that has an id (about, skills, projects...)
const sections = document.querySelectorAll('section[id]');

// IntersectionObserver watches elements and tells us when they enter the screen
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const id = entry.target.id;  // e.g. "skills"
      // Remove "active" from all links, then add it to the matching one
      navLinks.querySelectorAll('a').forEach((a) => {
        a.classList.toggle('active', a.getAttribute('href') === '#' + id);
      });
    }
  });
}, {
  // Counts a section as "current" when it's in the middle band of the screen
  rootMargin: '-45% 0px -50% 0px'
});

// Start watching each section
sections.forEach((section) => observer.observe(section));

// 3. COPY EMAIL BUTTON -------------------------------------------
const copyButton = document.getElementById('copy-email');
const copyNote = document.getElementById('copy-note');

copyButton.addEventListener('click', async () => {
  const email = copyButton.dataset.email; // reads data-email="..." from the HTML
  try {
    // Ask the browser to put the email on the clipboard
    await navigator.clipboard.writeText(email);
    copyNote.textContent = 'Copied ' + email;
  } catch (error) {
    // Some browsers block clipboard access; show the email so it can be copied by hand
    copyNote.textContent = 'Email: ' + email;
  }
  // Clear the message after 4 seconds (4000 milliseconds)
  setTimeout(() => { copyNote.textContent = ''; }, 4000);
});

// 4. FOOTER YEAR -------------------------------------------------
// Puts the current year in the footer so you never have to update it
document.getElementById('year').textContent = new Date().getFullYear();

// 5. SHOW THE PYTHON CODE IN THE LIVE DEMO -----------------------
// fetch() downloads a file from your own site. Here we grab batch_scaler.py
// and display it as text, so visitors see the exact code that's running.
// (fetch doesn't work if you open index.html by double-clicking it;
//  use serve.py to preview, and it works normally on Hostinger.)
const sourceBox = document.getElementById('python-source');
fetch('python/batch_scaler.py')
  .then((response) => response.text())       // read the file as plain text
  .then((code) => { sourceBox.textContent = code; }) // textContent shows it safely as text
  .catch(() => { sourceBox.textContent = 'The code is on my GitHub.'; });

// 6. BACKUP MESSAGE IF PYTHON DOESN'T LOAD ------------------------
// If PyScript hasn't switched the button on after 20 seconds
// (slow connection or blocked), tell the visitor instead of leaving them waiting
setTimeout(() => {
  const scaleButton = document.getElementById('scale-btn');
  if (scaleButton.disabled) {
    scaleButton.textContent = 'Python is still loading. Try refreshing.';
  }
}, 20000);
