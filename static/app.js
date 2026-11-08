/**
 * StreamGuard 2.0 - OTT Cinema, TV Series, Anime & Global Live TV Controller
 * Incorporates Movibox & CineHD UI/UX Patterns with Autonomous Security Shield
 */

// ----------------------------------------------------------------------------
// StreamGuard Anti-Popup & Anti-Clickjack Shield
// Neutralizes rogue window.open and clickjack redirects from third-party embeds
// ----------------------------------------------------------------------------
window.open = function(url, target, features) {
  console.warn("[StreamGuard AdBlock Shield] Intercepted and blocked rogue popup attempt:", url);
  return null;
};

document.addEventListener("click", function(e) {
  const anchor = e.target.closest("a");
  if (anchor) {
    if (anchor.hasAttribute("download")) {
      e.preventDefault();
      e.stopPropagation();
      console.warn("[StreamGuard AdBlock Shield] Blocked unapproved automatic download link.");
      return;
    }
    if (anchor.target === "_blank") {
      const href = anchor.getAttribute("href") || "";
      const isSafe = href.includes("github.com") || href.includes("twitter.com") || href.includes("whatsapp.com") || href.includes("render.com");
      if (!isSafe && (href.startsWith("javascript:") || href === "#" || href.includes("http"))) {
        e.preventDefault();
        e.stopPropagation();
        console.warn("[StreamGuard AdBlock Shield] Blocked unauthorized new tab clickjack:", href);
      }
    }
  }
}, true);

// ----------------------------------------------------------------------------
// Global Application State
// ----------------------------------------------------------------------------
const state = {
  viewMode: "all", // all | movie | series | anime | livetv | watchlist
  allVideos: [],
  channels: [],
  currentVideo: null,
  currentChannel: null,
  currentServerIndex: 0,
  featuredItem: null,
  hlsInstance: null,
  subtitlesActive: true,
  searchQuery: "",
  partyRoomCode: null,
  history: JSON.parse(localStorage.getItem("streamguard_history") || "{}"),
  watchlist: JSON.parse(localStorage.getItem("streamguard_watchlist") || "[]")
};

// ----------------------------------------------------------------------------
// DOM Elements
// ----------------------------------------------------------------------------
const heroBillboard = document.getElementById("heroBillboard");
const heroTitle = document.getElementById("heroTitle");
const heroSubtitle = document.getElementById("heroSubtitle");
const heroDesc = document.getElementById("heroDesc");
const heroBackdrop = document.getElementById("heroBackdrop");
const heroQuality = document.getElementById("heroQuality");
const heroRating = document.getElementById("heroRating");
const heroYear = document.getElementById("heroYear");
const heroAge = document.getElementById("heroAge");
const heroPlayBtn = document.getElementById("heroPlayBtn");
const heroWatchlistBtn = document.getElementById("heroWatchlistBtn");
const heroWatchlistText = document.getElementById("heroWatchlistText");
const heroPartyBtn = document.getElementById("heroPartyBtn");

const theaterSection = document.getElementById("theaterSection");
const activePlayerTitle = document.getElementById("activePlayerTitle");
const channelFlagBadge = document.getElementById("channelFlagBadge");
const closePlayerBtn = document.getElementById("closePlayerBtn");
const serverSelectBtn = document.getElementById("serverSelectBtn");
const currentServerLabel = document.getElementById("currentServerLabel");
const serverMenu = document.getElementById("serverMenu");

const playerContainer = document.getElementById("playerContainer");
const videoEl = document.getElementById("videoElement");
const embedPlayerFrame = document.getElementById("embedPlayerFrame");
const playerControls = document.getElementById("playerControls");
const subtitleTrack = document.getElementById("subtitleTrack");
const liveIndicatorTag = document.getElementById("liveIndicatorTag");
const centerPlayOverlay = document.getElementById("centerPlayOverlay");

// Pre-Roll Video Advertisement Overlay Elements
const prerollAdOverlay = document.getElementById("prerollAdOverlay");
const adVideoElement = document.getElementById("adVideoElement");
const adSponsorName = document.getElementById("adSponsorName");
const adTimeBadge = document.getElementById("adTimeBadge");
const adHeadline = document.getElementById("adHeadline");
const skipAdBtn = document.getElementById("skipAdBtn");
const skipBtnText = document.getElementById("skipBtnText");
const adProgressFill = document.getElementById("adProgressFill");

const playBtn = document.getElementById("playBtn");
const skipBack10 = document.getElementById("skipBack10");
const skipForward10 = document.getElementById("skipForward10");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const muteBtn = document.getElementById("muteBtn");
const volumeSlider = document.getElementById("volumeSlider");
const currentTimeEl = document.getElementById("currentTime");
const totalDurationEl = document.getElementById("totalDuration");
const scrubberWrapper = document.getElementById("scrubberWrapper");
const scrubberBar = document.getElementById("scrubberBar");
const bufferProgress = document.getElementById("bufferProgress");
const scrubberProgress = document.getElementById("scrubberProgress");
const scrubberThumb = document.getElementById("scrubberThumb");
const scrubberPreview = document.getElementById("scrubberPreview");
const previewTimeEl = document.getElementById("previewTime");

const ccToggleBtn = document.getElementById("ccToggleBtn");
const ccStatusText = document.getElementById("ccStatusText");
const speedBtn = document.getElementById("speedBtn");
const speedLabel = document.getElementById("speedLabel");
const speedMenu = document.getElementById("speedMenu");
const qualityText = document.getElementById("qualityText");
const theaterBtn = document.getElementById("theaterBtn");
const pipBtn = document.getElementById("pipBtn");
const fullscreenBtn = document.getElementById("fullscreenBtn");

const channelAvatar = document.getElementById("channelAvatar");
const channelName = document.getElementById("channelName");
const channelSubs = document.getElementById("channelSubs");
const tagsRow = document.getElementById("tagsRow");
const likeBtn = document.getElementById("likeBtn");
const likeCountEl = document.getElementById("likeCount");
const watchlistToggleBtn = document.getElementById("watchlistToggleBtn");
const watchlistBtnLabel = document.getElementById("watchlistBtnLabel");
const shareBtn = document.getElementById("shareBtn");
const downloadBtn = document.getElementById("downloadBtn");
const downloadBtnLabel = document.getElementById("downloadBtnLabel");
const videoDescription = document.getElementById("videoDescription");

const episodesDrawer = document.getElementById("episodesDrawer");
const episodesGrid = document.getElementById("episodesGrid");
const liveScheduleDrawer = document.getElementById("liveScheduleDrawer");
const scheduleTimeline = document.getElementById("scheduleTimeline");

const commentsCount = document.getElementById("commentsCount");
const commentAuthor = document.getElementById("commentAuthor");
const commentText = document.getElementById("commentText");
const submitCommentBtn = document.getElementById("submitCommentBtn");
const commentsList = document.getElementById("commentsList");

