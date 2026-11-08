/**
 * StreamGuard Application Logic
 * Integrates:
 * 1. On-Demand Cinema Video Player (YouTube + Netflix + Twitch features)
 * 2. 24/7 Global Live TV Broadcasting via Built-in Self-Gateway Proxy (In-App Tunnel)
 * 3. Autonomous Multi-Layer Security WAF Telemetry
 */

// Application State
const state = {
  viewMode: "videos", // "videos" | "livetv"
  videos: [],
  currentVideo: null,
  currentIndex: 0,
  
  // Live TV State
  channels: [],
  currentChannel: null,
  channelIndex: 0,
  hlsInstance: null,

  isPlaying: false,
  isMuted: false,
  volume: 1.0,
  playbackSpeed: 1.0,
  isTheater: false,
  autoplayNext: true,
  activeCategory: "All",
  searchQuery: ""
};

// DOM Elements
const videoEl = document.getElementById("videoElement");
const playerContainer = document.getElementById("playerContainer");
const mainLayout = document.getElementById("mainLayout");
const playBtn = document.getElementById("playBtn");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const centerPlayOverlay = document.getElementById("centerPlayOverlay");
const muteBtn = document.getElementById("muteBtn");
const volumeSlider = document.getElementById("volumeSlider");
const currentTimeEl = document.getElementById("currentTime");
const totalDurationEl = document.getElementById("totalDuration");
const scrubberWrapper = document.getElementById("scrubberWrapper");
const scrubberProgress = document.getElementById("scrubberProgress");
const bufferProgress = document.getElementById("bufferProgress");
const scrubberThumb = document.getElementById("scrubberThumb");
const scrubberPreview = document.getElementById("scrubberPreview");
const previewTimeEl = document.getElementById("previewTime");
const speedBtn = document.getElementById("speedBtn");
const speedLabel = document.getElementById("speedLabel");
const speedMenu = document.getElementById("speedMenu");
const speedWrapper = document.getElementById("speedWrapper");
const theaterBtn = document.getElementById("theaterBtn");
const pipBtn = document.getElementById("pipBtn");
const fullscreenBtn = document.getElementById("fullscreenBtn");
const autoplayCheck = document.getElementById("autoplayCheck");
const autoplayToggleWrap = document.getElementById("autoplayToggleWrap");
const liveIndicatorTag = document.getElementById("liveIndicatorTag");
const qualityBadge = document.getElementById("qualityBadge");
const qualityText = document.getElementById("qualityText");

// Mode Tabs
const tabVideosMode = document.getElementById("tabVideosMode");
const tabLiveTvMode = document.getElementById("tabLiveTvMode");
const categoryBar = document.getElementById("categoryBar");
const sidebarTitle = document.getElementById("sidebarTitle");

// Metadata elements
const videoTitleEl = document.getElementById("videoTitle");
const videoDescEl = document.getElementById("videoDescription");
const channelAvatarEl = document.getElementById("channelAvatar");
const channelNameEl = document.getElementById("channelName");
const channelSubsEl = document.getElementById("channelSubs");
const channelFlagBadge = document.getElementById("channelFlagBadge");
const likeBtn = document.getElementById("likeBtn");
const likeCountEl = document.getElementById("likeCount");
const shareBtn = document.getElementById("shareBtn");
const downloadBtn = document.getElementById("downloadBtn");
const downloadBtnLabel = document.getElementById("downloadBtnLabel");
const viewCountEl = document.getElementById("viewCount");
const publishDateEl = document.getElementById("publishDate");
const tagsRowEl = document.getElementById("tagsRow");
const queueListEl = document.getElementById("queueList");
const commentsSection = document.getElementById("commentsSection");
const commentsListEl = document.getElementById("commentsList");
const commentsCountEl = document.getElementById("commentsCount");
const submitCommentBtn = document.getElementById("submitCommentBtn");
const commentAuthorInput = document.getElementById("commentAuthor");
const commentTextInput = document.getElementById("commentText");

// Search
const searchInput = document.getElementById("searchInput");
const clearSearchBtn = document.getElementById("clearSearchBtn");

