from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session

from app.api import deps
from app.api.exceptions import NotFound, TrophyHasHash
from app.models import Trophy
from app.schemas import trophies


router = APIRouter()


@router.get(
    '/',
    response_model=list[trophies.Trophy],
    status_code=http_status.HTTP_200_OK,
)
def get_all_trophies(db: Session = Depends(deps.get_db)):
    return db.query(Trophy).all()


@router.put(
    '/{id}/',
    response_model=trophies.Trophy,
    status_code=http_status.HTTP_200_OK,
)
def set_trophy_hash(
    id: int,
    request_body: trophies.TrophyRequest,
    db: Session = Depends(deps.get_db),
):
    trophy = db.query(Trophy).filter(Trophy.id == id).first()
    if not trophy:
        raise NotFound()

    if trophy.tx_hash:
        raise TrophyHasHash()

    setattr(trophy, 'tx_hash', request_body.tx_hash)
    db.add(trophy)
    db.commit()
    return trophy
