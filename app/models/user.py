from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship, Mapped

from app.db.base_class import Base
from app.models.association_tables import users_quests

if TYPE_CHECKING:
    from app.models import Quest, Skill, Trophy


class User(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    nickname: int = Column(VARCHAR(255))
    wallet_address: str = Column(VARCHAR(255))
    level: int = Column(Integer, default=0)
    level_total_exp: int = Column(Integer)
    exp_to_next_level: int = Column(Integer)
    completed_quests: Mapped[list['Quest']] = relationship(
        secondary=users_quests, back_populates='users'
    )

    skills: Mapped[list['Skill']] = relationship(
        'Skill', back_populates='user', lazy='select'
    )

    trophies: Mapped[list['Trophy']] = relationship(
        'Trophy', back_populates='user', lazy='select'
    )
