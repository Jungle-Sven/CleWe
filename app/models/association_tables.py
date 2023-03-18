from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from app.models import UserTable, Quest


class UsersQuests(Base):
    user_id: Mapped[int] = Column(ForeignKey('usertable.id'), primary_key=True)
    quest_id: Mapped[int] = Column(ForeignKey('quest.id'), primary_key=True)
    user: Mapped["UserTable"] = relationship(back_populates="users_quests")
    quest: Mapped["Quest"] = relationship(back_populates="users_quests")
