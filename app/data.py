"""
Video Catalog & Streaming Data Store
Maintains video library, view counters, user comments, and metadata.
All video URLs use verified, permanent open-access MP4 sources.
"""

from typing import List, Dict, Any, Optional

VIDEOS_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "vid-01",
        "title": "Tears of Steel - Cyberpunk Sci-Fi VFX Showcase",
        "description": "Set in a dystopian future Amsterdam, a group of scientists and warriors attempt to stage a crucial historical event in order to rescue the world from destructive robotic sentinels.",
        "duration_seconds": 734,
        "duration_formatted": "12:14",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
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
        "title": "Big Buck Bunny - 4K Remastered Animation",
        "description": "A large and lovable rabbit deals with bullying forest creatures in this legendary open-source computer animated comedy film by the Blender Institute.",
        "duration_seconds": 596,
        "duration_formatted": "09:56",
        "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80",
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
        "title": "Sintel - The Dragon Quest Cinematic Fantasy",
        "description": "The poignant journey of a lonely girl named Sintel who rescues a wounded baby dragon, forming an unbreakable bond across a treacherous desert realm.",
        "duration_seconds": 888,
        "duration_formatted": "14:48",
        "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "views": 750100,
        "likes": 56000,
        "channel": {
            "name": "Fantasy World Cinema",
            "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&auto=format&fit=crop&q=80",
            "subscribers": "620K",
            "verified": True
        },
        "category": "Animation",
        "tags": ["fantasy", "dragon", "story", "epic", "emotional"],
        "published_at": "2 weeks ago",
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
        "title": "Elephant's Dream - Surreal Cyberpunk Odyssey",
        "description": "Proog and Emo guide you through the infinite mechanical labyrinths of a giant surreal organic machine, where human thoughts shape steel gears.",
        "duration_seconds": 653,
        "duration_formatted": "10:53",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
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
        "comments": []
    },
    {
        "id": "vid-05",
        "title": "Ocean Wilderness & Jellyfish 4K Showcase",
        "description": "Experience breathtaking high-definition underwater bioluminescent marine life, drifting jellyfish, and deep reef ecosystems.",
        "duration_seconds": 15,
        "duration_formatted": "00:15",
        "video_url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80",
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
        "comments": []
    },
    {
        "id": "vid-06",
        "title": "Big Buck Bunny - Forest Meadow Showcase",
        "description": "High-octane comedic forest animation featuring classic open-source 3D character animation and meadow wildlife.",
        "duration_seconds": 12,
        "duration_formatted": "00:12",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop&q=80",
        "views": 540800,
        "likes": 42100,
        "channel": {
            "name": "Speed & Style",
            "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=100&auto=format&fit=crop&q=80",
            "subscribers": "940K",
            "verified": True
        },
        "category": "Trending",
        "tags": ["cartoon", "funny", "classic", "animation"],
        "published_at": "1 month ago",
        "comments": []
    }
]

def get_all_videos(category: Optional[str] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
    """Returns list of videos filtered by category or search term."""
    results = VIDEOS_CATALOG
    if category and category.lower() != "all":
        results = [v for v in results if v["category"].lower() == category.lower()]
    if search:
        s = search.lower().strip()
        results = [
            v for v in results
            if s in v["title"].lower()
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
