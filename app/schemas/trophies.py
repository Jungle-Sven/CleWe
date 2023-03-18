from typing import Optional

from app.schemas.base import DBBaseModel


class Trophy(DBBaseModel):
    id: int
    tx_hash: Optional[str] = None
    img_url: str
    description: str