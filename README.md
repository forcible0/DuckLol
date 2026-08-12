# 🦆 DuckLoL

> **League of Legends Champion Guide, Live Meta & Draft Assistant**
> *Inspired by DeepLoL.gg, OP.GG, and Porofessor*

DuckLoL is a modern, high-performance champion analytics and draft assistant application for League of Legends. It provides real competitive builds, multi-lane role variations, full interactive rune trees, authentic 1-18 skill leveling progression, realistic matchup counters/synergies, and a real-time Draft AI.

![DuckLoL](https://img.shields.io/badge/League%20of%20Legends-Champion%20Guide-green)
![Patch](https://img.shields.io/badge/Patch-16.16.1%20Live-00d4aa)
![Champions](https://img.shields.io/badge/Champions-169%20Official-blue)

---

## ✨ Features

- 🏆 **169 Official Champions**: Full dataset with accurate Riot CDN assets, splash banners, and passive/Q/W/E/R ability cards.
- 🔄 **Multi-Lane Role Switcher**: Seamlessly toggle between champion roles (e.g. Yasuo Mid 74% / Top 18% / ADC 8%, Lux Support 68% / Mid 32%, Ahri Mid 92% / Support 8%).
- 📦 **Accurate Item Builds**: Authentic Summoner's Rift starter items, boots, core legendary rush items, item build progression, and situational items with gold costs and stat tooltips.
- 🔮 **Full DeepLoL Rune Trees**: Interactive primary and secondary rune matrices highlighting active keystones and perks with dimmed inactive runes + 3 stat shard modifiers.
- 📈 **Valid Skill Leveling (1-18)**: Realistic skill max order (e.g., `Q ➔ E ➔ W`) with strictly valid League leveling rules (Level 6/11/16 Ultimates, Level 9 rank-5 max, Level 13 rank-5 max).
- ⚔️ **Summoner Spells**: Role-optimized spell combinations with win rates and pick rates.
- 🎯 **Matchup & Synergy Intelligence**: Role-filtered Weak Against (hard counters), Strong Against (easy matchups), and Good Synergy (best jungle/duo lane combos).
- 🎲 **Interactive Draft Assistant**: Team builder (Enemy 5 vs Ally 5) calculating composite matchup advantages, synergy scores, and recommending top 8 counter picks with explanations.
- 🔍 **Search & Multi-Column Sorting**: Filter by lane role (Top, Jungle, Mid, ADC, Support) or search by name, title, or tag; sort by Meta Tier, Win Rate %, Pick Rate %, Ban Rate %, or Name.
- 📊 **Grid View & OP.GG Table View**: Switch between visual champion cards and detailed statistical tier list tables.
- 💬 **Rich Floating Tooltips**: Hover over any item, rune, summoner spell, or ability to view its name, gold cost, cooldown, and description.

---

## 🚀 Quick Start

### Run in Browser / Web
Open `index.html` in any modern web browser or run:
```bash
python3 -m http.server 3000
```
Then visit `http://localhost:3000`.

### Run Desktop App (Electron)
```bash
npm install
npm start
```

### Sync / Update Meta Data
To re-generate or synchronize the meta database with the latest patch:
```bash
npm run sync
# or
node sync-meta.js
```

---

## 📁 Project Structure

| File / Folder | Description |
|---|---|
| `index.html` | Modern DeepLoL-inspired web application UI (CSS + JS + HTML) |
| `data.json` | 100% verified League of Legends champion, item, rune, and matchup database |
| `main.js` | Electron main process configuration |
| `preload.js` | Secure Electron bridge API |
| `sync-meta.js` | Meta sync & database updater script |
| `package.json` | Project configuration and build scripts |

---

## 📜 License

Unlicense — Free to use, modify, and distribute.

---

Made with 🦆 by DuckLoL Team
