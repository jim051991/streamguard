# StreamGuard Production Deployment Guide

This guide provides end-to-end instructions for deploying StreamGuard to the public Internet without bugs or downtime.

---

## 📋 Pre-Flight Production Checklist

Before taking the application live, verify the following:

- [x] All 10 automated integration tests pass (`python test_suite.py`).
- [x] Python dependencies pinned in `requirements.txt`.
- [x] Dockerfile & `docker-compose.yml` configured with volume logging.
- [x] Anti-SSRF protection enabled on the Live TV streaming gateway.
- [x] Multi-jurisdictional safe harbor disclaimers active in the footer.
- [ ] *(Optional)* Update legal contact email addresses in `static/index.html`.

---

## 🚀 Option 1: 1-Click Cloud Deployment (Recommended - Easiest & Free SSL)

Deploying to cloud platform providers (like **Render**, **Railway**, or **Fly.io**) provides automatic HTTPS certificates, zero server maintenance, and automatic git deploys.

### Deploying on Render (Free / Pro)
1. Push this folder to a GitHub or GitLab repository:
   ```bash
   git init
   git add .
   git commit -m "Initial StreamGuard Release"
   git remote add origin https://github.com/your-username/streamguard.git
   git push -u origin main
   ```
2. Go to [Render.com](https://render.com) and click **"New +" ➔ "Web Service"**.
3. Select your GitHub repository.
4. Set the following settings:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python run.py`
5. Click **"Create Web Service"**.
   - Render automatically provisions an SSL/TLS HTTPS certificate (e.g., `https://streamguard.onrender.com`).

---

### Deploying on Railway
1. Go to [Railway.app](https://railway.app).
2. Click **"New Project" ➔ "Deploy from GitHub Repo"**.
3. Railway automatically detects the `Dockerfile` or `requirements.txt`.
4. In the Railway service settings:
   - Click **"Generate Domain"** to get a public `https://...up.railway.app` URL.

---

## 🐳 Option 2: Docker & Docker Compose (Any Cloud VPS)

If you have a Linux VPS (Ubuntu, Debian, AlmaLinux on DigitalOcean, Linode, AWS EC2, or Hetzner), Docker provides a single-command deploy:

1. Clone or copy your project folder to your VPS:
   ```bash
   scp -r "c:\Users\DELL\Downloads\Video streaming\StreamGuard_Production_Bundle" user@your-server-ip:/opt/streamguard
   ```
2. SSH into your VPS:
   ```bash
   ssh user@your-server-ip
   cd /opt/streamguard
   ```
3. Launch with Docker Compose:
   ```bash
   docker compose up -d --build
   ```
4. Verify the container is running and healthy:
   ```bash
   docker compose ps
   docker compose logs -f
   ```
5. All security logs (`threat_locations.log`, `access_hits.log`, `daily_report.log`) are automatically mounted in `/opt/streamguard/logs` on the host machine.

---

## 🐧 Option 3: Production Linux VPS (Ubuntu 22.04 / 24.04 LTS + Nginx + SSL)

This is the standard enterprise production setup using **Systemd**, **Nginx Reverse Proxy**, and free **Let's Encrypt SSL**.

### Step 1: Install System Prerequisites
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv nginx certbot python3-certbot-nginx
```

### Step 2: Set Up Application Directory & Virtual Environment
```bash
sudo mkdir -p /var/www/streamguard
sudo chown -R $USER:$USER /var/www/streamguard
cd /var/www/streamguard

# Copy files here, then create venv:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Create Systemd Background Service
Create the service unit file:
```bash
sudo nano /etc/systemd/system/streamguard.service
```

Paste the following configuration:
```ini
[Unit]
Description=StreamGuard Video Streaming & Autonomous Security Grid
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/streamguard
Environment="PATH=/var/www/streamguard/venv/bin"
Environment="PORT=8000"
Environment="APP_ENV=production"
Environment="HEADLESS=1"
ExecStart=/var/www/streamguard/venv/bin/python run.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo chown -R www-data:www-data /var/www/streamguard
sudo systemctl daemon-reload
sudo systemctl enable streamguard
sudo systemctl start streamguard
sudo systemctl status streamguard
```

### Step 4: Configure Nginx as Reverse Proxy
Create an Nginx configuration file:
```bash
sudo nano /etc/nginx/sites-available/streamguard
```

Paste the configuration (replace `yourdomain.com` with your domain):
```nginx
server {
    server_name yourdomain.com www.yourdomain.com;

    # Client upload limits for video/comment posts
    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Disable proxy buffering for live HLS streams
        proxy_buffering off;
        proxy_cache off;
    }
}
```

Enable the site and test configuration:
```bash
sudo ln -s /etc/nginx/sites-available/streamguard /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Step 5: Obtain Free SSL Certificate via Let's Encrypt
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```
Certbot will automatically install the SSL certificates and configure auto-renewal.

---

## 🪟 Option 4: Windows Server Deployment (Using NSSM)

If hosting on a dedicated Windows Server:
1. Download **NSSM (Non-Sucking Service Manager)**.
2. Open Administrator Command Prompt:
   ```cmd
   nssm install StreamGuard "C:\Python315\python.exe" "C:\Users\DELL\Downloads\Video streaming\run.py"
   nssm set StreamGuard AppDirectory "C:\Users\DELL\Downloads\Video streaming"
   nssm start StreamGuard
   ```
3. Set Windows Firewall to allow inbound traffic on port 8000.

---

## 🛡️ Monitoring & Audit Logs in Production

Once your site is live, you can monitor hits, security incidents, and hacker origin locations in real time:

- **Web Dashboard:** Access `https://yourdomain.com/security-dashboard`
- **Hacker Geolocation Log:** Check `logs/threat_locations.log`
- **Access Hit Log:** Check `logs/access_hits.log`
- **Daily Usage & Security Report:** Check `logs/daily_report_YYYY-MM-DD.log`
