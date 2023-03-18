import random

from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from faker import Faker

from app.api import deps
from app import models


router = APIRouter()

fake = Faker()

QUEST_NAMES = ['Crypto Wallet', 'Dex', 'DAO']

class Msg(BaseModel):
    msg: str


@router.get("/", response_model=Msg)
def test() -> Msg:
    """
    API Test
    """
    return Msg(msg='Hello world!')

@router.post('/fill-db', status_code=http_status.HTTP_200_OK)
def fill_db(db: Session = Depends(deps.get_db)):

    try:
        users = [
            models.UserTable(
                nickname=fake.name(),
                wallet_address=fake.word(),
                level=random.randint(0, 100),
                level_total_exp=random.randint(0, 100),
                exp_to_next_level=random.randint(0, 100),
            ) for _ in range(3)
        ]
        quests = [
            models.Quest(
                name=fake.word(),
                slug=f'slug: {i}',
                topic=QUEST_NAMES[i],
                skill_reward=round(random.uniform(0, 10), 1),
                description=fake.word(),
                difficulty=random.randint(1, 5),
                exp_reward=random.randint(0, 100),
            ) for i in range(len(users))
        ]

        db.bulk_save_objects(objects=users)
        db.bulk_save_objects(objects=quests)

        users = db.query(models.UserTable).all()
        quests = db.query(models.Quest).all()

        for i in range(len(users)):
            users[i].completed_quests.append(quests[i])

        skills = [
            models.Skill(
                user_id=users[i].id,
                topic=QUEST_NAMES[i].lower(),
                title=fake.word(),
                level=random.randint(0, 100),
                experience=round(random.uniform(0, 10), 1),
            ) for i in range(len(users))
        ]

        db.bulk_save_objects(objects=skills)
        db.commit()
        print(f"All tables are filled")
        return Msg(msg='All tables have been filled!')
    except Exception as exc:
        print(f"Error: {exc}")
        raise exc


@router.delete('/clear-db', status_code=http_status.HTTP_204_NO_CONTENT)
def clear_db(db: Session = Depends(deps.get_db)):
    db.query(models.UsersQuests).delete()
    db.query(models.UserTable).delete()
    db.query(models.Quest).delete()
    db.query(models.Trophy).delete()
    db.query(models.Skill).delete()
    db.commit()
    print("All tables cleared")
    return Msg(msg='All tables have been cleared!')
