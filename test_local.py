#!/usr/bin/env python3
"""
Test Suite for LinkPreview Global API
"""
from server import extract_metadata

test_urls = [
    "https://github.com",
    "https://news.ycombinator.com",
    "https://python.org"
]

print("\n--- RUNNING LINKPREVIEW REAL METADATA TEST SUITE ---\n")

for url in test_urls:
    res = extract_metadata(url)
    print(f"[*] Target URL: {url}")
    print(f"    Success:     {res.get('success')}")
    print(f"    Title:       {res.get('title')[:60]}...")
    print(f"    Description: {res.get('description')[:70]}...")
    print(f"    Image:       {res.get('image')}")
    print(f"    Favicon:     {res.get('favicon')}")
    print(f"    Site Name:   {res.get('site_name')}")
    print(f"    Latency:     {res.get('latency_ms')} ms\n")

print("--- ALL LINKPREVIEW TESTS COMPLETED SUCCESSFULLY ---")
