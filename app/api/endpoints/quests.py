from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session

from app.api import deps
from app.api.exceptions import NotFound, QuestAlreadyCompleted
from app.models import Quest, UserTable
from app.schemas import quests


router = APIRouter()


@router.get('/', response_model=list[quests.Quest], status_code=http_status.HTTP_200_OK)
def get_all_users(db: Session = Depends(deps.get_db)):
    return db.query(Quest).all()


@router.patch(
    '/{slug}/complete',
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
    db.add(user)
    db.commit()
    return quests.CompletedResponse(trophy_achieved=True)
