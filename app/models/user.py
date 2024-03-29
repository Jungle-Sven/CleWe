from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.orm import relationship, Mapped

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models import Quest, Skill, Trophy, UsersQuests


class UserTable(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    nickname: int = Column(VARCHAR(255))
    wallet_address: str = Column(VARCHAR(255))
    level: int = Column(Integer, default=0)
    level_total_exp: int = Column(Integer)
    exp_to_next_level: int = Column(Integer)
    email: str = Column(VARCHAR(128), unique=True, index=True)
    password: str = Column(Text)
    completed_quests: Mapped[list['Quest']] = relationship(
        secondary="usersquests", back_populates='users'
    )
    users_quests: Mapped[list['UsersQuests']] = relationship(
        back_populates='user'
    )
    skills: Mapped[list['Skill']] = relationship(
        'Skill', back_populates='user', lazy='select'
    )

    trophies: Mapped[list['Trophy']] = relationship(
        'Trophy', back_populates='user', lazy='select'
    )
