from fastapi import APIRouter, Depends, status as http_status
from sqlalchemy.orm import Session

from app.api import deps
from app.api.exceptions import NotFound, IncorrectAuthRequest
from app.models import UserTable
from app.schemas import users, auth_schema
from app import utils


router = APIRouter()


@router.get(
    '/', response_model=list[users.User], status_code=http_status.HTTP_200_OK
)
def get_all_users(db: Session = Depends(deps.get_db)):
    return db.query(UserTable).all()


@router.get(
    '/{id}/', response_model=users.User, status_code=http_status.HTTP_200_OK
)
def get_single_user(id: int, db: Session = Depends(deps.get_db)):
    user = db.query(UserTable).filter(UserTable.id == id).first()
    if not user:
        raise NotFound()

    return user


@router.post(
    '/signup/',
    summary='Create a new user',
    response_model=auth_schema.JWTTokenResponse,
)
async def create_user(
    data: users.UserCreate, db: Session = Depends(deps.get_db)
) -> auth_schema.JWTTokenResponse:
    user = UserTable(**data.dict())
    db.add(user)
    db.flush()
    db.commit()
    db.refresh(user)
    jwt_token = auth_schema.JWTTokenResponse(
        access_token=utils.create_access_token(user.email),
        refresh_token=utils.create_refresh_token(user.email),
    )
    return jwt_token


@router.post('/login/', response_model=auth_schema.JWTTokenResponse)
async def login(
    request_data: users.UserAuth, db: Session = Depends(deps.get_db)
) -> auth_schema.JWTTokenResponse:
    user = (
        db.query(UserTable)
        .filter(UserTable.email == request_data.email)
        .first()
    )
    if not user:
        raise IncorrectAuthRequest()

    if not utils.verify_password(request_data.password, user.password):
        raise IncorrectAuthRequest()

    jwt_token = auth_schema.JWTTokenResponse(
        access_token=utils.create_access_token(user.email),
        refresh_token=utils.create_refresh_token(user.email),
    )
    return jwt_token


@router.get(
    '/get/me/',
    response_model=users.UserResponse,
    status_code=http_status.HTTP_200_OK,
)
async def get_me(user: users.User = Depends(deps.get_current_user)):
    return users.UserResponse.from_orm(user)


@router.get(
    '/get/access-token/',
    response_model=auth_schema.JWTTokenResponse,
    status_code=http_status.HTTP_200_OK,
)
async def get_new_access_token(
    jwt_token: auth_schema.JWTTokenResponse = Depends(
        deps.get_new_access_token
    ),
):
    return jwt_token
