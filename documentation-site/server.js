const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8080;
const ROOT_DIR = path.join(__dirname, '..');  // Serve from assistant/ folder

const server = http.createServer((req, res) => {
    // Handle trailing slashes
    let url = req.url;
    if (url === '/') {
        url = '/documentation-site/index.html';
    }

    let filePath = path.join(ROOT_DIR, url);
    let resolvedPath = path.resolve(filePath);

    console.log(`Request: ${req.url} -> ${resolvedPath}`);

    // Security: prevent directory traversal outside ROOT_DIR
    if (!resolvedPath.startsWith(path.resolve(ROOT_DIR))) {
        res.writeHead(403);
        res.end('Forbidden');
        return;
    }

    // Read and serve file
    fs.readFile(filePath, (err, content) => {
        if (err) {
            if (err.code === 'ENOENT') {
                console.log(`File not found: ${filePath}`);
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('404 Not Found: ' + filePath);
                return;
            }
            console.log(`Error reading file: ${err.message}`);
            res.writeHead(500);
            res.end('Internal Server Error');
            return;
        }

        // Set content type
        const ext = path.extname(filePath);
        let contentType = 'text/html';
        if (ext === '.css') contentType = 'text/css';
        if (ext === '.js') contentType = 'application/javascript';
        if (ext === '.json') contentType = 'application/json';
        if (ext === '.md') contentType = 'text/plain; charset=utf-8';

        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content);
    });
});

server.listen(PORT, () => {
    console.log(`Documentation site running at http://localhost:${PORT}`);
});
