"""
Honeypot Canary & Deception Module
Creates decoy 'false files' and trap endpoints that lure attackers,
capture their identity and location, and waste their resources with fake credentials.
"""

from typing import Dict, Any
from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse

from app.geolocation import resolve_ip_location
from app.logger import log_honeypot_trap
from app.security import ip_manager

honeypot_router = APIRouter(tags=["Honeypot Decoys"])

# -----------------------------------------------------------------------------
# Decoy 1: Fake Environment Variables (.env)
# -----------------------------------------------------------------------------
FAKE_ENV_CONTENT = """# ====================================================================
# PRODUCTION ENVIRONMENT CONFIGURATION (CANARY TRAP DECOY)
# WARNING: UNAUTHORIZED ACCESS IS LOGGED AND MONITORED IN REAL-TIME
# ====================================================================

APP_ENV=production
APP_SECRET=decoy_secret_key_89f7a932b14e590c29a8f
DEBUG=false

# Database Decoy Credentials
DB_CONNECTION=postgresql
DB_HOST=10.142.0.12
DB_PORT=5432
DB_DATABASE=streamguard_master_vault
DB_USERNAME=admin_vault_master
DB_PASSWORD=P@ssw0rd_FakeDecoyVault#2026!

# Cloud Storage Decoy Keys (Canary Honeypot Tokens)
AWS_ACCESS_KEY_ID=CANARY_MOCK_AWS_ACCESS_KEY_DO_NOT_USE_9911
AWS_SECRET_ACCESS_KEY=CANARY_MOCK_AWS_SECRET_KEY_DO_NOT_USE_5544
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=streamguard-internal-secure-vault

# Payment Gateway Sandbox Decoy (Canary Honeypot Tokens)
STRIPE_SECRET_KEY=CANARY_MOCK_STRIPE_SECRET_KEY_DO_NOT_USE_8877
JWT_SECRET=super_secret_decoy_jwt_signature_key_2026

# Internal Admin Auth Token
INTERNAL_ADMIN_TOKEN=CANARY_TRAP_TOKEN_AUTH_ID_99014
"""

# -----------------------------------------------------------------------------
# Decoy 2: Fake SQL Database Dump (backup.sql)
# -----------------------------------------------------------------------------
FAKE_SQL_DUMP = """-- ====================================================================
-- STREAMGUARD DATABASE DUMP (CANARY TRAP)
-- Generated: 2026-11-01 03:00:00 UTC
-- Database: streamguard_users_backup
-- ====================================================================

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `admin_credentials`;
CREATE TABLE `admin_credentials` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `role` varchar(20) NOT NULL DEFAULT 'superadmin',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `admin_credentials` VALUES 
(1, 'root_admin', 'security@streamguard.internal', '$2y$12$e8YDECOYTRAPHASHNOTREAL1234567890abcdefghijklmnopqrst', 'master_admin'),
(2, 'sys_auditor', 'audit@streamguard.internal', '$2y$12$m7ZCANARYTOKENPASSWORDDONOTUSEabcdefghijklmnopqrst12345', 'auditor');

-- [HONEYPOT TRAP NOTICE: Access to this file has been permanently logged with your IP and Location]
"""

# -----------------------------------------------------------------------------
# Decoy 3: Fake Admin Login Panel
# -----------------------------------------------------------------------------
FAKE_ADMIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>StreamGuard | Master Superadmin Login</title>
  <style>
    body {
      background: #0b0f19;
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .login-box {
      background: #1e293b;
      padding: 40px;
      border-radius: 12px;
      border: 1px solid #334155;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      width: 360px;
    }
    h2 { margin-top: 0; color: #f43f5e; font-size: 22px; text-align: center; }
    .badge {
      display: inline-block;
      background: rgba(244, 63, 94, 0.15);
      color: #fb7185;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 11px;
      margin-bottom: 20px;
      text-align: center;
      width: 100%;
      box-sizing: border-box;
    }
    input {
      width: 100%;
      padding: 12px;
      margin: 8px 0 16px;
      background: #0f172a;
      border: 1px solid #475569;
      color: #fff;
      border-radius: 6px;
      box-sizing: border-box;
    }
    button {
      width: 100%;
      padding: 12px;
      background: #f43f5e;
      border: none;
      color: white;
      font-weight: bold;
      border-radius: 6px;
      cursor: pointer;
    }
    .warning {
      font-size: 11px;
      color: #94a3b8;
      text-align: center;
      margin-top: 20px;
      line-height: 1.4;
    }
    .error-msg {
      background: rgba(239, 68, 68, 0.2);
      border: 1px solid #ef4444;
      color: #fca5a5;
      padding: 10px;
      border-radius: 6px;
      font-size: 12px;
      margin-bottom: 15px;
      display: none;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <h2>RESTRICTED GATEWAY</h2>
    <div class="badge">INTERNAL CONTROL PANEL ONLY</div>
    <div id="errorBox" class="error-msg">Invalid master credentials or hardware token mismatch.</div>
    <form id="adminForm" onsubmit="event.preventDefault(); submitDecoy();">
      <label>Admin ID / Email</label>
      <input type="text" id="uname" placeholder="admin@streamguard.internal" required>
      <label>Master Security Key</label>
      <input type="password" id="pword" placeholder="••••••••••••••••" required>
      <button type="submit">Authenticate Session</button>
    </form>
    <div class="warning">
      Notice: This endpoint is equipped with autonomous intrusion telemetry.
      All unauthorized authentication probes are geolocated and recorded.
    </div>
  </div>
  <script>
    async function submitDecoy() {
      const u = document.getElementById('uname').value;
      const p = document.getElementById('pword').value;
      await fetch('/api/v1/honeypot/login-attempt', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username: u, password: p, origin: '/admin'})
      });
      document.getElementById('errorBox').style.display = 'block';
    }
  </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# Decoy 4: Fake Server Configuration (config.json)
