from app.schemas.base import DBBaseModel


class Quest(DBBaseModel):
    id: int
    name: str
    topic: str
    skill_reward: float
    description: str
    difficulty: int
    exp_reward: int
