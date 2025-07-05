# 🛠️ Issues & Insights Tracker

A mini SaaS portal for submitting and tracking issues, built with FastAPI, PostgreSQL, and a React + Vite frontend. Includes Prometheus for monitoring metrics.

---

## 📁 Project Structure

.
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── database.py
│ │ ├── models.py
│ │ ├── routers/
│ │ │ ├── issues.py
│ │ │ └── stats.py
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── vite.config.js
│
├── docker-compose.yml
└── README.md

yaml
Copy
Edit

---

## ✅ Prerequisites

Before you start, make sure you have installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/) (optional but useful)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/issues-insights-tracker.git
cd issues-insights-tracker
2️⃣ Start the Full Application
Use Docker Compose to run everything:

bash
Copy
Edit
docker-compose up --build
This command will:

Launch PostgreSQL database

Start FastAPI backend at http://localhost:8000

Launch React frontend at http://localhost:5173

🔧 Backend (FastAPI)
Tech Stack
FastAPI

SQLAlchemy

PostgreSQL

Prometheus

If Running Without Docker
bash
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
🎨 Frontend (React + Vite)
Tech Stack
React

Vite

Axios

Tailwind CSS

Run Without Docker
bash
Copy
Edit
cd frontend
npm install
npm run dev
This will start the frontend at http://localhost:5173.

📊 API & Metrics
API Docs (Swagger): http://localhost:8000/api/docs

Prometheus Metrics: http://localhost:8000/metrics

🧪 Endpoints Overview
Some available endpoints (depending on implementation):

POST /issues – Submit an issue

GET /issues – List all issues

GET /stats/open_by_severity – View open issue stats

GET /metrics – Prometheus metrics

🛠 Troubleshooting
Ensure your Docker is running.

If npm ci fails, replace it with npm install in frontend/Dockerfile.

If Swagger docs are not showing, make sure routes are mounted under /api.

🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss what you would like to change.

🛡️ License
This project is licensed under the MIT License.