const searchInput = document.getElementById("searchInput");
const clearSearchBtn = document.getElementById("clearSearchBtn");
const searchSuggestions = document.getElementById("searchSuggestions");
const headerPartyBtn = document.getElementById("headerPartyBtn");
const headerThreatCount = document.getElementById("headerThreatCount");
const watchlistCountBadge = document.getElementById("watchlistCountBadge");

// Rails
const railContinueWatchingWrap = document.getElementById("railContinueWatchingWrap");
const railContinueWatching = document.getElementById("railContinueWatching");
const clearHistoryBtn = document.getElementById("clearHistoryBtn");

const railWatchlistWrap = document.getElementById("railWatchlistWrap");
const railWatchlist = document.getElementById("railWatchlist");
const railWatchlistBadge = document.getElementById("railWatchlistBadge");

const railTrendingWrap = document.getElementById("railTrendingWrap");
const railTrending = document.getElementById("railTrending");

const railMoviesWrap = document.getElementById("railMoviesWrap");
const railMovies = document.getElementById("railMovies");

const railSeriesWrap = document.getElementById("railSeriesWrap");
const railSeries = document.getElementById("railSeries");

const railAnimeWrap = document.getElementById("railAnimeWrap");
const railAnime = document.getElementById("railAnime");

const railLiveTvWrap = document.getElementById("railLiveTvWrap");
const railLiveTv = document.getElementById("railLiveTv");

// Modals
const partyModal = document.getElementById("partyModal");
const closePartyModalBtn = document.getElementById("closePartyModalBtn");
const partyLinkInput = document.getElementById("partyLinkInput");
const copyPartyBtn = document.getElementById("copyPartyBtn");

const shortcutsModal = document.getElementById("shortcutsModal");
const shortcutsBtn = document.getElementById("shortcutsBtn");
const closeModalBtn = document.getElementById("closeModalBtn");

const legalModal = document.getElementById("legalModal");
const closeLegalModalBtn = document.getElementById("closeLegalModalBtn");

// ----------------------------------------------------------------------------
// Initialization
// ----------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", async () => {
  setupEventListeners();
  updateWatchlistBadge();
  checkPartyRoomUrl();

  // Load initial data
  await Promise.all([
    loadCatalogData(),
    loadLiveChannels(),
    updateSecurityTelemetry()
  ]);

  renderAllRails();
  setInterval(updateSecurityTelemetry, 5000);
});

// ----------------------------------------------------------------------------
// Data Loading & API Calls
// ----------------------------------------------------------------------------
async function loadCatalogData() {
  try {
    const res = await fetch("/api/videos");
    const data = await res.json();
    state.allVideos = data.videos || [];

    // Set Hero Billboard
    const featRes = await fetch("/api/videos/featured");
    const featData = await featRes.json();
    state.featuredItem = featData.featured || state.allVideos[0];
    renderHeroBillboard(state.featuredItem);
  } catch (err) {
    console.error("Error loading video catalog:", err);
  }
}

async function loadLiveChannels() {
  try {
    const res = await fetch("/api/live/channels");
    const data = await res.json();
    state.channels = data.channels || [];
  } catch (err) {
    console.error("Error loading live TV channels:", err);
  }
}

async function updateSecurityTelemetry() {
  try {
    const res = await fetch("/api/security/stats");
    const data = await res.json();
    if (data && data.metrics) {
      headerThreatCount.textContent = data.metrics.attacks_blocked || 0;
    }
  } catch (err) {
    // Offline resilience
  }
}

// ----------------------------------------------------------------------------
// Hero Billboard Rendering (Movibox & Netflix Model)
// ----------------------------------------------------------------------------
function renderHeroBillboard(item) {
  if (!item) return;
  state.featuredItem = item;

  heroTitle.textContent = item.title;
  heroSubtitle.textContent = item.subtitle || item.category || "Cinema Feature";
  heroDesc.textContent = item.description;
  heroBackdrop.src = item.backdrop_url || item.thumbnail_url;
  heroQuality.textContent = item.quality || "4K ULTRA HD";
  heroRating.innerHTML = `<i class="fa-solid fa-star"></i> ${item.imdb_rating || "8.8"} IMDb`;
  heroYear.textContent = item.release_year || "2024";
  heroAge.textContent = item.age_rating || "PG-13";

  const isInWatchlist = state.watchlist.includes(item.id);
  heroWatchlistText.textContent = isInWatchlist ? "✓ In Watchlist" : "Add to Watchlist";
  heroWatchlistBtn.classList.toggle("active", isInWatchlist);
}

// ----------------------------------------------------------------------------
// Horizontal OTT Rails Rendering
// ----------------------------------------------------------------------------
function renderAllRails() {
  renderContinueWatchingRail();
  renderWatchlistRail();
  renderTrendingRail();
  renderMoviesRail();
  renderSeriesRail();
  renderAnimeRail();
  renderLiveTvRail();
}

function renderCard(item, isChannel = false) {
  const isVideo = !isChannel;
  const id = item.id;
  const title = item.title || item.name;
  const poster = isVideo ? (item.poster_url || item.thumbnail_url) : item.logo;
  const quality = isVideo ? (item.quality || "1080p HD") : (item.resolution || "1080p");
  const rating = item.imdb_rating ? `⭐ ${item.imdb_rating}` : (item.flag ? `${item.flag} ${item.country}` : "⭐ 8.5");
  const subMeta = isVideo ? `${item.release_year || "2024"} • ${item.duration_formatted || "HD"}` : `${item.category}`;

  const inWatchlist = state.watchlist.includes(id);

  // Check progress
  const hist = state.history[id];
  const progressHtml = hist && hist.pct > 0 ? `
    <div class="card-progress-bar">
      <div class="card-progress-fill" style="width: ${Math.min(100, hist.pct)}%;"></div>
    </div>
  ` : "";

  return `
    <div class="ott-card ${isChannel ? "live-channel-card" : ""}" data-id="${id}" onclick="${isChannel ? `selectLiveChannel('${id}')` : `playVideoById('${id}')`}">
      <div class="card-poster-wrap">
        <img src="${poster}" alt="${title}" class="card-poster-img" loading="lazy">
        <span class="card-quality-tag">${quality}</span>
        <span class="card-rating-tag">${rating}</span>
        ${isVideo ? `
          <button class="card-watchlist-quick-btn ${inWatchlist ? "active" : ""}" onclick="event.stopPropagation(); toggleWatchlist('${id}');" title="${inWatchlist ? "Remove from Watchlist" : "Add to Watchlist"}">
            <i class="fa-${inWatchlist ? "solid" : "regular"} fa-bookmark"></i>
          </button>
        ` : ""}
        <div class="card-hover-overlay">
          <div class="card-hover-play-icon">
            <i class="fa-solid fa-play"></i>
          </div>
        </div>
        ${progressHtml}
      </div>
      <div class="card-info">
        <h4 class="card-title">${title}</h4>
        <div class="card-meta-row">
          <span>${subMeta}</span>
          ${isChannel ? '<span style="color:#ef4444; font-weight:bold;">● LIVE</span>' : `<span>${item.category || ""}</span>`}
        </div>
      </div>
    </div>
  `;
}