// Security indicators
const headerThreatCount = document.getElementById("headerThreatCount");
const sbHits = document.getElementById("sbHits");
const sbThreats = document.getElementById("sbThreats");

// Modals
const shortcutsModal = document.getElementById("shortcutsModal");
const shortcutsBtn = document.getElementById("shortcutsBtn");
const closeModalBtn = document.getElementById("closeModalBtn");

// ----------------------------------------------------------------------------
// Initialization
// ----------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", async () => {
  setupEventListeners();
  renderCategoryBar();
  await loadVideoCatalog();
  await updateSecurityTelemetry();
  setInterval(updateSecurityTelemetry, 5000);
});

function formatTime(seconds) {
  if (isNaN(seconds) || seconds < 0) return "00:00";
  const s = Math.floor(seconds % 60);
  const m = Math.floor((seconds / 60) % 60);
  const h = Math.floor(seconds / 3600);
  const pad = (n) => String(n).padStart(2, "0");
  return h > 0 ? `${h}:${pad(m)}:${pad(s)}` : `${pad(m)}:${pad(s)}`;
}

// ----------------------------------------------------------------------------
// Mode Switching: Cinema Videos vs Global Live TV
// ----------------------------------------------------------------------------
function setViewMode(mode) {
  if (state.viewMode === mode) return;
  state.viewMode = mode;
  state.activeCategory = "All";
  state.searchQuery = "";
  searchInput.value = "";
  clearSearchBtn.style.display = "none";

  tabVideosMode.classList.toggle("active", mode === "videos");
  tabLiveTvMode.classList.toggle("active", mode === "livetv");

  renderCategoryBar();

  if (mode === "videos") {
    sidebarTitle.innerHTML = '<i class="fa-solid fa-layer-group"></i> Up Next & Recommendations';
    liveIndicatorTag.style.display = "none";
    channelFlagBadge.style.display = "none";
    scrubberWrapper.style.display = "flex";
    speedWrapper.style.display = "block";
    autoplayToggleWrap.style.display = "flex";
    downloadBtnLabel.textContent = "Download";
    commentsSection.style.display = "block";
    destroyHls();
    loadVideoCatalog();
    showToast("Switched to Cinema & On-Demand Library");
  } else {
    sidebarTitle.innerHTML = '<i class="fa-solid fa-satellite-dish" style="color:#ef4444;"></i> Global Live TV Broadcasts';
    liveIndicatorTag.style.display = "flex";
    channelFlagBadge.style.display = "inline-block";
    scrubberWrapper.style.display = "none"; // Live streams use DVR/live indicator
    speedWrapper.style.display = "none";
    autoplayToggleWrap.style.display = "none";
    downloadBtnLabel.textContent = "Raw Stream";
    commentsSection.style.display = "block";
    loadLiveChannels();
    showToast("🔴 Live TV Global activated via Built-in Self-Gateway Tunnel");
  }
}

function renderCategoryBar() {
  categoryBar.innerHTML = "";
  let categories = [];

  if (state.viewMode === "videos") {
    categories = ["All", "Sci-Fi", "Animation", "Nature", "Trending"];
  } else {
    categories = [
      "All",
      "World News",
      "Science & Space",
      "Sports & Adventure",
      "Finance & Business",
      "Entertainment & Cinema",
      "United States",
      "Germany",
      "Turkey",
      "China"
    ];
  }

  categories.forEach((cat) => {
    const btn = document.createElement("button");
    btn.className = `category-pill ${state.activeCategory === cat ? "active" : ""}`;
    btn.textContent = cat;
    btn.addEventListener("click", () => {
      document.querySelectorAll(".category-pill").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      state.activeCategory = cat;
      if (state.viewMode === "videos") {
        loadVideoCatalog();
      } else {
        loadLiveChannels();
      }
    });
    categoryBar.appendChild(btn);
  });
}

