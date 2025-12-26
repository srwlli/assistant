// Load documents manifest and initialize app
async function init() {
    try {
        const response = await fetch('./docs.json');
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
                <small>Make sure docs.json exists in the docs/ directory</small>
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
            const response = await fetch('./docs.json');
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

    // Show loading
    const content = document.getElementById('content');
    content.innerHTML = '<div class="loading">Loading...</div>';
    document.getElementById('docTitle').textContent = doc.title;
    document.getElementById('docMeta').textContent = doc.path;

    try {
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