function renderContinueWatchingRail() {
  const historyKeys = Object.keys(state.history);
  if (historyKeys.length === 0) {
    railContinueWatchingWrap.style.display = "none";
    return;
  }

  railContinueWatchingWrap.style.display = "block";
  const items = historyKeys
    .map((k) => state.allVideos.find((v) => v.id === k))
    .filter(Boolean);

  railContinueWatching.innerHTML = items.map((item) => renderCard(item)).join("");
}

function renderWatchlistRail() {
  if (state.watchlist.length === 0) {
    railWatchlistWrap.style.display = "none";
    railWatchlistBadge.textContent = "0 titles";
    return;
  }

  railWatchlistWrap.style.display = "block";
  railWatchlistBadge.textContent = `${state.watchlist.length} titles`;
  const items = state.watchlist
    .map((id) => state.allVideos.find((v) => v.id === id))
    .filter(Boolean);

  railWatchlist.innerHTML = items.map((item) => renderCard(item)).join("");
}

function renderTrendingRail() {
  const trending = state.allVideos.filter((v) => v.is_trending);
  railTrending.innerHTML = (trending.length ? trending : state.allVideos).map((item) => renderCard(item)).join("");
}

function renderMoviesRail() {
  const movies = state.allVideos.filter((v) => v.content_type === "movie");
  railMovies.innerHTML = (movies.length ? movies : state.allVideos).map((item) => renderCard(item)).join("");
}

function renderSeriesRail() {
  const series = state.allVideos.filter((v) => v.content_type === "series");
  railSeries.innerHTML = (series.length ? series : state.allVideos).map((item) => renderCard(item)).join("");
}

function renderAnimeRail() {
  const anime = state.allVideos.filter((v) => v.content_type === "anime");
  railAnime.innerHTML = (anime.length ? anime : state.allVideos).map((item) => renderCard(item)).join("");
}

function renderLiveTvRail() {
  railLiveTv.innerHTML = state.channels.map((ch) => renderCard(ch, true)).join("");
}

// ----------------------------------------------------------------------------
// OTT Pre-Roll Video Advertisement Engine (YouTube / Hulu Model)
// Plays before movie/episode starts with a 5-second countdown to Skip Ad
// ----------------------------------------------------------------------------
const AD_CAMPAIGNS = [
  {
    title: "StreamGuard Pro • Dolby 4K Cinema",
    headline: "Zero-Lag Hollywood Streaming & Cinema Sound",
    sponsor: "StreamGuard Network",
    video_url: "https://test-videos.co.uk/vids/jellyfish/mp4/h264/720/Jellyfish_720_10s_5MB.mp4",
    duration: 10
  },
  {
    title: "CyberShield Security • Real-Time Protection",
    headline: "Autonomous Threat Defense for Ultra-HD Streams",
    sponsor: "CyberShield Global Security",
    video_url: "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4",
    duration: 12
  }
];

let adState = {
  isPlaying: false,
  countdownInterval: null,
  secondsRemaining: 5,
  currentCampaign: null,
  onFinishedCallback: null
};

function startPrerollAd(onFinished) {
  if (!prerollAdOverlay || !adVideoElement) {
    if (onFinished) onFinished();
    return;
  }

  // Clear any existing ad intervals/playback
  finishPrerollAd(false);

  adState.isPlaying = true;
  adState.onFinishedCallback = onFinished;
  adState.secondsRemaining = 5;

  // Pick ad campaign
  const campaign = AD_CAMPAIGNS[Math.floor(Math.random() * AD_CAMPAIGNS.length)];
  adState.currentCampaign = campaign;

  // Update Ad UI
  if (adSponsorName) adSponsorName.textContent = campaign.title;
  if (adHeadline) adHeadline.textContent = campaign.headline;
  if (adTimeBadge) adTimeBadge.textContent = "Ad • 0:10";
  if (skipBtnText) skipBtnText.textContent = "Skip in 5s";
  if (skipAdBtn) {
    skipAdBtn.setAttribute("disabled", "true");
    skipAdBtn.classList.remove("can-skip");
  }
  if (adProgressFill) adProgressFill.style.width = "0%";

  // Hide main video player & controls, show ad overlay
  videoEl.pause();
  destroyHls();
  if (embedPlayerFrame) {
    embedPlayerFrame.src = "about:blank";
    embedPlayerFrame.style.display = "none";
  }
  videoEl.style.display = "none";
  if (playerControls) playerControls.style.display = "none";
  if (centerPlayOverlay) centerPlayOverlay.style.display = "none";

  prerollAdOverlay.style.display = "block";

  // Load and play ad video
  adVideoElement.src = campaign.video_url;
  adVideoElement.currentTime = 0;
  
  const playPromise = adVideoElement.play();
  if (playPromise !== undefined) {
    playPromise.catch((err) => {
      console.warn("Autoplay held, trying muted ad playback:", err);
      adVideoElement.muted = true;
      adVideoElement.play().catch(() => {
        // If ad playback blocked, immediately proceed to movie
        finishPrerollAd(true);
      });
    });
  }

  // Countdown for Skip Button (5 seconds)
  adState.countdownInterval = setInterval(() => {
    adState.secondsRemaining--;
    if (adState.secondsRemaining > 0) {
      if (skipBtnText) skipBtnText.textContent = `Skip in ${adState.secondsRemaining}s`;
    } else {
      clearInterval(adState.countdownInterval);
      adState.countdownInterval = null;
      if (skipAdBtn) {
        skipAdBtn.removeAttribute("disabled");
        skipAdBtn.classList.add("can-skip");
      }
      if (skipBtnText) skipBtnText.textContent = "Skip Ad";
      showToast("You can now skip the advertisement");
    }
  }, 1000);
}

function finishPrerollAd(triggerCallback = true) {
  if (adState.countdownInterval) {
    clearInterval(adState.countdownInterval);
    adState.countdownInterval = null;
  }

  if (adVideoElement) {
    adVideoElement.pause();
    adVideoElement.removeAttribute("src");
  }

  if (prerollAdOverlay) {
    prerollAdOverlay.style.display = "none";
  }

  const cb = adState.onFinishedCallback;
  adState.isPlaying = false;
  adState.onFinishedCallback = null;

  if (triggerCallback && typeof cb === "function") {
    cb();
  }
}

