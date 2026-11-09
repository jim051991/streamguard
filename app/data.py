"""
StreamGuard 2.0 OTT Entertainment Catalog & Streaming Data Store
Houses Global Cinema from around the world (Hollywood, Korean Cinema, Bollywood,
Japanese Anime/Kaiju, European Masterpieces, and Latin American Cinema) + Hit TV Series and Anime.
Modeled after CineHD & Movibox catalog architecture with Verified Direct Dual Audio MP4 Streams & Cloud 4K Embeds.
"""

from typing import List, Dict, Any, Optional

DUB_AUDIO_LANGUAGES = [
    {"code": "en-US", "lang": "en", "label": "English (Original)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "hi-IN", "lang": "hi", "label": "हिन्दी (Hindi Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "ta-IN", "lang": "ta", "label": "தமிழ் (Tamil Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "te-IN", "lang": "te", "label": "తెలుగు (Telugu Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "ml-IN", "lang": "ml", "label": "മലയാളം (Malayalam Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "kn-IN", "lang": "kn", "label": "ಕನ್ನಡ (Kannada Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "mr-IN", "lang": "mr", "label": "मराठी (Marathi Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "es-MX", "lang": "es", "label": "Español (Spanish Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "fr-FR", "lang": "fr", "label": "Français (French Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "de-DE", "lang": "de", "label": "Deutsch (German Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "ja-JP", "lang": "ja", "label": "日本語 (Japanese Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"},
    {"code": "ko-KR", "lang": "ko", "label": "한국어 (Korean Dub)", "bitrate": "320 kbps", "codec": "MP3 Dolby"}
]

def generate_movie_audio_tracks(video_id: str) -> List[Dict[str, Any]]:
    return [
        {
            "code": item["code"],
            "lang": item["lang"],
            "label": item["label"],
            "bitrate": item["bitrate"],
            "codec": item["codec"],
            "url": f"/api/audio/dub/{video_id}/{item['lang']}.mp3",
            "download_url": f"/api/audio/dub/{video_id}/{item['lang']}.mp3?download=1",
            "file_name": f"{video_id}_{item['lang']}.mp3"
        }
        for item in DUB_AUDIO_LANGUAGES
    ]

VIDEOS_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "mov-maharaja-2024",
        "title": "Maharaja (2024)",
        "subtitle": "Hindi + Tamil Dual Audio HD 720p",
        "content_type": "movie",
        "description": "A barber seeks vengeance after his home is burglarized, cryptically telling police his 'Lakshmi' has been taken. A relentless search unfolds in this celebrated thriller.",
        "release_year": 2024,
        "age_rating": "UA 16+",
        "imdb_rating": 8.5,
        "tmdb_id": 1114738,
        "imdb_id": "tt26548265",
        "quality": "720p HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8460,
        "duration_formatted": "2h 21m",
        "video_url": "https://archive.org/download/maharaja-2024-hindi-tamil-dual-audio-un-cut-movie-hd-720p-esub/Maharaja%20%282024%29%20%28Hindi%20%2B%20Tamil%29%20Dual%20Audio%20UnCut%20Movie%20HD%20720p%20ESub.mp4",
        "dual_audio_meta": {
            "title_with_audio": "Maharaja (2024) (Hindi + Tamil)",
            "languages": "Hindi + Tamil",
            "quality_spec": "720p HD Dual Audio MP4 (859 MB)",
            "stream_url": "https://archive.org/download/maharaja-2024-hindi-tamil-dual-audio-un-cut-movie-hd-720p-esub/Maharaja%20%282024%29%20%28Hindi%20%2B%20Tamil%29%20Dual%20Audio%20UnCut%20Movie%20HD%20720p%20ESub.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + Tamil)",
                "type": "native",
                "url": "https://archive.org/download/maharaja-2024-hindi-tamil-dual-audio-un-cut-movie-hd-720p-esub/Maharaja%20%282024%29%20%28Hindi%20%2B%20Tamil%29%20Dual%20Audio%20UnCut%20Movie%20HD%20720p%20ESub.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1114738?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1114738"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1114738"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4820000,
        "likes": 412000,
        "channel": {
            "name": "Passion Studios",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "maharaja",
            "vijay-sethupathi",
            "hindi-tamil",
            "dual-audio",
            "thriller",
            "2024"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": True,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/en.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/en.mp3?download=1",
                "file_name": "mov-maharaja-2024_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/hi.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/hi.mp3?download=1",
                "file_name": "mov-maharaja-2024_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/ta.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/ta.mp3?download=1",
                "file_name": "mov-maharaja-2024_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/te.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/te.mp3?download=1",
                "file_name": "mov-maharaja-2024_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/ml.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/ml.mp3?download=1",
                "file_name": "mov-maharaja-2024_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/kn.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/kn.mp3?download=1",
                "file_name": "mov-maharaja-2024_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/mr.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/mr.mp3?download=1",
                "file_name": "mov-maharaja-2024_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/es.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/es.mp3?download=1",
                "file_name": "mov-maharaja-2024_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/fr.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/fr.mp3?download=1",
                "file_name": "mov-maharaja-2024_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/de.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/de.mp3?download=1",
                "file_name": "mov-maharaja-2024_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/ja.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/ja.mp3?download=1",
                "file_name": "mov-maharaja-2024_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-maharaja-2024/ko.mp3",
                "download_url": "/api/audio/dub/mov-maharaja-2024/ko.mp3?download=1",
                "file_name": "mov-maharaja-2024_ko.mp3"
            }
        ]
    },
    {
        "id": "mov-blackout-2024",
        "title": "Blackout (2024)",
        "subtitle": "Bollywood Hindi Original HD 720p",
        "content_type": "movie",
        "description": "A crime thriller following a man caught in a web of greed, crime, and chaos on a single chaotic night in Pune when citywide darkness envelops everything.",
        "release_year": 2024,
        "age_rating": "UA 16+",
        "imdb_rating": 7.4,
        "tmdb_id": 1284004,
        "imdb_id": "tt27995874",
        "quality": "720p HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7320,
        "duration_formatted": "2h 02m",
        "video_url": "https://archive.org/download/maharaja-2024-hindi-tamil-dual-audio-un-cut-movie-hd-720p-esub/Blackout%20%282024%29%20Bollywood%20Hindi%20Movies%20HD%20720p%20ESub.mp4",
        "dual_audio_meta": {
            "title_with_audio": "Blackout (2024) (Bollywood Hindi (Original))",
            "languages": "Bollywood Hindi (Original)",
            "quality_spec": "720p HD Hindi MP4 (708 MB)",
            "stream_url": "https://archive.org/download/maharaja-2024-hindi-tamil-dual-audio-un-cut-movie-hd-720p-esub/Blackout%20%282024%29%20Bollywood%20Hindi%20Movies%20HD%20720p%20ESub.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Bollywood Hindi (Original))",
                "type": "native",
                "url": "https://archive.org/download/maharaja-2024-hindi-tamil-dual-audio-un-cut-movie-hd-720p-esub/Blackout%20%282024%29%20Bollywood%20Hindi%20Movies%20HD%20720p%20ESub.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1284004?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1284004"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1284004"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 3210000,
        "likes": 298000,
        "channel": {
            "name": "Jio Studios",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "12.1M",
            "verified": True
        },
        "category": "Thriller",
        "tags": [
            "blackout",
            "vikrant-massey",
            "hindi",
            "bollywood",
            "crime",
            "2024"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/en.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/en.mp3?download=1",
                "file_name": "mov-blackout-2024_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/hi.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/hi.mp3?download=1",
                "file_name": "mov-blackout-2024_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/ta.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/ta.mp3?download=1",
                "file_name": "mov-blackout-2024_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/te.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/te.mp3?download=1",
                "file_name": "mov-blackout-2024_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/ml.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/ml.mp3?download=1",
                "file_name": "mov-blackout-2024_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/kn.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/kn.mp3?download=1",
                "file_name": "mov-blackout-2024_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/mr.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/mr.mp3?download=1",
                "file_name": "mov-blackout-2024_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/es.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/es.mp3?download=1",
                "file_name": "mov-blackout-2024_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/fr.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/fr.mp3?download=1",
                "file_name": "mov-blackout-2024_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/de.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/de.mp3?download=1",
                "file_name": "mov-blackout-2024_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/ja.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/ja.mp3?download=1",
                "file_name": "mov-blackout-2024_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-blackout-2024/ko.mp3",
                "download_url": "/api/audio/dub/mov-blackout-2024/ko.mp3?download=1",
                "file_name": "mov-blackout-2024_ko.mp3"
            }
        ]
    },
    {
        "id": "mov-artemis-fowl",
        "title": "Artemis Fowl",
        "subtitle": "Hindi DD 2.0 + English Dual Audio 720p HDRip",
        "content_type": "movie",
        "description": "Artemis Fowl, a young crime prodigy, hunts down a secret society of fairies to find his missing father. Features full dual audio with Hindi DD 2.0 and English soundtracks.",
        "release_year": 2020,
        "age_rating": "PG",
        "imdb_rating": 6.8,
        "tmdb_id": 475430,
        "imdb_id": "tt3089630",
        "quality": "720p HDRip",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 5700,
        "duration_formatted": "1h 35m",
        "video_url": "https://archive.org/download/artemis-fowl-2020-720p-hdrip-x-264-dual-audio-hindi-dd-2.0-english-dd-2.0/Artemis%20Fowl%202020%20%5BWorldfree4u.Cloud%5D%20720p%20HDRip%20x264%20%5BDual%20Audio%5D%20%5BHindi%20DD%202.0%20%2B%20English%20DD%202.0%5D.mp4",
        "dual_audio_meta": {
            "title_with_audio": "Artemis Fowl (Hindi DD 2.0 + English)",
            "languages": "Hindi DD 2.0 + English",
            "quality_spec": "720p HDRip Dual Audio MP4 (258 MB)",
            "stream_url": "https://archive.org/download/artemis-fowl-2020-720p-hdrip-x-264-dual-audio-hindi-dd-2.0-english-dd-2.0/Artemis%20Fowl%202020%20%5BWorldfree4u.Cloud%5D%20720p%20HDRip%20x264%20%5BDual%20Audio%5D%20%5BHindi%20DD%202.0%20%2B%20English%20DD%202.0%5D.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi DD 2.0 + English)",
                "type": "native",
                "url": "https://archive.org/download/artemis-fowl-2020-720p-hdrip-x-264-dual-audio-hindi-dd-2.0-english-dd-2.0/Artemis%20Fowl%202020%20%5BWorldfree4u.Cloud%5D%20720p%20HDRip%20x264%20%5BDual%20Audio%5D%20%5BHindi%20DD%202.0%20%2B%20English%20DD%202.0%5D.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/475430?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/475430"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/475430"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 2940000,
        "likes": 218000,
        "channel": {
            "name": "Walt Disney Pictures",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "15.8M",
            "verified": True
        },
        "category": "Fantasy",
        "tags": [
            "artemis-fowl",
            "disney",
            "hindi-dd",
            "dual-audio",
            "fantasy",
            "adventure"
        ],
        "published_at": "2020",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/en.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/en.mp3?download=1",
                "file_name": "mov-artemis-fowl_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/hi.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/hi.mp3?download=1",
                "file_name": "mov-artemis-fowl_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/ta.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/ta.mp3?download=1",
                "file_name": "mov-artemis-fowl_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/te.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/te.mp3?download=1",
                "file_name": "mov-artemis-fowl_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/ml.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/ml.mp3?download=1",
                "file_name": "mov-artemis-fowl_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/kn.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/kn.mp3?download=1",
                "file_name": "mov-artemis-fowl_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/mr.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/mr.mp3?download=1",
                "file_name": "mov-artemis-fowl_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/es.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/es.mp3?download=1",
                "file_name": "mov-artemis-fowl_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/fr.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/fr.mp3?download=1",
                "file_name": "mov-artemis-fowl_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/de.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/de.mp3?download=1",
                "file_name": "mov-artemis-fowl_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/ja.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/ja.mp3?download=1",
                "file_name": "mov-artemis-fowl_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-artemis-fowl/ko.mp3",
                "download_url": "/api/audio/dub/mov-artemis-fowl/ko.mp3?download=1",
                "file_name": "mov-artemis-fowl_ko.mp3"
            }
        ]
    },
    {
        "id": "mov-deadpool-wolverine",
        "title": "Deadpool & Wolverine",
        "subtitle": "Marvel Cinematic Multiverse Action",
        "content_type": "movie",
        "description": "A listless Wade Wilson toils away in civilian life with his days as the morally flexible mercenary Deadpool behind him. But when his homeworld faces an existential threat, Wade must reluctantly suit-up again with an even more reluctant Wolverine.",
        "release_year": 2024,
        "age_rating": "R",
        "imdb_rating": 7.8,
        "tmdb_id": 533535,
        "imdb_id": "tt6263850",
        "quality": "1080p HD",
        "is_dual_audio": True,
        "languages": "English (Original), हिन्दी (Hindi Dub), தமிழ் (Tamil Dub), తెలుగు (Telugu Dub), മലയാളം (Malayalam Dub), ಕನ್ನಡ (Kannada Dub), मराठी (Marathi Dub), Español (Spanish Dub), Français (French Dub), Deutsch (German Dub), 日本語 (Japanese Dub), 한국어 (Korean Dub)",
        "audio_tracks_count": 12,
        "duration_seconds": 7680,
        "duration_formatted": "2h 08m",
        "video_url": "https://archive.org/download/deadpool-wolverine_HD_DUBLADO_SINCRONIZADO/Deadpool%20%26%20Wolverine.ia.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Full Movie (All Languages Dual Audio 1080p)",
                "type": "native",
                "quality": "1080p HD",
                "url": "https://archive.org/download/deadpool-wolverine_HD_DUBLADO_SINCRONIZADO/Deadpool%20%26%20Wolverine.ia.mp4",
                "clean": True,
                "dual_audio": True,
                "size": "759 MB"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (VidLink 4K)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/533535?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/533535"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/533535"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 6480000,
        "likes": 542000,
        "channel": {
            "name": "Marvel Studios",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "20.4M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "deadpool",
            "wolverine",
            "marvel",
            "ryan-reynolds",
            "hugh-jackman",
            "4k",
            "hollywood"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": True,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/en.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/en.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/hi.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/hi.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/ta.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/ta.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/te.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/te.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/ml.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/ml.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/kn.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/kn.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/mr.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/mr.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/es.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/es.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/fr.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/fr.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/de.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/de.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/ja.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/ja.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-deadpool-wolverine/ko.mp3",
                "download_url": "/api/audio/dub/mov-deadpool-wolverine/ko.mp3?download=1",
                "file_name": "mov-deadpool-wolverine_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Deadpool & Wolverine (All Released Languages)",
            "languages": "English, Hindi, Tamil, Telugu, Malayalam, Kannada, Marathi, Spanish, French, German, Japanese, Korean",
            "quality_spec": "1080p HD Multi-Language (12 Released Dubs)",
            "stream_url": "https://archive.org/download/deadpool-wolverine_HD_DUBLADO_SINCRONIZADO/Deadpool%20%26%20Wolverine.ia.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-dune-2",
        "title": "Dune: Part Two",
        "subtitle": "Epic Sci-Fi Space Opera",
        "content_type": "movie",
        "description": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the known universe, he endeavors to prevent a terrible future only he can foresee.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 8.6,
        "tmdb_id": 693134,
        "imdb_id": "tt15239678",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 9960,
        "duration_formatted": "2h 46m",
        "video_url": "https://vidlink.pro/movie/693134?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/693134?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/693134"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/693134"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5480000,
        "likes": 482000,
        "channel": {
            "name": "Warner Bros. Pictures",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "11.2M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "dune",
            "sci-fi",
            "timothee-chalamet",
            "zendaya",
            "4k",
            "hollywood"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/en.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/en.mp3?download=1",
                "file_name": "mov-dune-2_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/hi.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/hi.mp3?download=1",
                "file_name": "mov-dune-2_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/ta.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/ta.mp3?download=1",
                "file_name": "mov-dune-2_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/te.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/te.mp3?download=1",
                "file_name": "mov-dune-2_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/ml.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/ml.mp3?download=1",
                "file_name": "mov-dune-2_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/kn.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/kn.mp3?download=1",
                "file_name": "mov-dune-2_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/mr.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/mr.mp3?download=1",
                "file_name": "mov-dune-2_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/es.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/es.mp3?download=1",
                "file_name": "mov-dune-2_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/fr.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/fr.mp3?download=1",
                "file_name": "mov-dune-2_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/de.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/de.mp3?download=1",
                "file_name": "mov-dune-2_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/ja.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/ja.mp3?download=1",
                "file_name": "mov-dune-2_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dune-2/ko.mp3",
                "download_url": "/api/audio/dub/mov-dune-2/ko.mp3?download=1",
                "file_name": "mov-dune-2_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Dune: Part Two (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/693134?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-oppenheimer",
        "title": "Oppenheimer",
        "subtitle": "Historical Thriller Masterpiece",
        "content_type": "movie",
        "description": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during the Manhattan Project, exploring the moral and political turmoil that followed.",
        "release_year": 2023,
        "age_rating": "R",
        "imdb_rating": 8.9,
        "tmdb_id": 872585,
        "imdb_id": "tt15398776",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10800,
        "duration_formatted": "3h 00m",
        "video_url": "https://vidlink.pro/movie/872585?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/872585?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/872585"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/872585"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4890000,
        "likes": 394000,
        "channel": {
            "name": "Universal Pictures",
            "avatar": "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=100",
            "subscribers": "9.8M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "oppenheimer",
            "christopher-nolan",
            "cillian-murphy",
            "oscar-winner",
            "hollywood"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/en.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/en.mp3?download=1",
                "file_name": "mov-oppenheimer_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/hi.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/hi.mp3?download=1",
                "file_name": "mov-oppenheimer_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/ta.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/ta.mp3?download=1",
                "file_name": "mov-oppenheimer_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/te.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/te.mp3?download=1",
                "file_name": "mov-oppenheimer_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/ml.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/ml.mp3?download=1",
                "file_name": "mov-oppenheimer_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/kn.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/kn.mp3?download=1",
                "file_name": "mov-oppenheimer_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/mr.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/mr.mp3?download=1",
                "file_name": "mov-oppenheimer_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/es.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/es.mp3?download=1",
                "file_name": "mov-oppenheimer_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/fr.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/fr.mp3?download=1",
                "file_name": "mov-oppenheimer_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/de.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/de.mp3?download=1",
                "file_name": "mov-oppenheimer_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/ja.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/ja.mp3?download=1",
                "file_name": "mov-oppenheimer_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-oppenheimer/ko.mp3",
                "download_url": "/api/audio/dub/mov-oppenheimer/ko.mp3?download=1",
                "file_name": "mov-oppenheimer_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Oppenheimer (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/872585?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-gladiator-2",
        "title": "Gladiator II",
        "subtitle": "Ridley Scott Roman Arena Epic",
        "content_type": "movie",
        "description": "Years after witnessing the death of the revered hero Maximus at the hands of his uncle, Lucius must enter the Colosseum after his home is conquered by the tyrannical Emperors who now lead Rome with an iron fist.",
        "release_year": 2024,
        "age_rating": "R",
        "imdb_rating": 7.2,
        "tmdb_id": 558449,
        "imdb_id": "tt9660502",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8880,
        "duration_formatted": "2h 28m",
        "video_url": "https://vidlink.pro/movie/558449?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/558449?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/558449"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/558449"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4120000,
        "likes": 328000,
        "channel": {
            "name": "Paramount Pictures",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "gladiator",
            "rome",
            "paul-mescal",
            "denzel-washington",
            "ridley-scott",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/en.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/en.mp3?download=1",
                "file_name": "mov-gladiator-2_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/hi.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/hi.mp3?download=1",
                "file_name": "mov-gladiator-2_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/ta.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/ta.mp3?download=1",
                "file_name": "mov-gladiator-2_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/te.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/te.mp3?download=1",
                "file_name": "mov-gladiator-2_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/ml.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/ml.mp3?download=1",
                "file_name": "mov-gladiator-2_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/kn.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/kn.mp3?download=1",
                "file_name": "mov-gladiator-2_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/mr.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/mr.mp3?download=1",
                "file_name": "mov-gladiator-2_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/es.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/es.mp3?download=1",
                "file_name": "mov-gladiator-2_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/fr.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/fr.mp3?download=1",
                "file_name": "mov-gladiator-2_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/de.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/de.mp3?download=1",
                "file_name": "mov-gladiator-2_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/ja.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/ja.mp3?download=1",
                "file_name": "mov-gladiator-2_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-gladiator-2/ko.mp3",
                "download_url": "/api/audio/dub/mov-gladiator-2/ko.mp3?download=1",
                "file_name": "mov-gladiator-2_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Gladiator II (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/558449?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-inside-out-2",
        "title": "Inside Out 2",
        "subtitle": "Disney Pixar Emotional Journey",
        "content_type": "movie",
        "description": "Teenager Riley's mind headquarters is undergoing a sudden demolition to make room for something entirely unexpected: new Emotions! Joy, Sadness, Anger, Fear and Disgust aren't sure how to feel when Anxiety shows up.",
        "release_year": 2024,
        "age_rating": "PG",
        "imdb_rating": 7.6,
        "tmdb_id": 1022789,
        "imdb_id": "tt22022452",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 5760,
        "duration_formatted": "1h 36m",
        "video_url": "https://vidlink.pro/movie/1022789?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1022789?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1022789"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1022789"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5890000,
        "likes": 512000,
        "channel": {
            "name": "Pixar Animation",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "14.2M",
            "verified": True
        },
        "category": "Animation",
        "tags": [
            "inside-out",
            "pixar",
            "disney",
            "animation",
            "family",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/en.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/en.mp3?download=1",
                "file_name": "mov-inside-out-2_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/hi.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/hi.mp3?download=1",
                "file_name": "mov-inside-out-2_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/ta.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/ta.mp3?download=1",
                "file_name": "mov-inside-out-2_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/te.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/te.mp3?download=1",
                "file_name": "mov-inside-out-2_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/ml.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/ml.mp3?download=1",
                "file_name": "mov-inside-out-2_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/kn.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/kn.mp3?download=1",
                "file_name": "mov-inside-out-2_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/mr.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/mr.mp3?download=1",
                "file_name": "mov-inside-out-2_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/es.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/es.mp3?download=1",
                "file_name": "mov-inside-out-2_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/fr.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/fr.mp3?download=1",
                "file_name": "mov-inside-out-2_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/de.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/de.mp3?download=1",
                "file_name": "mov-inside-out-2_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/ja.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/ja.mp3?download=1",
                "file_name": "mov-inside-out-2_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inside-out-2/ko.mp3",
                "download_url": "/api/audio/dub/mov-inside-out-2/ko.mp3?download=1",
                "file_name": "mov-inside-out-2_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Inside Out 2 (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/1022789?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-alien-romulus",
        "title": "Alien: Romulus",
        "subtitle": "Deep Space Survival Horror",
        "content_type": "movie",
        "description": "While scavenging the deep ends of a derelict space station, a group of young space colonizers come face to face with the most terrifying and deadly life form in the universe.",
        "release_year": 2024,
        "age_rating": "R",
        "imdb_rating": 7.3,
        "tmdb_id": 945961,
        "imdb_id": "tt18412256",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7140,
        "duration_formatted": "1h 59m",
        "video_url": "https://vidlink.pro/movie/945961?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/945961?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/945961"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/945961"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 3940000,
        "likes": 289000,
        "channel": {
            "name": "20th Century Studios",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "6.8M",
            "verified": True
        },
        "category": "Horror",
        "tags": [
            "alien",
            "romulus",
            "xenomorph",
            "sci-fi",
            "horror",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/en.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/en.mp3?download=1",
                "file_name": "mov-alien-romulus_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/hi.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/hi.mp3?download=1",
                "file_name": "mov-alien-romulus_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/ta.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/ta.mp3?download=1",
                "file_name": "mov-alien-romulus_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/te.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/te.mp3?download=1",
                "file_name": "mov-alien-romulus_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/ml.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/ml.mp3?download=1",
                "file_name": "mov-alien-romulus_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/kn.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/kn.mp3?download=1",
                "file_name": "mov-alien-romulus_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/mr.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/mr.mp3?download=1",
                "file_name": "mov-alien-romulus_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/es.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/es.mp3?download=1",
                "file_name": "mov-alien-romulus_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/fr.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/fr.mp3?download=1",
                "file_name": "mov-alien-romulus_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/de.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/de.mp3?download=1",
                "file_name": "mov-alien-romulus_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/ja.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/ja.mp3?download=1",
                "file_name": "mov-alien-romulus_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-alien-romulus/ko.mp3",
                "download_url": "/api/audio/dub/mov-alien-romulus/ko.mp3?download=1",
                "file_name": "mov-alien-romulus_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Alien: Romulus (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/945961?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-the-substance",
        "title": "The Substance",
        "subtitle": "Body Horror Satire Sensation",
        "content_type": "movie",
        "description": "A fading celebrity decides to use a black-market drug, a cell-replicating substance that temporarily creates a younger, better version of herself, leading to nightmarish consequences.",
        "release_year": 2024,
        "age_rating": "R",
        "imdb_rating": 7.7,
        "tmdb_id": 933260,
        "imdb_id": "tt17526714",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8460,
        "duration_formatted": "2h 21m",
        "video_url": "https://vidlink.pro/movie/933260?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/933260?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/933260"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/933260"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 3120000,
        "likes": 268000,
        "channel": {
            "name": "MUBI / Universal",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "5.4M",
            "verified": True
        },
        "category": "Horror",
        "tags": [
            "the-substance",
            "demi-moore",
            "margaret-qualley",
            "cannes-winner",
            "horror",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/en.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/en.mp3?download=1",
                "file_name": "mov-the-substance_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/hi.mp3?download=1",
                "file_name": "mov-the-substance_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/ta.mp3?download=1",
                "file_name": "mov-the-substance_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/te.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/te.mp3?download=1",
                "file_name": "mov-the-substance_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/ml.mp3?download=1",
                "file_name": "mov-the-substance_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/kn.mp3?download=1",
                "file_name": "mov-the-substance_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/mr.mp3?download=1",
                "file_name": "mov-the-substance_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/es.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/es.mp3?download=1",
                "file_name": "mov-the-substance_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/fr.mp3?download=1",
                "file_name": "mov-the-substance_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/de.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/de.mp3?download=1",
                "file_name": "mov-the-substance_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/ja.mp3?download=1",
                "file_name": "mov-the-substance_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-substance/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-substance/ko.mp3?download=1",
                "file_name": "mov-the-substance_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Substance (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/933260?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-the-wild-robot",
        "title": "The Wild Robot",
        "subtitle": "Heartwarming Nature Sci-Fi Animation",
        "content_type": "movie",
        "description": "After a shipwreck, an intelligent robot named Roz is stranded on an uninhabited island. To survive the harsh environment, Roz bonds with the island's animals and cares for an orphaned baby goose.",
        "release_year": 2024,
        "age_rating": "PG",
        "imdb_rating": 8.4,
        "tmdb_id": 1184918,
        "imdb_id": "tt29623480",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 6120,
        "duration_formatted": "1h 42m",
        "video_url": "https://vidlink.pro/movie/1184918?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1184918?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1184918"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1184918"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4450000,
        "likes": 395000,
        "channel": {
            "name": "DreamWorks Animation",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "10.1M",
            "verified": True
        },
        "category": "Animation",
        "tags": [
            "wild-robot",
            "dreamworks",
            "lupita-nyongo",
            "animation",
            "family",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/en.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/en.mp3?download=1",
                "file_name": "mov-the-wild-robot_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/hi.mp3?download=1",
                "file_name": "mov-the-wild-robot_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/ta.mp3?download=1",
                "file_name": "mov-the-wild-robot_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/te.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/te.mp3?download=1",
                "file_name": "mov-the-wild-robot_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/ml.mp3?download=1",
                "file_name": "mov-the-wild-robot_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/kn.mp3?download=1",
                "file_name": "mov-the-wild-robot_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/mr.mp3?download=1",
                "file_name": "mov-the-wild-robot_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/es.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/es.mp3?download=1",
                "file_name": "mov-the-wild-robot_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/fr.mp3?download=1",
                "file_name": "mov-the-wild-robot_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/de.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/de.mp3?download=1",
                "file_name": "mov-the-wild-robot_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/ja.mp3?download=1",
                "file_name": "mov-the-wild-robot_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-wild-robot/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-wild-robot/ko.mp3?download=1",
                "file_name": "mov-the-wild-robot_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Wild Robot (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/1184918?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-furiosa",
        "title": "Furiosa: A Mad Max Saga",
        "subtitle": "High-Octane Wasteland Action",
        "content_type": "movie",
        "description": "As the world fell, young Furiosa is snatched from the Green Place of Many Mothers and falls into the hands of a great Biker Horde led by the Warlord Dementus. Sweeping through the Wasteland, they come across the Citadel presided over by The Immortan Joe.",
        "release_year": 2024,
        "age_rating": "R",
        "imdb_rating": 7.6,
        "tmdb_id": 786892,
        "imdb_id": "tt12037194",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8880,
        "duration_formatted": "2h 28m",
        "video_url": "https://vidlink.pro/movie/786892?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/786892?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/786892"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/786892"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 3780000,
        "likes": 312000,
        "channel": {
            "name": "Warner Bros. Pictures",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "11.2M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "furiosa",
            "mad-max",
            "anya-taylor-joy",
            "chris-hemsworth",
            "action",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/en.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/en.mp3?download=1",
                "file_name": "mov-furiosa_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/hi.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/hi.mp3?download=1",
                "file_name": "mov-furiosa_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/ta.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/ta.mp3?download=1",
                "file_name": "mov-furiosa_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/te.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/te.mp3?download=1",
                "file_name": "mov-furiosa_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/ml.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/ml.mp3?download=1",
                "file_name": "mov-furiosa_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/kn.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/kn.mp3?download=1",
                "file_name": "mov-furiosa_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/mr.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/mr.mp3?download=1",
                "file_name": "mov-furiosa_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/es.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/es.mp3?download=1",
                "file_name": "mov-furiosa_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/fr.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/fr.mp3?download=1",
                "file_name": "mov-furiosa_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/de.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/de.mp3?download=1",
                "file_name": "mov-furiosa_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/ja.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/ja.mp3?download=1",
                "file_name": "mov-furiosa_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-furiosa/ko.mp3",
                "download_url": "/api/audio/dub/mov-furiosa/ko.mp3?download=1",
                "file_name": "mov-furiosa_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Furiosa: A Mad Max Saga (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/786892?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-top-gun-maverick",
        "title": "Top Gun: Maverick",
        "subtitle": "Aerial Combat Blockbuster",
        "content_type": "movie",
        "description": "After thirty years, Maverick is still pushing the envelope as a top naval aviator, but must confront ghosts of his past when he leads TOP GUN's elite graduates on an impossible mission that demands the ultimate sacrifice from those chosen to fly it.",
        "release_year": 2022,
        "age_rating": "PG-13",
        "imdb_rating": 8.3,
        "tmdb_id": 361743,
        "imdb_id": "tt1745960",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7800,
        "duration_formatted": "2h 10m",
        "video_url": "https://vidlink.pro/movie/361743?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/361743?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/361743"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/361743"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1519074069444-1ba4ea16e6f1?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1519074069444-1ba4ea16e6f1?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1519074069444-1ba4ea16e6f1?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 6120000,
        "likes": 534000,
        "channel": {
            "name": "Paramount Pictures",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "top-gun",
            "maverick",
            "tom-cruise",
            "aviation",
            "blockbuster",
            "4k"
        ],
        "published_at": "2022",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/en.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/en.mp3?download=1",
                "file_name": "mov-top-gun-maverick_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/hi.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/hi.mp3?download=1",
                "file_name": "mov-top-gun-maverick_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/ta.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/ta.mp3?download=1",
                "file_name": "mov-top-gun-maverick_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/te.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/te.mp3?download=1",
                "file_name": "mov-top-gun-maverick_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/ml.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/ml.mp3?download=1",
                "file_name": "mov-top-gun-maverick_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/kn.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/kn.mp3?download=1",
                "file_name": "mov-top-gun-maverick_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/mr.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/mr.mp3?download=1",
                "file_name": "mov-top-gun-maverick_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/es.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/es.mp3?download=1",
                "file_name": "mov-top-gun-maverick_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/fr.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/fr.mp3?download=1",
                "file_name": "mov-top-gun-maverick_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/de.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/de.mp3?download=1",
                "file_name": "mov-top-gun-maverick_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/ja.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/ja.mp3?download=1",
                "file_name": "mov-top-gun-maverick_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-top-gun-maverick/ko.mp3",
                "download_url": "/api/audio/dub/mov-top-gun-maverick/ko.mp3?download=1",
                "file_name": "mov-top-gun-maverick_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Top Gun: Maverick (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/361743?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-the-dark-knight",
        "title": "The Dark Knight",
        "subtitle": "Christopher Nolan Superhero Masterpiece",
        "content_type": "movie",
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "release_year": 2008,
        "age_rating": "PG-13",
        "imdb_rating": 9.0,
        "tmdb_id": 155,
        "imdb_id": "tt0468569",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 9120,
        "duration_formatted": "2h 32m",
        "video_url": "https://vidlink.pro/movie/155?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/155?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/155"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/155"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 9850000,
        "likes": 920000,
        "channel": {
            "name": "Warner Bros. Pictures",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "11.2M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "batman",
            "dark-knight",
            "heath-ledger",
            "joker",
            "nolan",
            "4k"
        ],
        "published_at": "2008",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/en.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/en.mp3?download=1",
                "file_name": "mov-the-dark-knight_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/hi.mp3?download=1",
                "file_name": "mov-the-dark-knight_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/ta.mp3?download=1",
                "file_name": "mov-the-dark-knight_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/te.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/te.mp3?download=1",
                "file_name": "mov-the-dark-knight_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/ml.mp3?download=1",
                "file_name": "mov-the-dark-knight_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/kn.mp3?download=1",
                "file_name": "mov-the-dark-knight_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/mr.mp3?download=1",
                "file_name": "mov-the-dark-knight_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/es.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/es.mp3?download=1",
                "file_name": "mov-the-dark-knight_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/fr.mp3?download=1",
                "file_name": "mov-the-dark-knight_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/de.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/de.mp3?download=1",
                "file_name": "mov-the-dark-knight_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/ja.mp3?download=1",
                "file_name": "mov-the-dark-knight_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-dark-knight/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-dark-knight/ko.mp3?download=1",
                "file_name": "mov-the-dark-knight_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Dark Knight (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/155?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-inception",
        "title": "Inception",
        "subtitle": "Mind-Bending Dream Heist Thriller",
        "content_type": "movie",
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
        "release_year": 2010,
        "age_rating": "PG-13",
        "imdb_rating": 8.8,
        "tmdb_id": 27205,
        "imdb_id": "tt1375666",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8880,
        "duration_formatted": "2h 28m",
        "video_url": "https://vidlink.pro/movie/27205?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/27205?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/27205"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/27205"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 8450000,
        "likes": 789000,
        "channel": {
            "name": "Warner Bros. Pictures",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "11.2M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "inception",
            "dreams",
            "leonardo-dicaprio",
            "nolan",
            "sci-fi",
            "4k"
        ],
        "published_at": "2010",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/en.mp3",
                "download_url": "/api/audio/dub/mov-inception/en.mp3?download=1",
                "file_name": "mov-inception_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/hi.mp3",
                "download_url": "/api/audio/dub/mov-inception/hi.mp3?download=1",
                "file_name": "mov-inception_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/ta.mp3",
                "download_url": "/api/audio/dub/mov-inception/ta.mp3?download=1",
                "file_name": "mov-inception_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/te.mp3",
                "download_url": "/api/audio/dub/mov-inception/te.mp3?download=1",
                "file_name": "mov-inception_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/ml.mp3",
                "download_url": "/api/audio/dub/mov-inception/ml.mp3?download=1",
                "file_name": "mov-inception_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/kn.mp3",
                "download_url": "/api/audio/dub/mov-inception/kn.mp3?download=1",
                "file_name": "mov-inception_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/mr.mp3",
                "download_url": "/api/audio/dub/mov-inception/mr.mp3?download=1",
                "file_name": "mov-inception_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/es.mp3",
                "download_url": "/api/audio/dub/mov-inception/es.mp3?download=1",
                "file_name": "mov-inception_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/fr.mp3",
                "download_url": "/api/audio/dub/mov-inception/fr.mp3?download=1",
                "file_name": "mov-inception_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/de.mp3",
                "download_url": "/api/audio/dub/mov-inception/de.mp3?download=1",
                "file_name": "mov-inception_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/ja.mp3",
                "download_url": "/api/audio/dub/mov-inception/ja.mp3?download=1",
                "file_name": "mov-inception_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-inception/ko.mp3",
                "download_url": "/api/audio/dub/mov-inception/ko.mp3?download=1",
                "file_name": "mov-inception_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Inception (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/27205?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-john-wick-4",
        "title": "John Wick: Chapter 4",
        "subtitle": "Legendary Hitman Action Ballet",
        "content_type": "movie",
        "description": "John Wick uncovers a path to defeating The High Table. But before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe and forces that turn old friends into foes.",
        "release_year": 2023,
        "age_rating": "R",
        "imdb_rating": 7.7,
        "tmdb_id": 603692,
        "imdb_id": "tt10366206",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10140,
        "duration_formatted": "2h 49m",
        "video_url": "https://vidlink.pro/movie/603692?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/603692?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/603692"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/603692"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4920000,
        "likes": 421000,
        "channel": {
            "name": "Lionsgate",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "7.1M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "john-wick",
            "keanu-reeves",
            "donnie-yen",
            "action",
            "4k"
        ],
        "published_at": "2023",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/en.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/en.mp3?download=1",
                "file_name": "mov-john-wick-4_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/hi.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/hi.mp3?download=1",
                "file_name": "mov-john-wick-4_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/ta.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/ta.mp3?download=1",
                "file_name": "mov-john-wick-4_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/te.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/te.mp3?download=1",
                "file_name": "mov-john-wick-4_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/ml.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/ml.mp3?download=1",
                "file_name": "mov-john-wick-4_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/kn.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/kn.mp3?download=1",
                "file_name": "mov-john-wick-4_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/mr.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/mr.mp3?download=1",
                "file_name": "mov-john-wick-4_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/es.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/es.mp3?download=1",
                "file_name": "mov-john-wick-4_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/fr.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/fr.mp3?download=1",
                "file_name": "mov-john-wick-4_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/de.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/de.mp3?download=1",
                "file_name": "mov-john-wick-4_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/ja.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/ja.mp3?download=1",
                "file_name": "mov-john-wick-4_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-john-wick-4/ko.mp3",
                "download_url": "/api/audio/dub/mov-john-wick-4/ko.mp3?download=1",
                "file_name": "mov-john-wick-4_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "John Wick: Chapter 4 (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/603692?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-interstellar",
        "title": "Interstellar",
        "subtitle": "Christopher Nolan Sci-Fi Epic",
        "content_type": "movie",
        "description": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
        "release_year": 2014,
        "age_rating": "PG-13",
        "imdb_rating": 8.7,
        "tmdb_id": 157336,
        "imdb_id": "tt0816692",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10140,
        "duration_formatted": "2h 49m",
        "video_url": "https://vidlink.pro/movie/157336?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/157336?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/157336"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/157336"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5210000,
        "likes": 482000,
        "channel": {
            "name": "Paramount Pictures",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "interstellar",
            "space",
            "nolan",
            "black-hole",
            "4k",
            "hollywood"
        ],
        "published_at": "2014",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/en.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/en.mp3?download=1",
                "file_name": "mov-interstellar_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/hi.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/hi.mp3?download=1",
                "file_name": "mov-interstellar_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/ta.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/ta.mp3?download=1",
                "file_name": "mov-interstellar_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/te.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/te.mp3?download=1",
                "file_name": "mov-interstellar_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/ml.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/ml.mp3?download=1",
                "file_name": "mov-interstellar_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/kn.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/kn.mp3?download=1",
                "file_name": "mov-interstellar_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/mr.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/mr.mp3?download=1",
                "file_name": "mov-interstellar_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/es.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/es.mp3?download=1",
                "file_name": "mov-interstellar_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/fr.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/fr.mp3?download=1",
                "file_name": "mov-interstellar_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/de.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/de.mp3?download=1",
                "file_name": "mov-interstellar_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/ja.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/ja.mp3?download=1",
                "file_name": "mov-interstellar_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-interstellar/ko.mp3",
                "download_url": "/api/audio/dub/mov-interstellar/ko.mp3?download=1",
                "file_name": "mov-interstellar_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Interstellar (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/157336?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-the-batman",
        "title": "The Batman",
        "subtitle": "Dark Detective Neo-Noir",
        "content_type": "movie",
        "description": "In his second year of fighting crime, Batman uncovers corruption in Gotham City that connects to his own family while facing a serial killer known as the Riddler.",
        "release_year": 2022,
        "age_rating": "PG-13",
        "imdb_rating": 7.8,
        "tmdb_id": 414906,
        "imdb_id": "tt1877830",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10560,
        "duration_formatted": "2h 56m",
        "video_url": "https://vidlink.pro/movie/414906?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/414906?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/414906"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/414906"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 2980000,
        "likes": 215000,
        "channel": {
            "name": "DC Films / Warner Bros.",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "11.2M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "the-batman",
            "robert-pattinson",
            "dc",
            "gotham",
            "4k",
            "hollywood"
        ],
        "published_at": "2022",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/en.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/en.mp3?download=1",
                "file_name": "mov-the-batman_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/hi.mp3?download=1",
                "file_name": "mov-the-batman_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/ta.mp3?download=1",
                "file_name": "mov-the-batman_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/te.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/te.mp3?download=1",
                "file_name": "mov-the-batman_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/ml.mp3?download=1",
                "file_name": "mov-the-batman_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/kn.mp3?download=1",
                "file_name": "mov-the-batman_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/mr.mp3?download=1",
                "file_name": "mov-the-batman_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/es.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/es.mp3?download=1",
                "file_name": "mov-the-batman_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/fr.mp3?download=1",
                "file_name": "mov-the-batman_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/de.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/de.mp3?download=1",
                "file_name": "mov-the-batman_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/ja.mp3?download=1",
                "file_name": "mov-the-batman_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-batman/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-batman/ko.mp3?download=1",
                "file_name": "mov-the-batman_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Batman (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/414906?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-avatar-2",
        "title": "Avatar: The Way of Water",
        "subtitle": "James Cameron Sci-Fi Phenomenon",
        "content_type": "movie",
        "description": "Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na'vi race to protect their home.",
        "release_year": 2022,
        "age_rating": "PG-13",
        "imdb_rating": 7.6,
        "tmdb_id": 76600,
        "imdb_id": "tt1630029",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 11520,
        "duration_formatted": "3h 12m",
        "video_url": "https://vidlink.pro/movie/76600?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/76600?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/76600"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/76600"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4750000,
        "likes": 367000,
        "channel": {
            "name": "20th Century Studios",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "6.8M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "avatar",
            "pandora",
            "james-cameron",
            "way-of-water",
            "4k",
            "hollywood"
        ],
        "published_at": "2022",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/en.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/en.mp3?download=1",
                "file_name": "mov-avatar-2_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/hi.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/hi.mp3?download=1",
                "file_name": "mov-avatar-2_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/ta.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/ta.mp3?download=1",
                "file_name": "mov-avatar-2_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/te.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/te.mp3?download=1",
                "file_name": "mov-avatar-2_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/ml.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/ml.mp3?download=1",
                "file_name": "mov-avatar-2_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/kn.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/kn.mp3?download=1",
                "file_name": "mov-avatar-2_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/mr.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/mr.mp3?download=1",
                "file_name": "mov-avatar-2_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/es.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/es.mp3?download=1",
                "file_name": "mov-avatar-2_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/fr.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/fr.mp3?download=1",
                "file_name": "mov-avatar-2_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/de.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/de.mp3?download=1",
                "file_name": "mov-avatar-2_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/ja.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/ja.mp3?download=1",
                "file_name": "mov-avatar-2_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-avatar-2/ko.mp3",
                "download_url": "/api/audio/dub/mov-avatar-2/ko.mp3?download=1",
                "file_name": "mov-avatar-2_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Avatar: The Way of Water (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/76600?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-spider-verse",
        "title": "The Amazing Spider-Man 2",
        "subtitle": "Hindi + English Dual Audio 720p BluRay",
        "content_type": "movie",
        "description": "Peter Parker faces his greatest challenge when Electro rises to menace New York. Features the authentic theatrical Hindi dubbing cast alongside the original English soundtrack muxed directly into the 720p BluRay stream with zero external overlays.",
        "release_year": 2014,
        "age_rating": "PG-13",
        "imdb_rating": 8.7,
        "tmdb_id": 102382,
        "imdb_id": "tt1872181",
        "quality": "720p BLURAY DUAL AUDIO",
        "is_dual_audio": True,
        "audio_tracks_count": 2,
        "duration_seconds": 8520,
        "duration_formatted": "2h 22m",
        "video_url": "https://archive.org/download/the-amazing-spider-man-2-2014-dual-audio-hindi-english-720p/The%20Amazing%20Spider-Man%202%20%282014%29%20Dual%20Audio%20%7BHindi-English%7D%20720p%20BluRay%201.2GB%20ESub%20%5BBollYFlix%5D.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/the-amazing-spider-man-2-2014-dual-audio-hindi-english-720p/The%20Amazing%20Spider-Man%202%20%282014%29%20Dual%20Audio%20%7BHindi-English%7D%20720p%20BluRay%201.2GB%20ESub%20%5BBollYFlix%5D.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/102382?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/102382"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/102382"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4120000,
        "likes": 381000,
        "channel": {
            "name": "Sony Pictures Animation",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "7.4M",
            "verified": True
        },
        "category": "Animation",
        "tags": [
            "spider-man",
            "miles-morales",
            "marvel",
            "animation",
            "4k",
            "hollywood"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/en.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/en.mp3?download=1",
                "file_name": "mov-spider-verse_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/hi.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/hi.mp3?download=1",
                "file_name": "mov-spider-verse_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/ta.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/ta.mp3?download=1",
                "file_name": "mov-spider-verse_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/te.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/te.mp3?download=1",
                "file_name": "mov-spider-verse_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/ml.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/ml.mp3?download=1",
                "file_name": "mov-spider-verse_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/kn.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/kn.mp3?download=1",
                "file_name": "mov-spider-verse_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/mr.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/mr.mp3?download=1",
                "file_name": "mov-spider-verse_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/es.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/es.mp3?download=1",
                "file_name": "mov-spider-verse_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/fr.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/fr.mp3?download=1",
                "file_name": "mov-spider-verse_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/de.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/de.mp3?download=1",
                "file_name": "mov-spider-verse_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/ja.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/ja.mp3?download=1",
                "file_name": "mov-spider-verse_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spider-verse/ko.mp3",
                "download_url": "/api/audio/dub/mov-spider-verse/ko.mp3?download=1",
                "file_name": "mov-spider-verse_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Amazing Spider-Man 2 (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p BluRay Dual Audio MP4 (857 MB)",
            "stream_url": "https://archive.org/download/the-amazing-spider-man-2-2014-dual-audio-hindi-english-720p/The%20Amazing%20Spider-Man%202%20%282014%29%20Dual%20Audio%20%7BHindi-English%7D%20720p%20BluRay%201.2GB%20ESub%20%5BBollYFlix%5D.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-parasite",
        "title": "Parasite",
        "subtitle": "Bong Joon-ho Masterpiece (기생충)",
        "content_type": "movie",
        "description": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident. Winner of the Palme d'Or and four Academy Awards including Best Picture.",
        "release_year": 2019,
        "age_rating": "R",
        "imdb_rating": 8.5,
        "tmdb_id": 496243,
        "imdb_id": "tt6751668",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7920,
        "duration_formatted": "2h 12m",
        "video_url": "https://vidlink.pro/movie/496243?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/496243?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/496243"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/496243"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 6890000,
        "likes": 640000,
        "channel": {
            "name": "CJ Entertainment",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "8.9M",
            "verified": True
        },
        "category": "Thriller",
        "tags": [
            "parasite",
            "korean",
            "k-movie",
            "bong-joon-ho",
            "oscar-winner",
            "4k",
            "world-cinema"
        ],
        "published_at": "2019",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/en.mp3",
                "download_url": "/api/audio/dub/mov-parasite/en.mp3?download=1",
                "file_name": "mov-parasite_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/hi.mp3",
                "download_url": "/api/audio/dub/mov-parasite/hi.mp3?download=1",
                "file_name": "mov-parasite_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/ta.mp3",
                "download_url": "/api/audio/dub/mov-parasite/ta.mp3?download=1",
                "file_name": "mov-parasite_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/te.mp3",
                "download_url": "/api/audio/dub/mov-parasite/te.mp3?download=1",
                "file_name": "mov-parasite_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/ml.mp3",
                "download_url": "/api/audio/dub/mov-parasite/ml.mp3?download=1",
                "file_name": "mov-parasite_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/kn.mp3",
                "download_url": "/api/audio/dub/mov-parasite/kn.mp3?download=1",
                "file_name": "mov-parasite_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/mr.mp3",
                "download_url": "/api/audio/dub/mov-parasite/mr.mp3?download=1",
                "file_name": "mov-parasite_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/es.mp3",
                "download_url": "/api/audio/dub/mov-parasite/es.mp3?download=1",
                "file_name": "mov-parasite_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/fr.mp3",
                "download_url": "/api/audio/dub/mov-parasite/fr.mp3?download=1",
                "file_name": "mov-parasite_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/de.mp3",
                "download_url": "/api/audio/dub/mov-parasite/de.mp3?download=1",
                "file_name": "mov-parasite_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/ja.mp3",
                "download_url": "/api/audio/dub/mov-parasite/ja.mp3?download=1",
                "file_name": "mov-parasite_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-parasite/ko.mp3",
                "download_url": "/api/audio/dub/mov-parasite/ko.mp3?download=1",
                "file_name": "mov-parasite_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Parasite (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/496243?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-exhuma",
        "title": "Exhuma",
        "subtitle": "Supernatural Mystery Thriller (파묘)",
        "content_type": "movie",
        "description": "After suffering from serial paranormal events, a wealthy family living in LA summons a young rising shaman duo to save the newborn of the family. The process of excavating an ominous grave in a remote Korean village unleashes an ancient buried terror.",
        "release_year": 2024,
        "age_rating": "NR",
        "imdb_rating": 7.1,
        "tmdb_id": 1011985,
        "imdb_id": "tt27850444",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8040,
        "duration_formatted": "2h 14m",
        "video_url": "https://vidlink.pro/movie/1011985?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1011985?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1011985"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1011985"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4350000,
        "likes": 378000,
        "channel": {
            "name": "Showbox Korea",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "4.2M",
            "verified": True
        },
        "category": "Horror",
        "tags": [
            "exhuma",
            "korean",
            "k-movie",
            "kim-go-eun",
            "choi-min-sik",
            "horror",
            "4k",
            "world-cinema"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/en.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/en.mp3?download=1",
                "file_name": "mov-exhuma_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/hi.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/hi.mp3?download=1",
                "file_name": "mov-exhuma_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/ta.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/ta.mp3?download=1",
                "file_name": "mov-exhuma_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/te.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/te.mp3?download=1",
                "file_name": "mov-exhuma_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/ml.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/ml.mp3?download=1",
                "file_name": "mov-exhuma_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/kn.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/kn.mp3?download=1",
                "file_name": "mov-exhuma_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/mr.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/mr.mp3?download=1",
                "file_name": "mov-exhuma_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/es.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/es.mp3?download=1",
                "file_name": "mov-exhuma_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/fr.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/fr.mp3?download=1",
                "file_name": "mov-exhuma_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/de.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/de.mp3?download=1",
                "file_name": "mov-exhuma_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/ja.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/ja.mp3?download=1",
                "file_name": "mov-exhuma_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-exhuma/ko.mp3",
                "download_url": "/api/audio/dub/mov-exhuma/ko.mp3?download=1",
                "file_name": "mov-exhuma_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Exhuma (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/1011985?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-train-to-busan",
        "title": "Train to Busan",
        "subtitle": "High-Speed Zombie Action (부산행)",
        "content_type": "movie",
        "description": "While a zombie virus breaks out in South Korea, passengers struggle to survive on the bullet train from Seoul to Busan, battling hordes of infected in claustrophobic train cars.",
        "release_year": 2016,
        "age_rating": "NR",
        "imdb_rating": 7.6,
        "tmdb_id": 396535,
        "imdb_id": "tt5700672",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7080,
        "duration_formatted": "1h 58m",
        "video_url": "https://vidlink.pro/movie/396535?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/396535?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/396535"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/396535"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5920000,
        "likes": 490000,
        "channel": {
            "name": "Next Entertainment World",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "3.8M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "train-to-busan",
            "gong-yoo",
            "zombie",
            "korean",
            "k-movie",
            "action",
            "world-cinema"
        ],
        "published_at": "2016",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/en.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/en.mp3?download=1",
                "file_name": "mov-train-to-busan_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/hi.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/hi.mp3?download=1",
                "file_name": "mov-train-to-busan_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/ta.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/ta.mp3?download=1",
                "file_name": "mov-train-to-busan_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/te.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/te.mp3?download=1",
                "file_name": "mov-train-to-busan_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/ml.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/ml.mp3?download=1",
                "file_name": "mov-train-to-busan_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/kn.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/kn.mp3?download=1",
                "file_name": "mov-train-to-busan_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/mr.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/mr.mp3?download=1",
                "file_name": "mov-train-to-busan_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/es.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/es.mp3?download=1",
                "file_name": "mov-train-to-busan_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/fr.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/fr.mp3?download=1",
                "file_name": "mov-train-to-busan_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/de.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/de.mp3?download=1",
                "file_name": "mov-train-to-busan_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/ja.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/ja.mp3?download=1",
                "file_name": "mov-train-to-busan_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-train-to-busan/ko.mp3",
                "download_url": "/api/audio/dub/mov-train-to-busan/ko.mp3?download=1",
                "file_name": "mov-train-to-busan_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Train to Busan (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/396535?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-godzilla-minus-one",
        "title": "Godzilla Minus One",
        "subtitle": "Oscar-Winning Kaiju Masterpiece (ゴジラ-1.0)",
        "content_type": "movie",
        "description": "Post-war Japan is at its lowest point when a new crisis emerges in the form of a giant monster, baptized in the horrific power of the atomic bomb. Desperate civilians and former soldiers must band together to defend their homeland.",
        "release_year": 2023,
        "age_rating": "PG-13",
        "imdb_rating": 7.9,
        "tmdb_id": 940721,
        "imdb_id": "tt23289160",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7440,
        "duration_formatted": "2h 04m",
        "video_url": "https://vidlink.pro/movie/940721?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/940721?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/940721"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/940721"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5340000,
        "likes": 478000,
        "channel": {
            "name": "TOHO Co., Ltd.",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "7.5M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "godzilla",
            "minus-one",
            "japanese",
            "japan",
            "kaiju",
            "oscar-winner",
            "4k",
            "world-cinema"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/en.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/en.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/hi.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/hi.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/ta.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/ta.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/te.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/te.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/ml.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/ml.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/kn.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/kn.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/mr.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/mr.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/es.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/es.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/fr.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/fr.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/de.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/de.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/ja.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/ja.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-minus-one/ko.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-minus-one/ko.mp3?download=1",
                "file_name": "mov-godzilla-minus-one_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Godzilla Minus One (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/940721?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-spirited-away",
        "title": "Spirited Away",
        "subtitle": "Hayao Miyazaki Masterpiece (千と千尋の神隠し)",
        "content_type": "movie",
        "description": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts. Academy Award Winner for Best Animated Feature.",
        "release_year": 2001,
        "age_rating": "PG",
        "imdb_rating": 8.6,
        "tmdb_id": 129,
        "imdb_id": "tt0245429",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7500,
        "duration_formatted": "2h 05m",
        "video_url": "https://archive.org/download/spirited-away-2001-dual-audio-hindi-japanese-1080-p-hevc/Spirited%20Away%202001%20Dual%20Audio%20Hindi%20Japanese%201080P%20Hevc.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + Japanese)",
                "type": "native",
                "url": "https://archive.org/download/spirited-away-2001-dual-audio-hindi-japanese-1080-p-hevc/Spirited%20Away%202001%20Dual%20Audio%20Hindi%20Japanese%201080P%20Hevc.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/129?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/129"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/129"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 8120000,
        "likes": 792000,
        "channel": {
            "name": "Studio Ghibli",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "12.8M",
            "verified": True
        },
        "category": "Animation",
        "tags": [
            "spirited-away",
            "ghibli",
            "miyazaki",
            "anime",
            "japanese",
            "fantasy",
            "oscar-winner",
            "world-cinema"
        ],
        "published_at": "2001",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/en.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/en.mp3?download=1",
                "file_name": "mov-spirited-away_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/hi.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/hi.mp3?download=1",
                "file_name": "mov-spirited-away_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/ta.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/ta.mp3?download=1",
                "file_name": "mov-spirited-away_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/te.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/te.mp3?download=1",
                "file_name": "mov-spirited-away_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/ml.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/ml.mp3?download=1",
                "file_name": "mov-spirited-away_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/kn.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/kn.mp3?download=1",
                "file_name": "mov-spirited-away_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/mr.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/mr.mp3?download=1",
                "file_name": "mov-spirited-away_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/es.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/es.mp3?download=1",
                "file_name": "mov-spirited-away_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/fr.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/fr.mp3?download=1",
                "file_name": "mov-spirited-away_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/de.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/de.mp3?download=1",
                "file_name": "mov-spirited-away_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/ja.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/ja.mp3?download=1",
                "file_name": "mov-spirited-away_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-spirited-away/ko.mp3",
                "download_url": "/api/audio/dub/mov-spirited-away/ko.mp3?download=1",
                "file_name": "mov-spirited-away_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Spirited Away (Hindi + Japanese)",
            "languages": "Hindi + Japanese",
            "quality_spec": "1080p HEVC Dual Audio MP4 (2060 MB)",
            "stream_url": "https://archive.org/download/spirited-away-2001-dual-audio-hindi-japanese-1080-p-hevc/Spirited%20Away%202001%20Dual%20Audio%20Hindi%20Japanese%201080P%20Hevc.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-your-name",
        "title": "Your Name.",
        "subtitle": "Makoto Shinkai Romance (君の名は。)",
        "content_type": "movie",
        "description": "Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart? A mesmerizing Japanese animated phenomenon that captured hearts worldwide.",
        "release_year": 2016,
        "age_rating": "PG",
        "imdb_rating": 8.4,
        "tmdb_id": 372058,
        "imdb_id": "tt5311514",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 6360,
        "duration_formatted": "1h 46m",
        "video_url": "https://archive.org/download/your-name-hindi-dubbed/Your%20Name%20Hindi%20Dubbed.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi Dubbed)",
                "type": "native",
                "url": "https://archive.org/download/your-name-hindi-dubbed/Your%20Name%20Hindi%20Dubbed.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/372058?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/372058"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/372058"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 7320000,
        "likes": 694000,
        "channel": {
            "name": "CoMix Wave Films",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "6.2M",
            "verified": True
        },
        "category": "Animation",
        "tags": [
            "your-name",
            "makoto-shinkai",
            "anime",
            "japanese",
            "romance",
            "4k",
            "world-cinema"
        ],
        "published_at": "2016",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/en.mp3",
                "download_url": "/api/audio/dub/mov-your-name/en.mp3?download=1",
                "file_name": "mov-your-name_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/hi.mp3",
                "download_url": "/api/audio/dub/mov-your-name/hi.mp3?download=1",
                "file_name": "mov-your-name_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/ta.mp3",
                "download_url": "/api/audio/dub/mov-your-name/ta.mp3?download=1",
                "file_name": "mov-your-name_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/te.mp3",
                "download_url": "/api/audio/dub/mov-your-name/te.mp3?download=1",
                "file_name": "mov-your-name_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/ml.mp3",
                "download_url": "/api/audio/dub/mov-your-name/ml.mp3?download=1",
                "file_name": "mov-your-name_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/kn.mp3",
                "download_url": "/api/audio/dub/mov-your-name/kn.mp3?download=1",
                "file_name": "mov-your-name_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/mr.mp3",
                "download_url": "/api/audio/dub/mov-your-name/mr.mp3?download=1",
                "file_name": "mov-your-name_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/es.mp3",
                "download_url": "/api/audio/dub/mov-your-name/es.mp3?download=1",
                "file_name": "mov-your-name_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/fr.mp3",
                "download_url": "/api/audio/dub/mov-your-name/fr.mp3?download=1",
                "file_name": "mov-your-name_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/de.mp3",
                "download_url": "/api/audio/dub/mov-your-name/de.mp3?download=1",
                "file_name": "mov-your-name_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/ja.mp3",
                "download_url": "/api/audio/dub/mov-your-name/ja.mp3?download=1",
                "file_name": "mov-your-name_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-your-name/ko.mp3",
                "download_url": "/api/audio/dub/mov-your-name/ko.mp3?download=1",
                "file_name": "mov-your-name_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Your Name. (Hindi Dubbed)",
            "languages": "Hindi Dubbed",
            "quality_spec": "1080p HD Hindi Dubbed MP4 (1840 MB)",
            "stream_url": "https://archive.org/download/your-name-hindi-dubbed/Your%20Name%20Hindi%20Dubbed.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-the-boy-and-the-heron",
        "title": "The Boy and the Heron",
        "subtitle": "Hayao Miyazaki 2024 Oscar Winner (君たちはどう生きるか)",
        "content_type": "movie",
        "description": "Through encounters with his friends and uncle, a young boy follows his spiritual growth in an enchanting world shared by the living and the dead. Winner of the 2024 Academy Award for Best Animated Feature.",
        "release_year": 2023,
        "age_rating": "PG-13",
        "imdb_rating": 7.5,
        "tmdb_id": 508883,
        "imdb_id": "tt6587046",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7440,
        "duration_formatted": "2h 04m",
        "video_url": "https://vidlink.pro/movie/508883?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/508883?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/508883"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/508883"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4890000,
        "likes": 425000,
        "channel": {
            "name": "Studio Ghibli",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "12.8M",
            "verified": True
        },
        "category": "Animation",
        "tags": [
            "boy-and-heron",
            "ghibli",
            "miyazaki",
            "anime",
            "oscar-winner",
            "4k",
            "world-cinema"
        ],
        "published_at": "2023",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/en.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/en.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/hi.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/ta.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/te.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/te.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/ml.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/kn.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/mr.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/es.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/es.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/fr.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/de.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/de.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/ja.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-boy-and-the-heron/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-boy-and-the-heron/ko.mp3?download=1",
                "file_name": "mov-the-boy-and-the-heron_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Boy and the Heron (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/508883?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-rrr",
        "title": "RRR",
        "subtitle": "Epic Indian Revolution Spectacle (Rise Roar Revolt)",
        "content_type": "movie",
        "description": "A fearless revolutionary and an officer in the British force, who once shared an unbreakable bond, decide to join hands and wage war against the British Raj. Global blockbuster that won the Academy Award and Golden Globe for Best Original Song.",
        "release_year": 2022,
        "age_rating": "PG-13",
        "imdb_rating": 7.8,
        "tmdb_id": 579974,
        "imdb_id": "tt8178634",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10920,
        "duration_formatted": "3h 02m",
        "video_url": "https://vidlink.pro/movie/579974?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/579974?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/579974"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/579974"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 8450000,
        "likes": 810000,
        "channel": {
            "name": "DVV Entertainment",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "9.4M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "rrr",
            "ss-rajamouli",
            "ntr-jr",
            "ram-charan",
            "tollywood",
            "indian",
            "oscar-winner",
            "4k",
            "world-cinema"
        ],
        "published_at": "2022",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/en.mp3",
                "download_url": "/api/audio/dub/mov-rrr/en.mp3?download=1",
                "file_name": "mov-rrr_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/hi.mp3",
                "download_url": "/api/audio/dub/mov-rrr/hi.mp3?download=1",
                "file_name": "mov-rrr_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/ta.mp3",
                "download_url": "/api/audio/dub/mov-rrr/ta.mp3?download=1",
                "file_name": "mov-rrr_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/te.mp3",
                "download_url": "/api/audio/dub/mov-rrr/te.mp3?download=1",
                "file_name": "mov-rrr_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/ml.mp3",
                "download_url": "/api/audio/dub/mov-rrr/ml.mp3?download=1",
                "file_name": "mov-rrr_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/kn.mp3",
                "download_url": "/api/audio/dub/mov-rrr/kn.mp3?download=1",
                "file_name": "mov-rrr_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/mr.mp3",
                "download_url": "/api/audio/dub/mov-rrr/mr.mp3?download=1",
                "file_name": "mov-rrr_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/es.mp3",
                "download_url": "/api/audio/dub/mov-rrr/es.mp3?download=1",
                "file_name": "mov-rrr_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/fr.mp3",
                "download_url": "/api/audio/dub/mov-rrr/fr.mp3?download=1",
                "file_name": "mov-rrr_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/de.mp3",
                "download_url": "/api/audio/dub/mov-rrr/de.mp3?download=1",
                "file_name": "mov-rrr_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/ja.mp3",
                "download_url": "/api/audio/dub/mov-rrr/ja.mp3?download=1",
                "file_name": "mov-rrr_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-rrr/ko.mp3",
                "download_url": "/api/audio/dub/mov-rrr/ko.mp3?download=1",
                "file_name": "mov-rrr_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "RRR (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/579974?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-kalki-2898-ad",
        "title": "Kalki 2898 AD",
        "subtitle": "Futuristic Indian Sci-Fi Mythology",
        "content_type": "movie",
        "description": "Set in a post-apocalyptic world in the year 2898 AD, a modern avatar of the Hindu god Vishnu is believed to have descended to Earth to protect the world from evil forces. Starring Prabhas, Amitabh Bachchan, and Deepika Padukone.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 7.5,
        "tmdb_id": 801688,
        "imdb_id": "tt12735488",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10860,
        "duration_formatted": "3h 01m",
        "video_url": "https://vidlink.pro/movie/801688?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/801688?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/801688"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/801688"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 6120000,
        "likes": 560000,
        "channel": {
            "name": "Vyjayanthi Movies",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "6.8M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "kalki-2898-ad",
            "prabhas",
            "amitabh-bachchan",
            "deepika-padukone",
            "sci-fi",
            "indian",
            "4k",
            "world-cinema"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/en.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/en.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/hi.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/hi.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/ta.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/ta.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/te.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/te.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/ml.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/ml.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/kn.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/kn.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/mr.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/mr.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/es.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/es.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/fr.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/fr.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/de.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/de.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/ja.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/ja.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-kalki-2898-ad/ko.mp3",
                "download_url": "/api/audio/dub/mov-kalki-2898-ad/ko.mp3?download=1",
                "file_name": "mov-kalki-2898-ad_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Kalki 2898 AD (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/801688?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-jawan",
        "title": "Jawan",
        "subtitle": "Shah Rukh Khan Action Mega-Hit",
        "content_type": "movie",
        "description": "A high-octane action thriller which outlines the emotional journey of a man who is set to rectify the wrongs in the society, backed by a band of formidable women. Highest-grossing Hindi movie of 2023.",
        "release_year": 2023,
        "age_rating": "PG-13",
        "imdb_rating": 7.0,
        "tmdb_id": 872906,
        "imdb_id": "tt15354916",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10140,
        "duration_formatted": "2h 49m",
        "video_url": "https://vidlink.pro/movie/872906?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/872906?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/872906"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/872906"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5940000,
        "likes": 530000,
        "channel": {
            "name": "Red Chillies Entertainment",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "14.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "jawan",
            "shah-rukh-khan",
            "srk",
            "atlee",
            "bollywood",
            "indian",
            "action",
            "4k",
            "world-cinema"
        ],
        "published_at": "2023",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/en.mp3",
                "download_url": "/api/audio/dub/mov-jawan/en.mp3?download=1",
                "file_name": "mov-jawan_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/hi.mp3",
                "download_url": "/api/audio/dub/mov-jawan/hi.mp3?download=1",
                "file_name": "mov-jawan_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/ta.mp3",
                "download_url": "/api/audio/dub/mov-jawan/ta.mp3?download=1",
                "file_name": "mov-jawan_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/te.mp3",
                "download_url": "/api/audio/dub/mov-jawan/te.mp3?download=1",
                "file_name": "mov-jawan_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/ml.mp3",
                "download_url": "/api/audio/dub/mov-jawan/ml.mp3?download=1",
                "file_name": "mov-jawan_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/kn.mp3",
                "download_url": "/api/audio/dub/mov-jawan/kn.mp3?download=1",
                "file_name": "mov-jawan_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/mr.mp3",
                "download_url": "/api/audio/dub/mov-jawan/mr.mp3?download=1",
                "file_name": "mov-jawan_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/es.mp3",
                "download_url": "/api/audio/dub/mov-jawan/es.mp3?download=1",
                "file_name": "mov-jawan_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/fr.mp3",
                "download_url": "/api/audio/dub/mov-jawan/fr.mp3?download=1",
                "file_name": "mov-jawan_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/de.mp3",
                "download_url": "/api/audio/dub/mov-jawan/de.mp3?download=1",
                "file_name": "mov-jawan_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/ja.mp3",
                "download_url": "/api/audio/dub/mov-jawan/ja.mp3?download=1",
                "file_name": "mov-jawan_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-jawan/ko.mp3",
                "download_url": "/api/audio/dub/mov-jawan/ko.mp3?download=1",
                "file_name": "mov-jawan_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Jawan (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/872906?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-stree-2",
        "title": "Stree 2: Sarkate Ka Aatank",
        "subtitle": "2024 Indian Horror-Comedy Phenomenon",
        "content_type": "movie",
        "description": "After the events of Stree, the town of Chanderi is being haunted again. This time, women are mysteriously abducted by a headless entity known as 'Sarkata'. Vicky and his friends must team up with their mysterious protector to save the town.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 7.3,
        "tmdb_id": 1151534,
        "imdb_id": "tt28362624",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8940,
        "duration_formatted": "2h 29m",
        "video_url": "https://vidlink.pro/movie/1151534?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1151534?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1151534"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1151534"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 6780000,
        "likes": 612000,
        "channel": {
            "name": "Maddock Films",
            "avatar": "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=100",
            "subscribers": "5.9M",
            "verified": True
        },
        "category": "Comedy",
        "tags": [
            "stree-2",
            "shraddha-kapoor",
            "rajkummar-rao",
            "horror-comedy",
            "bollywood",
            "indian",
            "4k",
            "world-cinema"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/en.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/en.mp3?download=1",
                "file_name": "mov-stree-2_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/hi.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/hi.mp3?download=1",
                "file_name": "mov-stree-2_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/ta.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/ta.mp3?download=1",
                "file_name": "mov-stree-2_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/te.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/te.mp3?download=1",
                "file_name": "mov-stree-2_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/ml.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/ml.mp3?download=1",
                "file_name": "mov-stree-2_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/kn.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/kn.mp3?download=1",
                "file_name": "mov-stree-2_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/mr.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/mr.mp3?download=1",
                "file_name": "mov-stree-2_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/es.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/es.mp3?download=1",
                "file_name": "mov-stree-2_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/fr.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/fr.mp3?download=1",
                "file_name": "mov-stree-2_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/de.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/de.mp3?download=1",
                "file_name": "mov-stree-2_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/ja.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/ja.mp3?download=1",
                "file_name": "mov-stree-2_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-stree-2/ko.mp3",
                "download_url": "/api/audio/dub/mov-stree-2/ko.mp3?download=1",
                "file_name": "mov-stree-2_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Stree 2: Sarkate Ka Aatank (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/1151534?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-dangal",
        "title": "Dangal",
        "subtitle": "Inspiring True Story Sports Phenomenon",
        "content_type": "movie",
        "description": "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression. Highest-grossing Indian film of all time globally.",
        "release_year": 2016,
        "age_rating": "PG",
        "imdb_rating": 8.3,
        "tmdb_id": 360814,
        "imdb_id": "tt5074352",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 9660,
        "duration_formatted": "2h 41m",
        "video_url": "https://vidlink.pro/movie/360814?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/360814?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/360814"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/360814"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 9420000,
        "likes": 880000,
        "channel": {
            "name": "Aamir Khan Productions",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "8.1M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "dangal",
            "aamir-khan",
            "wrestling",
            "bollywood",
            "indian",
            "world-cinema",
            "4k"
        ],
        "published_at": "2016",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/en.mp3",
                "download_url": "/api/audio/dub/mov-dangal/en.mp3?download=1",
                "file_name": "mov-dangal_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/hi.mp3",
                "download_url": "/api/audio/dub/mov-dangal/hi.mp3?download=1",
                "file_name": "mov-dangal_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/ta.mp3",
                "download_url": "/api/audio/dub/mov-dangal/ta.mp3?download=1",
                "file_name": "mov-dangal_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/te.mp3",
                "download_url": "/api/audio/dub/mov-dangal/te.mp3?download=1",
                "file_name": "mov-dangal_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/ml.mp3",
                "download_url": "/api/audio/dub/mov-dangal/ml.mp3?download=1",
                "file_name": "mov-dangal_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/kn.mp3",
                "download_url": "/api/audio/dub/mov-dangal/kn.mp3?download=1",
                "file_name": "mov-dangal_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/mr.mp3",
                "download_url": "/api/audio/dub/mov-dangal/mr.mp3?download=1",
                "file_name": "mov-dangal_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/es.mp3",
                "download_url": "/api/audio/dub/mov-dangal/es.mp3?download=1",
                "file_name": "mov-dangal_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/fr.mp3",
                "download_url": "/api/audio/dub/mov-dangal/fr.mp3?download=1",
                "file_name": "mov-dangal_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/de.mp3",
                "download_url": "/api/audio/dub/mov-dangal/de.mp3?download=1",
                "file_name": "mov-dangal_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/ja.mp3",
                "download_url": "/api/audio/dub/mov-dangal/ja.mp3?download=1",
                "file_name": "mov-dangal_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-dangal/ko.mp3",
                "download_url": "/api/audio/dub/mov-dangal/ko.mp3?download=1",
                "file_name": "mov-dangal_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Dangal (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/360814?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-anatomy-of-a-fall",
        "title": "Anatomy of a Fall",
        "subtitle": "Palme d'Or & Oscar Winning Thriller (Anatomie d'une chute)",
        "content_type": "movie",
        "description": "A woman is suspected of her husband's murder, and their blind son faces a moral dilemma as the main witness. A tour-de-force courtroom thriller and psychological drama from director Justine Triet.",
        "release_year": 2023,
        "age_rating": "R",
        "imdb_rating": 7.7,
        "tmdb_id": 915935,
        "imdb_id": "tt17009710",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 9060,
        "duration_formatted": "2h 31m",
        "video_url": "https://vidlink.pro/movie/915935?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/915935?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/915935"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/915935"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4120000,
        "likes": 365000,
        "channel": {
            "name": "Le Pacte / Neon",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "3.2M",
            "verified": True
        },
        "category": "Thriller",
        "tags": [
            "anatomy-of-a-fall",
            "french",
            "france",
            "palme-dor",
            "oscar-winner",
            "courtroom",
            "4k",
            "world-cinema"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/en.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/en.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/hi.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/hi.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/ta.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/ta.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/te.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/te.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/ml.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/ml.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/kn.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/kn.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/mr.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/mr.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/es.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/es.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/fr.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/fr.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/de.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/de.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/ja.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/ja.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-anatomy-of-a-fall/ko.mp3",
                "download_url": "/api/audio/dub/mov-anatomy-of-a-fall/ko.mp3?download=1",
                "file_name": "mov-anatomy-of-a-fall_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Anatomy of a Fall (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/915935?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-count-of-monte-cristo",
        "title": "The Count of Monte-Cristo",
        "subtitle": "2024 French Epic Adventure (Le Comte de Monte-Cristo)",
        "content_type": "movie",
        "description": "Edmond Dantes becomes the target of a sinister plot and is arrested on his wedding day for a crime he did not commit. After 14 years in the island prison of Chateau d'If, he stages a daring escape and returns as the Count of Monte-Cristo to seek vengeance.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 7.9,
        "tmdb_id": 1005331,
        "imdb_id": "tt26450654",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 10680,
        "duration_formatted": "2h 58m",
        "video_url": "https://vidlink.pro/movie/1005331?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1005331?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1005331"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1005331"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 3890000,
        "likes": 340000,
        "channel": {
            "name": "Pathe / Chapter 2",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "4.1M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "monte-cristo",
            "french",
            "france",
            "pierre-niney",
            "adventure",
            "4k",
            "world-cinema"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/en.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/en.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/hi.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/hi.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/ta.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/ta.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/te.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/te.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/ml.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/ml.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/kn.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/kn.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/mr.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/mr.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/es.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/es.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/fr.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/fr.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/de.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/de.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/ja.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/ja.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-count-of-monte-cristo/ko.mp3",
                "download_url": "/api/audio/dub/mov-count-of-monte-cristo/ko.mp3?download=1",
                "file_name": "mov-count-of-monte-cristo_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Count of Monte-Cristo (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/1005331?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-society-of-the-snow",
        "title": "Society of the Snow",
        "subtitle": "Andes Survival Miracle (La sociedad de la nieve)",
        "content_type": "movie",
        "description": "In 1972, a Uruguayan rugby team's flight crashes onto a glacier in the heart of the Andes. The few passengers who survive the crash find themselves in one of the world's toughest environments to survive.",
        "release_year": 2023,
        "age_rating": "R",
        "imdb_rating": 7.8,
        "tmdb_id": 906126,
        "imdb_id": "tt16277224",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8640,
        "duration_formatted": "2h 24m",
        "video_url": "https://vidlink.pro/movie/906126?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/906126?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/906126"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/906126"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4780000,
        "likes": 420000,
        "channel": {
            "name": "Netflix / J.A. Bayona",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "15.0M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "society-of-the-snow",
            "spanish",
            "spain",
            "andes",
            "survival",
            "oscar-nominated",
            "4k",
            "world-cinema"
        ],
        "published_at": "2023",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/en.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/en.mp3?download=1",
                "file_name": "mov-society-of-the-snow_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/hi.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/hi.mp3?download=1",
                "file_name": "mov-society-of-the-snow_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/ta.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/ta.mp3?download=1",
                "file_name": "mov-society-of-the-snow_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/te.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/te.mp3?download=1",
                "file_name": "mov-society-of-the-snow_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/ml.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/ml.mp3?download=1",
                "file_name": "mov-society-of-the-snow_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/kn.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/kn.mp3?download=1",
                "file_name": "mov-society-of-the-snow_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/mr.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/mr.mp3?download=1",
                "file_name": "mov-society-of-the-snow_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/es.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/es.mp3?download=1",
                "file_name": "mov-society-of-the-snow_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/fr.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/fr.mp3?download=1",
                "file_name": "mov-society-of-the-snow_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/de.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/de.mp3?download=1",
                "file_name": "mov-society-of-the-snow_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/ja.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/ja.mp3?download=1",
                "file_name": "mov-society-of-the-snow_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-society-of-the-snow/ko.mp3",
                "download_url": "/api/audio/dub/mov-society-of-the-snow/ko.mp3?download=1",
                "file_name": "mov-society-of-the-snow_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Society of the Snow (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/906126?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-poor-things",
        "title": "Poor Things",
        "subtitle": "Yorgos Lanthimos 4x Oscar-Winning Masterpiece",
        "content_type": "movie",
        "description": "The incredible tale and fantastical evolution of Bella Baxter, a young woman brought back to life by the brilliant and unorthodox scientist Dr. Godwin Baxter. Winner of four Academy Awards including Best Actress for Emma Stone.",
        "release_year": 2023,
        "age_rating": "R",
        "imdb_rating": 7.9,
        "tmdb_id": 792307,
        "imdb_id": "tt14230458",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 8460,
        "duration_formatted": "2h 21m",
        "video_url": "https://vidlink.pro/movie/792307?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/792307?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/792307"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/792307"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 4350000,
        "likes": 390000,
        "channel": {
            "name": "Searchlight Pictures",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "4.8M",
            "verified": True
        },
        "category": "Comedy",
        "tags": [
            "poor-things",
            "emma-stone",
            "mark-ruffalo",
            "oscar-winner",
            "4k",
            "world-cinema"
        ],
        "published_at": "2023",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/en.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/en.mp3?download=1",
                "file_name": "mov-poor-things_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/hi.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/hi.mp3?download=1",
                "file_name": "mov-poor-things_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/ta.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/ta.mp3?download=1",
                "file_name": "mov-poor-things_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/te.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/te.mp3?download=1",
                "file_name": "mov-poor-things_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/ml.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/ml.mp3?download=1",
                "file_name": "mov-poor-things_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/kn.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/kn.mp3?download=1",
                "file_name": "mov-poor-things_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/mr.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/mr.mp3?download=1",
                "file_name": "mov-poor-things_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/es.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/es.mp3?download=1",
                "file_name": "mov-poor-things_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/fr.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/fr.mp3?download=1",
                "file_name": "mov-poor-things_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/de.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/de.mp3?download=1",
                "file_name": "mov-poor-things_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/ja.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/ja.mp3?download=1",
                "file_name": "mov-poor-things_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-poor-things/ko.mp3",
                "download_url": "/api/audio/dub/mov-poor-things/ko.mp3?download=1",
                "file_name": "mov-poor-things_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Poor Things (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/792307?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-city-of-god",
        "title": "City of God",
        "subtitle": "Brazilian Cinema Legend (Cidade de Deus)",
        "content_type": "movie",
        "description": "In the slums of Rio, two kids' paths diverge as one struggles to become a photographer and the other a kingpin. Widely recognized as one of the greatest international films in cinema history.",
        "release_year": 2002,
        "age_rating": "R",
        "imdb_rating": 8.6,
        "tmdb_id": 598,
        "imdb_id": "tt0317248",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7800,
        "duration_formatted": "2h 10m",
        "video_url": "https://vidlink.pro/movie/598?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/598?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/598"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/598"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 6120000,
        "likes": 580000,
        "channel": {
            "name": "O2 Filmes / Miramax",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "3.5M",
            "verified": True
        },
        "category": "Crime",
        "tags": [
            "city-of-god",
            "brazil",
            "brazilian",
            "rio",
            "cidade-de-deus",
            "oscar-nominated",
            "4k",
            "world-cinema"
        ],
        "published_at": "2002",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/en.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/en.mp3?download=1",
                "file_name": "mov-city-of-god_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/hi.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/hi.mp3?download=1",
                "file_name": "mov-city-of-god_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/ta.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/ta.mp3?download=1",
                "file_name": "mov-city-of-god_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/te.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/te.mp3?download=1",
                "file_name": "mov-city-of-god_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/ml.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/ml.mp3?download=1",
                "file_name": "mov-city-of-god_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/kn.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/kn.mp3?download=1",
                "file_name": "mov-city-of-god_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/mr.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/mr.mp3?download=1",
                "file_name": "mov-city-of-god_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/es.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/es.mp3?download=1",
                "file_name": "mov-city-of-god_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/fr.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/fr.mp3?download=1",
                "file_name": "mov-city-of-god_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/de.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/de.mp3?download=1",
                "file_name": "mov-city-of-god_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/ja.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/ja.mp3?download=1",
                "file_name": "mov-city-of-god_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-city-of-god/ko.mp3",
                "download_url": "/api/audio/dub/mov-city-of-god/ko.mp3?download=1",
                "file_name": "mov-city-of-god_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "City of God (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/598?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-pans-labyrinth",
        "title": "Pan's Labyrinth",
        "subtitle": "Guillermo del Toro Dark Fantasy (El laberinto del fauno)",
        "content_type": "movie",
        "description": "In the Falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world. Winner of three Academy Awards.",
        "release_year": 2006,
        "age_rating": "R",
        "imdb_rating": 8.2,
        "tmdb_id": 1417,
        "imdb_id": "tt0457430",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7080,
        "duration_formatted": "1h 58m",
        "video_url": "https://vidlink.pro/movie/1417?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1417?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1417"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1417"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 5340000,
        "likes": 490000,
        "channel": {
            "name": "Picturehouse / Tequila Gang",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "4.2M",
            "verified": True
        },
        "category": "Fantasy",
        "tags": [
            "pans-labyrinth",
            "guillermo-del-toro",
            "mexican",
            "spanish",
            "dark-fantasy",
            "oscar-winner",
            "4k",
            "world-cinema"
        ],
        "published_at": "2006",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/en.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/en.mp3?download=1",
                "file_name": "mov-pans-labyrinth_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/hi.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/hi.mp3?download=1",
                "file_name": "mov-pans-labyrinth_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/ta.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/ta.mp3?download=1",
                "file_name": "mov-pans-labyrinth_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/te.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/te.mp3?download=1",
                "file_name": "mov-pans-labyrinth_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/ml.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/ml.mp3?download=1",
                "file_name": "mov-pans-labyrinth_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/kn.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/kn.mp3?download=1",
                "file_name": "mov-pans-labyrinth_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/mr.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/mr.mp3?download=1",
                "file_name": "mov-pans-labyrinth_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/es.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/es.mp3?download=1",
                "file_name": "mov-pans-labyrinth_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/fr.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/fr.mp3?download=1",
                "file_name": "mov-pans-labyrinth_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/de.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/de.mp3?download=1",
                "file_name": "mov-pans-labyrinth_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/ja.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/ja.mp3?download=1",
                "file_name": "mov-pans-labyrinth_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-pans-labyrinth/ko.mp3",
                "download_url": "/api/audio/dub/mov-pans-labyrinth/ko.mp3?download=1",
                "file_name": "mov-pans-labyrinth_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Pan's Labyrinth (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/1417?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-capernaum",
        "title": "Capernaum",
        "subtitle": "Nadine Labaki Cannes Jury Prize Winner (کفرناحوم)",
        "content_type": "movie",
        "description": "While serving a five-year sentence for a violent crime, a 12-year-old boy in Beirut sues his parents for neglect and for giving him life in a world where he cannot be cared for. Nominated for the Academy Award for Best Foreign Film.",
        "release_year": 2018,
        "age_rating": "R",
        "imdb_rating": 8.4,
        "tmdb_id": 517814,
        "imdb_id": "tt8267604",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 7560,
        "duration_formatted": "2h 06m",
        "video_url": "https://vidlink.pro/movie/517814?primaryColor=06b6d4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/517814?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/517814"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/517814"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cinema Stream (Direct CDN)",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "views": 3890000,
        "likes": 350000,
        "channel": {
            "name": "Sony Pictures Classics",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "3.1M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "capernaum",
            "lebanese",
            "lebanon",
            "arabic",
            "cannes-winner",
            "drama",
            "4k",
            "world-cinema"
        ],
        "published_at": "2018",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": True,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/en.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/en.mp3?download=1",
                "file_name": "mov-capernaum_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/hi.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/hi.mp3?download=1",
                "file_name": "mov-capernaum_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/ta.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/ta.mp3?download=1",
                "file_name": "mov-capernaum_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/te.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/te.mp3?download=1",
                "file_name": "mov-capernaum_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/ml.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/ml.mp3?download=1",
                "file_name": "mov-capernaum_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/kn.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/kn.mp3?download=1",
                "file_name": "mov-capernaum_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/mr.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/mr.mp3?download=1",
                "file_name": "mov-capernaum_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/es.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/es.mp3?download=1",
                "file_name": "mov-capernaum_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/fr.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/fr.mp3?download=1",
                "file_name": "mov-capernaum_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/de.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/de.mp3?download=1",
                "file_name": "mov-capernaum_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/ja.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/ja.mp3?download=1",
                "file_name": "mov-capernaum_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-capernaum/ko.mp3",
                "download_url": "/api/audio/dub/mov-capernaum/ko.mp3?download=1",
                "file_name": "mov-capernaum_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Capernaum (Cloud 4K Multi-Audio)",
            "languages": "Original Cinema Audio",
            "quality_spec": "4K Ultra HD Cinema Stream",
            "stream_url": "https://vidlink.pro/movie/517814?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ser-stranger-things",
        "title": "Stranger Things",
        "subtitle": "Netflix Global Sci-Fi Phenomenon",
        "content_type": "series",
        "description": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl with telekinetic powers.",
        "release_year": 2024,
        "age_rating": "TV-14",
        "imdb_rating": 8.7,
        "tmdb_id": 66732,
        "imdb_id": "tt4574334",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 3600,
        "duration_formatted": "4 Seasons",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/66732/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt4574334&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/66732/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 4,
                "season_title": "Season 4",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "Chapter One: The Hellfire Club",
                        "duration": "1h 16m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Chapter Two: Vecna's Curse",
                        "duration": "1h 17m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"
                    }
                ]
            }
        ],
        "views": 9840000,
        "likes": 920000,
        "channel": {
            "name": "Netflix Originals",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "26.4M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "stranger-things",
            "eleven",
            "upside-down",
            "sci-fi",
            "netflix",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/en.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/en.mp3?download=1",
                "file_name": "ser-stranger-things_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/hi.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/hi.mp3?download=1",
                "file_name": "ser-stranger-things_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/ta.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/ta.mp3?download=1",
                "file_name": "ser-stranger-things_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/te.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/te.mp3?download=1",
                "file_name": "ser-stranger-things_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/ml.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/ml.mp3?download=1",
                "file_name": "ser-stranger-things_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/kn.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/kn.mp3?download=1",
                "file_name": "ser-stranger-things_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/mr.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/mr.mp3?download=1",
                "file_name": "ser-stranger-things_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/es.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/es.mp3?download=1",
                "file_name": "ser-stranger-things_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/fr.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/fr.mp3?download=1",
                "file_name": "ser-stranger-things_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/de.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/de.mp3?download=1",
                "file_name": "ser-stranger-things_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/ja.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/ja.mp3?download=1",
                "file_name": "ser-stranger-things_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-stranger-things/ko.mp3",
                "download_url": "/api/audio/dub/ser-stranger-things/ko.mp3?download=1",
                "file_name": "ser-stranger-things_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Stranger Things (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/66732/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ser-house-of-the-dragon",
        "title": "House of the Dragon",
        "subtitle": "HBO Targaryen Civil War Epic",
        "content_type": "series",
        "description": "An internal succession war within House Targaryen at the height of its power, 172 years before the birth of Daenerys Targaryen. Dragons clash across Westeros.",
        "release_year": 2024,
        "age_rating": "TV-MA",
        "imdb_rating": 8.5,
        "tmdb_id": 94997,
        "imdb_id": "tt11198330",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 3600,
        "duration_formatted": "2 Seasons",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/94997/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt11198330&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/94997/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 2,
                "season_title": "Season 2",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "A Son for a Son",
                        "duration": "59m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Rhaenyra the Cruel",
                        "duration": "1h 09m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"
                    }
                ]
            }
        ],
        "views": 8120000,
        "likes": 745000,
        "channel": {
            "name": "HBO / Max",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "18.3M",
            "verified": True
        },
        "category": "Fantasy",
        "tags": [
            "house-of-the-dragon",
            "targaryen",
            "dragons",
            "game-of-thrones",
            "hbo",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/en.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/en.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/hi.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/hi.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/ta.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/ta.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/te.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/te.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/ml.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/ml.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/kn.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/kn.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/mr.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/mr.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/es.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/es.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/fr.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/fr.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/de.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/de.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/ja.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/ja.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-house-of-the-dragon/ko.mp3",
                "download_url": "/api/audio/dub/ser-house-of-the-dragon/ko.mp3?download=1",
                "file_name": "ser-house-of-the-dragon_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "House of the Dragon (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/94997/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ser-shogun",
        "title": "Shōgun",
        "subtitle": "2024 Record-Breaking Historical Drama",
        "content_type": "series",
        "description": "When a mysterious European ship is found marooned in a nearby fishing village in Japan, Lord Yoshii Toranaga discovers secrets that could tip the scales of power against formidable enemies. Winner of a record 18 Emmy Awards.",
        "release_year": 2024,
        "age_rating": "TV-MA",
        "imdb_rating": 8.7,
        "tmdb_id": 126308,
        "imdb_id": "tt2788316",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 3600,
        "duration_formatted": "10 Episodes",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/126308/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt2788316&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/126308/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "Chapter One: Anjin",
                        "duration": "1h 10m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Chapter Two: Servants of Two Masters",
                        "duration": "58m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"
                    }
                ]
            }
        ],
        "views": 7650000,
        "likes": 680000,
        "channel": {
            "name": "FX Networks / Hulu",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "8.9M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "shogun",
            "japan",
            "samurai",
            "toranaga",
            "hiroyuki-sanada",
            "emmy-winner",
            "4k"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/en.mp3",
                "download_url": "/api/audio/dub/ser-shogun/en.mp3?download=1",
                "file_name": "ser-shogun_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/hi.mp3",
                "download_url": "/api/audio/dub/ser-shogun/hi.mp3?download=1",
                "file_name": "ser-shogun_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/ta.mp3",
                "download_url": "/api/audio/dub/ser-shogun/ta.mp3?download=1",
                "file_name": "ser-shogun_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/te.mp3",
                "download_url": "/api/audio/dub/ser-shogun/te.mp3?download=1",
                "file_name": "ser-shogun_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/ml.mp3",
                "download_url": "/api/audio/dub/ser-shogun/ml.mp3?download=1",
                "file_name": "ser-shogun_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/kn.mp3",
                "download_url": "/api/audio/dub/ser-shogun/kn.mp3?download=1",
                "file_name": "ser-shogun_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/mr.mp3",
                "download_url": "/api/audio/dub/ser-shogun/mr.mp3?download=1",
                "file_name": "ser-shogun_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/es.mp3",
                "download_url": "/api/audio/dub/ser-shogun/es.mp3?download=1",
                "file_name": "ser-shogun_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/fr.mp3",
                "download_url": "/api/audio/dub/ser-shogun/fr.mp3?download=1",
                "file_name": "ser-shogun_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/de.mp3",
                "download_url": "/api/audio/dub/ser-shogun/de.mp3?download=1",
                "file_name": "ser-shogun_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/ja.mp3",
                "download_url": "/api/audio/dub/ser-shogun/ja.mp3?download=1",
                "file_name": "ser-shogun_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-shogun/ko.mp3",
                "download_url": "/api/audio/dub/ser-shogun/ko.mp3?download=1",
                "file_name": "ser-shogun_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Shōgun (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/126308/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ser-the-last-of-us",
        "title": "The Last of Us",
        "subtitle": "Post-Apocalyptic Masterpiece",
        "content_type": "series",
        "description": "After a global pandemic destroys civilization, a hardened survivor takes charge of a 14-year-old girl who may be humanity's last hope. Based on the acclaimed video game by Naughty Dog.",
        "release_year": 2023,
        "age_rating": "TV-MA",
        "imdb_rating": 8.8,
        "tmdb_id": 100088,
        "imdb_id": "tt3581920",
        "quality": "4K ULTRA HD",
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "duration_seconds": 3600,
        "duration_formatted": "9 Episodes",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/100088/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt3581920&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/100088/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "When You're Lost in the Darkness",
                        "duration": "1h 21m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Infected",
                        "duration": "53m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"
                    }
                ]
            }
        ],
        "views": 9120000,
        "likes": 834000,
        "channel": {
            "name": "HBO / Max",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "18.3M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "the-last-of-us",
            "pedro-pascal",
            "bella-ramsey",
            "cordyceps",
            "hbo",
            "4k"
        ],
        "published_at": "2023",
        "is_trending": False,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/en.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/en.mp3?download=1",
                "file_name": "ser-the-last-of-us_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/hi.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/hi.mp3?download=1",
                "file_name": "ser-the-last-of-us_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/ta.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/ta.mp3?download=1",
                "file_name": "ser-the-last-of-us_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/te.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/te.mp3?download=1",
                "file_name": "ser-the-last-of-us_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/ml.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/ml.mp3?download=1",
                "file_name": "ser-the-last-of-us_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/kn.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/kn.mp3?download=1",
                "file_name": "ser-the-last-of-us_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/mr.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/mr.mp3?download=1",
                "file_name": "ser-the-last-of-us_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/es.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/es.mp3?download=1",
                "file_name": "ser-the-last-of-us_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/fr.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/fr.mp3?download=1",
                "file_name": "ser-the-last-of-us_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/de.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/de.mp3?download=1",
                "file_name": "ser-the-last-of-us_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/ja.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/ja.mp3?download=1",
                "file_name": "ser-the-last-of-us_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ser-the-last-of-us/ko.mp3",
                "download_url": "/api/audio/dub/ser-the-last-of-us/ko.mp3?download=1",
                "file_name": "ser-the-last-of-us_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "The Last of Us (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/100088/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ani-solo-leveling",
        "title": "Solo Leveling",
        "subtitle": "Global Manhwa Anime Sensation",
        "content_type": "anime",
        "description": "In a world where hunters, humans who possess magical powers, must battle deadly monsters to protect the human race, Sung Jinwoo, notoriously the weakest hunter of all mankind, finds himself in a mysterious double dungeon.",
        "release_year": 2024,
        "age_rating": "TV-MA",
        "imdb_rating": 8.4,
        "tmdb_id": 209867,
        "imdb_id": "tt21209876",
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "12 Episodes",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/209867/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt21209876&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/209867/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "I'm Used to It",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "If I Had One More Chance",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"
                    }
                ]
            }
        ],
        "views": 7890000,
        "likes": 845000,
        "channel": {
            "name": "A-1 Pictures",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "9.1M",
            "verified": True
        },
        "category": "Anime",
        "tags": [
            "solo-leveling",
            "sung-jinwoo",
            "hunter",
            "anime",
            "action"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/en.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/en.mp3?download=1",
                "file_name": "ani-solo-leveling_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/hi.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/hi.mp3?download=1",
                "file_name": "ani-solo-leveling_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/ta.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/ta.mp3?download=1",
                "file_name": "ani-solo-leveling_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/te.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/te.mp3?download=1",
                "file_name": "ani-solo-leveling_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/ml.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/ml.mp3?download=1",
                "file_name": "ani-solo-leveling_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/kn.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/kn.mp3?download=1",
                "file_name": "ani-solo-leveling_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/mr.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/mr.mp3?download=1",
                "file_name": "ani-solo-leveling_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/es.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/es.mp3?download=1",
                "file_name": "ani-solo-leveling_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/fr.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/fr.mp3?download=1",
                "file_name": "ani-solo-leveling_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/de.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/de.mp3?download=1",
                "file_name": "ani-solo-leveling_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/ja.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/ja.mp3?download=1",
                "file_name": "ani-solo-leveling_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-solo-leveling/ko.mp3",
                "download_url": "/api/audio/dub/ani-solo-leveling/ko.mp3?download=1",
                "file_name": "ani-solo-leveling_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Solo Leveling (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/209867/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ani-demon-slayer",
        "title": "Demon Slayer: Hashira Training Arc",
        "subtitle": "Ufotable Action Masterpiece",
        "content_type": "anime",
        "description": "Tanjiro goes to see the Stone Hashira, Himejima, who intends to prepare him for the battles to come. The training to become a Hashira is rigorous and demanding, earning Himejima's approval seems impossible.",
        "release_year": 2024,
        "age_rating": "TV-14",
        "imdb_rating": 8.6,
        "tmdb_id": 85937,
        "imdb_id": "tt9335498",
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "4 Seasons",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/85937/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt9335498&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/85937/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 4,
                "season_title": "Hashira Training Arc",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "To Defeat Muzan Kibutsuji",
                        "duration": "48m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Water Hashira Giyu Tomioka's Pain",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"
                    }
                ]
            }
        ],
        "views": 9450000,
        "likes": 910000,
        "channel": {
            "name": "Ufotable / Aniplex",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100",
            "subscribers": "12.4M",
            "verified": True
        },
        "category": "Anime",
        "tags": [
            "demon-slayer",
            "kimetsu-no-yaiba",
            "tanjiro",
            "hashira",
            "ufotable",
            "anime"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/en.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/en.mp3?download=1",
                "file_name": "ani-demon-slayer_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/hi.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/hi.mp3?download=1",
                "file_name": "ani-demon-slayer_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/ta.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/ta.mp3?download=1",
                "file_name": "ani-demon-slayer_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/te.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/te.mp3?download=1",
                "file_name": "ani-demon-slayer_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/ml.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/ml.mp3?download=1",
                "file_name": "ani-demon-slayer_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/kn.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/kn.mp3?download=1",
                "file_name": "ani-demon-slayer_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/mr.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/mr.mp3?download=1",
                "file_name": "ani-demon-slayer_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/es.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/es.mp3?download=1",
                "file_name": "ani-demon-slayer_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/fr.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/fr.mp3?download=1",
                "file_name": "ani-demon-slayer_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/de.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/de.mp3?download=1",
                "file_name": "ani-demon-slayer_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/ja.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/ja.mp3?download=1",
                "file_name": "ani-demon-slayer_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-demon-slayer/ko.mp3",
                "download_url": "/api/audio/dub/ani-demon-slayer/ko.mp3?download=1",
                "file_name": "ani-demon-slayer_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Demon Slayer: Hashira Training Arc (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/85937/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ani-attack-on-titan",
        "title": "Attack on Titan",
        "subtitle": "Legendary Dark Fantasy Saga",
        "content_type": "anime",
        "description": "After his hometown is destroyed and his mother is killed, young Eren Jaeger vows to cleanse the earth of the giant humanoid Titans that have brought humanity to the brink of extinction.",
        "release_year": 2023,
        "age_rating": "TV-MA",
        "imdb_rating": 9.1,
        "tmdb_id": 1429,
        "imdb_id": "tt2560140",
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "4 Seasons",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/1429/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt2560140&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/1429/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 4,
                "season_title": "The Final Season",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "The Other Side of the Sea",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Midnight Train",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"
                    }
                ]
            }
        ],
        "views": 8920000,
        "likes": 980000,
        "channel": {
            "name": "MAPPA / Wit Studio",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100",
            "subscribers": "15.1M",
            "verified": True
        },
        "category": "Anime",
        "tags": [
            "attack-on-titan",
            "eren-yeager",
            "titans",
            "mappa",
            "anime"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/en.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/en.mp3?download=1",
                "file_name": "ani-attack-on-titan_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/hi.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/hi.mp3?download=1",
                "file_name": "ani-attack-on-titan_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/ta.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/ta.mp3?download=1",
                "file_name": "ani-attack-on-titan_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/te.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/te.mp3?download=1",
                "file_name": "ani-attack-on-titan_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/ml.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/ml.mp3?download=1",
                "file_name": "ani-attack-on-titan_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/kn.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/kn.mp3?download=1",
                "file_name": "ani-attack-on-titan_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/mr.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/mr.mp3?download=1",
                "file_name": "ani-attack-on-titan_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/es.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/es.mp3?download=1",
                "file_name": "ani-attack-on-titan_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/fr.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/fr.mp3?download=1",
                "file_name": "ani-attack-on-titan_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/de.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/de.mp3?download=1",
                "file_name": "ani-attack-on-titan_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/ja.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/ja.mp3?download=1",
                "file_name": "ani-attack-on-titan_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-attack-on-titan/ko.mp3",
                "download_url": "/api/audio/dub/ani-attack-on-titan/ko.mp3?download=1",
                "file_name": "ani-attack-on-titan_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Attack on Titan (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/1429/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "ani-cyberpunk-edgerunners",
        "title": "Cyberpunk: Edgerunners",
        "subtitle": "Night City Anime Masterpiece",
        "content_type": "anime",
        "description": "A street kid trying to survive in a technology and body modification-obsessed city of the future. Having everything to lose, he chooses to stay alive by becoming an edgerunner: a mercenary outlaw.",
        "release_year": 2023,
        "age_rating": "TV-MA",
        "imdb_rating": 8.3,
        "tmdb_id": 105248,
        "imdb_id": "tt12590266",
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "10 Episodes",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Full Series (Cloud 4K VidLink)",
                "type": "embed_tv",
                "url": "https://vidlink.pro/tv/105248/1/1?primaryColor=06b6d4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Fast Cloud Mirror (2Embed)",
                "type": "embed_tv",
                "url": "https://www.2embed.cc/embedtv/tt12590266&s=1&e=1"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Cloud Mirror (AutoEmbed)",
                "type": "embed_tv",
                "url": "https://autoembed.co/tv/tmdb/105248/1/1"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Direct HD Stream",
                "type": "native",
                "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            }
        ],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "City of Dreams",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"
                    },
                    {
                        "episode_number": 2,
                        "title": "Like a Boy",
                        "duration": "24m",
                        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"
                    }
                ]
            }
        ],
        "views": 4320000,
        "likes": 472000,
        "channel": {
            "name": "Studio Trigger",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100",
            "subscribers": "7.9M",
            "verified": True
        },
        "category": "Anime",
        "tags": [
            "cyberpunk",
            "edgerunners",
            "david-martinez",
            "lucy",
            "studio-trigger"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "comments": [],
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/en.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/en.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/hi.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/hi.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/ta.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/ta.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/te.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/te.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/ml.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/ml.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/kn.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/kn.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/mr.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/mr.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/es.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/es.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/fr.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/fr.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/de.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/de.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/ja.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/ja.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/ani-cyberpunk-edgerunners/ko.mp3",
                "download_url": "/api/audio/dub/ani-cyberpunk-edgerunners/ko.mp3?download=1",
                "file_name": "ani-cyberpunk-edgerunners_ko.mp3"
            }
        ],
        "dual_audio_meta": {
            "title_with_audio": "Cyberpunk: Edgerunners (HD Series Stream)",
            "languages": "English / Original",
            "quality_spec": "1080p HD Full Season",
            "stream_url": "https://vidlink.pro/tv/105248/1/1?primaryColor=06b6d4",
            "direct_mp4_available": False
        }
    },
    {
        "id": "mov-titanic",
        "title": "Titanic",
        "subtitle": "1997 • Drama, Romance",
        "content_type": "movie",
        "description": "Titanic (1997) streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 1997,
        "age_rating": "PG-13",
        "imdb_rating": 7.9,
        "tmdb_id": 597,
        "imdb_id": "tt0120338",
        "quality": "1080p Full HD",
        "duration_seconds": 7200,
        "duration_formatted": "2h 10m",
        "video_url": "https://archive.org/download/titanic-1997-dual-audio-hindi-english-1080p-blu-ray-3.1-gb-esub-boll-yflix_202610/Titanic%20%281997%29%20Dual%20Audio%20%7BHindi-English%7D%201080p%20BluRay%203.1GB%20ESub%20%5BBollYFlix%5D.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/titanic-1997-dual-audio-hindi-english-1080p-blu-ray-3.1-gb-esub-boll-yflix_202610/Titanic%20%281997%29%20Dual%20Audio%20%7BHindi-English%7D%201080p%20BluRay%203.1GB%20ESub%20%5BBollYFlix%5D.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/597?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/597"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/597"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1850000,
        "likes": 95000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "dual-audio",
            "hindi-dubbed",
            "direct-mp4",
            "cinema"
        ],
        "published_at": "1997",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/en.mp3",
                "download_url": "/api/audio/dub/mov-titanic/en.mp3?download=1",
                "file_name": "mov-titanic_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/hi.mp3",
                "download_url": "/api/audio/dub/mov-titanic/hi.mp3?download=1",
                "file_name": "mov-titanic_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/ta.mp3",
                "download_url": "/api/audio/dub/mov-titanic/ta.mp3?download=1",
                "file_name": "mov-titanic_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/te.mp3",
                "download_url": "/api/audio/dub/mov-titanic/te.mp3?download=1",
                "file_name": "mov-titanic_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/ml.mp3",
                "download_url": "/api/audio/dub/mov-titanic/ml.mp3?download=1",
                "file_name": "mov-titanic_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/kn.mp3",
                "download_url": "/api/audio/dub/mov-titanic/kn.mp3?download=1",
                "file_name": "mov-titanic_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/mr.mp3",
                "download_url": "/api/audio/dub/mov-titanic/mr.mp3?download=1",
                "file_name": "mov-titanic_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/es.mp3",
                "download_url": "/api/audio/dub/mov-titanic/es.mp3?download=1",
                "file_name": "mov-titanic_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/fr.mp3",
                "download_url": "/api/audio/dub/mov-titanic/fr.mp3?download=1",
                "file_name": "mov-titanic_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/de.mp3",
                "download_url": "/api/audio/dub/mov-titanic/de.mp3?download=1",
                "file_name": "mov-titanic_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/ja.mp3",
                "download_url": "/api/audio/dub/mov-titanic/ja.mp3?download=1",
                "file_name": "mov-titanic_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-titanic/ko.mp3",
                "download_url": "/api/audio/dub/mov-titanic/ko.mp3?download=1",
                "file_name": "mov-titanic_ko.mp3"
            }
        ],
        "comments": [],
        "dual_audio_meta": {
            "title_with_audio": "Titanic (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "1080p BluRay Dual Audio MP4 (1112 MB)",
            "stream_url": "https://archive.org/download/titanic-1997-dual-audio-hindi-english-1080p-blu-ray-3.1-gb-esub-boll-yflix_202610/Titanic%20%281997%29%20Dual%20Audio%20%7BHindi-English%7D%201080p%20BluRay%203.1GB%20ESub%20%5BBollYFlix%5D.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-aquaman",
        "title": "Aquaman",
        "subtitle": "2018 • Action, Adventure, Fantasy",
        "content_type": "movie",
        "description": "Aquaman (2018) streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 2018,
        "age_rating": "PG-13",
        "imdb_rating": 6.8,
        "tmdb_id": 297802,
        "imdb_id": "tt1477834",
        "quality": "1080p Full HD",
        "duration_seconds": 7200,
        "duration_formatted": "2h 10m",
        "video_url": "https://archive.org/download/aquaman-2018-hindi-english-dual-audio-hollywood-movie-imax-blu-ray-hd-720p-esub/Aquaman%20%282018%29%20%28Hindi%20%2B%20English%29%20Dual%20Audio%20Hollywood%20Movie%20IMAX%20BluRay%20HD%20720p%20ESub.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/aquaman-2018-hindi-english-dual-audio-hollywood-movie-imax-blu-ray-hd-720p-esub/Aquaman%20%282018%29%20%28Hindi%20%2B%20English%29%20Dual%20Audio%20Hollywood%20Movie%20IMAX%20BluRay%20HD%20720p%20ESub.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/297802?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/297802"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/297802"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1850000,
        "likes": 95000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "dual-audio",
            "hindi-dubbed",
            "direct-mp4",
            "cinema"
        ],
        "published_at": "2018",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/en.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/en.mp3?download=1",
                "file_name": "mov-aquaman_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/hi.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/hi.mp3?download=1",
                "file_name": "mov-aquaman_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/ta.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/ta.mp3?download=1",
                "file_name": "mov-aquaman_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/te.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/te.mp3?download=1",
                "file_name": "mov-aquaman_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/ml.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/ml.mp3?download=1",
                "file_name": "mov-aquaman_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/kn.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/kn.mp3?download=1",
                "file_name": "mov-aquaman_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/mr.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/mr.mp3?download=1",
                "file_name": "mov-aquaman_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/es.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/es.mp3?download=1",
                "file_name": "mov-aquaman_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/fr.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/fr.mp3?download=1",
                "file_name": "mov-aquaman_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/de.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/de.mp3?download=1",
                "file_name": "mov-aquaman_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/ja.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/ja.mp3?download=1",
                "file_name": "mov-aquaman_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aquaman/ko.mp3",
                "download_url": "/api/audio/dub/mov-aquaman/ko.mp3?download=1",
                "file_name": "mov-aquaman_ko.mp3"
            }
        ],
        "comments": [],
        "dual_audio_meta": {
            "title_with_audio": "Aquaman (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p IMAX BluRay Dual Audio MP4 (823 MB)",
            "stream_url": "https://archive.org/download/aquaman-2018-hindi-english-dual-audio-hollywood-movie-imax-blu-ray-hd-720p-esub/Aquaman%20%282018%29%20%28Hindi%20%2B%20English%29%20Dual%20Audio%20Hollywood%20Movie%20IMAX%20BluRay%20HD%20720p%20ESub.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-venom-2",
        "title": "Venom: Let There Be Carnage",
        "subtitle": "2021 • Action, Sci-Fi, Thriller",
        "content_type": "movie",
        "description": "Venom: Let There Be Carnage (2021) streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 2021,
        "age_rating": "PG-13",
        "imdb_rating": 5.9,
        "tmdb_id": 580489,
        "imdb_id": "tt7097896",
        "quality": "1080p Full HD",
        "duration_seconds": 7200,
        "duration_formatted": "2h 10m",
        "video_url": "https://archive.org/download/venom-2-venom-let-there-be-carnage-2021-hindi-english-dual-audio-mcu-movie-blu-ray-hd-720p-esub/Venom%202%20%28Venom%20Let%20There%20Be%20Carnage%29%20%282021%29%20%28Hindi%20%2B%20English%29%20Dual%20Audio%20MCU%20Movie%20BluRay%20HD%20720p%20ESub.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/venom-2-venom-let-there-be-carnage-2021-hindi-english-dual-audio-mcu-movie-blu-ray-hd-720p-esub/Venom%202%20%28Venom%20Let%20There%20Be%20Carnage%29%20%282021%29%20%28Hindi%20%2B%20English%29%20Dual%20Audio%20MCU%20Movie%20BluRay%20HD%20720p%20ESub.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/580489?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/580489"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/580489"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1850000,
        "likes": 95000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "dual-audio",
            "hindi-dubbed",
            "direct-mp4",
            "cinema"
        ],
        "published_at": "2021",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/en.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/en.mp3?download=1",
                "file_name": "mov-venom-2_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/hi.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/hi.mp3?download=1",
                "file_name": "mov-venom-2_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/ta.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/ta.mp3?download=1",
                "file_name": "mov-venom-2_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/te.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/te.mp3?download=1",
                "file_name": "mov-venom-2_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/ml.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/ml.mp3?download=1",
                "file_name": "mov-venom-2_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/kn.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/kn.mp3?download=1",
                "file_name": "mov-venom-2_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/mr.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/mr.mp3?download=1",
                "file_name": "mov-venom-2_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/es.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/es.mp3?download=1",
                "file_name": "mov-venom-2_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/fr.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/fr.mp3?download=1",
                "file_name": "mov-venom-2_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/de.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/de.mp3?download=1",
                "file_name": "mov-venom-2_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/ja.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/ja.mp3?download=1",
                "file_name": "mov-venom-2_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-venom-2/ko.mp3",
                "download_url": "/api/audio/dub/mov-venom-2/ko.mp3?download=1",
                "file_name": "mov-venom-2_ko.mp3"
            }
        ],
        "comments": [],
        "dual_audio_meta": {
            "title_with_audio": "Venom: Let There Be Carnage (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p BluRay Dual Audio MP4 (561 MB)",
            "stream_url": "https://archive.org/download/venom-2-venom-let-there-be-carnage-2021-hindi-english-dual-audio-mcu-movie-blu-ray-hd-720p-esub/Venom%202%20%28Venom%20Let%20There%20Be%20Carnage%29%20%282021%29%20%28Hindi%20%2B%20English%29%20Dual%20Audio%20MCU%20Movie%20BluRay%20HD%20720p%20ESub.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-the-sixth-sense",
        "title": "The Sixth Sense",
        "subtitle": "1999 • Drama, Mystery, Thriller",
        "content_type": "movie",
        "description": "The Sixth Sense (1999) streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 1999,
        "age_rating": "PG-13",
        "imdb_rating": 8.2,
        "tmdb_id": 745,
        "imdb_id": "tt0167404",
        "quality": "1080p Full HD",
        "duration_seconds": 7200,
        "duration_formatted": "2h 10m",
        "video_url": "https://archive.org/download/TheSixthSense1999720pWWW.DesiPirates.TKBRRipDualAudioHindiEnglish/The%20Sixth%20Sense%20%281999%29%20720p%20WWW.DesiPirates.TK%20BRRip%20Dual%20Audio%20Hindi-English.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/TheSixthSense1999720pWWW.DesiPirates.TKBRRipDualAudioHindiEnglish/The%20Sixth%20Sense%20%281999%29%20720p%20WWW.DesiPirates.TK%20BRRip%20Dual%20Audio%20Hindi-English.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/745?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/745"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/745"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1850000,
        "likes": 95000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "dual-audio",
            "hindi-dubbed",
            "direct-mp4",
            "cinema"
        ],
        "published_at": "1999",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/en.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/en.mp3?download=1",
                "file_name": "mov-the-sixth-sense_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/hi.mp3?download=1",
                "file_name": "mov-the-sixth-sense_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/ta.mp3?download=1",
                "file_name": "mov-the-sixth-sense_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/te.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/te.mp3?download=1",
                "file_name": "mov-the-sixth-sense_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/ml.mp3?download=1",
                "file_name": "mov-the-sixth-sense_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/kn.mp3?download=1",
                "file_name": "mov-the-sixth-sense_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/mr.mp3?download=1",
                "file_name": "mov-the-sixth-sense_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/es.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/es.mp3?download=1",
                "file_name": "mov-the-sixth-sense_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/fr.mp3?download=1",
                "file_name": "mov-the-sixth-sense_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/de.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/de.mp3?download=1",
                "file_name": "mov-the-sixth-sense_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/ja.mp3?download=1",
                "file_name": "mov-the-sixth-sense_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-sixth-sense/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-sixth-sense/ko.mp3?download=1",
                "file_name": "mov-the-sixth-sense_ko.mp3"
            }
        ],
        "comments": [],
        "dual_audio_meta": {
            "title_with_audio": "The Sixth Sense (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p BRRip Dual Audio MP4 (637 MB)",
            "stream_url": "https://archive.org/download/TheSixthSense1999720pWWW.DesiPirates.TKBRRipDualAudioHindiEnglish/The%20Sixth%20Sense%20%281999%29%20720p%20WWW.DesiPirates.TK%20BRRip%20Dual%20Audio%20Hindi-English.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-the-martian",
        "title": "The Martian",
        "subtitle": "2015 • Adventure, Drama, Sci-Fi",
        "content_type": "movie",
        "description": "The Martian (2015) streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 2015,
        "age_rating": "PG-13",
        "imdb_rating": 8.0,
        "tmdb_id": 286217,
        "imdb_id": "tt3659388",
        "quality": "1080p Full HD",
        "duration_seconds": 7200,
        "duration_formatted": "2h 10m",
        "video_url": "https://archive.org/download/the-martian-2015-bolly-4u.org-blu-ray-extended-dual-audio-720p-1.1-gb/The%20Martian%20%282015%29%20%5B%20Bolly4u.org%5D%20BluRay%20Extended%20Dual%20audio%20720p%201.1GB.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/the-martian-2015-bolly-4u.org-blu-ray-extended-dual-audio-720p-1.1-gb/The%20Martian%20%282015%29%20%5B%20Bolly4u.org%5D%20BluRay%20Extended%20Dual%20audio%20720p%201.1GB.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/286217?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/286217"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/286217"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1850000,
        "likes": 95000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Adventure",
        "tags": [
            "dual-audio",
            "hindi-dubbed",
            "direct-mp4",
            "cinema"
        ],
        "published_at": "2015",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/en.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/en.mp3?download=1",
                "file_name": "mov-the-martian_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/hi.mp3?download=1",
                "file_name": "mov-the-martian_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/ta.mp3?download=1",
                "file_name": "mov-the-martian_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/te.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/te.mp3?download=1",
                "file_name": "mov-the-martian_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/ml.mp3?download=1",
                "file_name": "mov-the-martian_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/kn.mp3?download=1",
                "file_name": "mov-the-martian_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/mr.mp3?download=1",
                "file_name": "mov-the-martian_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/es.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/es.mp3?download=1",
                "file_name": "mov-the-martian_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/fr.mp3?download=1",
                "file_name": "mov-the-martian_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/de.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/de.mp3?download=1",
                "file_name": "mov-the-martian_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/ja.mp3?download=1",
                "file_name": "mov-the-martian_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-martian/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-martian/ko.mp3?download=1",
                "file_name": "mov-the-martian_ko.mp3"
            }
        ],
        "comments": [],
        "dual_audio_meta": {
            "title_with_audio": "The Martian (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p BluRay Extended Dual Audio MP4 (845 MB)",
            "stream_url": "https://archive.org/download/the-martian-2015-bolly-4u.org-blu-ray-extended-dual-audio-720p-1.1-gb/The%20Martian%20%282015%29%20%5B%20Bolly4u.org%5D%20BluRay%20Extended%20Dual%20audio%20720p%201.1GB.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-godzilla-final-wars",
        "title": "Godzilla: Final Wars",
        "subtitle": "2004 • Action, Adventure, Fantasy",
        "content_type": "movie",
        "description": "Godzilla: Final Wars (2004) streaming in verified direct Dual Audio (Hindi Dubbed).",
        "release_year": 2004,
        "age_rating": "PG-13",
        "imdb_rating": 6.4,
        "tmdb_id": 15301,
        "imdb_id": "tt0399102",
        "quality": "1080p Full HD",
        "duration_seconds": 7200,
        "duration_formatted": "2h 10m",
        "video_url": "https://archive.org/download/godzilla-final-wars-hindi-dubbed-version/Godzilla%20Final%20Wars%20-%20Hindi%20dubbed%20version.ia.mp4",
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi Dubbed)",
                "type": "native",
                "url": "https://archive.org/download/godzilla-final-wars-hindi-dubbed-version/Godzilla%20Final%20Wars%20-%20Hindi%20dubbed%20version.ia.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/15301?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/15301"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/15301"
            }
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1850000,
        "likes": 95000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "dual-audio",
            "hindi-dubbed",
            "direct-mp4",
            "cinema"
        ],
        "published_at": "2004",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/en.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/en.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/hi.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/hi.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/ta.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/ta.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/te.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/te.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/ml.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/ml.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/kn.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/kn.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/mr.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/mr.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/es.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/es.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/fr.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/fr.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/de.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/de.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/ja.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/ja.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-godzilla-final-wars/ko.mp3",
                "download_url": "/api/audio/dub/mov-godzilla-final-wars/ko.mp3?download=1",
                "file_name": "mov-godzilla-final-wars_ko.mp3"
            }
        ],
        "comments": [],
        "dual_audio_meta": {
            "title_with_audio": "Godzilla: Final Wars (Hindi Dubbed)",
            "languages": "Hindi Dubbed",
            "quality_spec": "1080p HD Hindi Dubbed MP4 (2108 MB)",
            "stream_url": "https://archive.org/download/godzilla-final-wars-hindi-dubbed-version/Godzilla%20Final%20Wars%20-%20Hindi%20dubbed%20version.ia.mp4",
            "direct_mp4_available": True
        }
    },
    {
        "id": "mov-hi-nanna",
        "title": "Hi Nanna (2023)",
        "subtitle": "2023 • Romance, Drama, Family",
        "content_type": "movie",
        "description": "Hi Nanna (2023) starring Nani and Mrunal Thakur streaming in verified direct Dual Audio (Hindi + Telugu).",
        "release_year": 2023,
        "age_rating": "PG",
        "imdb_rating": 8.2,
        "tmdb_id": 1198642,
        "imdb_id": "tt28381677",
        "quality": "1080p Full HD",
        "duration_seconds": 9300,
        "duration_formatted": "2h 35m",
        "video_url": "https://archive.org/download/hi-nannas/Hi%20Nanna%20%282023%29%201080p%20HDRip.%20%5BDual%20Audio%5D%20%5BHindi%20%2B%20Telugu%5D%20x264%20ESubs%20%5B3.2GB%5D%20-%20QRips.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 2100000,
        "likes": 145000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Romance",
        "tags": [
            "hi-nanna",
            "dual-audio",
            "hindi-telugu",
            "direct-mp4"
        ],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "dual_audio_meta": {
            "title_with_audio": "Hi Nanna (Hindi + Telugu)",
            "languages": "Hindi + Telugu",
            "quality_spec": "1080p HDRip Dual Audio MP4 (3.2 GB)",
            "stream_url": "https://archive.org/download/hi-nannas/Hi%20Nanna%20%282023%29%201080p%20HDRip.%20%5BDual%20Audio%5D%20%5BHindi%20%2B%20Telugu%5D%20x264%20ESubs%20%5B3.2GB%5D%20-%20QRips.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + Telugu)",
                "type": "native",
                "url": "https://archive.org/download/hi-nannas/Hi%20Nanna%20%282023%29%201080p%20HDRip.%20%5BDual%20Audio%5D%20%5BHindi%20%2B%20Telugu%5D%20x264%20ESubs%20%5B3.2GB%5D%20-%20QRips.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1198642?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1198642"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1198642"
            }
        ],
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/en.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/en.mp3?download=1",
                "file_name": "mov-hi-nanna_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/hi.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/hi.mp3?download=1",
                "file_name": "mov-hi-nanna_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/ta.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/ta.mp3?download=1",
                "file_name": "mov-hi-nanna_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/te.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/te.mp3?download=1",
                "file_name": "mov-hi-nanna_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/ml.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/ml.mp3?download=1",
                "file_name": "mov-hi-nanna_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/kn.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/kn.mp3?download=1",
                "file_name": "mov-hi-nanna_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/mr.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/mr.mp3?download=1",
                "file_name": "mov-hi-nanna_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/es.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/es.mp3?download=1",
                "file_name": "mov-hi-nanna_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/fr.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/fr.mp3?download=1",
                "file_name": "mov-hi-nanna_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/de.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/de.mp3?download=1",
                "file_name": "mov-hi-nanna_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/ja.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/ja.mp3?download=1",
                "file_name": "mov-hi-nanna_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hi-nanna/ko.mp3",
                "download_url": "/api/audio/dub/mov-hi-nanna/ko.mp3?download=1",
                "file_name": "mov-hi-nanna_ko.mp3"
            }
        ],
        "comments": []
    },
    {
        "id": "mov-aavesham",
        "title": "Aavesham (2024)",
        "subtitle": "2024 • Action, Comedy",
        "content_type": "movie",
        "description": "Aavesham (2024) starring Fahadh Faasil streaming in verified direct Dual Audio (Hindi + Malayalam).",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 8.0,
        "tmdb_id": 1111624,
        "imdb_id": "tt27056116",
        "quality": "1080p Full HD",
        "duration_seconds": 9480,
        "duration_formatted": "2h 38m",
        "video_url": "https://archive.org/download/aavesham-2024-malayalam-movie-in-hindi-org-dual-audio-south-movie-uncut-1080p-hdrip-2.69-gb-esubs/Aav3sham%20%282024%29%20M%40l%40yal4m%20Movie%20in%20Hindi%20ORG%20Dual%20Audio%20South%20Movie%20UNCUT%201080p%20HDRip%202.69GB%20ESubs.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 2400000,
        "likes": 178000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Action",
        "tags": [
            "aavesham",
            "dual-audio",
            "hindi-malayalam",
            "fahadh-faasil"
        ],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "dual_audio_meta": {
            "title_with_audio": "Aavesham (Hindi + Malayalam)",
            "languages": "Hindi + Malayalam",
            "quality_spec": "1080p HDRip Dual Audio MP4 (2.69 GB)",
            "stream_url": "https://archive.org/download/aavesham-2024-malayalam-movie-in-hindi-org-dual-audio-south-movie-uncut-1080p-hdrip-2.69-gb-esubs/Aav3sham%20%282024%29%20M%40l%40yal4m%20Movie%20in%20Hindi%20ORG%20Dual%20Audio%20South%20Movie%20UNCUT%201080p%20HDRip%202.69GB%20ESubs.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + Malayalam)",
                "type": "native",
                "url": "https://archive.org/download/aavesham-2024-malayalam-movie-in-hindi-org-dual-audio-south-movie-uncut-1080p-hdrip-2.69-gb-esubs/Aav3sham%20%282024%29%20M%40l%40yal4m%20Movie%20in%20Hindi%20ORG%20Dual%20Audio%20South%20Movie%20UNCUT%201080p%20HDRip%202.69GB%20ESubs.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/1111624?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/1111624"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/1111624"
            }
        ],
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/en.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/en.mp3?download=1",
                "file_name": "mov-aavesham_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/hi.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/hi.mp3?download=1",
                "file_name": "mov-aavesham_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/ta.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/ta.mp3?download=1",
                "file_name": "mov-aavesham_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/te.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/te.mp3?download=1",
                "file_name": "mov-aavesham_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/ml.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/ml.mp3?download=1",
                "file_name": "mov-aavesham_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/kn.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/kn.mp3?download=1",
                "file_name": "mov-aavesham_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/mr.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/mr.mp3?download=1",
                "file_name": "mov-aavesham_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/es.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/es.mp3?download=1",
                "file_name": "mov-aavesham_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/fr.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/fr.mp3?download=1",
                "file_name": "mov-aavesham_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/de.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/de.mp3?download=1",
                "file_name": "mov-aavesham_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/ja.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/ja.mp3?download=1",
                "file_name": "mov-aavesham_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-aavesham/ko.mp3",
                "download_url": "/api/audio/dub/mov-aavesham/ko.mp3?download=1",
                "file_name": "mov-aavesham_ko.mp3"
            }
        ],
        "comments": []
    },
    {
        "id": "mov-hitchhikers-guide",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "subtitle": "2005 • Adventure, Comedy, Sci-Fi",
        "content_type": "movie",
        "description": "The Hitchhiker's Guide to the Galaxy (2005) streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 2005,
        "age_rating": "PG",
        "imdb_rating": 6.8,
        "tmdb_id": 7453,
        "imdb_id": "tt0371724",
        "quality": "720p HD",
        "duration_seconds": 6540,
        "duration_formatted": "1h 49m",
        "video_url": "https://archive.org/download/the.-hitchhikers.-guide.to.the.-gaaxy.-2005.720p.-brrip.-hindi.-dual-audio/The.Hitchhikers.Guide.to.the.Gaaxy.2005.720p.BRRip.Hindi.Dual-Audio.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1650000,
        "likes": 88000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "sci-fi",
            "dual-audio",
            "hindi-english",
            "cult-classic"
        ],
        "published_at": "2005",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "dual_audio_meta": {
            "title_with_audio": "The Hitchhiker's Guide to the Galaxy (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p BRRip Dual Audio MP4 (890 MB)",
            "stream_url": "https://archive.org/download/the.-hitchhikers.-guide.to.the.-gaaxy.-2005.720p.-brrip.-hindi.-dual-audio/The.Hitchhikers.Guide.to.the.Gaaxy.2005.720p.BRRip.Hindi.Dual-Audio.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/the.-hitchhikers.-guide.to.the.-gaaxy.-2005.720p.-brrip.-hindi.-dual-audio/The.Hitchhikers.Guide.to.the.Gaaxy.2005.720p.BRRip.Hindi.Dual-Audio.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/7453?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/7453"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/7453"
            }
        ],
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/en.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/en.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/hi.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/hi.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/ta.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/ta.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/te.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/te.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/ml.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/ml.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/kn.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/kn.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/mr.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/mr.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/es.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/es.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/fr.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/fr.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/de.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/de.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/ja.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/ja.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-hitchhikers-guide/ko.mp3",
                "download_url": "/api/audio/dub/mov-hitchhikers-guide/ko.mp3?download=1",
                "file_name": "mov-hitchhikers-guide_ko.mp3"
            }
        ],
        "comments": []
    },
    {
        "id": "mov-the-blackout-invasion",
        "title": "The Blackout: Invasion Earth",
        "subtitle": "2020 • Action, Sci-Fi, Thriller",
        "content_type": "movie",
        "description": "The Blackout: Invasion Earth (2020) streaming in verified direct Dual Audio (Hindi DD 2.0 + English).",
        "release_year": 2020,
        "age_rating": "R",
        "imdb_rating": 6.1,
        "tmdb_id": 574982,
        "imdb_id": "tt9193764",
        "quality": "720p HD",
        "duration_seconds": 9180,
        "duration_formatted": "2h 33m",
        "video_url": "https://archive.org/download/the-blackout-2020-cloud-720p-blu-ray-x-264-dual-audio-hindi-dd-2.0-english-dd-2.0/The%20Blackout%202020%20%5BWorldfree4u.Cloud%5D%20720p%20BluRay%20x264%20%5BDual%20Audio%5D%20%5BHindi%20DD%202.0%20%2B%20English%20DD%202.0%5D.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1780000,
        "likes": 92000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Sci-Fi",
        "tags": [
            "invasion",
            "dual-audio",
            "hindi-english",
            "alien-action"
        ],
        "published_at": "2020",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "dual_audio_meta": {
            "title_with_audio": "The Blackout: Invasion Earth (Hindi DD 2.0 + English)",
            "languages": "Hindi DD 2.0 + English",
            "quality_spec": "720p BluRay Dual Audio MP4 (750 MB)",
            "stream_url": "https://archive.org/download/the-blackout-2020-cloud-720p-blu-ray-x-264-dual-audio-hindi-dd-2.0-english-dd-2.0/The%20Blackout%202020%20%5BWorldfree4u.Cloud%5D%20720p%20BluRay%20x264%20%5BDual%20Audio%5D%20%5BHindi%20DD%202.0%20%2B%20English%20DD%202.0%5D.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi DD 2.0 + English)",
                "type": "native",
                "url": "https://archive.org/download/the-blackout-2020-cloud-720p-blu-ray-x-264-dual-audio-hindi-dd-2.0-english-dd-2.0/The%20Blackout%202020%20%5BWorldfree4u.Cloud%5D%20720p%20BluRay%20x264%20%5BDual%20Audio%5D%20%5BHindi%20DD%202.0%20%2B%20English%20DD%202.0%5D.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/574982?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/574982"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/574982"
            }
        ],
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/en.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/en.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/hi.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/ta.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/te.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/te.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/ml.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/kn.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/mr.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/es.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/es.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/fr.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/de.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/de.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/ja.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-blackout-invasion/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-blackout-invasion/ko.mp3?download=1",
                "file_name": "mov-the-blackout-invasion_ko.mp3"
            }
        ],
        "comments": []
    },
    {
        "id": "mov-the-founder",
        "title": "The Founder",
        "subtitle": "2016 • Biography, Drama",
        "content_type": "movie",
        "description": "The Founder (2016) starring Michael Keaton streaming in verified direct Dual Audio (Hindi + English).",
        "release_year": 2016,
        "age_rating": "PG-13",
        "imdb_rating": 7.2,
        "tmdb_id": 310307,
        "imdb_id": "tt4276820",
        "quality": "720p HD",
        "duration_seconds": 6900,
        "duration_formatted": "1h 55m",
        "video_url": "https://archive.org/download/the-founder-2016-dual-audio-480p-blu-ray-in-hindi/The%20Founder%202016%20Dual%20Audio%20Hindi%20%20%5BMoviesMore.Net%5Dfo%20480p%20BluRay.mp4",
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "subtitles": [
            {
                "label": "English [CC]",
                "srclang": "en",
                "src": "/static/subtitles/english.vtt"
            },
            {
                "label": "Hindi",
                "srclang": "hi",
                "src": "/static/subtitles/hindi.vtt"
            }
        ],
        "views": 1520000,
        "likes": 84000,
        "channel": {
            "name": "Cinema Dual Audio Vault",
            "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100",
            "subscribers": "8.5M",
            "verified": True
        },
        "category": "Drama",
        "tags": [
            "biography",
            "dual-audio",
            "hindi-english",
            "michael-keaton"
        ],
        "published_at": "2016",
        "is_trending": True,
        "is_featured": False,
        "is_world_cinema": False,
        "is_dual_audio": True,
        "dual_audio_meta": {
            "title_with_audio": "The Founder (Hindi + English)",
            "languages": "Hindi + English",
            "quality_spec": "720p BluRay Dual Audio MP4 (450 MB)",
            "stream_url": "https://archive.org/download/the-founder-2016-dual-audio-480p-blu-ray-in-hindi/The%20Founder%202016%20Dual%20Audio%20Hindi%20%20%5BMoviesMore.Net%5Dfo%20480p%20BluRay.mp4",
            "direct_mp4_available": True
        },
        "servers": [
            {
                "id": "srv-1",
                "name": "Server 1: Stream Direct Dual Audio MP4 (Hindi + English)",
                "type": "native",
                "url": "https://archive.org/download/the-founder-2016-dual-audio-480p-blu-ray-in-hindi/The%20Founder%202016%20Dual%20Audio%20Hindi%20%20%5BMoviesMore.Net%5Dfo%20480p%20BluRay.mp4"
            },
            {
                "id": "srv-2",
                "name": "Server 2: Full Movie (Cloud 4K VidLink)",
                "type": "embed",
                "url": "https://vidlink.pro/movie/310307?primaryColor=06b6d4"
            },
            {
                "id": "srv-3",
                "name": "Server 3: Fast Cloud Mirror (2Embed)",
                "type": "embed",
                "url": "https://www.2embed.cc/embed/310307"
            },
            {
                "id": "srv-4",
                "name": "Server 4: Cloud Mirror (AutoEmbed)",
                "type": "embed",
                "url": "https://autoembed.co/movie/tmdb/310307"
            }
        ],
        "audio_tracks_count": 48,
        "audio_tracks": [
            {
                "code": "en-US",
                "lang": "en",
                "label": "English (Original)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/en.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/en.mp3?download=1",
                "file_name": "mov-the-founder_en.mp3"
            },
            {
                "code": "hi-IN",
                "lang": "hi",
                "label": "हिन्दी (Hindi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/hi.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/hi.mp3?download=1",
                "file_name": "mov-the-founder_hi.mp3"
            },
            {
                "code": "ta-IN",
                "lang": "ta",
                "label": "தமிழ் (Tamil Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/ta.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/ta.mp3?download=1",
                "file_name": "mov-the-founder_ta.mp3"
            },
            {
                "code": "te-IN",
                "lang": "te",
                "label": "తెలుగు (Telugu Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/te.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/te.mp3?download=1",
                "file_name": "mov-the-founder_te.mp3"
            },
            {
                "code": "ml-IN",
                "lang": "ml",
                "label": "മലയാളം (Malayalam Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/ml.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/ml.mp3?download=1",
                "file_name": "mov-the-founder_ml.mp3"
            },
            {
                "code": "kn-IN",
                "lang": "kn",
                "label": "ಕನ್ನಡ (Kannada Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/kn.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/kn.mp3?download=1",
                "file_name": "mov-the-founder_kn.mp3"
            },
            {
                "code": "mr-IN",
                "lang": "mr",
                "label": "मराठी (Marathi Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/mr.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/mr.mp3?download=1",
                "file_name": "mov-the-founder_mr.mp3"
            },
            {
                "code": "es-MX",
                "lang": "es",
                "label": "Español (Spanish Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/es.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/es.mp3?download=1",
                "file_name": "mov-the-founder_es.mp3"
            },
            {
                "code": "fr-FR",
                "lang": "fr",
                "label": "Français (French Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/fr.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/fr.mp3?download=1",
                "file_name": "mov-the-founder_fr.mp3"
            },
            {
                "code": "de-DE",
                "lang": "de",
                "label": "Deutsch (German Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/de.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/de.mp3?download=1",
                "file_name": "mov-the-founder_de.mp3"
            },
            {
                "code": "ja-JP",
                "lang": "ja",
                "label": "日本語 (Japanese Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/ja.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/ja.mp3?download=1",
                "file_name": "mov-the-founder_ja.mp3"
            },
            {
                "code": "ko-KR",
                "lang": "ko",
                "label": "한국어 (Korean Dub)",
                "bitrate": "320 kbps",
                "codec": "MP3 Dolby",
                "url": "/api/audio/dub/mov-the-founder/ko.mp3",
                "download_url": "/api/audio/dub/mov-the-founder/ko.mp3?download=1",
                "file_name": "mov-the-founder_ko.mp3"
            }
        ],
        "comments": []
    }
]
def get_hero_featured() -> Dict[str, Any]:
    """Returns the top spotlight trending video for the hero billboard banner."""
    for v in VIDEOS_CATALOG:
        if v.get("is_featured") and v.get("is_trending"):
            return v
    return VIDEOS_CATALOG[0]

