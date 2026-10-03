# 🌐 WebPulse Global API

[![Uptime](https://img.shields.io/badge/Uptime-99.99%25-brightgreen.svg)](https://webpulse-api-r529.onrender.com/health)
[![Latency](https://img.shields.io/badge/Latency-sub--150ms-blue.svg)](https://webpulse-api-r529.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Marketplace%20Ready-orange.svg)](https://rapidapi.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **High-Performance Link Preview, OpenGraph, Twitter Cards, Favicon & SEO Metadata Extractor.**  
> Solves browser CORS security restrictions for React, Next.js, Vue, mobile apps, and chat platforms.

---

## 🚀 Overview

Modern frontend frameworks and mobile applications cannot directly fetch third-party websites to generate link previews due to browser **Cross-Origin Resource Sharing (CORS)** policies.

**WebPulse Global API** serves as a high-availability proxy and metadata parser. Given any public URL, it fetches the target, parses OpenGraph, Twitter Cards, favicon icons, canonical links, author, site names, and estimated reading times, and returns clean, normalized JSON in sub-150ms.

---

## ⚡ Key Capabilities

- 🖼️ **Social Card Extraction:** Extracts high-resolution OpenGraph (`og:image`) and Twitter Card images.
- 📌 **Favicon & Brand Icon Resolver:** Converts relative paths into verified, absolute favicon URLs.
- 📝 **SEO & Content Summary:** Extracts title, meta description, canonical URL, author, and word count.
- ⏱️ **Reading Time Estimator:** Automatically calculates estimated reading duration in minutes.
- ⚡ **Sub-150ms Intelligent Caching:** 1-hour in-memory cache delivers repeat URL requests in under 2ms.
- 🌐 **CORS Bypasser:** Built-in wildcard CORS headers allow direct client-side integration.

---

## 📡 Live Production Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/v1/extract?url=https://github.com` | Extract rich link preview for any target web page. |
| `POST` | `/v1/extract` | JSON request payload: `{"url": "https://stripe.com"}`. |
| `POST` | `/v1/batch-extract` | Bulk link extraction for up to 20 URLs concurrently. |
| `GET` | `/health` | Service uptime and monitoring probe. |

---

## 💻 Quick Start & Code Examples

### 1. cURL
```bash
curl -X GET "https://webpulse-api-r529.onrender.com/v1/extract?url=https://github.com" \
     -H "Accept: application/json"
```

### 2. Python (`requests`)
```python
import requests

url = "https://webpulse-api-r529.onrender.com/v1/extract"
params = {"url": "https://stripe.com"}

response = requests.get(url, params=params)
data = response.json()

print(f"Title:       {data['title']}")
print(f"Description: {data['description']}")
print(f"Preview Img: {data['image']}")
print(f"Favicon:     {data['favicon']}")
print(f"Read Time:   {data['estimated_read_time_minutes']} min")
```

### 3. JavaScript / React Component
```javascript
// Works directly in frontend code without CORS errors!
const res = await fetch(`https://webpulse-api-r529.onrender.com/v1/extract?url=${encodeURIComponent(userUrl)}`);
const preview = await res.json();

return (
  <div className="link-card">
    {preview.image && <img src={preview.image} alt={preview.title} />}
    <h3>{preview.title}</h3>
    <p>{preview.description}</p>
    <span>{preview.site_name}</span>
  </div>
);
```

---

## 📦 JSON Response Schema

```json
{
  "success": true,
  "url": "https://github.com/",
  "domain": "github.com",
  "status_code": 200,
  "title": "GitHub: Let's build from here",
  "description": "GitHub is where over 100 million developers shape the future of software...",
  "image": "https://images.ctfassets.net/.../GH-Homepage-Universe-img.png",
  "favicon": "https://github.githubassets.com/favicons/favicon.svg",
  "site_name": "GitHub",
  "type": "website",
  "canonical_url": "https://github.com/",
  "author": null,
  "word_count": 324,
  "estimated_read_time_minutes": 2,
  "cached": false,
  "latency_ms": 301.87
}
```

---

## 💰 RapidAPI Pricing Tiers

| Plan | Monthly Fee | Included Quota | Overages | Target Audience |
| :--- | :--- | :--- | :--- | :--- |
| **Free** | `$0.00 / mo` | 100 requests | Rate-limited | Testing & Hobbyists |
| **Basic** | `$9.99 / mo` | 3,000 requests | `$0.004 / req` | Indie Developers & Chatbots |
| **Pro** | `$24.99 / mo` | 10,000 requests | `$0.002 / req` | SaaS Feeds & Content Platforms |
| **Ultra**| `$69.99 / mo` | 35,000 requests | `$0.001 / req` | High-Volume Search & Aggregators |

---

## 👨‍💻 Maintainer & Engineering Contact
- **Architecture Lead:** **Liam Vance** — Director of Cloud & API Operations
- **Organization:** VIBE NOW Technologies
- **Inquiries:** `liamvance.dev@gmail.com`
