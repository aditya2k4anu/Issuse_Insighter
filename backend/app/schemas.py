from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Role(str, Enum):
    REPORTER = "REPORTER"
    MAINTAINER = "MAINTAINER"
    ADMIN = "ADMIN"

class Status(str, Enum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class IssueCreate(BaseModel):
    title: str
    description: str
    severity: str

class IssueResponse(IssueCreate):
    id: int
    status: Status
    created_at: datetime
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
