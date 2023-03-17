
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Text, DECIMAL

from app.db.base_class import Base


class Skill(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), index=True)
    topic: str = Column(VARCHAR(255))
    title: str = Column(VARCHAR(255))
    level: int = Column(Integer, default=0)
    experience: int = Column(DECIMAL)
