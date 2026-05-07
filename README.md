# Palia Guides

Reference guides for Palia — fish, bugs, hunting, bundles, crafting, gardening, and economy.

🌐 **Live at:** https://brimdor.github.io/palia-guides/

## How to Add a Guide

1. Drop the `.html` file into the repo root
2. Add an entry to `guides.json`:

```json
{
  "slug": "your-guide-filename-no-extension",
  "title": "Your Guide Title",
  "description": "Short description for the card",
  "category": "fishing|bugs|crafting|bundles|gardening|foraging|economy",
  "date": "YYYY-MM-DD",
  "icon": "🎣",
  "tags": ["keyword1", "keyword2"]
}
```

3. Commit and push — the landing page auto-updates

## How to Remove a Guide

1. Delete the `.html` file
2. Remove its entry from `guides.json`
3. Commit and push

## Categories

| Category | Icon | Color |
|----------|------|-------|
| fishing | 🎣 | Orange |
| bugs | 🦋 | Purple |
| crafting | 🔨 | Red |
| bundles | 🏛️ | Cyan |
| gardening | 🌱 | Green |
| foraging | 🍄 | Yellow |
| economy | 💰 | Gold |

## Search

The landing page has live search — filters by title, description, and tags. Category buttons further narrow results.
