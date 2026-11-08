"""
IP Geolocation & Threat Origin Tracker
Resolves the geographic location (Country, City, Region, Coordinates, ISP)
for any suspicious or attacking IP address.
"""

import ipaddress
import logging
from typing import Dict, Any, Optional
import httpx

logger = logging.getLogger("security.geolocation")

# In-memory cache for resolved IP locations to minimize latency and avoid rate limits
_GEO_CACHE: Dict[str, Dict[str, Any]] = {}

def is_private_or_local_ip(ip_str: str) -> bool:
    """Check if an IP is loopback, link-local, or private RFC1918."""
    try:
        # Strip port or ipv6 brackets if present
        cleaned_ip = ip_str.split(":")[0].strip("[]") if ":" in ip_str and not ip_str.startswith(":") else ip_str
        if cleaned_ip in ("localhost", "127.0.0.1", "::1", "testclient"):
            return True
        ip_obj = ipaddress.ip_address(cleaned_ip)
        return ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_link_local
    except ValueError:
        return False

async def resolve_ip_location(ip: str) -> Dict[str, Any]:
    """
    Resolves the geographic location of an IP address.
    Returns details including Country, City, Region, Coordinates, ISP, and Organization.
    """
    clean_ip = ip.strip()
    if clean_ip in _GEO_CACHE:
        return _GEO_CACHE[clean_ip]

    # Handle local / private testing addresses
    if is_private_or_local_ip(clean_ip):
        location_data = {
            "ip": clean_ip,
            "status": "success",
            "country": "Localhost / Internal Network",
            "country_code": "LOC",
            "region": "Development Subnet",
            "city": "Local Machine / Test Lab",
            "zip": "00000",
            "lat": 0.0,
            "lon": 0.0,
            "timezone": "Local",
            "isp": "Localhost / Loopback Adapter",
            "org": "Internal Developer Environment",
            "as": "AS0 Localhost",
            "is_local": True,
            "formatted": f"Local Environment ({clean_ip})"
        }
        _GEO_CACHE[clean_ip] = location_data
        return location_data

    # For public internet IPs, query public IP Geolocation API
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            resp = await client.get(f"http://ip-api.com/json/{clean_ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query")
            if resp.status_code == 200:
                data = resp.json()
                if data.get("status") == "success":
                    location_data = {
                        "ip": clean_ip,
                        "status": "success",
                        "country": data.get("country", "Unknown Country"),
                        "country_code": data.get("countryCode", "XX"),
                        "region": data.get("regionName", "Unknown Region"),
                        "city": data.get("city", "Unknown City"),
                        "zip": data.get("zip", ""),
                        "lat": data.get("lat", 0.0),
                        "lon": data.get("lon", 0.0),
                        "timezone": data.get("timezone", "UTC"),
                        "isp": data.get("isp", "Unknown ISP"),
                        "org": data.get("org", "Unknown Org"),
                        "as": data.get("as", ""),
                        "is_local": False,
                        "formatted": f"{data.get('city', 'Unknown City')}, {data.get('regionName', '')}, {data.get('country', 'Unknown Country')} [Lat: {data.get('lat')}, Lon: {data.get('lon')}] - ISP: {data.get('isp', 'Unknown')}"
                    }
                    _GEO_CACHE[clean_ip] = location_data
                    return location_data
    except Exception as e:
        logger.warning(f"Primary Geolocation lookup failed for {clean_ip}: {e}")

    # Fallback response if offline or lookup fails
    fallback_data = {
        "ip": clean_ip,
        "status": "partial",
        "country": "Remote Internet Host",
        "country_code": "NET",
        "region": "External Network",
        "city": "Undetermined City",
        "zip": "N/A",
        "lat": 0.0,
        "lon": 0.0,
        "timezone": "UTC",
        "isp": "External Gateway / Proxy",
        "org": "External Network",
        "as": "N/A",
        "is_local": False,
        "formatted": f"External Host ({clean_ip}) - Geolocation Offline/Unreachable"
    }
    _GEO_CACHE[clean_ip] = fallback_data
    return fallback_data