// ----------------------------------------------------------------------------
// Video Catalog API (On-Demand Mode)
// ----------------------------------------------------------------------------
async function loadVideoCatalog() {
  try {
    let url = `/api/videos?category=${encodeURIComponent(state.activeCategory)}`;
    if (state.searchQuery) {
      url += `&search=${encodeURIComponent(state.searchQuery)}`;
    }
    const res = await fetch(url);
    const data = await res.json();
    state.videos = data.videos || [];

    if (state.videos.length > 0) {
      renderQueueList();
      if (!state.currentVideo || state.viewMode !== "videos") {
        selectVideo(state.videos[0].id);
      }
    } else {
      queueListEl.innerHTML = '<div style="color:#64748b; padding:20px; text-align:center;">No videos match your filter.</div>';
    }
  } catch (err) {
    console.error("Error loading video catalog:", err);
  }
}

async function selectVideo(videoId, shouldPlay = false) {
  try {
    destroyHls();
    const res = await fetch(`/api/videos/${videoId}`);
    const data = await res.json();
    state.currentVideo = data.video;
    state.currentIndex = state.videos.findIndex((v) => v.id === videoId);

    // Update HTML5 Video element
    videoEl.src = state.currentVideo.video_url;
    videoEl.load();

    // Update Metadata
    videoTitleEl.textContent = state.currentVideo.title;
    videoDescEl.textContent = state.currentVideo.description;
    channelAvatarEl.src = state.currentVideo.channel.avatar;
    channelNameEl.textContent = state.currentVideo.channel.name;
    channelSubsEl.textContent = `${state.currentVideo.channel.subscribers} subscribers`;
    likeCountEl.textContent = state.currentVideo.likes.toLocaleString();
    viewCountEl.textContent = `${state.currentVideo.views.toLocaleString()} views`;
    publishDateEl.textContent = state.currentVideo.published_at;
    qualityText.textContent = "1080p HD";

    // Render tags
    tagsRowEl.innerHTML = (state.currentVideo.tags || [])
      .map((t) => `<span class="video-tag">#${t}</span>`)
      .join(" ");

    // Render comments
    renderComments(state.currentVideo.comments || []);
    renderQueueList();

    if (shouldPlay) {
      videoEl.play().catch(() => {});
    }
  } catch (err) {
    console.error("Error selecting video:", err);
  }
}

function renderQueueList() {
  if (!state.videos || state.videos.length === 0) return;

  queueListEl.innerHTML = state.videos
    .map((vid) => {
      const isCurrent = state.currentVideo && state.currentVideo.id === vid.id;
      return `
        <div class="queue-card ${isCurrent ? "active" : ""}" onclick="selectVideo('${vid.id}', true)">
          <div class="thumb-wrap">
            <img src="${vid.thumbnail_url}" alt="${vid.title}">
            <span class="duration-tag">${vid.duration_formatted}</span>
          </div>
          <div class="queue-info">
            <h4 class="queue-title">${vid.title}</h4>
            <span class="queue-channel">${vid.channel.name}</span>
            <span class="queue-stats">${vid.views.toLocaleString()} views • ${vid.category}</span>
          </div>
        </div>
      `;
    })
    .join("");
}

// ----------------------------------------------------------------------------
// Global Live TV API & HLS Streaming (Live TV Mode via Self-Gateway)
// ----------------------------------------------------------------------------
async function loadLiveChannels() {
  try {
    let url = "/api/live/channels";
    const params = new URLSearchParams();

    if (state.activeCategory !== "All") {
      // Check if active category is a country or category
      if (["United States", "Germany", "Turkey", "China"].includes(state.activeCategory)) {
        params.append("country", state.activeCategory);
      } else {
        params.append("category", state.activeCategory);
      }
    }
    if (state.searchQuery) {
      params.append("search", state.searchQuery);
    }

    if (params.toString()) {
      url += `?${params.toString()}`;
    }

    const res = await fetch(url);
    const data = await res.json();
    state.channels = data.channels || [];

    if (state.channels.length > 0) {
      renderLiveChannelList();
      if (!state.currentChannel || state.viewMode !== "livetv") {
        selectLiveChannel(state.channels[0].id, false);
      }
    } else {
      queueListEl.innerHTML = '<div style="color:#64748b; padding:20px; text-align:center;">No live TV channels match your filter.</div>';
    }
  } catch (err) {
    console.error("Error loading live channels:", err);
  }
}

