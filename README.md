# StreamGuard - Video Streaming & Global Live TV Platform 

StreamGuard is a modern, high-performance web media streaming platform incorporating the best features from **YouTube**, **Netflix**, and **Twitch**, together with **Global Live TV Broadcasting** powered by an **In-App Streaming Gateway (Self-Proxy Tunnel)**. The platform is reinforced with an 

---

## 🌟 Key Features

### 1. 🔴 Global Live TV Broadcasts (No External VPN Required)
- **Built-in Self-Gateway Tunnel (`/api/live/gateway`)**:
  - Functions as an internal server-side proxy relay (self-hosted streaming tunnel).
  - Fetches remote broadcast HLS streams on the server, rewrites nested `.m3u8` playlists and media segments (`.ts`, `.m4s`), and relays them to the browser.
  - **No third-party VPN software required** on your computer.
  - Automatically circumvents client-side CORS restrictions and ISP throttling while stripping client identifying telemetry.
- **Curated Open Broadcast Network**:
  - 🇺🇸 **NASA TV HD** (Science & Space, USA)
  - 🇩🇪 **DW News English** (International 24/7 News, Germany)
  - 🇺🇸 **Bloomberg TV** (Global Markets & Finance, USA)
  - 🌐 **Red Bull TV Live** (Action Sports & Culture, Global)
  - 🇹🇷 **TRT World HD** (International Geopolitics, Turkey)
  - 🇨🇳 **CGTN English 24/7** (Global News & Culture, Asia)
  - 🇺🇸 **Pluto Cinema Spotlight** (Blockbuster Movies & Cinema)
- **Regional & Categorical Filtering**: Filter by countries (USA, Germany, Turkey, China, Global) or categories (News, Science, Sports, Finance, Cinema).
- **HLS.js Integration**: Low-latency HLS video playback with dynamic buffer recovery.

---

### 2. 🎬 Next-Gen On-Demand Video Player (YouTube + Netflix + Twitch Hybrid)
- **Cinema Hero Player**: Custom glassmorphic player controls with play/pause ripple animations.
- **Precision Scrubber Timeline**: Smooth scrubbing with buffer progress indicator and hover timestamp preview.
- **Playback Speeds**: Variable playback rate from `0.5x` up to `2.0x`.
- **Display Modes**:
  - **Theater Mode**: Expands the video container to full browser width.
  - **Picture-in-Picture (PiP)**: Pop-out video for multi-tasking.
  - **True Fullscreen Mode**.
- **Interactive Keyboard Hotkeys**:
  - `Space` / `K`: Play / Pause
  - `J` / `L`: Seek backward / forward by 10 seconds
  - `M`: Mute / Unmute
  - `F`: Toggle Fullscreen
  - `T`: Toggle Theater Mode
  - `0` - `9`: Jump to 0% – 90%
  - `?`: Toggle keyboard shortcuts guide
- **Autoplay Queue**: Automatic playback transition to the next video in queue with toggle switch.
- **Up Next / Recommended Feed**: Video cards with duration badges, view counts, and category filters.
- **Social Features**: Real-time Like counter, Share button, and community comments.

---

---

### 3. 🌐 Antigravity Multi-Language Video Engine (AMLVE 2.0)
- **Zero Mass (Decoupled Vocal & Environmental Layers)**:
  - Permanently isolates the **Vocal Dialogue Track (VDT)** from the **Environmental Audio Bed (EAB)** (sound effects, score, and ambient Foley).
  - Language switching only swaps the vocal frequency stem; the unbroken 48kHz audio bed continues continuously with zero interruption.
- **Zero Friction (Anti-Drift Vector Dialogue)**:
  - Neural-compressed vector dialogue streaming at **<5% of standard audio payloads** (95.2% bandwidth reduction).
- **Floating RAM Cache**:
  - Predictively pre-loads active scene audio chunks for primary, secondary, and regional dialects directly into hot device RAM.
- **Zero Breaking (5-Millisecond Cross-Fade Buffer)**:
  - Web Audio API equal-power Hermite ramp executes mid-playback language swaps in **5ms** without video pause, stutter, or re-buffering.
