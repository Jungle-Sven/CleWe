from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class TokenPayload(BaseModel):
    exp: int
    sub: str


class JWTTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
