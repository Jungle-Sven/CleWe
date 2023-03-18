from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session

from app.api import deps
from app.api.exceptions import NotFound, TrophyHasHash
from app.models import Trophy
from app.schemas import trophies


router = APIRouter()


@router.put('/{id}/', response_model=trophies.Trophy, status_code=http_status.HTTP_200_OK)
def set_trophy_hash(id: int, tx_hash: str, db: Session = Depends(deps.get_db)):
    trophy = db.query(Trophy).filter(Trophy.id == id).first()
    if not trophy:
        raise NotFound()

    if trophy.tx_hash:
        raise TrophyHasHash()

    setattr(trophy, 'tx_hash', tx_hash)
    db.add(trophy)
    db.commit()
    return trophy