async function selectLiveChannel(channelId, shouldPlay = true) {
  try {
    const res = await fetch(`/api/live/channels/${channelId}`);
    const data = await res.json();
    state.currentChannel = data.channel;
    state.channelIndex = state.channels.findIndex((c) => c.id === channelId);

    // Update Channel UI Metadata
    videoTitleEl.innerHTML = `<span style="color:#ef4444; margin-right:8px;"><i class="fa-solid fa-satellite-dish"></i></span> ${state.currentChannel.name}`;
    videoDescEl.textContent = state.currentChannel.description;
    channelAvatarEl.src = state.currentChannel.logo;
    channelNameEl.textContent = state.currentChannel.name;
    channelSubsEl.textContent = `${state.currentChannel.category} • ${state.currentChannel.country}`;
    channelFlagBadge.textContent = state.currentChannel.flag;
    channelFlagBadge.style.display = "inline-block";
    viewCountEl.innerHTML = `<span style="color:#ef4444; font-weight:bold;">● LIVE</span> ${state.currentChannel.views}`;
    publishDateEl.textContent = "Broadcasting Now";
    qualityText.textContent = state.currentChannel.resolution || "1080p HD";

    tagsRowEl.innerHTML = `
      <span class="video-tag">${state.currentChannel.flag} ${state.currentChannel.country}</span>
      <span class="video-tag">#${state.currentChannel.category}</span>
      <span class="video-tag" style="color:#38bdf8;"><i class="fa-solid fa-shield"></i> Self-Gateway Relayed</span>
    `;

    renderLiveComments();
    renderLiveChannelList();

    // Stream via In-App Self-Gateway Proxy
    playLiveStreamHls(state.currentChannel.gateway_url, shouldPlay);
    showToast(`Streaming ${state.currentChannel.name} via Self-Gateway Tunnel`);
  } catch (err) {
    console.error("Error playing live channel:", err);
  }
}

function renderLiveChannelList() {
  if (!state.channels || state.channels.length === 0) return;

  queueListEl.innerHTML = state.channels
    .map((ch) => {
      const isCurrent = state.currentChannel && state.currentChannel.id === ch.id;
      return `
        <div class="channel-card ${isCurrent ? "active" : ""}" onclick="selectLiveChannel('${ch.id}', true)">
          <div class="channel-thumb">
            <img src="${ch.logo}" alt="${ch.name}">
            <span class="channel-live-dot"></span>
          </div>
          <div class="channel-meta">
            <div class="channel-title-row">
              <span class="channel-name">${ch.flag} ${ch.name}</span>
            </div>
            <span class="channel-country-badge">${ch.country} • ${ch.category}</span>
            <div class="channel-cat-row">
              <span>${ch.views}</span>
              <span class="gateway-secured-icon"><i class="fa-solid fa-shield-halved"></i> Self-Proxy</span>
            </div>
          </div>
        </div>
      `;
    })
    .join("");
}

function playLiveStreamHls(streamUrl, shouldPlay = true) {
  destroyHls();

  if (Hls.isSupported()) {
    state.hlsInstance = new Hls({
      enableWorker: true,
      lowLatencyMode: true,
      backBufferLength: 90
    });

    state.hlsInstance.loadSource(streamUrl);
    state.hlsInstance.attachMedia(videoEl);

    state.hlsInstance.on(Hls.Events.MANIFEST_PARSED, () => {
      currentTimeEl.textContent = "LIVE";
      totalDurationEl.textContent = "LIVE";
      if (shouldPlay) {
        videoEl.play().catch(() => {});
      }
    });

    state.hlsInstance.on(Hls.Events.ERROR, (event, data) => {
      if (data.fatal) {
        switch (data.type) {
          case Hls.ErrorTypes.NETWORK_ERROR:
            state.hlsInstance.startLoad();
            break;
          case Hls.ErrorTypes.MEDIA_ERROR:
            state.hlsInstance.recoverMediaError();
            break;
          default:
            destroyHls();
            break;
        }
      }
    });
  } else if (videoEl.canPlayType("application/vnd.apple.mpegurl")) {
    // Native HLS for Safari/iOS
    videoEl.src = streamUrl;
    if (shouldPlay) {
      videoEl.play().catch(() => {});
    }
  }
}

