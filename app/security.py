"""
Multi-Layer Autonomous Threat Defense & WAF System
Provides defense-in-depth protection against human hackers, automated bots,
and AI-driven exploitation engines.
"""

import re
import time
import asyncio
from typing import Tuple, Optional, Dict, Any, List
from datetime import datetime
from urllib.parse import unquote

from app.geolocation import resolve_ip_location
from app.logger import log_threat_location

# -----------------------------------------------------------------------------
# Layer 1: Threat Pattern Detection Signatures
# -----------------------------------------------------------------------------

# SQL Injection Patterns
SQLI_PATTERNS = [
    re.compile(r"(\b(UNION(\s+ALL)?|SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|EXEC|EXECUTE)\b.{1,100}\b(FROM|INTO|TABLE|DATABASE|WHERE)\b)", re.IGNORECASE),
    re.compile(r"('|\")?\s*(OR|AND)\s+('?\d+'?\s*=\s*'?\d+'|true|false)", re.IGNORECASE),
    re.compile(r"(\bWAITFOR\s+DELAY\b|\bSLEEP\s*\(\s*\d+\s*\)|\bBENCHMARK\s*\()", re.IGNORECASE),
    re.compile(r"(--|#|/\*.*?\*/|;\s*$)", re.IGNORECASE),
    re.compile(r"(\bINFORMATION_SCHEMA\b|\bSYS\.TABLES\b|\bPG_CATALOG\b)", re.IGNORECASE),
    re.compile(r"(\bHAVING\s+1\s*=\s*1\b|\bORDER\s+BY\s+\d+--)", re.IGNORECASE),
]

# Cross-Site Scripting (XSS) Patterns
XSS_PATTERNS = [
    re.compile(r"<\s*script[^>]*>", re.IGNORECASE),
    re.compile(r"javascript\s*:", re.IGNORECASE),
    re.compile(r"<\s*img[^>]+(onerror|onload)\s*=", re.IGNORECASE),
    re.compile(r"<\s*svg[^>]+(onload|onerror)\s*=", re.IGNORECASE),
    re.compile(r"<\s*iframe[^>]*>", re.IGNORECASE),
    re.compile(r"(\bonerror\s*=|\bonload\s*=|\bonclick\s*=|\bonmouseover\s*=)", re.IGNORECASE),
    re.compile(r"document\.(cookie|location|write)", re.IGNORECASE),
    re.compile(r"data:text/html", re.IGNORECASE),
]

# Path Traversal & Local/Remote File Inclusion (LFI/RFI)
PATH_TRAVERSAL_PATTERNS = [
    re.compile(r"(\.\./|\.\.\\|%2e%2e%2f|%2e%2e\/|\.\.%2f)", re.IGNORECASE),
    re.compile(r"(/etc/passwd|/etc/shadow|/etc/hosts|windows/win\.ini|windows/system32|boot\.ini)", re.IGNORECASE),
    re.compile(r"(\x00|%00)", re.IGNORECASE),  # Null byte injection
]

# Remote Code Execution (RCE) / Command Injection
RCE_PATTERNS = [
    re.compile(r"(;\s*(ls|cat|nc|bash|sh|cmd|powershell|curl|wget|whoami|id|uname|dir)\b)", re.IGNORECASE),
    re.compile(r"(\|\s*(cat|sh|bash|powershell|cmd))", re.IGNORECASE),
    re.compile(r"(\$\([^\)]+\)|`[^`]+`)", re.IGNORECASE),  # Subshell execution
    re.compile(r"(\bbase64_decode\b|\beval\s*\(|\bsystem\s*\()", re.IGNORECASE),
]

# Server-Side Template Injection (SSTI) & Expression Injection
SSTI_PATTERNS = [
    re.compile(r"(\{\{[^}]*(7\*7|config|self|class|mro|subclasses)[^}]*\}\})", re.IGNORECASE),
    re.compile(r"(\$\{[^}]*(7\*7|process|getRuntime)[^}]*\})", re.IGNORECASE),
]

