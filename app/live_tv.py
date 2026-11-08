"""
Global Live TV & In-App Streaming Gateway (Self-Proxy Relay)
Delivers legitimate open-broadcast Live TV streams from around the world
routed through an internal server-side proxy gateway to bypass CORS and ISP restrictions
without requiring client-side third-party VPN software.
"""

import re
import ipaddress
from urllib.parse import urlparse, urljoin, quote, unquote
from typing import List, Dict, Any, Optional
import httpx
from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import Response, StreamingResponse

live_router = APIRouter(prefix="/api/live", tags=["Live TV & Stream Gateway"])

# -----------------------------------------------------------------------------
# Curated Directory of Legitimate Global Public Live Broadcasts
# -----------------------------------------------------------------------------
GLOBAL_LIVE_CHANNELS: List[Dict[str, Any]] = [
    {
        "id": "live-nasa",
        "name": "NASA TV HD",
        "category": "Science & Space",
        "country": "United States",
        "country_code": "US",
        "flag": "🇺🇸",
        "language": "English",
        "stream_url": "https://ntv1.akamaized.net/hls/live/2014075/NASA-NTV1-HLS/master.m3u8",
        "logo": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=300&auto=format&fit=crop&q=80",
        "description": "Official 24/7 live television broadcast from NASA showcasing real-time spacewalks, rocket launches, and International Space Station research.",
        "views": "1.2M watching",
        "resolution": "1080p 60fps",
        "schedule": [
            {"time": "14:00 - 16:30", "title": "ISS Live Earth Stream & Astronaut Research", "status": "LIVE NOW"},
            {"time": "16:30 - 18:00", "title": "Artemis II Lunar Orbital Briefing", "status": "UPCOMING"},
            {"time": "18:00 - 20:00", "title": "James Webb Deep Field Discoveries", "status": "UPCOMING"},
            {"time": "20:00 - 22:00", "title": "Mars Rover Perseverance Science Log", "status": "UPCOMING"}
        ]
    },
    {
        "id": "live-dw",
        "name": "DW News English",
        "category": "World News",
        "country": "Germany",
        "country_code": "DE",
        "flag": "🇩🇪",
        "language": "English",
        "stream_url": "https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8",
        "logo": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?w=300&auto=format&fit=crop&q=80",
        "description": "Deutsche Welle's flagship international news broadcast offering global investigative journalism, documentaries, and European headlines.",
        "views": "840K watching",
        "resolution": "720p HD",
        "schedule": [
            {"time": "14:00 - 15:00", "title": "DW News Global Round-Up", "status": "LIVE NOW"},
            {"time": "15:00 - 16:00", "title": "Eco Africa: Climate & Innovation", "status": "UPCOMING"},
            {"time": "16:00 - 17:00", "title": "Business Beyond: European Markets", "status": "UPCOMING"}
        ]
    },
    {
        "id": "live-bloomberg",
        "name": "Bloomberg TV",
        "category": "Finance & Business",
        "country": "United States",
        "country_code": "US",
        "flag": "🇺🇸",
        "language": "English",
        "stream_url": "https://bloomberg.com/media-manifest/streams/us.m3u8",
        "logo": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=300&auto=format&fit=crop&q=80",
        "description": "Global financial intelligence, live Wall Street market analysis, macroeconomic reporting, and technology sector interviews.",
        "views": "920K watching",
        "resolution": "1080p HD",
        "schedule": [
            {"time": "14:00 - 16:00", "title": "Bloomberg Markets: The Close", "status": "LIVE NOW"},
            {"time": "16:00 - 17:00", "title": "Technology & AI Venture Spotlight", "status": "UPCOMING"},
            {"time": "17:00 - 19:00", "title": "Global Macro Surveillance", "status": "UPCOMING"}
        ]
    },
    {
        "id": "live-redbull",
        "name": "Red Bull TV Live",
        "category": "Sports & Adventure",
        "country": "Global",
        "country_code": "GL",
        "flag": "🌐",
        "language": "English",
        "stream_url": "https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8",
        "logo": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?w=300&auto=format&fit=crop&q=80",
        "description": "World-class extreme action sports, motorsport championships, mountain biking, downhill skiing, and live cultural events.",
        "views": "670K watching",
        "resolution": "1080p HD",
        "schedule": [
            {"time": "13:30 - 15:30", "title": "Red Bull Rampage: Utah Cliffs Championship", "status": "LIVE NOW"},
            {"time": "15:30 - 17:00", "title": "WRC Rally Masters Stage 4", "status": "UPCOMING"},
            {"time": "17:00 - 19:00", "title": "Cliff Diving World Series Finale", "status": "UPCOMING"}
        ]
    },
    {
        "id": "live-trt",
        "name": "TRT World HD",
        "category": "World News",
        "country": "Turkey",
        "country_code": "TR",
        "flag": "🇹🇷",
        "language": "English",
        "stream_url": "https://tv-trtworld.medya.trt.com.tr/master_720.m3u8",
        "logo": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=300&auto=format&fit=crop&q=80",
        "description": "24/7 international English news network offering in-depth coverage across Eurasia, Middle East, and worldwide geopolitical developments.",
        "views": "410K watching",
        "resolution": "720p HD",
        "schedule": [
            {"time": "14:00 - 15:00", "title": "The Newsmakers: Diplomatic Forum", "status": "LIVE NOW"},
            {"time": "15:00 - 16:30", "title": "Across The Balkans Documentary", "status": "UPCOMING"}
        ]
    },
    {
        "id": "live-cgtn",
        "name": "CGTN English 24/7",
        "category": "World News",
        "country": "China",
        "country_code": "CN",
        "flag": "🇨🇳",
        "language": "English",
        "stream_url": "https://news.cgtn.com/resource/live/english/cgtn-news.m3u8",
        "logo": "https://images.unsplash.com/photo-1495020689067-958852a7765e?w=300&auto=format&fit=crop&q=80",
        "description": "Global multilingual television broadcaster offering comprehensive news coverage, Asian business analysis, and cultural documentaries.",
        "views": "530K watching",
        "resolution": "1080p HD",
        "schedule": [
            {"time": "14:00 - 15:00", "title": "Global Watch & Asian Markets", "status": "LIVE NOW"},
            {"time": "15:00 - 16:00", "title": "The Point with Liu Xin", "status": "UPCOMING"}
        ]
    },
    {
        "id": "live-pluto",
        "name": "Pluto Cinema Spotlight",
        "category": "Entertainment & Cinema",
        "country": "United States",
        "country_code": "US",
        "flag": "🇺🇸",
        "language": "English",
        "stream_url": "https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5d9cf9854d92eb0009581c79/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientDeviceType=0&deviceDNT=0&deviceId=unknown&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=5a9b3a3c-b258-452a-9293-f1165a6cbf09&userId=",
        "logo": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=300&auto=format&fit=crop&q=80",
        "description": "Curated 24/7 movie marathon broadcasting top blockbuster features, classic cinema, and award-winning motion pictures.",
        "views": "1.5M watching",
        "resolution": "1080p HD",
        "schedule": [
            {"time": "13:30 - 15:45", "title": "Classic Sci-Fi Spotlight: Solaris Reborn", "status": "LIVE NOW"},
            {"time": "15:45 - 18:00", "title": "Indie Director Showcase", "status": "UPCOMING"}
        ]
    }
]

