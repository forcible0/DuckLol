# 🦆 DuckLoL

> **League of Legends Champion Guide & Draft Assistant**

DuckLoL is a web-based champion guide and draft assistant for League of Legends, inspired by DeepLoL.gg and OP.GG. It provides builds, runes, skill orders, counters, synergies, and a real-time draft assistant.

![DuckLoL](https://img.shields.io/badge/League%20of%20Legends-Champion%20Guide-green)
![Patch](https://img.shields.io/badge/Patch-16.16.1-blue)

## ✨ Features

- 🏆 **173 Champions** with full data
- 📦 **Build Paths** — Starter → Core → Boots
- 🔮 **Runes** — Primary & Secondary trees with keystones
- 📈 **Skill Order** — Level-by-level ability progression
- ⚔️ **Summoner Spells** — Role-optimized
- 🎯 **Matchups** — Weak Against / Strong Against / Good Synergy
- 🎲 **Draft Assistant** — Select enemy team, get counter pick recommendations
- 🔍 **Search & Filter** — By role or name
- 🌙 **Dark Theme** — DeepLoL.gg inspired design

## 🚀 Live Demo

Deploy to GitHub Pages: [Settings → Pages → Source: main branch]

## 🛠️ Tech Stack

- Pure HTML/CSS/JS (no frameworks)
- Riot Data Dragon API for assets
- Static JSON data (no backend required)

## 📁 Files

| File | Size | Description |
|------|------|-------------|
| `index.html` | ~25 KB | Main application (CSS + JS + HTML) |
| `data.json` | ~480 KB | Champion builds, items, runes, counters |

## 📝 Data Sources

- Champion images & stats: [Riot Data Dragon](https://developer.riotgames.com/docs/lol#data-dragon)
- Builds & counters: Generated from game logic + statistical modeling

## 🏗️ Future Improvements

- [ ] Riot API integration for live match data
- [ ] Real win rates from Riot API
- [ ] Item tooltip descriptions
- [ ] Runes tooltip descriptions
- [ ] Mobile app (React Native / Flutter)
- [ ] Multi-language support

## 📜 License

Unlicense — Free to use, modify, and distribute.

---

Made with 🦆 by DuckLoL Team
