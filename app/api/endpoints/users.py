from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session

from app.api import deps
from app.api.exceptions import NotFound
from app.models import UserTable
from app.schemas import users


router = APIRouter()


@router.get('/', response_model=list[users.User], status_code=http_status.HTTP_200_OK)
def get_all_users(db: Session = Depends(deps.get_db)):
    return db.query(UserTable).all()

@router.get('/{id}/', response_model=users.User, status_code=http_status.HTTP_200_OK)
def get_single_user(id: int, db: Session = Depends(deps.get_db)):
    user = db.query(UserTable).filter(UserTable.id == id).first()
    if not user:
        raise NotFound()

    return user
