from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str

class StandartOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detail: str