// ----------------------------------------------------------------------------
// Video Playback Engine (Cinema & On-Demand)
// ----------------------------------------------------------------------------
async function playVideoById(videoId, autoPlay = true, episodeIndex = null) {
  try {
    destroyHls();
    const res = await fetch(`/api/videos/${videoId}`);
    const data = await res.json();
    state.currentVideo = data.video;
    state.currentChannel = null;
    state.currentServerIndex = 0;
    state.currentEpisodeIndex = episodeIndex !== null ? episodeIndex : 0;

    // Show theater container
    theaterSection.style.display = "block";
    theaterSection.scrollIntoView({ behavior: "smooth", block: "start" });
    liveIndicatorTag.style.display = "none";
    channelFlagBadge.style.display = "none";

    // Update Player Top Bar
    activePlayerTitle.textContent = state.currentVideo.title;
    qualityText.textContent = state.currentVideo.quality || "4K ULTRA HD";

    // Setup Multi-Server options
    renderServerOptions(state.currentVideo.servers || [
      { id: "srv-1", name: "Server 1: Full Original Movie (Cloud 4K)", type: "embed", url: state.currentVideo.video_url }
    ]);

    // Handle Episode Playback if TV series or Anime
    if (state.currentVideo.seasons && state.currentVideo.seasons.length > 0) {
      episodesDrawer.style.display = "block";
      renderEpisodesDrawer(state.currentVideo.seasons[0], state.currentEpisodeIndex);
      const activeEp = state.currentVideo.seasons[0].episodes[state.currentEpisodeIndex];
      if (activeEp) {
        activePlayerTitle.textContent = `${state.currentVideo.title} - S1:E${activeEp.episode_number} "${activeEp.title}"`;
      }
    } else {
      episodesDrawer.style.display = "none";
    }

    liveScheduleDrawer.style.display = "none";

    // Meta details
    channelAvatar.src = state.currentVideo.channel?.avatar || "";
    channelName.textContent = state.currentVideo.channel?.name || "Cinema";
    channelSubs.textContent = `${state.currentVideo.channel?.subscribers || "10M"} subscribers`;
    likeCountEl.textContent = (state.currentVideo.likes || 12000).toLocaleString();
    downloadBtnLabel.textContent = "Source";
    videoDescription.textContent = state.currentVideo.description;

    tagsRow.innerHTML = (state.currentVideo.tags || [])
      .map((t) => `<span class="meta-tag">#${t}</span>`)
      .join(" ");

    updateWatchlistButtonState();
    renderComments(state.currentVideo.comments || []);

    // Play Pre-Roll Advertisement with 5-second skip option before the movie starts!
    startPrerollAd(() => {
      loadActiveStream(autoPlay);
    });
  } catch (err) {
    console.error("Error playing video:", err);
  }
}

// ----------------------------------------------------------------------------
// Stream Dispatcher: Cloud 4K Embed (VidLink / VidSrc) vs Native HTML5 Player
// ----------------------------------------------------------------------------
function loadActiveStream(autoPlay = true) {
  if (!state.currentVideo) return;
  const servers = state.currentVideo.servers || [
    { id: "srv-1", name: "Server 1: Full Original Movie (Cloud 4K)", type: "embed", url: state.currentVideo.video_url }
  ];
  const srv = servers[state.currentServerIndex] || servers[0];

  if (srv.type === "embed" || srv.type === "embed_tv") {
    // 1. Pause & clear native HTML5 video
    videoEl.pause();
    destroyHls();
    while (videoEl.firstChild) {
      videoEl.removeChild(videoEl.firstChild);
    }
    videoEl.removeAttribute("src");
    videoEl.style.display = "none";
    if (playerControls) playerControls.style.display = "none";
    if (centerPlayOverlay) centerPlayOverlay.style.display = "none";

    // 2. Build Embed URL
    let embedUrl = srv.url;
    if (srv.type === "embed_tv") {
      const epNum = (state.currentEpisodeIndex || 0) + 1;
      const seasonNum = 1;
      if (embedUrl.includes("vidlink.pro")) {
        const cleanBase = embedUrl.split("?")[0].replace(/\/+$/, "");
        embedUrl = `${cleanBase}/${seasonNum}/${epNum}?primaryColor=06b6d4`;
      } else if (embedUrl.includes("vidsrc")) {
        const cleanBase = embedUrl.replace(/\/+$/, "");
        embedUrl = `${cleanBase}/${seasonNum}/${epNum}`;
      } else {
        const cleanBase = embedUrl.replace(/\/+$/, "");
        embedUrl = `${cleanBase}/${seasonNum}/${epNum}`;
      }
    }

    // 3. Mount in iframe
    if (embedPlayerFrame) {
      embedPlayerFrame.style.display = "block";
      embedPlayerFrame.src = embedUrl;
    }
    showToast(`Streaming ${state.currentVideo.title} via ${srv.name}`);
  } else {
    // Native HTML5 Video Stream (Direct / Fallback)
    if (embedPlayerFrame) {
      embedPlayerFrame.src = "about:blank";
      embedPlayerFrame.style.display = "none";
    }
    videoEl.style.display = "block";
    if (playerControls) playerControls.style.display = "flex";
    if (centerPlayOverlay) centerPlayOverlay.style.display = "flex";

    let nativeUrl = srv.url;
    if (state.currentVideo.seasons && state.currentVideo.seasons.length > 0) {
      const ep = state.currentVideo.seasons[0].episodes[state.currentEpisodeIndex || 0];
      if (ep && ep.video_url) {
        nativeUrl = ep.video_url;
      }
    }

    while (videoEl.firstChild) {
      videoEl.removeChild(videoEl.firstChild);
    }
    videoEl.removeAttribute("src");
    videoEl.removeAttribute("crossorigin");

    if (state.currentVideo.subtitles && state.currentVideo.subtitles.length > 0) {
      const sub = state.currentVideo.subtitles[0];
      const track = document.createElement("track");
      track.kind = "subtitles";
      track.label = sub.label;
      track.srclang = sub.srclang;
      track.src = sub.src;
      track.default = true;
      videoEl.appendChild(track);
    }

    videoEl.src = nativeUrl;
    videoEl.load();

    scrubberProgress.style.width = "0%";
    scrubberThumb.style.left = "0%";
    currentTimeEl.textContent = "00:00";
    totalDurationEl.textContent = state.currentVideo.duration_formatted || "12:14";

    const savedHist = state.history[state.currentVideo.id];
    if (savedHist && savedHist.timestamp > 5 && savedHist.pct < 95) {
      videoEl.currentTime = savedHist.timestamp;
      showToast(`Resumed from ${formatTime(savedHist.timestamp)}`);
    }

    if (autoPlay) {
      videoEl.play().catch((err) => {
        console.warn("Autoplay held by browser policy.", err);
      });
    }
    showToast(`Streaming ${state.currentVideo.title} via ${srv.name}`);
  }
}

