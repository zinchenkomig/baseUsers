from pydantic import BaseModel


class BaseORM(BaseModel):

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserRead(BaseORM):
    username: str
    email: str


