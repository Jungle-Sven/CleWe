
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Text

from app.db.base_class import Base


class Trophy(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), index=True)
    tx_hash: str = Column(VARCHAR(255), unique=True)
    img_url: str = Column(VARCHAR(255))
    description: str = Column(Text)