// ----------------------------------------------------------------------------
// Live TV Streaming Engine (Via Built-in Self-Gateway Tunnel)
// ----------------------------------------------------------------------------
async function selectLiveChannel(channelId, autoPlay = true) {
  try {
    destroyHls();
    finishPrerollAd(false);
    const res = await fetch(`/api/live/channels/${channelId}`);
    const data = await res.json();
    state.currentChannel = data.channel;
    state.currentVideo = null;
    state.currentServerIndex = 0;

    // Show theater container
    theaterSection.style.display = "block";
    theaterSection.scrollIntoView({ behavior: "smooth", block: "start" });
    liveIndicatorTag.style.display = "flex";
    channelFlagBadge.textContent = state.currentChannel.flag;
    channelFlagBadge.style.display = "inline-block";

    activePlayerTitle.textContent = state.currentChannel.name;
    qualityText.textContent = state.currentChannel.resolution || "1080p HD";

    // Setup Server Options
    renderServerOptions([
      { id: "srv-gw", name: "Self-Gateway Tunnel (Proxy Relay)", type: "native", url: state.currentChannel.gateway_url },
      { id: "srv-raw", name: "Direct Akamai CDN", type: "native", url: state.currentChannel.stream_url }
    ]);

    episodesDrawer.style.display = "none";

    // CineHD-style Live Schedule Timetable
    if (state.currentChannel.schedule && state.currentChannel.schedule.length > 0) {
      liveScheduleDrawer.style.display = "block";
      renderLiveSchedule(state.currentChannel.schedule);
    } else {
      liveScheduleDrawer.style.display = "none";
    }

    // Meta details
    channelAvatar.src = state.currentChannel.logo;
    channelName.textContent = state.currentChannel.name;
    channelSubs.textContent = `${state.currentChannel.category} • ${state.currentChannel.country}`;
    likeCountEl.textContent = state.currentChannel.views || "1.2M";
    downloadBtnLabel.textContent = "Raw Stream";
    videoDescription.textContent = state.currentChannel.description;

    tagsRow.innerHTML = `
      <span class="meta-tag">#LiveTV</span>
      <span class="meta-tag">#${state.currentChannel.country}</span>
      <span class="meta-tag">#${state.currentChannel.category}</span>
    `;

    // Ensure embed player is stopped and hidden
    if (embedPlayerFrame) {
      embedPlayerFrame.src = "about:blank";
      embedPlayerFrame.style.display = "none";
    }
    videoEl.style.display = "block";
    if (playerControls) playerControls.style.display = "flex";
    if (centerPlayOverlay) centerPlayOverlay.style.display = "flex";

    // Stream via In-App Gateway
    playHlsStream(state.currentChannel.gateway_url, autoPlay);
    showToast(`Streaming ${state.currentChannel.name} via Self-Gateway Tunnel`);
  } catch (err) {
    console.error("Error selecting live channel:", err);
  }
}

function playHlsStream(streamUrl, autoPlay = true) {
  destroyHls();
  while (videoEl.firstChild) {
    videoEl.removeChild(videoEl.firstChild);
  }
  videoEl.removeAttribute("src");

  if (Hls.isSupported()) {
    state.hlsInstance = new Hls({
      enableWorker: true,
      lowLatencyMode: true,
      backBufferLength: 60
    });
    state.hlsInstance.loadSource(streamUrl);
    state.hlsInstance.attachMedia(videoEl);
    state.hlsInstance.on(Hls.Events.MANIFEST_PARSED, () => {
      if (autoPlay) {
        videoEl.play().catch(() => {});
      }
    });
  } else if (videoEl.canPlayType("application/vnd.apple.mpegurl")) {
    videoEl.src = streamUrl;
    if (autoPlay) {
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

// ----------------------------------------------------------------------------
// Multi-Server Streaming Switcher (Movibox Style)
// ----------------------------------------------------------------------------
function updateServerMenuUI(activeIndex) {
  if (!serverMenu) return;
  const buttons = serverMenu.querySelectorAll(".server-option");
  buttons.forEach((btn, idx) => {
    btn.classList.toggle("active", idx === activeIndex);
    const check = btn.querySelector("i");
    if (check) {
      check.style.display = idx === activeIndex ? "inline-block" : "none";
    }
  });
}

function renderServerOptions(servers) {
  if (!servers || servers.length === 0) return;
  currentServerLabel.textContent = servers[0].name;

  serverMenu.innerHTML = servers
    .map(
      (srv, idx) => `
      <button class="server-option ${idx === 0 ? "active" : ""}" onclick="switchServer(${idx})">
        <span>${srv.name}</span>
        <i class="fa-solid fa-check" style="${idx === 0 ? "" : "display:none;"}"></i>
      </button>
    `
    )
    .join("");
}

function switchServer(serverIndex) {
  state.currentServerIndex = serverIndex;
  updateServerMenuUI(serverIndex);
  serverMenu.classList.remove("show");

  if (state.currentChannel) {
    const servers = [
      { id: "srv-gw", name: "Self-Gateway Tunnel (Proxy Relay)", type: "native", url: state.currentChannel.gateway_url },
      { id: "srv-raw", name: "Direct Akamai CDN", type: "native", url: state.currentChannel.stream_url }
    ];
    const srv = servers[serverIndex];
    if (srv) {
      currentServerLabel.textContent = srv.name;
      playHlsStream(srv.url, true);
      showToast(`Switched to ${srv.name}`);
    }
  } else if (state.currentVideo) {
    const servers = state.currentVideo.servers || [];
    const srv = servers[serverIndex];
    if (srv) {
      currentServerLabel.textContent = srv.name;
      loadActiveStream(true);
    }
  }
}

// ----------------------------------------------------------------------------
// Episodes Drawer & Live Schedule Rendering (CineHD Style)
// ----------------------------------------------------------------------------
function selectEpisode(idx) {
  if (!state.currentVideo) return;
  state.currentEpisodeIndex = idx;

  const cards = episodesGrid.querySelectorAll(".episode-card");
  cards.forEach((c, i) => c.classList.toggle("active", i === idx));

  const season = state.currentVideo.seasons && state.currentVideo.seasons[0];
  const ep = season && season.episodes[idx];
  if (ep) {
    activePlayerTitle.textContent = `${state.currentVideo.title} - S1:E${ep.episode_number} "${ep.title}"`;
  }

  startPrerollAd(() => {
    loadActiveStream(true);
  });
}

function renderEpisodesDrawer(season, activeIdx = 0) {
  episodesGrid.innerHTML = season.episodes
    .map(
      (ep, idx) => `
      <div class="episode-card ${idx === activeIdx ? "active" : ""}" onclick="selectEpisode(${idx})">
        <div class="episode-thumb-wrap">
          <img src="${ep.thumbnail}" alt="${ep.title}">
        </div>
        <div class="episode-card-info">
          <h4>${ep.episode_number}. ${ep.title}</h4>
          <span>${ep.duration}</span>
        </div>
      </div>
    `
    )
    .join("");
}

function renderLiveSchedule(schedule) {
  scheduleTimeline.innerHTML = schedule
    .map(
      (item) => `
      <div class="schedule-item ${item.status === "LIVE NOW" ? "live-now" : ""}">
        <div class="schedule-time">
          <span>${item.time}</span>
          <span class="schedule-badge ${item.status === "LIVE NOW" ? "live" : "upcoming"}">${item.status}</span>
        </div>
        <div class="schedule-title">${item.title}</div>
      </div>
    `
    )
    .join("");
}

// ----------------------------------------------------------------------------
// Watchlist & Personalization (LocalStorage Engine)
// ----------------------------------------------------------------------------
function toggleWatchlist(videoId) {
  const idx = state.watchlist.indexOf(videoId);
  if (idx === -1) {
    state.watchlist.push(videoId);
    showToast("Added to My Watchlist");
  } else {
    state.watchlist.splice(idx, 1);
    showToast("Removed from My Watchlist");
  }

  localStorage.setItem("streamguard_watchlist", JSON.stringify(state.watchlist));
  updateWatchlistBadge();
  updateWatchlistButtonState();
  renderWatchlistRail();

  // Re-render hero if it matches
  if (state.featuredItem && state.featuredItem.id === videoId) {
    renderHeroBillboard(state.featuredItem);
  }
}

function updateWatchlistBadge() {
  watchlistCountBadge.textContent = state.watchlist.length;
}

function updateWatchlistButtonState() {
  if (!state.currentVideo) return;
  const inList = state.watchlist.includes(state.currentVideo.id);
  watchlistBtnLabel.textContent = inList ? "✓ In Watchlist" : "Add to Watchlist";
  watchlistToggleBtn.classList.toggle("active", inList);
}

// ----------------------------------------------------------------------------
// Continue Watching Engine
// ----------------------------------------------------------------------------
function savePlayProgress() {
  if (!state.currentVideo || !videoEl.duration) return;
  const current = videoEl.currentTime;
  const total = videoEl.duration;
  const pct = Math.round((current / total) * 100);

  state.history[state.currentVideo.id] = {
    timestamp: current,
    total: total,
    pct: pct,
    date: Date.now()
  };

  localStorage.setItem("streamguard_history", JSON.stringify(state.history));
}

// ----------------------------------------------------------------------------
// Player Controls Logic
// ----------------------------------------------------------------------------
function togglePlay() {
  if (videoEl.paused || videoEl.ended) {
    const playPromise = videoEl.play();
    if (playPromise !== undefined) {
      playPromise.catch((err) => {
        console.warn("Playback error / autoplay interrupted:", err);
      });
    }
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
  if (state.currentChannel) {
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

  savePlayProgress();
}

function seekTimeline(e) {
  if (state.currentChannel || !videoEl.duration) return;
  const rect = scrubberWrapper.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, clickX / rect.width));
  videoEl.currentTime = pct * videoEl.duration;
}

function updateHoverPreview(e) {
  if (state.currentChannel || !videoEl.duration) return;
  const rect = scrubberWrapper.getBoundingClientRect();
  const hoverX = e.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, hoverX / rect.width));
  const hoverTime = pct * videoEl.duration;

  scrubberPreview.style.left = `${hoverX}px`;
  scrubberPreview.style.opacity = "1";
  previewTimeEl.textContent = formatTime(hoverTime);
}

function hideHoverPreview() {
  scrubberPreview.style.opacity = "0";
}

function setVolume(val) {
  const vol = parseFloat(val);
  videoEl.volume = vol;
  videoEl.muted = vol === 0;
  updateVolumeIcon();
}

function toggleMute() {
  videoEl.muted = !videoEl.muted;
  updateVolumeIcon();
}

function updateVolumeIcon() {
  if (videoEl.muted || videoEl.volume === 0) {
    muteBtn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
  } else if (videoEl.volume < 0.5) {
    muteBtn.innerHTML = '<i class="fa-solid fa-volume-low"></i>';
  } else {
    muteBtn.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
  }
}

function toggleSubtitles() {
  state.subtitlesActive = !state.subtitlesActive;
  if (videoEl.textTracks && videoEl.textTracks.length > 0) {
    videoEl.textTracks[0].mode = state.subtitlesActive ? "showing" : "hidden";
  }
  ccToggleBtn.classList.toggle("active", state.subtitlesActive);
  showToast(state.subtitlesActive ? "Subtitles [CC] Enabled" : "Subtitles Disabled");
}

function setPlaybackSpeed(speed) {
  videoEl.playbackRate = speed;
  speedLabel.textContent = `${speed}x`;
  document.querySelectorAll(".speed-opt").forEach((btn) => {
    btn.classList.toggle("active", parseFloat(btn.dataset.speed) === speed);
  });
  speedMenu.classList.remove("show");
  showToast(`Speed: ${speed}x`);
}

function toggleTheaterMode() {
  theaterSection.classList.toggle("expanded");
  showToast("Toggled Theater Mode");
}

async function togglePiP() {
  try {
    if (document.pictureInPictureElement) {
      await document.exitPictureInPicture();
    } else if (document.pictureInPictureEnabled) {
      await videoEl.requestPictureInPicture();
    }
  } catch (err) {
    console.error("PiP error:", err);
  }
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    playerContainer.requestFullscreen().catch(() => {});
  } else {
    document.exitFullscreen();
  }
}

