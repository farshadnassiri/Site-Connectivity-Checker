## 🌐 Site Connectivity Checker

Check if multiple websites are online with a fast and friendly Streamlit app. Add URLs, run a concurrent availability check, and see results instantly. Perfect for quick health checks and demos. ⚡

---

### ✨ Features
- ✅ Check multiple websites concurrently
- 🧠 Smart URL normalization (auto-adds https://www.)
- 🪄 Clean Streamlit UI with status indicators
- 🧵 Uses `ThreadPoolExecutor` for speed

---

### 📦 Requirements
- Python 3.9+
- Packages: `streamlit`, `requests`

Install dependencies:

```bash
pip install streamlit requests
```

---

### 🚀 Quick Start
From the project root:

```bash
streamlit run src/app.py
```

Then open the URL Streamlit prints (typically `http://localhost:8501`).

---

### 🖥️ How to Use
1. Enter a website URL (any format is okay — the app normalizes it).
2. Click "Add URL" to put it in the list. Add as many as you like.
3. Click "Check Availability" to run concurrent checks.
4. See per-site status:
   - ✅ Online
   - ❌ Offline
   - ⏳ Not checked yet
5. Use "Clear URLs" to reset the list.

---

### 🧭 Example
- Input: `google.com`
- Normalized to: `https://www.google.com`
- Status: ✅ Online

---

### 🧩 Architecture Overview

```mermaid
flowchart LR
  U[User] -->|types URLs| UI[Streamlit UI]
  UI --> BTN["Check Availability"]
  BTN --> EXEC[ThreadPoolExecutor]
  EXEC -->|concurrent GET| REQ[requests]
  REQ -->|HTTP(S)| S1[(Site 1)]
  REQ -->|HTTP(S)| S2[(Site 2)]
  REQ -->|HTTP(S)| S3[(Site N)]
  REQ -. status .-> UI
  UI -->|render statuses| U
```

---

### ⚙️ Implementation Notes
- URL normalization strips any existing scheme and `www.`, then rebuilds as `https://www.<domain>`.
- Requests are made with a desktop-like User-Agent and a 5s timeout.
- A 200 HTTP status is considered "Online"; any exception counts as "Offline".

---

### 🧪 Local Development Tips
- Run with auto-reload: `streamlit run src/app.py`
- Modify logic in `src/app.py` (functions: `format_url`, `check_site_availability`, `main`).
- If you are on WSL, ensure your browser can open `localhost:8501`.

---

### 🛠️ Troubleshooting
- "Module not found": install dependencies with `pip install streamlit requests`.
- Sites always show ❌: check network, VPN, firewall, or try increasing timeout in code.
- Non-200 but reachable sites will still show ❌ (by design). Adjust logic if needed.

---

### 🗺️ Roadmap Ideas
- Custom timeout and retries
- CSV import/export of URL lists
- Display response time and HTTP code
- Persist URL list in session or file

---

### 📄 License
Choose a license (e.g., MIT) and add it here if you plan to share publicly.