# Known Malicious Scanners, Bot Harvesters, and Exploitation Frameworks
MALICIOUS_BOT_SIGNATURES = [
    "sqlmap", "nikto", "masscan", "acunetix", "nmap", "gobuster",
    "dirbuster", "ffuf", "havij", "wpscan", "hydra", "metasploit",
    "zgrab", "shodan", "censys", "burpcollaborator", "nuclei",
    "scrapy", "python-requests/threat", "curl/7.0.0-exploit"
]

# -----------------------------------------------------------------------------
# Layer 2: Autonomous IP Quarantine & Blacklist Manager
# -----------------------------------------------------------------------------

class AutonomousIPManager:
    """Manages active quarantine, auto-bans, and whitelist for clients."""
    def __init__(self):
        self.banned_ips: Dict[str, Dict[str, Any]] = {}
        self.whitelist = {"127.0.0.1", "::1"}  # Whitelist can be bypassed for simulated attacks

    def is_banned(self, ip: str) -> Tuple[bool, Optional[str]]:
        now = time.time()
        if ip in self.banned_ips:
            ban_info = self.banned_ips[ip]
            if ban_info["expires_at"] > now:
                return True, ban_info["reason"]
            else:
                # Ban expired
                del self.banned_ips[ip]
        return False, None

    def ban_ip(self, ip: str, reason: str, duration_seconds: int = 3600):
        """Bans an IP address for a specified duration (default 1 hour)."""
        now = time.time()
        self.banned_ips[ip] = {
            "ip": ip,
            "reason": reason,
            "banned_at": now,
            "expires_at": now + duration_seconds,
            "banned_at_iso": datetime.now().isoformat()
        }

    def unban_ip(self, ip: str):
        if ip in self.banned_ips:
            del self.banned_ips[ip]

    def get_all_banned(self) -> List[Dict[str, Any]]:
        return list(self.banned_ips.values())

ip_manager = AutonomousIPManager()

# -----------------------------------------------------------------------------
# Layer 3: Adaptive Rate Limiter (Anti-DDoS / Anti-Brute-Force)
# -----------------------------------------------------------------------------

