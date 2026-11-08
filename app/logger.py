"""
Security & Usage Logging Engine
Handles:
1. access_hits.log (every web hit/request)
2. threat_locations.log (dedicated separate file recording attacker IPs, attack types, and geolocations)
3. honeypot_traps.log (canary / decoy hits)
4. daily_report_YYYY-MM-DD.log (daily traffic & security audit report)
"""

import os
import json
import asyncio
from datetime import datetime, date
from pathlib import Path
from typing import Dict, Any, List, Optional

# Base logs directory
LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

ACCESS_HITS_LOG = LOGS_DIR / "access_hits.log"
THREAT_LOCATIONS_LOG = LOGS_DIR / "threat_locations.log"
HONEYPOT_TRAPS_LOG = LOGS_DIR / "honeypot_traps.log"

# Thread-safe in-memory metrics for real-time reporting & daily aggregation
class MetricsStore:
    def __init__(self):
        self.lock = asyncio.Lock()
        self.daily_hits = 0
        self.unique_ips = set()
        self.video_plays = 0
        self.attacks_blocked = 0
        self.honeypot_triggers = 0
        self.attack_types = {}
        self.recent_threats: List[Dict[str, Any]] = []
        self.recent_hits: List[Dict[str, Any]] = []
        self.hourly_traffic: Dict[str, int] = {f"{h:02d}:00": 0 for h in range(24)}

metrics = MetricsStore()