function destroyHls() {
  if (state.hlsInstance) {
    state.hlsInstance.destroy();
    state.hlsInstance = null;
  }
}

function renderLiveComments() {
  commentsCountEl.textContent = "2.4K";
  const liveMockReactions = [
    { author: "GlobalViewer_99", text: "The stream resolution through the self-gateway proxy is razor sharp!", time: "Just now" },
    { author: "OrbitWatch", text: "Watching the live feed from Sydney! Zero buffering.", time: "1 min ago" },
    { author: "EurasiaStream", text: "Incredible broadcast stability. No external VPN required.", time: "3 mins ago" }
  ];

  commentsListEl.innerHTML = liveMockReactions
    .map((c) => `
      <div class="comment-item">
        <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&auto=format&fit=crop&q=80" alt="${c.author}" class="comment-avatar">
        <div class="comment-body">
          <div class="comment-meta">
            <span class="comment-author">${c.author}</span>
            <span class="comment-time">${c.time}</span>
          </div>
          <div class="comment-content">${c.text}</div>
        </div>
      </div>
    `)
    .join("");
}

function renderComments(comments) {
  commentsCountEl.textContent = comments.length;
  if (comments.length === 0) {
    commentsListEl.innerHTML = '<div style="color:#64748b; font-size:13px;">No comments yet. Start the conversation!</div>';
    return;
  }

  commentsListEl.innerHTML = comments
    .map((c) => `
      <div class="comment-item">
        <img src="${c.avatar}" alt="${c.author}" class="comment-avatar">
        <div class="comment-body">
          <div class="comment-meta">
            <span class="comment-author">${c.author}</span>
            <span class="comment-time">${c.timestamp}</span>
          </div>
          <div class="comment-content">${c.text}</div>
        </div>
      </div>
    `)
    .join("");
}

// ----------------------------------------------------------------------------
// Custom Video Player Controls
// ----------------------------------------------------------------------------
function togglePlay() {
  if (videoEl.paused || videoEl.ended) {
    videoEl.play();
  } else {
    videoEl.pause();
  }
}

function updatePlayButton() {
  if (videoEl.paused) {
    playBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
    playerContainer.classList.add("paused");
  } else {
    playBtn.innerHTML = '<i class="fa-solid fa-pause"></i>';
    playerContainer.classList.remove("paused");
  }
}

function flashCenterOverlay(iconClass) {
  centerPlayOverlay.innerHTML = `<i class="fa-solid ${iconClass}"></i>`;
  centerPlayOverlay.classList.add("show");
  setTimeout(() => centerPlayOverlay.classList.remove("show"), 400);
}

function updateTimeline() {
  if (state.viewMode === "livetv") {
    currentTimeEl.textContent = "LIVE";
    totalDurationEl.textContent = "LIVE";
    return;
  }

  if (!videoEl.duration) return;
  const current = videoEl.currentTime;
  const total = videoEl.duration;
  const pct = (current / total) * 100;

  scrubberProgress.style.width = `${pct}%`;
  scrubberThumb.style.left = `${pct}%`;
  currentTimeEl.textContent = formatTime(current);
  totalDurationEl.textContent = formatTime(total);

  if (videoEl.buffered.length > 0) {
    const bufferedEnd = videoEl.buffered.end(videoEl.buffered.length - 1);
    const bufPct = (bufferedEnd / total) * 100;
    bufferProgress.style.width = `${bufPct}%`;
  }
}

function seekTimeline(e) {
  if (state.viewMode === "livetv") return;
  const rect = scrubberWrapper.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, clickX / rect.width));
  videoEl.currentTime = pct * videoEl.duration;
}

function updateHoverPreview(e) {
  if (state.viewMode === "livetv") return;
  const rect = scrubberWrapper.getBoundingClientRect();
  const hoverX = e.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, hoverX / rect.width));
  const hoverTime = pct * (videoEl.duration || 0);

  scrubberPreview.style.left = `${hoverX}px`;
  scrubberPreview.style.opacity = "1";
  previewTimeEl.textContent = formatTime(hoverTime);
}

