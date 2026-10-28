#!/usr/bin/env python3
"""
WebPulse Global API - OpenGraph, Twitter Card, Favicon & Metadata Extractor
High-performance standard library web scraping & preview engine.
"""
import http.server
import json
import os
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

PORT = int(os.environ.get("PORT", 8080))

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.favicon = None
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        tag = tag.lower()
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            prop = (attr_dict.get("property") or attr_dict.get("name") or "").lower()
            cont = attr_dict.get("content")
            if prop and cont:
                self.meta[prop] = cont
        elif tag == "link":
            rel = (attr_dict.get("rel") or "").lower()
            href = attr_dict.get("href")
            if "icon" in rel and href and not self.favicon:
                self.favicon = href
            elif rel == "canonical" and href:
                self.canonical = href

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title and not self.title:
            self.title = data.strip()

def extract_meta(url: str) -> dict:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    start = time.time()
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            html = resp.read(250000).decode("utf-8", errors="ignore")
            status = resp.status
    except Exception as e:
        return {"success": False, "url": url, "error": str(e)}

    parser = MetaParser()
    try:
        parser.feed(html)
    except Exception:
        pass

    netloc = urllib.parse.urlparse(url).netloc
    fav = parser.favicon
    fav_url = urllib.parse.urljoin(url, fav) if fav else f"https://{netloc}/favicon.ico"

    return {
        "success": True,
        "url": url,
        "domain": netloc,
        "title": parser.meta.get("og:title") or parser.meta.get("twitter:title") or parser.title or netloc,
        "description": parser.meta.get("og:description") or parser.meta.get("twitter:description") or parser.meta.get("description") or "",
        "image": parser.meta.get("og:image") or parser.meta.get("twitter:image"),
        "favicon": fav_url,
        "canonical": parser.canonical or url,
        "status_code": status,
        "latency_ms": round((time.time() - start) * 1000, 2)
    }

class WebPulseHandler(http.server.BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-RapidAPI-Key")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-RapidAPI-Key")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)

        if parsed.path in ["/", "/health"]:
            self.send_json({
                "status": "healthy",
                "service": "WebPulse Global API",
                "version": "2.0.0",
                "uptime": "100.0%"
            })
            return

        if "/extract" in parsed.path or "/preview" in parsed.path:
            url = query.get("url", [""])[0].strip()
            if not url:
                self.send_json({"success": False, "error": "Missing required query parameter: 'url'"}, status=400)
                return
            data = extract_meta(url)
            self.send_json(data)
            return

        self.send_json({"error": "Endpoint not found"}, status=404)

if __name__ == "__main__":
    http.server.HTTPServer(("0.0.0.0", PORT), WebPulseHandler).serve_forever()
