# app/routers/stats.py
from fastapi import APIRouter
from collections import Counter

router = APIRouter()

# Reuse issues_db from issues router (for demo)
from app.routers.issues import issues_db

@router.get("/open_by_severity")
def open_by_severity():
    counts = Counter()
    for issue in issues_db:
        if issue.status == "OPEN":
            counts[issue.severity] += 1
    return counts