function formatTime(seconds) {
  if (isNaN(seconds) || seconds < 0) return "00:00";
  const s = Math.floor(seconds % 60);
  const m = Math.floor((seconds / 60) % 60);
  const h = Math.floor(seconds / 3600);
  const pad = (n) => String(n).padStart(2, "0");
  return h > 0 ? `${h}:${pad(m)}:${pad(s)}` : `${pad(m)}:${pad(s)}`;
}

// ----------------------------------------------------------------------------
// CineHD-style Watch Party Room Engine
// ----------------------------------------------------------------------------
function openPartyModal() {
  const roomCode = state.partyRoomCode || `SG-${Math.floor(1000 + Math.random() * 9000)}`;
  state.partyRoomCode = roomCode;
  const currentId = state.currentVideo ? state.currentVideo.id : (state.currentChannel ? state.currentChannel.id : "vid-01");
  const url = `${window.location.origin}/?party=${roomCode}&media=${currentId}`;
  partyLinkInput.value = url;
  partyModal.style.display = "flex";
}

function closePartyModal() {
  partyModal.style.display = "none";
}

function copyPartyLink() {
  navigator.clipboard.writeText(partyLinkInput.value);
  showToast("Party Room Link copied to clipboard!");
}

function checkPartyRoomUrl() {
  const params = new URLSearchParams(window.location.search);
  const party = params.get("party");
  const media = params.get("media");
  if (party) {
    state.partyRoomCode = party;
    showToast(`Joined Watch Party: Room ${party}`);
    if (media) {
      setTimeout(() => {
        if (media.startsWith("live-")) {
          selectLiveChannel(media);
        } else {
          playVideoById(media);
        }
      }, 600);
    }
  }
}

