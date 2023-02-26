from pydantic import BaseModel


class BaseORM(BaseModel):

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

