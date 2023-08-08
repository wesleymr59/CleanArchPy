from fastapi import APIRouter, Depends, HTTPException
from app.entities.dtos.user_schemas import UserCreateSchema
from app.usecases.user_usecase import UserUseCase
from infrastructure.db.mysql.repositories.user_repository import UserRepository 
from infrastructure.db.mysql.settings.connection import DBConnectionHandler 

router = APIRouter()

user_repository = UserRepository()
user_usecase = UserUseCase(user_repository)

@router.post("/users/", response_model=None)
def create_user(
    user_data: UserCreateSchema,
    user_usecase: UserUseCase = Depends(lambda: user_usecase)
):
    try:
        user_usecase.create_user(user_data.username, user_data.email, user_data.cpf, user_data.phone_number)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
