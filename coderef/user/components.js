// Shared components for CodeRef documentation pages

const Components = {
  header: `
    <header class="header">
        <button class="hamburger" aria-label="Open navigation menu"><i class="fa-solid fa-bars"></i></button>
        <h1 class="header-title">CodeRef Documentation</h1>
        <span class="header-subtitle">User Guide Hub</span>
    </header>
  `,

  sidebar: `
    <nav class="drawer">
        <div class="drawer-header">
            <h2 class="drawer-title">Navigation</h2>
            <button class="drawer-close" aria-label="Close navigation menu"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <ul class="drawer-nav">
            <li><a href="index.html"><span class="nav-icon"><i class="fa-solid fa-home"></i></span> Home</a></li>
            <li><a href="coderef-setup.html"><span class="nav-icon"><i class="fa-solid fa-gear"></i></span> Setup Workflow</a></li>
            <li><a href="coderef-output-capabilities.html"><span class="nav-icon"><i class="fa-solid fa-file-export"></i></span> Output Capabilities</a></li>
            <li><a href="coderef-scripts.html"><span class="nav-icon"><i class="fa-solid fa-scroll"></i></span> Scripts Reference</a></li>
            <li><a href="coderef-commands.html"><span class="nav-icon"><i class="fa-solid fa-terminal"></i></span> Commands Reference</a></li>
            <li><a href="coderef-workflows.html"><span class="nav-icon"><i class="fa-solid fa-rotate"></i></span> Workflows Guide</a></li>
            <li><a href="coderef-tools.html"><span class="nav-icon"><i class="fa-solid fa-wrench"></i></span> MCP Tools Reference</a></li>
        </ul>
    </nav>
    <div class="drawer-overlay"></div>
  `
};

// Load components on page load
document.addEventListener('DOMContentLoaded', function() {
  // Inject header
  const headerContainer = document.getElementById('header-container');
  if (headerContainer) {
    headerContainer.innerHTML = Components.header;
  }

  // Inject sidebar
  const sidebarContainer = document.getElementById('sidebar-container');
  if (sidebarContainer) {
    sidebarContainer.innerHTML = Components.sidebar;
  }

  // Initialize navigation after components are loaded
  if (typeof initNavigation === 'function') {
    initNavigation();
  }
});