class AdaptiveRateLimiter:
    """
    Sliding window rate limiter to detect rapid volumetric bursts,
    DDoS spikes, or brute-force automation.
    """
    def __init__(self, max_requests: int = 120, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.client_hits: Dict[str, List[float]] = {}
        self._lock = asyncio.Lock()

    async def check_rate_limit(self, ip: str) -> Tuple[bool, int]:
        """
        Returns (is_allowed, remaining_quota).
        If threshold exceeded, marks as violation.
        """
        async with self._lock:
            now = time.time()
            cutoff = now - self.window_seconds

            # Filter old requests
            hits = [ts for ts in self.client_hits.get(ip, []) if ts > cutoff]
            hits.append(now)
            self.client_hits[ip] = hits

            if len(hits) > self.max_requests:
                return False, 0
            return True, self.max_requests - len(hits)

rate_limiter = AdaptiveRateLimiter(max_requests=150, window_seconds=60)

# -----------------------------------------------------------------------------
# Layer 4: Deep Threat Inspection Engine
# -----------------------------------------------------------------------------

def inspect_payload(text: str) -> Optional[Tuple[str, str]]:
    """
    Inspects any arbitrary text string (URL, query parameter, body, header)
    against known threat vectors.
    Returns (Threat_Type, Matched_Rule) or None.
    """
    if not text:
        return None

    # URL-decode up to 2 times to catch double-encoding evasion
    decoded = text
    try:
        decoded = unquote(unquote(text))
    except Exception:
        pass

    # Check SQL Injection
    for pattern in SQLI_PATTERNS:
        if pattern.search(decoded):
            return ("SQL_INJECTION", pattern.pattern)

    # Check XSS
    for pattern in XSS_PATTERNS:
        if pattern.search(decoded):
            return ("XSS_ATTACK", pattern.pattern)

    # Check Path Traversal
    for pattern in PATH_TRAVERSAL_PATTERNS:
        if pattern.search(decoded):
            return ("PATH_TRAVERSAL", pattern.pattern)

    # Check RCE
    for pattern in RCE_PATTERNS:
        if pattern.search(decoded):
            return ("COMMAND_INJECTION", pattern.pattern)

    # Check SSTI
    for pattern in SSTI_PATTERNS:
        if pattern.search(decoded):
            return ("SSTI_EXPLOIT", pattern.pattern)

    return None


def inspect_user_agent(ua: str) -> Optional[str]:
    """Inspects User-Agent header for automated hacking tools or scanners."""
    if not ua:
        return None
    lower_ua = ua.lower()
    for signature in MALICIOUS_BOT_SIGNATURES:
        if signature in lower_ua:
            return f"MALICIOUS_BOT_OR_SCANNER ({signature})"
    return None


async def evaluate_request_security(
    ip: str,
    method: str,
    path: str,
    query_string: str,
    headers: Dict[str, str],
    body_text: str = ""
) -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Evaluates incoming request through all security inspection layers.
    Returns:
        (is_threat: bool, threat_type: Optional[str], offending_payload: Optional[str])
    """
    # 1. Check if IP is already in quarantine
    banned, reason = ip_manager.is_banned(ip)
    if banned:
        return True, "IP_QUARANTINED", f"IP already banned for: {reason}"

    # 2. Check Rate Limit
    allowed, remaining = await rate_limiter.check_rate_limit(ip)
    if not allowed:
        ip_manager.ban_ip(ip, "Rate limit flood exceeded", duration_seconds=600)
        return True, "RATE_LIMIT_DDOS_BURST", "Excessive request velocity (>150 req/min)"

    # 3. Check User-Agent
    ua = headers.get("user-agent", "")
    bot_threat = inspect_user_agent(ua)
    if bot_threat:
        ip_manager.ban_ip(ip, f"Identified malicious scanner: {bot_threat}", duration_seconds=7200)
        return True, "AUTOMATED_SCANNER_BOT", ua

    # 4. Check Path
    path_threat = inspect_payload(path)
    if path_threat:
        ip_manager.ban_ip(ip, f"Path exploit: {path_threat[0]}", duration_seconds=3600)
        return True, path_threat[0], path

    # 5. Check Query Parameters
    if query_string:
        query_threat = inspect_payload(query_string)
        if query_threat:
            ip_manager.ban_ip(ip, f"Query exploit: {query_threat[0]}", duration_seconds=3600)
            return True, query_threat[0], query_string

    # 6. Check Request Body (e.g. comment submissions, form posts)
    if body_text and len(body_text) < 100000:
        body_threat = inspect_payload(body_text)
        if body_threat:
            ip_manager.ban_ip(ip, f"Body payload exploit: {body_threat[0]}", duration_seconds=3600)
            return True, body_threat[0], body_text[:200]

    return False, None, None


async def trigger_security_reaction(
    ip: str,
    threat_type: str,
    path: str,
    payload: str
) -> Dict[str, Any]:
    """
    Executes autonomous security defense reaction:
    1. Resolves attacker geolocation
    2. Writes to threat_locations.log
    3. Auto-bans attacker IP
    4. Returns threat profile
    """
    # Resolve geographic location of the attacker
    geo_data = await resolve_ip_location(ip)

    # Log to dedicated threat_locations.log
    log_threat_location(
        ip=ip,
        threat_type=threat_type,
        path=path,
        payload=payload,
        geo_data=geo_data,
        action="BLOCKED_AND_QUARANTINED"
    )

    return {
        "status": "blocked",
        "shield": "Multi-Layer Defensive Grid",
        "threat_type": threat_type,
        "action": "Immediate Quarantine & Blacklist",
        "attacker_ip": ip,
        "location": geo_data.get("formatted", "Unknown"),
        "timestamp": datetime.now().isoformat()
    }
