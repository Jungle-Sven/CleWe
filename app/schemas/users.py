from typing import Optional

from pydantic import validator, Field

from app.schemas.base import DBBaseModel, BaseModel
from app.schemas.skills import Skill
from app.schemas.trophies import Trophy
from app.schemas.quests import Quest
from app import utils


class User(DBBaseModel):
    id: int
    nickname: str
    wallet_address: str
    level: int
    level_total_exp: int
    exp_to_next_level: int
    skills: list[Optional[Skill]]
    trophies: list[Optional[Trophy]]
    completed_quests: list[Optional[Quest]]


class UserAuth(BaseModel):
    email: str
    password: str


class UserCreate(DBBaseModel):
    nickname: str
    wallet_address: str
    email: str
    password: str = Field(min_length=9)

    @validator('password')
    def get_hashed_password(cls, value):
        return utils.get_hashed_password(value)


class UserResponse(User):
    level_total_exp: Optional[int]
    exp_to_next_level: Optional[int]
    skills: list[Optional[Skill]]
    trophies: list[Optional[Trophy]]
    completed_quests: list[Optional[Quest]]
