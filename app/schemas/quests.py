from app.schemas.base import DBBaseModel, BaseModel


class Quest(DBBaseModel):
    id: int
    name: str
    topic: str
    skill_reward: float
    slug: str
    description: str
    difficulty: int
    exp_reward: int


class QuestRequest(DBBaseModel):
    user_id: int


class CompletedResponse(BaseModel):
    trophy_achieved: bool = False
