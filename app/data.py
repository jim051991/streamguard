"""
Video Catalog & Streaming Data Store - StreamGuard 2.0 OTT Architecture
Maintains video library, multi-server sources, episodic series, metadata,
IMDb ratings, subtitles, and horizontal discovery rails (Movibox & CineHD style).
All video URLs use verified, permanent open-access MP4 sources.
"""

from typing import List, Dict, Any, Optional

VIDEOS_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "vid-01",
        "title": "Tears of Steel",
        "subtitle": "Cyberpunk Sci-Fi VFX Showcase",
        "content_type": "movie",  # movie | series | anime
        "description": "Set in a dystopian future Amsterdam, a squad of resistance scientists and combat specialists attempt to stage a crucial historical event in order to rescue the world from destructive robotic sentinels.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 8.9,
        "quality": "4K ULTRA HD",
        "duration_seconds": 734,
        "duration_formatted": "12:14",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"},
            {"id": "srv-3", "name": "Server 3 (StreamGuard Relay)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}
        ],
        "views": 482190,
        "likes": 32800,
        "channel": {
            "name": "Blender VFX Studio",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80",
            "subscribers": "1.4M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": ["sci-fi", "cyberpunk", "vfx", "cinematic", "blender"],
        "published_at": "3 days ago",
        "is_trending": True,
        "is_featured": True,
        "comments": [
            {
                "id": "c1",
                "author": "NeoVFX",
                "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&auto=format&fit=crop&q=80",
                "text": "The lighting and tracking shots in the rocket base are breathtaking!",
                "timestamp": "2 hours ago",
                "likes": 142
            },
            {
                "id": "c2",
                "author": "CyberPulse",
                "avatar": "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=100&auto=format&fit=crop&q=80",
                "text": "The custom player buffering and playback speed controls work so smoothly.",
                "timestamp": "5 hours ago",
                "likes": 89
            }
        ]
    },
    {
        "id": "vid-02",
        "title": "Big Buck Bunny",
        "subtitle": "4K Remastered Animation",
        "content_type": "anime",
        "description": "A large and lovable rabbit deals with bullying forest creatures in this legendary computer animated comedy film by the Blender Institute.",
        "release_year": 2024,
        "age_rating": "ALL",
        "imdb_rating": 8.5,
        "quality": "4K ULTRA HD",
        "duration_seconds": 596,
        "duration_formatted": "09:56",
        "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}
        ],
        "views": 1289400,
        "likes": 98200,
        "channel": {
            "name": "Open Animation Archive",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80",
            "subscribers": "850K",
            "verified": True
        },
        "category": "Animation",
        "tags": ["animation", "comedy", "cartoon", "4k", "family"],
        "published_at": "1 week ago",
        "is_trending": True,
        "is_featured": False,
        "comments": [
            {
                "id": "c3",
                "author": "AnimLover",
                "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80",
                "text": "A timeless classic! Never gets old.",
                "timestamp": "1 day ago",
                "likes": 215
            }
        ]
    },
    {
        "id": "vid-03",
        "title": "Sintel - Chronicles of the Dragon",
        "subtitle": "Epic Fantasy Adventure Series",
        "content_type": "series",
        "description": "The poignant journey of a lonely warrior named Sintel who rescues a wounded baby dragon, forming an unbreakable bond across a treacherous desert realm.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 8.7,
        "quality": "1080p HD",
        "duration_seconds": 888,
        "duration_formatted": "14:48",
        "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}
        ],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1: The Awakening",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "The Wounded Hatchling",
                        "duration": "14:48",
                        "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400&auto=format&fit=crop&q=80"
                    },
                    {
                        "episode_number": 2,
                        "title": "Crossing the Whispering Sands",
                        "duration": "12:14",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=400&auto=format&fit=crop&q=80"
                    },
                    {
                        "episode_number": 3,
                        "title": "The Obsidian Gates",
                        "duration": "10:53",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400&auto=format&fit=crop&q=80"
                    }
                ]
            }
        ],
        "views": 750100,
        "likes": 56000,
        "channel": {
            "name": "Fantasy World Cinema",
            "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&auto=format&fit=crop&q=80",
            "subscribers": "620K",
            "verified": True
        },
        "category": "Animation",
        "tags": ["fantasy", "dragon", "story", "epic", "series"],
        "published_at": "2 weeks ago",
        "is_trending": True,
        "is_featured": False,
        "comments": [
            {
                "id": "c4",
                "author": "StoryCrafter",
                "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&auto=format&fit=crop&q=80",
                "text": "That ending twist still gives me chills every time.",
                "timestamp": "3 days ago",
                "likes": 310
            }
        ]
    },
    {
        "id": "vid-04",
        "title": "Elephant's Dream",
        "subtitle": "Surreal Cyber-Organic Odyssey",
        "content_type": "movie",
        "description": "Proog and Emo guide you through the infinite mechanical labyrinths of a giant surreal organic machine, where human thoughts shape steel gears.",
        "release_year": 2023,
        "age_rating": "PG",
        "imdb_rating": 8.1,
        "quality": "1080p HD",
        "duration_seconds": 653,
        "duration_formatted": "10:53",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}
        ],
        "views": 320400,
        "likes": 18400,
        "channel": {
            "name": "Blender VFX Studio",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80",
            "subscribers": "1.4M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": ["surreal", "cyberpunk", "experimental", "cgi"],
        "published_at": "3 weeks ago",
        "is_trending": False,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "vid-05",
        "title": "Ocean Wilderness & Bioluminescent Reefs",
        "subtitle": "4K Ultra-HD Nature Documentary",
        "content_type": "movie",
        "description": "Experience breathtaking high-definition underwater bioluminescent marine life, drifting jellyfish, and deep reef ecosystems across the Pacific deep abyss.",
        "release_year": 2025,
        "age_rating": "ALL",
        "imdb_rating": 8.6,
        "quality": "4K ULTRA HD",
        "duration_seconds": 15,
        "duration_formatted": "00:15",
        "video_url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}
        ],
        "views": 915200,
        "likes": 74300,
        "channel": {
            "name": "Alpine Expeditions",
            "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&auto=format&fit=crop&q=80",
            "subscribers": "2.1M",
            "verified": True
        },
        "category": "Nature",
        "tags": ["nature", "travel", "ocean", "4k", "adventure"],
        "published_at": "1 month ago",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "vid-06",
        "title": "Meadow Mischief: Bunny Chronicles",
        "subtitle": "Classic Slapstick Comedy Series",
        "content_type": "anime",
        "description": "High-octane comedic forest animation featuring classic open-source 3D character animation and meadow wildlife.",
        "release_year": 2024,
        "age_rating": "ALL",
        "imdb_rating": 8.3,
        "quality": "1080p HD",
        "duration_seconds": 12,
        "duration_formatted": "00:12",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://www.w3schools.com/html/mov_bbb.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}
        ],
        "views": 540800,
        "likes": 42100,
        "channel": {
            "name": "Speed & Style",
            "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=100&auto=format&fit=crop&q=80",
            "subscribers": "940K",
            "verified": True
        },
        "category": "Animation",
        "tags": ["cartoon", "funny", "classic", "animation"],
        "published_at": "1 month ago",
        "is_trending": False,
        "is_featured": False,
        "comments": []
    }
]

