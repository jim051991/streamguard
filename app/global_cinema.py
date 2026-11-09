"""
StreamGuard 2.0 - Global Cinema Discovery Engine
Enables dynamic discovery and real-time streaming of any movie or TV series
in existence across world cinema using global metadata and cloud resolvers.
"""

import re
import httpx
from typing import Dict, Any, List, Optional
from fastapi import APIRouter, HTTPException, Query

global_router = APIRouter(prefix="/api/global", tags=["Global Cinema Discovery"])

# In-memory LRU-like cache for discovered global titles
GLOBAL_DISCOVERY_CACHE: Dict[str, Dict[str, Any]] = {}

OMDB_API_URL = "https://www.omdbapi.com/?apikey=trilogy"

def format_global_title(item: Dict[str, Any]) -> Dict[str, Any]:
    """Formats raw search/detail item into full StreamGuard media structure."""
    imdb_id = item.get("imdbID") or item.get("imdb_id")
    raw_type = (item.get("Type") or item.get("content_type") or "movie").lower()
    content_type = "series" if raw_type in ("series", "tv", "episode") else "movie"
    title = item.get("Title") or item.get("title") or "Unknown Title"
    year_str = str(item.get("Year") or item.get("release_year") or "2024")
    clean_year = int(re.sub(r"\D", "", year_str)[:4]) if any(c.isdigit() for c in year_str) else 2024
    
    poster = item.get("Poster") or item.get("poster_url")
    if not poster or poster == "N/A":
        poster = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=500&auto=format&fit=crop&q=80"

    runtime = item.get("Runtime") or "2h 00m"
    genre = item.get("Genre") or "Cinema"
    plot = item.get("Plot") or f"Global cinema release: {title} ({clean_year}). Streaming in 4K Ultra HD with multi-language AMLVE audio support."
    director = item.get("Director") or "Global Director"
    actors = item.get("Actors") or "World Cinema Cast"
    rating_str = item.get("imdbRating")
    try:
        imdb_rating = float(rating_str) if rating_str and rating_str != "N/A" else 8.0
    except ValueError:
        imdb_rating = 8.0

    if content_type == "movie":
        servers = [
            {"id": "srv-1", "name": "Server 1: Full Original Movie (Cloud 4K)", "type": "embed", "url": f"https://vidlink.pro/movie/{imdb_id}?primaryColor=06b6d4"},
            {"id": "srv-2", "name": "Server 2: Fast Cloud Mirror (AutoEmbed)", "type": "embed", "url": f"https://autoembed.co/movie/imdb/{imdb_id}"},
            {"id": "srv-3", "name": "Server 3: Fast Native Stream (Demo)", "type": "native", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ]
    else:
        servers = [
            {"id": "srv-1", "name": "Server 1: Full Original Series (Cloud 4K)", "type": "embed_tv", "url": f"https://vidlink.pro/tv/{imdb_id}/1/1?primaryColor=06b6d4"},
            {"id": "srv-2", "name": "Server 2: Fast Cloud Mirror (AutoEmbed)", "type": "embed_tv", "url": f"https://autoembed.co/tv/imdb/{imdb_id}"},
            {"id": "srv-3", "name": "Server 3: Fast Native Stream (Demo)", "type": "native", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ]

    video_obj = {
        "id": f"global-{imdb_id}",
        "title": title,
        "subtitle": f"{clean_year} • {genre}",
        "content_type": content_type,
        "description": plot,
        "release_year": clean_year,
        "age_rating": item.get("Rated") if item.get("Rated") != "N/A" else "PG-13",
        "imdb_rating": imdb_rating,
        "imdb_id": imdb_id,
        "quality": "4K ULTRA HD",
        "duration_seconds": 7200,
        "duration_formatted": runtime if runtime != "N/A" else "2h 05m",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": servers,
        "thumbnail_url": poster,
        "poster_url": poster,
        "backdrop_url": poster,
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 2500000,
        "likes": 180000,
        "channel": {
            "name": director if director != "N/A" else "Global Cinema Studios",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "10M",
            "verified": True
        },
        "category": genre.split(",")[0].strip() if genre else "Cinema",
        "tags": [t.strip().lower() for t in genre.split(",") if t.strip()] + ["global", "world-cinema", "4k"],
        "published_at": str(clean_year),
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "is_global_dynamic": True,
        "comments": []
    }

    if content_type == "series":
        video_obj["seasons"] = [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {"episode_number": 1, "title": "Episode 1", "duration": "45m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": poster},
                    {"episode_number": 2, "title": "Episode 2", "duration": "45m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": poster}
                ]
            }
        ]

    return video_obj


@global_router.get("/search")
async def search_global_movies(query: str = Query(..., min_length=1)):
    """
    Searches worldwide cinema database for any movie or series ever made.
    Returns playable StreamGuard titles with Cloud 4K resolvers.
    """
    clean_q = query.strip()
    if not clean_q:
        return {"query": clean_q, "results": [], "total": 0}

    # Query global discovery endpoint
    try:
        async with httpx.AsyncClient(timeout=6.0) as client:
            resp = await client.get(f"{OMDB_API_URL}&s={clean_q}")
            if resp.status_code == 200:
                data = resp.json()
                if data.get("Response") == "True":
                    formatted = []
                    for item in data.get("Search", []):
                        if not item.get("imdbID"):
                            continue
                        f_item = format_global_title(item)
                        # Store in cache
                        GLOBAL_DISCOVERY_CACHE[f_item["id"]] = f_item
                        GLOBAL_DISCOVERY_CACHE[f_item["imdb_id"]] = f_item
                        formatted.append(f_item)
                    return {"query": clean_q, "results": formatted, "total": len(formatted)}
    except Exception as e:
        print(f"[Global Cinema] Search error for '{clean_q}':", e)

    return {"query": clean_q, "results": [], "total": 0}


@global_router.get("/video/{video_id}")
async def get_global_video_details(video_id: str):
    """
    Fetches full metadata for any global movie or series by ID.
    """
    # 1. Check in-memory discovery cache
    if video_id in GLOBAL_DISCOVERY_CACHE:
        return {"video": GLOBAL_DISCOVERY_CACHE[video_id], "recommended": []}

    imdb_id = video_id.replace("global-", "")
    try:
        async with httpx.AsyncClient(timeout=6.0) as client:
            resp = await client.get(f"{OMDB_API_URL}&i={imdb_id}&plot=full")
            if resp.status_code == 200:
                data = resp.json()
                if data.get("Response") == "True":
                    formatted = format_global_title(data)
                    GLOBAL_DISCOVERY_CACHE[video_id] = formatted
                    GLOBAL_DISCOVERY_CACHE[imdb_id] = formatted
                    return {"video": formatted, "recommended": []}
    except Exception as e:
        print(f"[Global Cinema] Details fetch error for '{video_id}':", e)

    raise HTTPException(status_code=404, detail="Global video title not found")


def get_cached_global_video(video_id: str) -> Optional[Dict[str, Any]]:
    """Helper to retrieve a cached global video object by ID."""
    if video_id in GLOBAL_DISCOVERY_CACHE:
        return GLOBAL_DISCOVERY_CACHE[video_id]
    imdb_id = video_id.replace("global-", "")
    if imdb_id in GLOBAL_DISCOVERY_CACHE:
        return GLOBAL_DISCOVERY_CACHE[imdb_id]
    return None
