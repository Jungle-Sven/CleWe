from typing import Optional

from app.schemas.base import DBBaseModel, BaseModel


class Trophy(DBBaseModel):
    id: int
    tx_hash: Optional[str] = None
    img_url: str
    description: str


class TrophyRequest(BaseModel):
    tx_hash: str
