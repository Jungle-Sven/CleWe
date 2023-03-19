from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DECIMAL
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from app.models import UserTable

class Skill(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey('usertable.id', ondelete='CASCADE'), index=True)
    topic: str = Column(VARCHAR(255))
    title: str = Column(VARCHAR(255))
    level: int = Column(Integer, default=0)
    experience: float = Column(DECIMAL)

    user: Mapped["UserTable"] = relationship(
        'UserTable',
        back_populates='skills',
    )