# -----------------------------------------------------------------------------
# Anti-SSRF Security Validation
# -----------------------------------------------------------------------------
def is_safe_external_url(url: str) -> bool:
    """
    Validates that a URL is a legitimate public HTTP/HTTPS stream
    and does not target private loopback or internal LAN subnets.
    """
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        hostname = parsed.hostname
        if not hostname:
            return False
        
        # Deny localhost and local domains
        if hostname.lower() in ("localhost", "127.0.0.1", "::1", "0.0.0.0", "internal", "testserver"):
            return False

        # If IP address, verify not private/link-local
        try:
            ip_obj = ipaddress.ip_address(hostname)
            if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_link_local:
                return False
        except ValueError:
            # Domain name is ok
            pass

        return True
    except Exception:
        return False

# -----------------------------------------------------------------------------
# In-App Streaming Gateway (Self-Proxy Relay)
# -----------------------------------------------------------------------------
@live_router.get("/channels")
async def list_live_channels(
    category: Optional[str] = None,
    country: Optional[str] = None,
    search: Optional[str] = None
):
    """Returns curated directory of global live TV channels with self-gateway endpoints."""
    results = GLOBAL_LIVE_CHANNELS
    if category and category.lower() != "all":
        results = [c for c in results if c["category"].lower() == category.lower()]
    if country and country.lower() != "all":
        results = [c for c in results if c["country_code"].lower() == country.lower() or c["country"].lower() == country.lower()]
    if search:
        s = search.lower().strip()
        results = [
            c for c in results
            if s in c["name"].lower()
            or s in c["description"].lower()
            or s in c["country"].lower()
            or s in c["category"].lower()
        ]

    # Decorate channels with self-gateway streaming URLs
    enriched = []
    for c in results:
        copy_c = dict(c)
        copy_c["gateway_url"] = f"/api/live/gateway?url={quote(c['stream_url'], safe='')}"
        enriched.append(copy_c)

    return {
        "status": "success",
        "channels": enriched,
        "total": len(enriched),
        "gateway_active": True,
        "gateway_mode": "Self-Proxy Stream Tunnel (No external VPN required)"
    }

