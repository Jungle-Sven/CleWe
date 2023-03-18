from app.schemas.base import DBBaseModel


class Skill(DBBaseModel):
    id: int
    topic: str
    title: str
    level: int
    experience: float
