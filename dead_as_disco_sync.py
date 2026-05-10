#!/usr/bin/env python3
"""
Dead as Disco - BPM & Sync Tool v6
Single-file Python app. Fully offline.
Drop any audio file onto the app to analyze.
"""
import os, sys, time, socket, threading, subprocess
import webbrowser, zlib, base64
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── Embedded HTML (all analysis runs in the browser via Web Audio API) ──
_HTML = zlib.decompress(base64.b64decode("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"))

APP_TITLE  = "Dead as Disco \u2013 BPM & Sync Tool"
APP_W, APP_H = 1150, 900

# ── Find a free local port ──
def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

# ── Serve the HTML from memory - no files needed ──
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(_HTML)))
            self.end_headers()
            self.wfile.write(_HTML)
        else:
            self.send_response(404)
            self.end_headers()

def start_server(port):
    server = HTTPServer(("127.0.0.1", port), Handler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    return server

def wait_for_server(port, timeout=5):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.3):
                return True
        except Exception:
            time.sleep(0.05)
    return False

# ── Window: pywebview (best - true native window) ──
def try_pywebview(url):
    try:
        import webview
        webview.create_window(
            APP_TITLE, url,
            width=APP_W, height=APP_H,
            resizable=True, min_size=(800, 600)
        )
        webview.start()
        return True
    except Exception:
        return False

# ── Window: Edge in --app mode (no browser UI) ──
def try_edge(url):
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
    ]
    for p in candidates:
        if os.path.exists(p):
            subprocess.Popen([
                p, f"--app={url}",
                f"--window-size={APP_W},{APP_H}",
                "--window-position=80,60",
                "--no-first-run",
                "--disable-extensions",
            ])
            return True
    return False

# ── Window: Chrome in --app mode ──
def try_chrome(url):
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    ]
    for p in candidates:
        if os.path.exists(p):
            subprocess.Popen([
                p, f"--app={url}",
                f"--window-size={APP_W},{APP_H}",
                "--window-position=80,60",
                "--no-first-run",
                "--disable-extensions",
            ])
            return True
    return False

# ── Window: tkinter fallback ──
def try_tkinter(url):
    try:
        import tkinter as tk
        root = tk.Tk()
        root.title(APP_TITLE)
        root.geometry(f"{APP_W}x{APP_H}+80+60")
        root.configure(bg="#09000f")
        root.minsize(800, 600)
        tk.Label(root, text="Dead as Disco",
                 font=("Arial", 24, "bold"), fg="#ff2d78", bg="#09000f").pack(pady=(80, 5))
        tk.Label(root, text="BPM & Sync Tool",
                 font=("Arial", 14), fg="#9b30ff", bg="#09000f").pack(pady=(0, 30))
        tk.Label(root, text=f"Running at:\n{url}",
                 font=("Courier", 11), fg="#00f0ff", bg="#09000f").pack(pady=5)
        tk.Label(root, text="Keep this window open while using the tool.",
                 font=("Arial", 11), fg="#888888", bg="#09000f").pack(pady=10)
        tk.Button(root, text="Open in Browser",
                  command=lambda: webbrowser.open(url),
                  bg="#9b30ff", fg="white", font=("Arial", 12, "bold"),
                  relief="flat", padx=20, pady=10, cursor="hand2").pack(pady=20)
        root.after(800, lambda: webbrowser.open(url))
        root.mainloop()
        return True
    except Exception:
        return False

def main():
    port = free_port()
    url  = f"http://127.0.0.1:{port}"

    start_server(port)
    wait_for_server(port)

    # Try best window method available
    if try_pywebview(url):
        return

    if sys.platform == "win32":
        if try_edge(url) or try_chrome(url):
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
            return

    if try_tkinter(url):
        return

    # Last resort: open in default browser
    webbrowser.open(url)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