// ----------------------------------------------------------------------------
// Live Instant Search Dropdown
// ----------------------------------------------------------------------------
function handleSearchInput(e) {
  const query = e.target.value.trim().toLowerCase();
  state.searchQuery = query;
  clearSearchBtn.style.display = query ? "block" : "none";

  if (!query) {
    searchSuggestions.style.display = "none";
    return;
  }

  const matchedVideos = state.allVideos.filter(
    (v) =>
      v.title.toLowerCase().includes(query) ||
      (v.subtitle && v.subtitle.toLowerCase().includes(query)) ||
      (v.tags && v.tags.some((t) => t.toLowerCase().includes(query)))
  );

  const matchedChannels = state.channels.filter(
    (c) =>
      c.name.toLowerCase().includes(query) ||
      c.category.toLowerCase().includes(query) ||
      c.country.toLowerCase().includes(query)
  );

  const allMatches = [
    ...matchedVideos.map((v) => ({ ...v, type: "video" })),
    ...matchedChannels.map((c) => ({ ...c, type: "channel" }))
  ].slice(0, 5);

  if (allMatches.length === 0) {
    searchSuggestions.innerHTML = '<div style="padding:10px; color:#64748b; font-size:12px; text-align:center;">No matching titles found.</div>';
    searchSuggestions.style.display = "block";
    return;
  }

  searchSuggestions.innerHTML = allMatches
    .map((m) => {
      const isVid = m.type === "video";
      const thumb = isVid ? (m.poster_url || m.thumbnail_url) : m.logo;
      const title = m.title || m.name;
      const sub = isVid ? `${m.release_year || "2024"} • ${m.category}` : `🔴 Live TV • ${m.country}`;
      const clickAction = isVid ? `playVideoById('${m.id}')` : `selectLiveChannel('${m.id}')`;

      return `
        <div class="suggestion-item" onclick="${clickAction}; searchSuggestions.style.display='none';">
          <img src="${thumb}" alt="${title}" class="suggestion-thumb">
          <div class="suggestion-info">
            <h4>${title}</h4>
            <span>${sub}</span>
          </div>
        </div>
      `;
    })
    .join("");

  searchSuggestions.style.display = "block";
}

// ----------------------------------------------------------------------------
// Comments System with Defensive Shield
// ----------------------------------------------------------------------------
function renderComments(comments) {
  commentsCount.textContent = comments.length;
  commentsList.innerHTML = comments
    .map(
      (c) => `
      <div class="comment-item">
        <span class="comment-author">${c.author}:</span>
        <span class="comment-text">${c.text}</span>
      </div>
    `
    )
    .join("");
}

async function submitComment() {
  const author = commentAuthor.value.trim() || "Viewer";
  const text = commentText.value.trim();
  if (!text) return;

  if (state.currentVideo) {
    try {
      const res = await fetch(`/api/videos/${state.currentVideo.id}/comment`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ author, text })
      });

      if (res.status === 403) {
        const err = await res.json();
        alert(`🛡️ StreamGuard Autonomous Shield Intercepted Threat!\nType: ${err.threat_classification}\nForensic logged to threat_locations.log`);
        return;
      }

      const data = await res.json();
      if (data.status === "success") {
        state.currentVideo.comments.unshift(data.comment);
        renderComments(state.currentVideo.comments);
        commentText.value = "";
        showToast("Comment published securely.");
      }
    } catch (err) {
      console.error("Error submitting comment:", err);
    }
  } else {
    // Live TV comment reaction
    const newComment = { author, text };
    const div = document.createElement("div");
    div.className = "comment-item";
    div.innerHTML = `<span class="comment-author">${author}:</span> <span class="comment-text">${text}</span>`;
    commentsList.prepend(div);
    commentText.value = "";
    showToast("Live reaction posted.");
  }
}

// ----------------------------------------------------------------------------
// Modals & Legal Disclaimers
// ----------------------------------------------------------------------------
function openLegalModal(tabId = "legal-global-safe-harbor") {
  legalModal.style.display = "flex";
  document.querySelectorAll(".legal-tab-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.tab === tabId);
  });
  document.querySelectorAll(".legal-panel").forEach((panel) => {
    panel.classList.toggle("active", panel.id === tabId);
  });
}

