from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportData(BaseModel):
    url: str
    text: str


class ResponseModel(BaseModel):
    data: UserData
    support: SupportData