function hideHoverPreview() {
  scrubberPreview.style.opacity = "0";
}

function setVolume(val) {
  state.volume = parseFloat(val);
  videoEl.volume = state.volume;
  videoEl.muted = state.volume === 0;
  updateVolumeIcon();
}

function toggleMute() {
  videoEl.muted = !videoEl.muted;
  updateVolumeIcon();
}

function updateVolumeIcon() {
  if (videoEl.muted || videoEl.volume === 0) {
    muteBtn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
    volumeSlider.value = 0;
  } else if (videoEl.volume > 0.5) {
    muteBtn.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
    volumeSlider.value = videoEl.volume;
  } else {
    muteBtn.innerHTML = '<i class="fa-solid fa-volume-low"></i>';
    volumeSlider.value = videoEl.volume;
  }
}

function setPlaybackSpeed(speed) {
  state.playbackSpeed = speed;
  videoEl.playbackRate = speed;
  speedLabel.textContent = speed === 1.0 ? "1x" : `${speed}x`;
  document.querySelectorAll(".speed-opt").forEach((btn) => {
    btn.classList.toggle("active", parseFloat(btn.dataset.speed) === speed);
  });
  speedMenu.classList.remove("show");
  showToast(`Playback speed set to ${speed}x`);
}

function toggleTheaterMode() {
  state.isTheater = !state.isTheater;
  mainLayout.classList.toggle("theater-active", state.isTheater);
  theaterBtn.style.color = state.isTheater ? "var(--accent-cyan)" : "#fff";
  showToast(state.isTheater ? "Theater Mode: Enabled" : "Theater Mode: Normal");
}

async function togglePiP() {
  try {
    if (document.pictureInPictureElement) {
      await document.exitPictureInPicture();
    } else if (videoEl !== document.pictureInPictureElement) {
      await videoEl.requestPictureInPicture();
    }
  } catch (err) {
    showToast("Picture-in-Picture not supported in this view.");
  }
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    if (playerContainer.requestFullscreen) {
      playerContainer.requestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}

function playNextItem() {
  if (state.viewMode === "videos") {
    if (state.videos.length === 0) return;
    const nextIdx = (state.currentIndex + 1) % state.videos.length;
    selectVideo(state.videos[nextIdx].id, true);
    showToast(`Playing next: ${state.videos[nextIdx].title}`);
  } else {
    if (state.channels.length === 0) return;
    const nextCh = (state.channelIndex + 1) % state.channels.length;
    selectLiveChannel(state.channels[nextCh].id, true);
  }
}

function playPrevItem() {
  if (state.viewMode === "videos") {
    if (state.videos.length === 0) return;
    const prevIdx = (state.currentIndex - 1 + state.videos.length) % state.videos.length;
    selectVideo(state.videos[prevIdx].id, true);
  } else {
    if (state.channels.length === 0) return;
    const prevCh = (state.channelIndex - 1 + state.channels.length) % state.channels.length;
    selectLiveChannel(state.channels[prevCh].id, true);
  }
}

// ----------------------------------------------------------------------------
// Comment Submission with Defensive Security
// ----------------------------------------------------------------------------
async function submitComment() {
  const author = commentAuthorInput.value.trim() || "Viewer";
  const text = commentTextInput.value.trim();
  if (!text) return;

  if (state.viewMode === "videos") {
    if (!state.currentVideo) return;
    try {
      const res = await fetch(`/api/videos/${state.currentVideo.id}/comment`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ author, text })
      });

      if (res.status === 403) {
        const err = await res.json();
        alert(`🛡️ StreamGuard Autonomous Shield Intercepted Threat!\nType: ${err.threat_classification}\nLogged to threat_locations.log`);
        return;
      }

      const data = await res.json();
      if (data.status === "success") {
        state.currentVideo.comments.unshift(data.comment);
        renderComments(state.currentVideo.comments);
        commentTextInput.value = "";
        showToast("Comment published securely.");
      }
    } catch (err) {
      console.error("Error submitting comment:", err);
    }
  } else {
    // Live stream reaction
    const newComment = {
      author,
      text,
      timestamp: "Just now",
      avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80"
    };
    const div = document.createElement("div");
    div.className = "comment-item";
    div.innerHTML = `
      <img src="${newComment.avatar}" class="comment-avatar">
      <div class="comment-body">
        <div class="comment-meta">
          <span class="comment-author">${newComment.author}</span>
          <span class="comment-time">${newComment.timestamp}</span>
        </div>
        <div class="comment-content">${newComment.text}</div>
      </div>
    `;
    commentsListEl.prepend(div);
    commentTextInput.value = "";
    showToast("Live reaction sent.");
  }
}

