# app/routers/issues.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Issue(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    status: str

# In-memory store (for demo only)
issues_db: List[Issue] = []

@router.get("/", response_model=List[Issue])
def get_issues():
    return issues_db

@router.post("/", response_model=Issue)
def create_issue(issue: Issue):
    issues_db.append(issue)
    return issue
