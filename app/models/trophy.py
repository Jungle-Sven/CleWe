from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Text
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from app.models import UserTable


class Trophy(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey('usertable.id', ondelete='CASCADE'), index=True)
    img_url: str = Column(VARCHAR(255))
    tx_hash: Optional[str] = Column(VARCHAR(255), unique=True)
    description: str = Column(Text)

    user: Mapped["UserTable"] = relationship(
        'UserTable',
        back_populates='trophies',
    )