# -----------------------------------------------------------------------------
FAKE_CONFIG_JSON = {
    "system_name": "StreamGuard Distributed Media Cluster",
    "cluster_environment": "production-internal",
    "version": "4.8.2-enterprise",
    "internal_gateways": [
        "10.240.10.1:8080",
        "10.240.10.2:8080"
    ],
    "storage_credentials": {
        "storage_provider": "decoy_cloud_storage",
        "access_token": "DECOY_CANARY_TOKEN_99182371"
    },
    "security_warning": "CANARY ASSET: All reads from this endpoint generate forensic telemetry."
}


async def _handle_honeypot_hit(request: Request, canary_name: str, response_data: Response):
    """Processes a canary hit: extracts IP, resolves location, and logs to threat files."""
    client_ip = request.client.host if request.client else "127.0.0.1"
    ua = request.headers.get("user-agent", "-")

    # Geolocation lookup for the intruder
    geo_data = await resolve_ip_location(client_ip)

    # Log to dedicated honeypot & threat files
    log_honeypot_trap(
        ip=client_ip,
        honeypot_path=str(request.url.path),
        geo_data=geo_data,
        user_agent=ua,
        decoy_served=f"Decoy File: {canary_name}"
    )

    # Quarantine the attacker IP
    ip_manager.ban_ip(
        ip=client_ip,
        reason=f"Triggered Honeypot Decoy: {canary_name}",
        duration_seconds=3600
    )

    return response_data


# Canary Endpoints:
@honeypot_router.get("/.env")
@honeypot_router.get("/env")
async def honeypot_env(request: Request):
    """Decoy environment secrets file."""
    return await _handle_honeypot_hit(
        request,
        ".env (Environment Variables Canary)",
        PlainTextResponse(FAKE_ENV_CONTENT, media_type="text/plain")
    )


@honeypot_router.get("/admin")
@honeypot_router.get("/wp-admin")
@honeypot_router.get("/administrator")
@honeypot_router.get("/login/admin")
async def honeypot_admin(request: Request):
    """Decoy admin login portal."""
    return await _handle_honeypot_hit(
        request,
        "Admin Portal Honeypot",
        HTMLResponse(FAKE_ADMIN_HTML)
    )


@honeypot_router.get("/backup.sql")
@honeypot_router.get("/dump.sql")
@honeypot_router.get("/database.sql")
async def honeypot_sql(request: Request):
    """Decoy database backup SQL dump."""
    return await _handle_honeypot_hit(
        request,
        "backup.sql (Database Dump Canary)",
        PlainTextResponse(FAKE_SQL_DUMP, media_type="application/sql")
    )


@honeypot_router.get("/config.json")
@honeypot_router.get("/internal/config")
async def honeypot_config(request: Request):
    """Decoy internal cluster configuration."""
    return await _handle_honeypot_hit(
        request,
        "config.json (Cluster Configuration Canary)",
        JSONResponse(FAKE_CONFIG_JSON)
    )


@honeypot_router.get("/api/v1/secret-keys")
@honeypot_router.get("/api/internal/tokens")
async def honeypot_api_tokens(request: Request):
    """Decoy API tokens endpoint."""
    return await _handle_honeypot_hit(
        request,
        "API Secret Keys Canary",
        JSONResponse({
            "service": "StreamGuard Security Decoy",
            "mock_tokens": ["CANARY_KEY_PROD_001", "CANARY_KEY_PROD_002"],
            "alert": "Intrusion registered"
        })
    )


@honeypot_router.post("/api/v1/honeypot/login-attempt")
async def honeypot_login_probe(request: Request):
    """Captures intruder brute-force credentials."""
    client_ip = request.client.host if request.client else "127.0.0.1"
    ua = request.headers.get("user-agent", "-")
    geo_data = await resolve_ip_location(client_ip)

    try:
        body = await request.json()
    except Exception:
        body = {}

    log_honeypot_trap(
        ip=client_ip,
        honeypot_path="/api/v1/honeypot/login-attempt",
        geo_data=geo_data,
        user_agent=ua,
        decoy_served=f"Captured Intruder Credentials: user={body.get('username')}"
    )

    return JSONResponse(
        status_code=401,
        content={"error": "Authentication failed", "code": "AUTH_REJECTED"}
    )
