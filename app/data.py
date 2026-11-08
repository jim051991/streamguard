"""
StreamGuard 2.0 OTT Entertainment Catalog & Streaming Data Store
Houses Hollywood Blockbusters, Hit TV Series, and Top Anime inspired by Movibox.net and CineHD.dev.
Includes multi-server fallback, multi-episode seasons, IMDb ratings, and high-definition posters.
All stream sources use verified, permanent open-access video streams.
"""

from typing import List, Dict, Any, Optional

VIDEOS_CATALOG: List[Dict[str, Any]] = [
    # =========================================================================
    # 1. TRENDING & FEATURE MOVIES (Hollywood Blockbusters)
    # =========================================================================
    {
        "id": "mov-dune-2",
        "title": "Dune: Part Two",
        "subtitle": "Epic Sci-Fi Space Opera",
        "content_type": "movie",
        "description": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the known universe, he endeavors to prevent a terrible future only he can foresee.",
        "release_year": 2024,
        "age_rating": "PG-13",
        "imdb_rating": 8.6,
        "quality": "4K ULTRA HD",
        "duration_seconds": 9960,
        "duration_formatted": "2h 46m",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4"},
            {"id": "srv-3", "name": "Server 3 (StreamGuard Relay)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 2480000,
        "likes": 182000,
        "channel": {"name": "Warner Bros. Pictures", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&auto=format&fit=crop&q=80", "subscribers": "11.2M", "verified": True},
        "category": "Sci-Fi",
        "tags": ["dune", "sci-fi", "timothee-chalamet", "zendaya", "4k"],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": True,
        "comments": [
            {"id": "c101", "author": "ArrakisWatcher", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100", "text": "Denis Villeneuve created an absolute cinematic triumph. The sandworm ride sequence was breathtaking!", "timestamp": "1 hour ago", "likes": 542}
        ]
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
        "quality": "4K ULTRA HD",
        "duration_seconds": 10800,
        "duration_formatted": "3h 00m",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 3890000,
        "likes": 294000,
        "channel": {"name": "Universal Pictures", "avatar": "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=100", "subscribers": "9.8M", "verified": True},
        "category": "Drama",
        "tags": ["oppenheimer", "christopher-nolan", "cillian-murphy", "oscar-winner"],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "mov-spider-verse",
        "title": "Spider-Man: Across the Spider-Verse",
        "subtitle": "Multiverse Animated Action",
        "content_type": "movie",
        "description": "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence. When the heroes clash on how to handle a new threat, Miles must redefine what it means to be a hero.",
        "release_year": 2023,
        "age_rating": "PG",
        "imdb_rating": 8.7,
        "quality": "4K ULTRA HD",
        "duration_seconds": 8400,
        "duration_formatted": "2h 20m",
        "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 4120000,
        "likes": 381000,
        "channel": {"name": "Sony Pictures Animation", "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100", "subscribers": "7.4M", "verified": True},
        "category": "Animation",
        "tags": ["spider-man", "miles-morales", "marvel", "animation", "4k"],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "comments": []
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
        "quality": "4K ULTRA HD",
        "duration_seconds": 10140,
        "duration_formatted": "2h 49m",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 5920000,
        "likes": 482000,
        "channel": {"name": "Paramount Pictures", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100", "subscribers": "8.1M", "verified": True},
        "category": "Sci-Fi",
        "tags": ["interstellar", "space", "black-hole", "nolan", "zimmer"],
        "published_at": "2014",
        "is_trending": False,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "mov-the-batman",
        "title": "The Batman",
        "subtitle": "Gotham Detective Noir Action",
        "content_type": "movie",
        "description": "When a sadistic serial killer begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement.",
        "release_year": 2022,
        "age_rating": "PG-13",
        "imdb_rating": 7.8,
        "quality": "4K ULTRA HD",
        "duration_seconds": 10560,
        "duration_formatted": "2h 56m",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 3120000,
        "likes": 218000,
        "channel": {"name": "DC Films", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100", "subscribers": "6.2M", "verified": True},
        "category": "Action",
        "tags": ["batman", "dc", "robert-pattinson", "gotham", "noir"],
        "published_at": "2022",
        "is_trending": False,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "mov-avatar-2",
        "title": "Avatar: The Way of Water",
        "subtitle": "Pandora Oceanic Sci-Fi",
        "content_type": "movie",
        "description": "Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na'vi race to protect their home.",
        "release_year": 2022,
        "age_rating": "PG-13",
        "imdb_rating": 7.6,
        "quality": "4K ULTRA HD",
        "duration_seconds": 11520,
        "duration_formatted": "3h 12m",
        "video_url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "views": 4750000,
        "likes": 320000,
        "channel": {"name": "20th Century Studios", "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100", "subscribers": "5.9M", "verified": True},
        "category": "Sci-Fi",
        "tags": ["avatar", "james-cameron", "pandora", "ocean", "4k"],
        "published_at": "2022",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },

    # =========================================================================
    # 2. TOP TELEVISION SERIES (Multi-Episode Seasons)
    # =========================================================================
    {
        "id": "ser-stranger-things",
        "title": "Stranger Things",
        "subtitle": "The Upside Down Chronicles",
        "content_type": "series",
        "description": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces, and one strange little girl with telekinetic abilities.",
        "release_year": 2024,
        "age_rating": "TV-14",
        "imdb_rating": 8.7,
        "quality": "4K ULTRA HD",
        "duration_seconds": 3200,
        "duration_formatted": "4 Seasons",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 4,
                "season_title": "Season 4",
                "episodes": [
                    {"episode_number": 1, "title": "Chapter One: The Hellfire Club", "duration": "1h 16m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
                    {"episode_number": 2, "title": "Chapter Two: Vecna's Curse", "duration": "1h 17m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"},
                    {"episode_number": 3, "title": "Chapter Three: The Monster and the Superhero", "duration": "1h 03m", "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4", "thumbnail": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400"},
                    {"episode_number": 4, "title": "Chapter Four: Dear Billy", "duration": "1h 18m", "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4", "thumbnail": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=400"}
                ]
            }
        ],
        "views": 6240000,
        "likes": 512000,
        "channel": {"name": "Netflix Originals", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100", "subscribers": "26.4M", "verified": True},
        "category": "Sci-Fi",
        "tags": ["stranger-things", "eleven", "upside-down", "80s", "supernatural"],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "ser-house-of-the-dragon",
        "title": "House of the Dragon",
        "subtitle": "The Targaryen Civil War",
        "content_type": "series",
        "description": "An internal succession war within House Targaryen at the height of its power, 172 years before the birth of Daenerys Targaryen. Dragons clash as green and black factions struggle for the Iron Throne.",
        "release_year": 2024,
        "age_rating": "TV-MA",
        "imdb_rating": 8.5,
        "quality": "4K ULTRA HD",
        "duration_seconds": 3600,
        "duration_formatted": "2 Seasons",
        "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud 4K)", "url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 2,
                "season_title": "Season 2: Dance of the Dragons",
                "episodes": [
                    {"episode_number": 1, "title": "A Son for a Son", "duration": "59m", "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4", "thumbnail": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=400"},
                    {"episode_number": 2, "title": "Rhaenyra the Cruel", "duration": "1h 04m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
                    {"episode_number": 3, "title": "The Burning Mill", "duration": "1h 01m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"}
                ]
            }
        ],
        "views": 5120000,
        "likes": 420000,
        "channel": {"name": "HBO Max", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100", "subscribers": "14.8M", "verified": True},
        "category": "Fantasy",
        "tags": ["house-of-the-dragon", "game-of-thrones", "dragons", "targaryen", "hbo"],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "ser-shogun",
        "title": "Shōgun",
        "subtitle": "Feudal Japan Historical Epic",
        "content_type": "series",
        "description": "When a mysterious European ship is found marooned in a nearby fishing village, Lord Yoshii Toranaga discovers secrets that could tip the scales of power in 1600s Japan.",
        "release_year": 2024,
        "age_rating": "TV-MA",
        "imdb_rating": 8.8,
        "quality": "4K ULTRA HD",
        "duration_seconds": 3600,
        "duration_formatted": "10 Episodes",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1528164344705-475426879c0d?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1528164344705-475426879c0d?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1528164344705-475426879c0d?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {"episode_number": 1, "title": "Chapter One: Anjin", "duration": "1h 10m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": "https://images.unsplash.com/photo-1528164344705-475426879c0d?w=400"},
                    {"episode_number": 2, "title": "Chapter Two: Servants of Two Masters", "duration": "58m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
                    {"episode_number": 3, "title": "Chapter Three: Tomorrow is Tomorrow", "duration": "56m", "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4", "thumbnail": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=400"}
                ]
            }
        ],
        "views": 3980000,
        "likes": 341000,
        "channel": {"name": "FX Productions", "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100", "subscribers": "4.2M", "verified": True},
        "category": "Drama",
        "tags": ["shogun", "samurai", "japan", "history", "emmy-winner"],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "ser-the-last-of-us",
        "title": "The Last of Us",
        "subtitle": "Post-Apocalyptic Survival Odyssey",
        "content_type": "series",
        "description": "After a global fungal pandemic destroys civilization, a hardened survivor takes charge of a 14-year-old girl who may be humanity's last hope.",
        "release_year": 2023,
        "age_rating": "TV-MA",
        "imdb_rating": 8.8,
        "quality": "4K ULTRA HD",
        "duration_seconds": 3600,
        "duration_formatted": "9 Episodes",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {"episode_number": 1, "title": "When You're Lost in the Darkness", "duration": "1h 21m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"},
                    {"episode_number": 2, "title": "Infected", "duration": "53m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
                    {"episode_number": 3, "title": "Long, Long Time", "duration": "1h 16m", "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4", "thumbnail": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=400"}
                ]
            }
        ],
        "views": 4450000,
        "likes": 398000,
        "channel": {"name": "HBO Max", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100", "subscribers": "14.8M", "verified": True},
        "category": "Drama",
        "tags": ["the-last-of-us", "pedro-pascal", "bella-ramsey", "survival", "zombie"],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },

    # =========================================================================
    # 3. HIT ANIME & 3D ANIMATION (Movibox & CineHD Top Anime Section)
    # =========================================================================
    {
        "id": "ani-solo-leveling",
        "title": "Solo Leveling",
        "subtitle": "Arise: Shadow Monarch Awakening",
        "content_type": "anime",
        "description": "In a world where hunters with supernatural powers battle deadly monsters, weak hunter Sung Jin-woo is on the brink of death when he receives a mysterious quest window that allows him to level up indefinitely.",
        "release_year": 2024,
        "age_rating": "TV-14",
        "imdb_rating": 8.5,
        "quality": "1080p HD",
        "duration_seconds": 1440,
        "duration_formatted": "12 Episodes",
        "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4"},
            {"id": "srv-2", "name": "Server 2 (Fast Mirror)", "url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {"episode_number": 1, "title": "I'm Used to It", "duration": "24m", "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4", "thumbnail": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=400"},
                    {"episode_number": 2, "title": "If I Had One More Chance", "duration": "24m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
                    {"episode_number": 3, "title": "It's Like a Quest", "duration": "24m", "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4", "thumbnail": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400"}
                ]
            }
        ],
        "views": 5890000,
        "likes": 612000,
        "channel": {"name": "A-1 Pictures", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100", "subscribers": "8.8M", "verified": True},
        "category": "Anime",
        "tags": ["solo-leveling", "sung-jinwoo", "anime", "action", "fantasy"],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "ani-demon-slayer",
        "title": "Demon Slayer: Kimetsu no Yaiba",
        "subtitle": "Hashira Training Arc",
        "content_type": "anime",
        "description": "A family is attacked by demons and only two members survive - Tanjiro and his sister Nezuko, who is turning into a demon. Tanjiro sets out on a dangerous quest to find a cure and avenge his family.",
        "release_year": 2024,
        "age_rating": "TV-14",
        "imdb_rating": 8.7,
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "4 Seasons",
        "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 4,
                "season_title": "Season 4: Hashira Training Arc",
                "episodes": [
                    {"episode_number": 1, "title": "To Defeat Muzan Kibutsuji", "duration": "48m", "video_url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4", "thumbnail": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400"},
                    {"episode_number": 2, "title": "Water Hashira Giyu Tomioka's Pain", "duration": "24m", "video_url": "https://archive.org/download/Sintel/sintel-2048-stereo.mp4", "thumbnail": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=400"}
                ]
            }
        ],
        "views": 7410000,
        "likes": 830000,
        "channel": {"name": "Ufotable", "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100", "subscribers": "12.4M", "verified": True},
        "category": "Anime",
        "tags": ["demon-slayer", "tanjiro", "nezuko", "ufotable", "anime"],
        "published_at": "2024",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    },
    {
        "id": "ani-attack-on-titan",
        "title": "Attack on Titan",
        "subtitle": "Shingeki no Kyojin: The Final Season",
        "content_type": "anime",
        "description": "After his hometown is destroyed and his mother is killed, young Eren Jaeger vows to cleanse the earth of the giant humanoid Titans that have brought humanity to the brink of extinction.",
        "release_year": 2023,
        "age_rating": "TV-MA",
        "imdb_rating": 9.1,
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "4 Seasons",
        "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 4,
                "season_title": "The Final Season",
                "episodes": [
                    {"episode_number": 1, "title": "The Other Side of the Sea", "duration": "24m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
                    {"episode_number": 2, "title": "Midnight Train", "duration": "24m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"}
                ]
            }
        ],
        "views": 8920000,
        "likes": 980000,
        "channel": {"name": "MAPPA / Wit Studio", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100", "subscribers": "15.1M", "verified": True},
        "category": "Anime",
        "tags": ["attack-on-titan", "eren-yeager", "titans", "mappa", "anime"],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "comments": []
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
        "quality": "1080p HD",
        "duration_seconds": 1500,
        "duration_formatted": "10 Episodes",
        "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
        "servers": [
            {"id": "srv-1", "name": "Server 1 (Cloud HD)", "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"}
        ],
        "thumbnail_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
        "backdrop_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600&auto=format&fit=crop&q=80",
        "subtitles": [{"label": "English [CC]", "srclang": "en", "src": "/static/subtitles/english.vtt"}],
        "seasons": [
            {
                "season_number": 1,
                "season_title": "Season 1",
                "episodes": [
                    {"episode_number": 1, "title": "City of Dreams", "duration": "24m", "video_url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4", "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400"},
                    {"episode_number": 2, "title": "Like a Boy", "duration": "24m", "video_url": "https://archive.org/download/Tears-of-Steel/tears_of_steel_720p.mp4", "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"}
                ]
            }
        ],
        "views": 4320000,
        "likes": 472000,
        "channel": {"name": "Studio Trigger", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100", "subscribers": "7.9M", "verified": True},
        "category": "Anime",
        "tags": ["cyberpunk", "edgerunners", "david-martinez", "lucy", "studio-trigger"],
        "published_at": "2023",
        "is_trending": True,
        "is_featured": False,
        "comments": []
    }
]

def get_hero_featured() -> Dict[str, Any]:
    """Returns top featured blockbuster for the Cinematic Hero Billboard."""
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