def log_access_hit(
    ip: str,
    method: str,
    path: str,
    status_code: int,
    latency_ms: float,
    user_agent: str = "-",
    referer: str = "-"
):
    """Logs every HTTP request hit to access_hits.log and updates in-memory counters."""
    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    hour_key = now.strftime("%H:00")

    # Update in-memory metrics
    metrics.daily_hits += 1
    metrics.unique_ips.add(ip)
    if hour_key in metrics.hourly_traffic:
        metrics.hourly_traffic[hour_key] += 1
    if "/api/videos/" in path and method == "GET":
        metrics.video_plays += 1

    hit_record = {
        "timestamp": timestamp_str,
        "ip": ip,
        "method": method,
        "path": path,
        "status": status_code,
        "latency_ms": round(latency_ms, 2),
        "user_agent": user_agent[:150]
    }
    metrics.recent_hits.insert(0, hit_record)
    if len(metrics.recent_hits) > 100:
        metrics.recent_hits.pop()

    log_line = (
        f"[{timestamp_str}] [HIT] IP={ip} METHOD={method} PATH={path} "
        f"STATUS={status_code} LATENCY={latency_ms:.2f}ms UA=\"{user_agent}\" REF=\"{referer}\"\n"
    )

    try:
        with open(ACCESS_HITS_LOG, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print(f"Error writing to access_hits.log: {e}")


def log_threat_location(
    ip: str,
    threat_type: str,
    path: str,
    payload: str,
    geo_data: Dict[str, Any],
    action: str = "BLOCKED_AND_BANNED"
):
    """
    Writes directly to threat_locations.log:
    Records the attacker's IP, detected attack technique, and resolved geographic location.
    """
    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Update metrics
    metrics.attacks_blocked += 1
    metrics.attack_types[threat_type] = metrics.attack_types.get(threat_type, 0) + 1

    threat_entry = {
        "timestamp": timestamp_str,
        "ip": ip,
        "threat_type": threat_type,
        "path": path,
        "payload": payload[:250],
        "geo": geo_data,
        "action": action
    }
    metrics.recent_threats.insert(0, threat_entry)
    if len(metrics.recent_threats) > 100:
        metrics.recent_threats.pop()

    country = geo_data.get("country", "Unknown")
    city = geo_data.get("city", "Unknown")
    region = geo_data.get("region", "Unknown")
    isp = geo_data.get("isp", "Unknown")
    lat = geo_data.get("lat", 0.0)
    lon = geo_data.get("lon", 0.0)
    loc_summary = f"{city}, {region}, {country} (Coords: {lat}, {lon}) [ISP: {isp}]"

    log_line = (
        f"[{timestamp_str}] [THREAT_DETECTED] | "
        f"TYPE={threat_type} | "
        f"IP={ip} | "
        f"LOCATION=\"{loc_summary}\" | "
        f"PATH={path} | "
        f"PAYLOAD=\"{payload[:150]}\" | "
        f"ACTION={action}\n"
    )

    try:
        with open(THREAT_LOCATIONS_LOG, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print(f"Error writing to threat_locations.log: {e}")


def log_honeypot_trap(
    ip: str,
    honeypot_path: str,
    geo_data: Dict[str, Any],
    user_agent: str = "-",
    decoy_served: str = "Fake Credentials/Configuration Decoy"
):
    """Logs when an attacker or scanner triggers a honeypot canary file."""
    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
    metrics.honeypot_triggers += 1

    loc_str = geo_data.get("formatted", f"{geo_data.get('city')}, {geo_data.get('country')}")

    log_line = (
        f"[{timestamp_str}] [HONEYPOT_TRAP] | "
        f"CANARY_TARGET={honeypot_path} | "
        f"INTRUDER_IP={ip} | "
        f"LOCATION=\"{loc_str}\" | "
        f"DECOY=\"{decoy_served}\" | "
        f"USER_AGENT=\"{user_agent}\"\n"
    )

    try:
        with open(HONEYPOT_TRAPS_LOG, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print(f"Error writing to honeypot_traps.log: {e}")

    # Also record in threat_locations.log
    log_threat_location(
        ip=ip,
        threat_type="HONEYPOT_DECOY_INTRUSION",
        path=honeypot_path,
        payload=f"Attempted access to decoy file: {honeypot_path}",
        geo_data=geo_data,
        action="TRAPPED_AND_BLACKLISTED"
    )


def generate_daily_report(target_date: Optional[date] = None) -> Dict[str, Any]:
    """
    Generates a structured daily usage and security report for the site.
    Saves both a formatted text log (daily_report_YYYY-MM-DD.log) and returns the report dict.
    """
    if target_date is None:
        target_date = date.today()

    date_str = target_date.strftime("%Y-%m-%d")
    report_file = LOGS_DIR / f"daily_report_{date_str}.log"
    report_json_file = LOGS_DIR / f"daily_report_{date_str}.json"

    # Compile data
    total_hits = metrics.daily_hits
    unique_visitors = len(metrics.unique_ips)
    attacks_thwarted = metrics.attacks_blocked
    honeypots_triggered = metrics.honeypot_triggers
    video_plays = metrics.video_plays

    threat_summary_lines = []
    for threat in metrics.recent_threats[:25]:
        threat_summary_lines.append(
            f"  - [{threat['timestamp']}] IP: {threat['ip']} ({threat['geo'].get('city', 'Unknown')}, "
            f"{threat['geo'].get('country', 'Unknown')}) -> {threat['threat_type']} on {threat['path']}"
        )

    if not threat_summary_lines:
        threat_summary_text = "  None recorded for this period."
    else:
        threat_summary_text = "\n".join(threat_summary_lines)

    hourly_breakdown_lines = []
    for hour, count in sorted(metrics.hourly_traffic.items()):
        if count > 0:
            bar = "#" * min(count, 40)
            hourly_breakdown_lines.append(f"  {hour} : {count:4d} hits | {bar}")
    if not hourly_breakdown_lines:
        hourly_breakdown_text = "  No traffic recorded yet."
    else:
        hourly_breakdown_text = "\n".join(hourly_breakdown_lines)

    report_text = f"""================================================================================
          STREAMGUARD VIDEO PLATFORM - DAILY USAGE & SECURITY AUDIT
                          Report Date: {date_str}
               Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
================================================================================

1. SITE TRAFFIC & USAGE SUMMARY
--------------------------------------------------------------------------------
* Total Website Hits (Requests):       {total_hits}
* Unique Visitor IP Addresses:         {unique_visitors}
* Total Video Playback Streams:        {video_plays}
* Multi-Layer Defense Status:          ONLINE (Autonomous Shield Enforcing)

2. SECURITY & THREAT MITIGATION SUMMARY
--------------------------------------------------------------------------------
* Total Hostile Attacks Thwarted:      {attacks_thwarted}
* Honeypot Decoys Triggered:           {honeypots_triggered}
* Attack Breakdown by Category:
{chr(10).join([f"    - {k}: {v}" for k, v in metrics.attack_types.items()]) if metrics.attack_types else "    - No malicious attacks logged."}

3. IDENTIFIED HACKER & ATTACKER ORIGIN LOCATIONS (Sample of Latest Records)
--------------------------------------------------------------------------------
{threat_summary_text}

4. HOURLY TRAFFIC ACTIVITY PROFILE
--------------------------------------------------------------------------------
{hourly_breakdown_text}

5. LOG DIRECTORY AUDIT
--------------------------------------------------------------------------------
* Access Hits Log:           {ACCESS_HITS_LOG}
* Attacker Geolocation Log:  {THREAT_LOCATIONS_LOG}
* Honeypot Canary Log:       {HONEYPOT_TRAPS_LOG}

================================================================================
                    END OF DAILY SECURITY REPORT
================================================================================
"""

    try:
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report_text)

        report_data = {
            "date": date_str,
            "generated_at": datetime.now().isoformat(),
            "total_hits": total_hits,
            "unique_visitors": unique_visitors,
            "video_plays": video_plays,
            "attacks_thwarted": attacks_thwarted,
            "honeypots_triggered": honeypots_triggered,
            "attack_types": metrics.attack_types,
            "recent_threats": metrics.recent_threats[:20],
            "hourly_traffic": metrics.hourly_traffic,
            "log_files": {
                "access_hits": str(ACCESS_HITS_LOG),
                "threat_locations": str(THREAT_LOCATIONS_LOG),
                "honeypot_traps": str(HONEYPOT_TRAPS_LOG),
                "daily_report": str(report_file)
            }
        }

        with open(report_json_file, "w", encoding="utf-8") as jf:
            json.dump(report_data, jf, indent=2)

        return report_data
    except Exception as e:
        print(f"Error generating daily report: {e}")
        return {"error": str(e), "date": date_str}
