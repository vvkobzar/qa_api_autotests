from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class TokenSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    refresh_token: str = Field(alias='refreshToken')


class RefreshResponseSchema(BaseModel):
    token: TokenSchema