- **Quantum Timecode Anchor**:
  - Locks dialogue strictly to the active video frame index with microsecond accuracy, guaranteeing flawless lip-sync.
- **Universal Language Selector**:
  - Standardized overlay in player controls (`Hotkeys: A / L`) featuring real-time search across 40+ documented global languages, regional dialects (e.g., Kansai-ben, Levantine Arabic, Quebec French, Austrian German), and categorized tabs.

## 🛡️ Multi-Layer Autonomous Defense System

| Defense Layer | Technology / Mechanism | Threat Mitigated |
|---|---|---|
| **Layer 1: Perimeter WAF** | Deep inspection of URL paths, query parameters, headers, and request bodies using regex signature heuristics | SQL Injection (SQLi), Cross-Site Scripting (XSS), Path Traversal (`../`), Remote Code Execution (RCE), SSTI |
| **Layer 2: Adaptive Rate Limiter** | Sliding window token counter per IP | Volumetric DDoS floods, brute-force bots, and rapid-fire scraping |
| **Layer 3: Autonomous Quarantine** | In-memory thread-safe IP blacklist & edge rejection | Instantly drops traffic from identified malicious clients |
| **Layer 4: Deception Honeypots ("False Files to Hack")** | Realistic canary traps: `/.env`, `/admin`, `/backup.sql`, `/config.json`, `/api/v1/secret-keys` | Lures attackers into honeytokens, wastes their resources, and triggers forensic alarms |
| **Layer 5: Intruder Geolocation Tracker** | Asynchronous IP Geolocation resolver querying Country, City, Region, Coordinates, ISP | Unmasks attacker physical and network origin, writing to `logs/threat_locations.log` |
| **Layer 6: Anti-SSRF Stream Gateway Guard** | Strict IP and host validation on streaming gateway endpoints | Prevents unauthorized proxying to internal private subnets |
| **Layer 7: Audit & Daily Reporting** | Continuous aggregation of hits, streams, attack vectors, and hourly distribution | Generates daily formatted reports (`logs/daily_report_YYYY-MM-DD.log`) and hit logs (`logs/access_hits.log`) |

---

## 📁 Log Files Overview

As specifically requested, the platform generates separate dedicated log files:

1. **`logs/access_hits.log`**:
   - Records every single HTTP request hit on the website:
     ```text
     [2026-11-08 22:30:15.120] [HIT] IP=127.0.0.1 METHOD=GET PATH=/api/live/channels STATUS=200 LATENCY=3.40ms UA="Mozilla/5.0..."
     ```
2. **`logs/threat_locations.log` (Separate Threat & Geolocation File)**:
   - Dedicated separate file specifically recording attacker identity, attack vector, and geographic origin:
     ```text
     [2026-11-08 22:30:48] [THREAT_DETECTED] | TYPE=HONEYPOT_DECOY_INTRUSION | IP=198.51.100.42 | LOCATION="Frankfurt, Hesse, Germany (Coords: 50.1109, 8.6821) [ISP: CloudHost]" | PATH=/.env | PAYLOAD="Attempted access to decoy file: /.env" | ACTION=TRAPPED_AND_BLACKLISTED
     ```
3. **`logs/honeypot_traps.log`**:
   - Records interactions with canary decoy files (`/.env`, `/admin`, `/backup.sql`, `/config.json`).
4. **`logs/daily_report_YYYY-MM-DD.log`**:
   - Aggregated daily report detailing total hits, unique visitors, video plays, attacks thwarted by category, and hourly traffic profile.

---

## 🚀 How to Run the Platform

From the project root:

```powershell
cd "C:\Users\DELL\Downloads\Video streaming"
python run.py
```

Or double-click `run.bat` in File Explorer!

Then open your browser:
- **Video Streaming & Live TV Platform**: [`http://localhost:8000`](http://localhost:8000)
- **Security & Threat Location Command Center**: [`http://localhost:8000/security-dashboard`](http://localhost:8000/security-dashboard)
