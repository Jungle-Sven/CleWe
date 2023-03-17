from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Text, Float
from sqlalchemy.orm import relationship, Mapped

from app.db.base_class import Base
from app.models.association_tables import users_quests

if TYPE_CHECKING:
    from app.models import User


class Quest(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(VARCHAR(255))
    slug: str = Column(VARCHAR(255), unique=True)
    topic: str = Column(VARCHAR(255))
    skill_reward = Column(Float)
    description: str = Column(Text)
    difficulty: int = Column(Integer)
    exp_reward: int = Column(Integer)
    users: Mapped[list['User']] = relationship(
        secondary=users_quests, back_populates='completed_quests'
    )
