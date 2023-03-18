import random

from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session

from app.api import deps
from app.api.exceptions import NotFound, QuestAlreadyCompleted
from app.models import Quest, UserTable, Trophy
from app.schemas import quests


router = APIRouter()

IMAGE_NAMES = ['completedq-l.png', 'gempost-b.png']


@router.get('/', response_model=list[quests.Quest], status_code=http_status.HTTP_200_OK)
def get_all_quests(db: Session = Depends(deps.get_db)):
    return db.query(Quest).all()


@router.patch(
    '/{slug}/complete/',
    response_model=quests.CompletedResponse,
    status_code=http_status.HTTP_200_OK
)
def complete_quest(slug: str, id: int, db: Session = Depends(deps.get_db)):
    quest = (
        db.query(Quest)
        .filter(Quest.slug == slug)
        .first()
    )
    user = db.query(UserTable).filter(UserTable.id == id).first()
    if not (quest and user):
        raise NotFound()

    if quest in user.completed_quests:
        raise QuestAlreadyCompleted()

    user.completed_quests.append(quest)
    trophy = Trophy(
        user_id=user.id,
        img_url=IMAGE_NAMES[random.randint(0, 1)],
        description='I love blockchain'
    )
    db.add(user)
    db.add(trophy)
    db.commit()
    return quests.CompletedResponse(trophy_achieved=True)