def get_content_rails() -> Dict[str, List[Dict[str, Any]]]:
    """Returns structured horizontal rails for Netflix / Movibox / CineHD layout."""
    trending = [v for v in VIDEOS_CATALOG if v.get("is_trending")]
    movies = [v for v in VIDEOS_CATALOG if v.get("content_type") == "movie"]
    dual_audio = [v for v in VIDEOS_CATALOG if v.get("is_dual_audio")]
    world_cinema = [v for v in VIDEOS_CATALOG if v.get("content_type") == "movie" and v.get("is_world_cinema")]
    series = [v for v in VIDEOS_CATALOG if v.get("content_type") == "series"]
    anime = [v for v in VIDEOS_CATALOG if v.get("content_type") == "anime"]

    return {
        "trending": trending,
        "movies": movies,
        "world_cinema": world_cinema,
        "series": series,
        "anime": anime,
        "dual_audio": dual_audio
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
            or any(s in tag.lower() for tag in v.get("tags", []))
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
                "id": f"c_{len(v.get('comments', [])) + 1}",
                "author": author[:30] or "Anonymous Streamer",
                "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80",
                "text": text[:300],
                "timestamp": "Just now",
                "likes": 0
            }
            if "comments" not in v:
                v["comments"] = []
            v["comments"].insert(0, comment)
            return comment
    return None

# Attach audio_tracks to all catalog movies
for _v in VIDEOS_CATALOG:
    _v['audio_tracks'] = generate_movie_audio_tracks(_v['id'])
