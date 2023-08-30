from fastapi import APIRouter, HTTPException
from schemas import UserCreateInput, StandartOutput, ErrorOutput
from services import UserService

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model=StandartOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))