// ----------------------------------------------------------------------------
// Like, Share & Download
// ----------------------------------------------------------------------------
async function likeVideo() {
  if (state.viewMode === "videos" && state.currentVideo) {
    try {
      const res = await fetch(`/api/videos/${state.currentVideo.id}/like`, { method: "POST" });
      const data = await res.json();
      likeCountEl.textContent = data.likes.toLocaleString();
      likeBtn.style.color = "var(--accent-cyan)";
      showToast("Liked video!");
    } catch (err) {
      console.error("Error liking video:", err);
    }
  } else {
    showToast("Liked live channel stream!");
    likeBtn.style.color = "#ef4444";
  }
}

function shareVideo() {
  navigator.clipboard.writeText(window.location.href);
  showToast("Stream link copied to clipboard!");
}

function downloadOrSource() {
  if (state.viewMode === "videos" && state.currentVideo) {
    window.open(state.currentVideo.video_url, "_blank");
  } else if (state.currentChannel) {
    window.open(state.currentChannel.stream_url, "_blank");
  }
}

// ----------------------------------------------------------------------------
// Telemetry & Defense Poller
// ----------------------------------------------------------------------------
async function updateSecurityTelemetry() {
  try {
    const res = await fetch("/api/security/stats");
    const data = await res.json();
    if (data && data.metrics) {
      headerThreatCount.textContent = data.metrics.attacks_blocked;
      sbHits.textContent = data.metrics.total_hits;
      sbThreats.textContent = data.metrics.attacks_blocked;
    }
  } catch (err) {
    // Graceful offline fallback
  }
}

function showToast(msg) {
  const container = document.getElementById("toastContainer");
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `<i class="fa-solid fa-circle-info" style="color:var(--accent-cyan); margin-right:8px;"></i>${msg}`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = "0";
    setTimeout(() => toast.remove(), 300);
  }, 2500);
}

