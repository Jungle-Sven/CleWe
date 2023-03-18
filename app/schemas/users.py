from typing import Optional

from app.schemas.base import DBBaseModel, BaseModel
from app.schemas.skills import Skill
from app.schemas.trophies import Trophy
from app.schemas.quests import Quest


class User(DBBaseModel):
    id: int
    nickname: str
    wallet_address: str
    level: int
    level_total_exp: int
    exp_to_next_level: int
    skills: list[Optional[Skill]]
    trophies: list[Trophy]
    completed_quests: list[Optional[Quest]]