def get_hero_featured() -> Dict[str, Any]:
    """Returns top featured title for the Cinematic Hero Billboard."""
    for v in VIDEOS_CATALOG:
        if v.get("is_featured"):
            return v
    return VIDEOS_CATALOG[0]

def get_content_rails() -> Dict[str, List[Dict[str, Any]]]:
    """Returns structured horizontal rails for Netflix / Movibox layout."""
    trending = [v for v in VIDEOS_CATALOG if v.get("is_trending")]
    movies = [v for v in VIDEOS_CATALOG if v.get("content_type") == "movie"]
    series = [v for v in VIDEOS_CATALOG if v.get("content_type") == "series"]
    anime = [v for v in VIDEOS_CATALOG if v.get("content_type") == "anime"]

    return {
        "trending": trending,
        "movies": movies,
        "series": series,
        "anime": anime
    }

def get_all_videos(category: Optional[str] = None, search: Optional[str] = None, content_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """Returns list of videos filtered by category, search term, or content type."""
    results = VIDEOS_CATALOG
    if content_type and content_type.lower() != "all":
        results = [v for v in results if v.get("content_type", "").lower() == content_type.lower()]
    if category and category.lower() != "all":
        results = [v for v in results if v["category"].lower() == category.lower()]
    if search:
        s = search.lower().strip()
        results = [
            v for v in results
            if s in v["title"].lower()
            or s in v.get("subtitle", "").lower()
            or s in v["description"].lower()
            or any(s in tag.lower() for tag in v["tags"])
        ]
    return results

def get_video_by_id(video_id: str) -> Optional[Dict[str, Any]]:
    """Finds a video by ID and increments view counter."""
    for v in VIDEOS_CATALOG:
        if v["id"] == video_id:
            v["views"] += 1
            return v
    return None

def toggle_like_video(video_id: str) -> Optional[int]:
    """Toggles or increments like count for a video."""
    for v in VIDEOS_CATALOG:
        if v["id"] == video_id:
            v["likes"] += 1
            return v["likes"]
    return None

def add_video_comment(video_id: str, author: str, text: str) -> Optional[Dict[str, Any]]:
    """Adds a new comment to a video."""
    for v in VIDEOS_CATALOG:
        if v["id"] == video_id:
            comment = {
                "id": f"c_{len(v['comments']) + 1}",
                "author": author[:30] or "Anonymous Streamer",
                "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80",
                "text": text[:300],
                "timestamp": "Just now",
                "likes": 0
            }
            v["comments"].insert(0, comment)
            return comment
    return None
