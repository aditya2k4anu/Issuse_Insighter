from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from .database import Base

class RoleEnum(PyEnum):
    REPORTER = "REPORTER"
    MAINTAINER = "MAINTAINER"
    ADMIN = "ADMIN"

class StatusEnum(PyEnum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.REPORTER)

class Issue(Base):
    __tablename__ = "issues"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    file_path = Column(String, nullable=True)
    severity = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.OPEN)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class DailyStats(Base):
    __tablename__ = "daily_stats"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(StatusEnum))
    count = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)
