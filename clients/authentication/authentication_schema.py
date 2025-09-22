from pydantic import BaseModel, Field
from tools.fakers import fake


class TokenSchema(BaseModel):
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias='refreshToken')