@live_router.get("/channels/{channel_id}")
async def get_live_channel(channel_id: str):
    """Retrieve details for a specific live channel."""
    for c in GLOBAL_LIVE_CHANNELS:
        if c["id"] == channel_id:
            channel_data = dict(c)
            channel_data["gateway_url"] = f"/api/live/gateway?url={quote(c['stream_url'], safe='')}"
            return {"status": "success", "channel": channel_data}
    raise HTTPException(status_code=404, detail="Live channel not found")

@live_router.get("/gateway")
async def stream_proxy_gateway(url: str = Query(..., description="Target HLS manifest or media segment URL")):
    """
    Self-Hosted Streaming Proxy Tunnel ("Self-VPN Relay"):
    1. Strips client origin / IP telemetry and applies generic user-agent headers.
    2. Fetches HLS .m3u8 playlists or .ts video segments from remote broadcast CDNs.
    3. Rewrites sub-manifests and video chunk URLs so they continue routing through this gateway.
    4. Bypasses client-side CORS and ISP domain blocks without client VPN software.
    """
    target_url = unquote(url).strip()
    if not is_safe_external_url(target_url):
        raise HTTPException(status_code=400, detail="Invalid or restricted stream URL.")

    # Upstream request headers: mask client identity
    forward_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    try:
        async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
            resp = await client.get(target_url, headers=forward_headers)

            if resp.status_code >= 400:
                raise HTTPException(status_code=resp.status_code, detail="Upstream broadcast host returned error.")

            content_type = resp.headers.get("content-type", "")
            
            # Check if this is an M3U8 playlist
            is_m3u8 = (
                "mpegurl" in content_type.lower()
                or target_url.endswith(".m3u8")
                or resp.text.startswith("#EXTM3U")
            )

            if is_m3u8:
                # Rewrite M3U8 playlist to tunnel sub-playlists and .ts segments through our gateway
                original_text = resp.text
                rewritten_lines = []
                for line in original_text.splitlines():
                    trimmed = line.strip()
                    if not trimmed:
                        continue
                    if trimmed.startswith("#"):
                        # Process URI attributes inside tags (e.g. #EXT-X-KEY, #EXT-X-MAP)
                        if 'URI="' in line:
                            def replace_uri(match):
                                sub_uri = match.group(1)
                                abs_sub = urljoin(target_url, sub_uri)
                                return f'URI="/api/live/gateway?url={quote(abs_sub, safe="")}"'
                            line = re.sub(r'URI="([^"]+)"', replace_uri, line)
                        rewritten_lines.append(line)
                    else:
                        # This line is a segment or sub-manifest URI
                        abs_url = urljoin(target_url, trimmed)
                        rewritten_url = f"/api/live/gateway?url={quote(abs_url, safe='')}"
                        rewritten_lines.append(rewritten_url)

                rewritten_manifest = "\n".join(rewritten_lines)
                return Response(
                    content=rewritten_manifest,
                    media_type="application/vnd.apple.mpegurl",
                    headers={
                        "Access-Control-Allow-Origin": "*",
                        "Cache-Control": "no-cache, no-store, must-revalidate",
                        "X-Stream-Gateway": "Self-Proxy-Relay-Active"
                    }
                )

            # If it's a binary video segment (.ts, .aac, .m4s), stream bytes directly
            return Response(
                content=resp.content,
                media_type=content_type or "video/mp2t",
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Cache-Control": "public, max-age=3600",
                    "X-Stream-Gateway": "Self-Proxy-Relay-Active"
                }
            )

    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"Streaming Gateway Relay failed to connect: {str(e)}")
