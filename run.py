"""
StreamGuard Launcher Script
Initializes the video streaming platform with multi-layer autonomous defense,
canary honeypots, and real-time intruder geolocation logging.
"""

import os
import sys
import threading
import time
import webbrowser
from pathlib import Path
import uvicorn

# Dynamically resolve project root directory and set working directory
BASE_DIR = Path(__file__).resolve().parent
os.chdir(str(BASE_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.logger import generate_daily_report, ACCESS_HITS_LOG, THREAT_LOCATIONS_LOG, HONEYPOT_TRAPS_LOG

def open_browser(port: int = 8000):
    """Wait for server to start, then open the platform in the default browser."""
    if os.getenv("HEADLESS") == "1" or os.getenv("APP_ENV") == "production":
        return
    time.sleep(1.5)
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass

def main():
    port = int(os.getenv("PORT", "8000"))
    print("=" * 75)
    print("       STREAMGUARD - VIDEO STREAMING PLATFORM & AUTONOMOUS DEFENSE")
    print("=" * 75)
    print(f" [✓] Project Root Directory:   {BASE_DIR}")
    print(" [✓] Initializing Security Grid & Log Handlers...")
    
    # Generate initial daily report
    generate_daily_report()
    
    print(f" [✓] Access Hits Log:         {ACCESS_HITS_LOG}")
    print(f" [✓] Hacker Location Log:     {THREAT_LOCATIONS_LOG}")
    print(f" [✓] Honeypot Canary Log:     {HONEYPOT_TRAPS_LOG}")
    print(" [✓] Active Canary Decoys:    /.env, /admin, /backup.sql, /config.json")
    print("-" * 75)
    print(f" [★] Main Video Platform:     http://localhost:{port}")
    print(f" [★] Security Command Center: http://localhost:{port}/security-dashboard")
    print("=" * 75)
    print(f" Server starting on http://0.0.0.0:{port} ... (Press Ctrl+C to stop)")

    # Launch browser in separate thread
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()

    # Launch Uvicorn with explicit app_dir so it works from any location
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        app_dir=str(BASE_DIR),
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
