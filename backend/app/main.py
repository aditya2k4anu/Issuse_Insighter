from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
import prometheus_client
from prometheus_client import make_asgi_app

from app.routers import issues, stats  # ✅ Assuming you have these

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app with custom docs URL
app = FastAPI(
    title="Issues & Insights Tracker API",
    version="1.0.0",
    docs_url="/api/docs",           # ✅ Custom docs URL
    redoc_url="/api/redoc",         # Optional
    openapi_url="/api/openapi.json" # OpenAPI schema
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Issues Tracker Backend"}

# Mount Prometheus metrics
app.mount("/metrics", make_asgi_app())

# ✅ Include your routers
app.include_router(issues.router, prefix="/issues", tags=["Issues"])
app.include_router(stats.router, prefix="/stats", tags=["Stats"])
