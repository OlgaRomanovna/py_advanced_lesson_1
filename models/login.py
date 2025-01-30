from pydantic import BaseModel


class LoginData(BaseModel):
    email: str | None = None
    password: str | None = None


class ResponseLogin(BaseModel):
    id: int
    token: str



