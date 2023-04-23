from typing import Generator
from datetime import datetime

from sqlalchemy.orm import Session
from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError

from app.db.session import SessionLocal
from app.core.config import settings
from app.schemas.auth_schema import TokenPayload
from app.schemas.auth_schema import JWTTokenResponse
from app.models.user import UserTable
from app import utils


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl='/login',
    scheme_name='JWT',
)


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as db:
        yield db


async def get_current_user(
    token: str = Depends(reuseable_oauth), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token expired',
                headers={'WWW-Authenticate': 'Bearer'},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    user = (
        db.query(UserTable).filter(UserTable.email == token_data.sub).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Could not find user',
        )

    return user


async def get_new_access_token(
    token: str = Depends(reuseable_oauth), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        token_data = TokenPayload(**payload)
        access_token = utils.create_access_token(token_data.sub)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    jwt_token = JWTTokenResponse(
        access_token=access_token, refresh_token=token
    )
    return jwt_token