function closeLegalModal() {
  legalModal.style.display = "none";
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
// Event Listeners Setup
// ----------------------------------------------------------------------------
function setupEventListeners() {
  // Navigation Tabs (All, Movies, TV Series, Anime, Live TV, Watchlist)
  document.querySelectorAll(".nav-tab").forEach((tab) => {
    tab.addEventListener("click", () => {
      document.querySelectorAll(".nav-tab").forEach((t) => t.classList.remove("active"));
      tab.classList.add("active");
      const type = tab.dataset.type;
      state.viewMode = type;

      if (type === "all") {
        document.querySelectorAll(".ott-rail").forEach((r) => (r.style.display = "block"));
        if (!state.watchlist.length) railWatchlistWrap.style.display = "none";
        if (!Object.keys(state.history).length) railContinueWatchingWrap.style.display = "none";
      } else if (type === "livetv") {
        document.querySelectorAll(".ott-rail").forEach((r) => (r.style.display = "none"));
        railLiveTvWrap.style.display = "block";
      } else if (type === "watchlist") {
        document.querySelectorAll(".ott-rail").forEach((r) => (r.style.display = "none"));
        railWatchlistWrap.style.display = "block";
      } else {
        document.querySelectorAll(".ott-rail").forEach((r) => (r.style.display = "none"));
        if (type === "movie") railMoviesWrap.style.display = "block";
        if (type === "series") railSeriesWrap.style.display = "block";
        if (type === "anime") railAnimeWrap.style.display = "block";
      }
    });
  });

  // Hero Actions
  heroPlayBtn.addEventListener("click", () => {
    if (state.featuredItem) {
      playVideoById(state.featuredItem.id);
    }
  });

  heroWatchlistBtn.addEventListener("click", () => {
    if (state.featuredItem) {
      toggleWatchlist(state.featuredItem.id);
    }
  });

  heroPartyBtn.addEventListener("click", openPartyModal);
  headerPartyBtn.addEventListener("click", openPartyModal);

  // Close Player
  closePlayerBtn.addEventListener("click", () => {
    theaterSection.style.display = "none";
    videoEl.pause();
    destroyHls();
    finishPrerollAd(false);
    if (embedPlayerFrame) {
      embedPlayerFrame.src = "about:blank";
      embedPlayerFrame.style.display = "none";
    }
  });

  // Pre-Roll Video Advertisement Listeners
  if (skipAdBtn) {
    skipAdBtn.addEventListener("click", () => {
      if (!skipAdBtn.hasAttribute("disabled") && skipAdBtn.classList.contains("can-skip")) {
        finishPrerollAd(true);
      }
    });
  }

  if (adVideoElement) {
    adVideoElement.addEventListener("timeupdate", () => {
      if (adVideoElement.duration) {
        const pct = (adVideoElement.currentTime / adVideoElement.duration) * 100;
        if (adProgressFill) adProgressFill.style.width = `${pct}%`;
        const remainingSec = Math.max(0, Math.ceil(adVideoElement.duration - adVideoElement.currentTime));
        if (adTimeBadge) adTimeBadge.textContent = `Ad • 0:${remainingSec < 10 ? '0' : ''}${remainingSec}`;
      }
    });

    adVideoElement.addEventListener("ended", () => {
      finishPrerollAd(true);
    });

    adVideoElement.addEventListener("error", (e) => {
      console.warn("Pre-roll ad video error, immediately proceeding to feature film:", e);
      finishPrerollAd(true);
    });
  }

  // Server Switcher Dropdown
  serverSelectBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    serverMenu.classList.toggle("show");
  });
  document.addEventListener("click", () => serverMenu.classList.remove("show"));

  // Video Events
  videoEl.addEventListener("click", () => {
    togglePlay();
    flashCenterOverlay(videoEl.paused ? "fa-pause" : "fa-play");
  });
  videoEl.addEventListener("play", updatePlayButton);
  videoEl.addEventListener("pause", updatePlayButton);
  videoEl.addEventListener("timeupdate", updateTimeline);
  videoEl.addEventListener("ended", () => {
    if (state.currentVideo) {
      const episodes = state.currentVideo.seasons?.[0]?.episodes || [];
      if (episodes.length > 0 && state.currentEpisodeIndex + 1 < episodes.length) {
        playVideoById(state.currentVideo.id, true, state.currentEpisodeIndex + 1);
        showToast(`Auto-playing Episode ${state.currentEpisodeIndex + 2}`);
      } else {
        const curIdx = state.allVideos.findIndex((v) => v.id === state.currentVideo.id);
        const nextIdx = (curIdx + 1) % state.allVideos.length;
        playVideoById(state.allVideos[nextIdx].id, true);
        showToast(`Auto-playing Next: ${state.allVideos[nextIdx].title}`);
      }
    }
  });

  // Controls
  playBtn.addEventListener("click", togglePlay);
  prevBtn.addEventListener("click", () => {
    if (state.currentVideo) {
      const episodes = state.currentVideo.seasons?.[0]?.episodes || [];
      if (episodes.length > 0 && state.currentEpisodeIndex > 0) {
        playVideoById(state.currentVideo.id, true, state.currentEpisodeIndex - 1);
      } else {
        const curIdx = state.allVideos.findIndex((v) => v.id === state.currentVideo.id);
        const prevIdx = (curIdx - 1 + state.allVideos.length) % state.allVideos.length;
        playVideoById(state.allVideos[prevIdx].id, true);
      }
    }
  });
  nextBtn.addEventListener("click", () => {
    if (state.currentVideo) {
      const episodes = state.currentVideo.seasons?.[0]?.episodes || [];
      if (episodes.length > 0 && state.currentEpisodeIndex + 1 < episodes.length) {
        playVideoById(state.currentVideo.id, true, state.currentEpisodeIndex + 1);
      } else {
        const curIdx = state.allVideos.findIndex((v) => v.id === state.currentVideo.id);
        const nextIdx = (curIdx + 1) % state.allVideos.length;
        playVideoById(state.allVideos[nextIdx].id, true);
      }
    }
  });
  skipBack10.addEventListener("click", () => {
    videoEl.currentTime = Math.max(0, videoEl.currentTime - 10);
    flashCenterOverlay("fa-rotate-left");
  });
  skipForward10.addEventListener("click", () => {
    videoEl.currentTime = Math.min(videoEl.duration || 0, videoEl.currentTime + 10);
    flashCenterOverlay("fa-rotate-right");
  });

  scrubberWrapper.addEventListener("click", seekTimeline);
  scrubberWrapper.addEventListener("mousemove", updateHoverPreview);
  scrubberWrapper.addEventListener("mouseleave", hideHoverPreview);

  muteBtn.addEventListener("click", toggleMute);
  volumeSlider.addEventListener("input", (e) => setVolume(e.target.value));
  ccToggleBtn.addEventListener("click", toggleSubtitles);

  speedBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    speedMenu.classList.toggle("show");
  });
  document.addEventListener("click", () => speedMenu.classList.remove("show"));
  document.querySelectorAll(".speed-opt").forEach((btn) => {
    btn.addEventListener("click", () => setPlaybackSpeed(parseFloat(btn.dataset.speed)));
  });

  theaterBtn.addEventListener("click", toggleTheaterMode);
  pipBtn.addEventListener("click", togglePiP);
  fullscreenBtn.addEventListener("click", toggleFullscreen);

  // Clear History
  clearHistoryBtn.addEventListener("click", () => {
    state.history = {};
    localStorage.removeItem("streamguard_history");
    renderContinueWatchingRail();
    showToast("Playback history cleared.");
  });

  // Player Meta Actions
  watchlistToggleBtn.addEventListener("click", () => {
    if (state.currentVideo) {
      toggleWatchlist(state.currentVideo.id);
    }
  });

  shareBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(window.location.href);
    showToast("Stream link copied to clipboard!");
  });

  downloadBtn.addEventListener("click", () => {
    if (state.currentVideo) {
      window.open(state.currentVideo.video_url, "_blank");
    } else if (state.currentChannel) {
      window.open(state.currentChannel.stream_url, "_blank");
    }
  });

  submitCommentBtn.addEventListener("click", submitComment);

  // Search input
  searchInput.addEventListener("input", handleSearchInput);
  clearSearchBtn.addEventListener("click", () => {
    searchInput.value = "";
    state.searchQuery = "";
    clearSearchBtn.style.display = "none";
    searchSuggestions.style.display = "none";
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".search-container")) {
      searchSuggestions.style.display = "none";
    }
  });

  // Rail Horizontal Scroll Arrows
  document.querySelectorAll(".rail-arrow").forEach((btn) => {
    btn.addEventListener("click", () => {
      const railId = btn.dataset.rail;
      const track = document.getElementById(railId);
      if (track) {
        const scrollAmount = track.clientWidth * 0.75;
        track.scrollBy({
          left: btn.classList.contains("prev") ? -scrollAmount : scrollAmount,
          behavior: "smooth"
        });
      }
    });
  });

  // Watch Party Modal
  closePartyModalBtn.addEventListener("click", closePartyModal);
  copyPartyBtn.addEventListener("click", copyPartyLink);

  // Shortcuts & Legal Modals
  shortcutsBtn.addEventListener("click", () => (shortcutsModal.style.display = "flex"));
  closeModalBtn.addEventListener("click", () => (shortcutsModal.style.display = "none"));
  closeLegalModalBtn.addEventListener("click", closeLegalModal);

  document.querySelectorAll(".legal-tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => openLegalModal(btn.dataset.tab));
  });

  // Keyboard Hotkeys
  document.addEventListener("keydown", (e) => {
    if (["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;
    if (e.code === "Space" || e.key === "k" || e.key === "K") {
      e.preventDefault();
      togglePlay();
    } else if (e.key === "j" || e.key === "J") {
      videoEl.currentTime = Math.max(0, videoEl.currentTime - 10);
    } else if (e.key === "l" || e.key === "L") {
      videoEl.currentTime = Math.min(videoEl.duration || 0, videoEl.currentTime + 10);
    } else if (e.key === "m" || e.key === "M") {
      toggleMute();
    } else if (e.key === "c" || e.key === "C") {
      toggleSubtitles();
    } else if (e.key === "f" || e.key === "F") {
      toggleFullscreen();
    } else if (e.key === "t" || e.key === "T") {
      toggleTheaterMode();
    } else if (e.key === "?") {
      shortcutsModal.style.display = shortcutsModal.style.display === "none" ? "flex" : "none";
    }
  });
}
