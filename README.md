# 🌐 LinkPreview Global API

Enterprise-grade Link Preview, OpenGraph, Twitter Cards, and Favicon Extractor.

## 🚀 Overview
Solves browser CORS limitations for frontend applications (React, Next.js, Vue, mobile apps). Fetches any public URL and extracts rich preview metadata in sub-150ms.

## 📡 Endpoints
- `GET /v1/extract?url=https://github.com` - Single link preview metadata.
- `POST /v1/extract` - JSON payload `{ "url": "https://stripe.com" }`.
- `POST /v1/batch-extract` - Batch array `{ "urls": ["...", "..."] }`.
- `GET /health` - Uptime health check.

## 💰 RapidAPI Pricing Tiers
- **Free**: 100 requests/mo
- **Basic**: $9.99/mo (3,000 requests)
- **Pro**: $29.99/mo (12,000 requests)
- **Ultra**: $79.99/mo (50,000 requests)
