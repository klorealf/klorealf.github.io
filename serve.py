"""
serve.py — preview your website on your own computer before uploading.

How to use:
  1. Open a terminal in this folder (the one with index.html)
  2. Run:  python serve.py      (on some Macs: python3 serve.py)
  3. Open http://localhost:8000 in your browser
  4. Press Ctrl+C in the terminal to stop
"""

# http.server and socketserver come built into Python; nothing to install
import http.server
import socketserver
import webbrowser  # lets us open the browser automatically

PORT = 8000  # the "door number" the preview runs on

# SimpleHTTPRequestHandler serves the files in the current folder
Handler = http.server.SimpleHTTPRequestHandler

# Create the server and keep it running until you stop it
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Previewing your site at {url}  (press Ctrl+C to stop)")
    webbrowser.open(url)      # opens the page for you
    httpd.serve_forever()     # keeps answering requests
