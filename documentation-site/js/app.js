// ========== SIDEBAR COLLAPSE STATE MANAGEMENT ==========
/**
 * Manages sidebar collapse/expand state via chevron button in sidebar header
 * - Chevron button toggles between < (expanded) and > (collapsed)
 * - Sidebar width animates smoothly from 320px (full) to 60px (minimal)
 * - State persists to localStorage
 *
 * Alignment:
 * - Expanded: "📄 Documents" label + document list visible
 * - Collapsed: chevron only visible, document list hidden via overflow
 * - Chevron rotates 180° to show state
 */

function initializeSidebarToggle() {
    const chevronBtn = document.getElementById('sidebarToggle');
    const layout = document.getElementById('layout');

    // State key for localStorage persistence
    const STATE_KEY = 'sidebar-collapsed';

    // Load saved state from localStorage (defaults to false = expanded)
    const savedState = localStorage.getItem(STATE_KEY);
    const isCollapsed = savedState === 'true';

    // Apply saved state on page load
    if (isCollapsed) {
        layout.classList.add('sidebar-collapsed');
    }

    // Handle chevron click - collapse/expand sidebar
    chevronBtn.addEventListener('click', () => {
        // Toggle the sidebar-collapsed class on layout
        // This triggers CSS to:
        // 1. Change grid: 320px 1fr <-> 60px 1fr
        // 2. Sidebar width: 320px <-> 60px
        // 3. Hide/show title via display: none
        // 4. Rotate chevron 180° via transform
        layout.classList.toggle('sidebar-collapsed');

        // Persist new state to localStorage
        const newState = layout.classList.contains('sidebar-collapsed');
        localStorage.setItem(STATE_KEY, newState.toString());
    });
}

// ========== DOCUMENT LOADING AND RENDERING ==========

// Load documents manifest and initialize app
async function init() {
    // Initialize sidebar toggle functionality first
    initializeSidebarToggle();
    try {
        const response = await fetch('/documentation-site/docs.json');
        if (!response.ok) throw new Error('Failed to load documents manifest');

        const data = await response.json();
        const documents = data.documents;

        renderDocList(documents);

        // Load first document by default
        if (documents.length > 0) {
            loadDocument(documents[0].id, documents);
        }
    } catch (error) {
        console.error('Error initializing app:', error);
        document.getElementById('content').innerHTML = `
            <div class="error">
                <strong>Error loading documentation:</strong> ${error.message}<br>
                <small>Make sure docs.json exists in the root directory</small>
            </div>
        `;
    }
}

// Render document list in sidebar
function renderDocList(documents) {
    const docList = document.getElementById('docList');
    docList.innerHTML = documents.map(doc => `
        <li class="doc-item">
            <a href="#" onclick="loadDocument('${doc.id}', null); return false;" data-id="${doc.id}">
                ${doc.icon} ${doc.title}
            </a>
        </li>
    `).join('');
}

// Load and display markdown document
async function loadDocument(docId, documents) {
    // Fetch documents if not provided
    if (!documents) {
        try {
            const response = await fetch('/documentation-site/docs.json');
            const data = await response.json();
            documents = data.documents;
        } catch (error) {
            console.error('Error fetching documents:', error);
            return;
        }
    }

    const doc = documents.find(d => d.id === docId);
    if (!doc) return;

    // Update active state
    document.querySelectorAll('.doc-item a').forEach(el => el.classList.remove('active'));
    document.querySelector(`[data-id="${docId}"]`).classList.add('active');

    // Show loading state while fetching document
    const content = document.getElementById('content');
    content.innerHTML = '<div class="loading">Loading...</div>';

    try {
        // Fetch markdown document from path
        const response = await fetch(doc.path);
        if (!response.ok) throw new Error('Document not found');

        const markdown = await response.text();
        const html = marked.parse(markdown);
        content.innerHTML = html;

        // Scroll to top
        content.scrollTop = 0;
    } catch (error) {
        content.innerHTML = `
            <div class="error">
                <strong>Error loading document:</strong> ${error.message}<br>
                <small>Path: ${doc.path}</small>
            </div>
        `;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', init);
