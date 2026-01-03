// CodeRef Navigation - Drawer functionality
// Last Updated: 2025-12-31

function initNavigation() {
  const hamburger = document.querySelector('.hamburger');
  const drawer = document.querySelector('.drawer');
  const drawerOverlay = document.querySelector('.drawer-overlay');
  const drawerClose = document.querySelector('.drawer-close');

  if (!hamburger || !drawer || !drawerOverlay || !drawerClose) {
    console.warn('Navigation elements not found');
    return;
  }

  // Open drawer
  hamburger.addEventListener('click', function() {
    drawer.classList.add('open');
    drawerOverlay.classList.add('active');
  });

  // Close drawer
  function closeDrawer() {
    drawer.classList.remove('open');
    drawerOverlay.classList.remove('active');
  }

  drawerClose.addEventListener('click', closeDrawer);
  drawerOverlay.addEventListener('click', closeDrawer);

  // Set active nav item based on current page
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.drawer-nav a');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    }
  });

  // Close drawer when clicking a nav link
  navLinks.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  // Close drawer on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}