// ----------------------------------------------------------------------------
// Event Listeners
// ----------------------------------------------------------------------------
function setupEventListeners() {
  // Mode switcher tabs
  tabVideosMode.addEventListener("click", () => setViewMode("videos"));
  tabLiveTvMode.addEventListener("click", () => setViewMode("livetv"));

  // Video playback
  videoEl.addEventListener("click", () => {
    togglePlay();
    flashCenterOverlay(videoEl.paused ? "fa-pause" : "fa-play");
  });
  videoEl.addEventListener("play", updatePlayButton);
  videoEl.addEventListener("pause", updatePlayButton);
  videoEl.addEventListener("timeupdate", updateTimeline);
  videoEl.addEventListener("ended", () => {
    if (autoplayCheck.checked && state.viewMode === "videos") {
      playNextItem();
    }
  });

  playBtn.addEventListener("click", togglePlay);
  prevBtn.addEventListener("click", playPrevItem);
  nextBtn.addEventListener("click", playNextItem);

  // Scrubber events
  scrubberWrapper.addEventListener("click", seekTimeline);
  scrubberWrapper.addEventListener("mousemove", updateHoverPreview);
  scrubberWrapper.addEventListener("mouseleave", hideHoverPreview);

  // Volume
  muteBtn.addEventListener("click", toggleMute);
  volumeSlider.addEventListener("input", (e) => setVolume(e.target.value));

  // Speed dropdown
  speedBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    speedMenu.classList.toggle("show");
  });
  document.addEventListener("click", () => speedMenu.classList.remove("show"));
  document.querySelectorAll(".speed-opt").forEach((btn) => {
    btn.addEventListener("click", () => setPlaybackSpeed(parseFloat(btn.dataset.speed)));
  });

  // Display toggles
  theaterBtn.addEventListener("click", toggleTheaterMode);
  pipBtn.addEventListener("click", togglePiP);
  fullscreenBtn.addEventListener("click", toggleFullscreen);

  // Meta actions
  likeBtn.addEventListener("click", likeVideo);
  shareBtn.addEventListener("click", shareVideo);
  downloadBtn.addEventListener("click", downloadOrSource);
  submitCommentBtn.addEventListener("click", submitComment);

  // Search input
  searchInput.addEventListener("input", (e) => {
    state.searchQuery = e.target.value;
    clearSearchBtn.style.display = state.searchQuery ? "block" : "none";
    if (state.viewMode === "videos") {
      loadVideoCatalog();
    } else {
      loadLiveChannels();
    }
  });

  clearSearchBtn.addEventListener("click", () => {
    searchInput.value = "";
    state.searchQuery = "";
    clearSearchBtn.style.display = "none";
    if (state.viewMode === "videos") {
      loadVideoCatalog();
    } else {
      loadLiveChannels();
    }
  });

  // Shortcuts modal
  shortcutsBtn.addEventListener("click", () => (shortcutsModal.style.display = "flex"));
  closeModalBtn.addEventListener("click", () => (shortcutsModal.style.display = "none"));
  shortcutsModal.addEventListener("click", (e) => {
    if (e.target === shortcutsModal) shortcutsModal.style.display = "none";
  });

  // Hotkeys
  document.addEventListener("keydown", (e) => {
    if (["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;

    switch (e.key.toLowerCase()) {
      case " ":
      case "k":
        e.preventDefault();
        togglePlay();
        flashCenterOverlay(videoEl.paused ? "fa-pause" : "fa-play");
        break;
      case "j":
        if (state.viewMode === "videos") {
          e.preventDefault();
          videoEl.currentTime = Math.max(0, videoEl.currentTime - 10);
          showToast("Seek -10s");
        }
        break;
      case "l":
        if (state.viewMode === "videos") {
          e.preventDefault();
          videoEl.currentTime = Math.min(videoEl.duration, videoEl.currentTime + 10);
          showToast("Seek +10s");
        }
        break;
      case "m":
        e.preventDefault();
        toggleMute();
        break;
      case "f":
        e.preventDefault();
        toggleFullscreen();
        break;
      case "t":
        e.preventDefault();
        toggleTheaterMode();
        break;
      case "?":
        e.preventDefault();
        shortcutsModal.style.display = shortcutsModal.style.display === "none" ? "flex" : "none";
        break;
      default:
        if (state.viewMode === "videos" && e.key >= "0" && e.key <= "9" && videoEl.duration) {
          const pct = parseInt(e.key, 10) / 10;
          videoEl.currentTime = pct * videoEl.duration;
          showToast(`Jumped to ${pct * 100}%`);
        }
        break;
    }
  });
}

// ----------------------------------------------------------------------------
// Legal Disclaimers Modal Logic
// ----------------------------------------------------------------------------
const legalModal = document.getElementById("legalModal");
const closeLegalModalBtn = document.getElementById("closeLegalModalBtn");

function openLegalModal(tabId = "legal-dmca") {
  if (!legalModal) return;
  legalModal.style.display = "flex";
  switchLegalTab(tabId);
}

function switchLegalTab(tabId) {
  document.querySelectorAll(".legal-tab-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.tab === tabId);
  });
  document.querySelectorAll(".legal-panel").forEach((p) => {
    p.classList.toggle("active", p.id === tabId);
  });
}

if (closeLegalModalBtn) {
  closeLegalModalBtn.addEventListener("click", () => {
    legalModal.style.display = "none";
  });
}

if (legalModal) {
  legalModal.addEventListener("click", (e) => {
    if (e.target === legalModal) legalModal.style.display = "none";
  });
  document.querySelectorAll(".legal-tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => switchLegalTab(btn.dataset.tab));
  });
}
