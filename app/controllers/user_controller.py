from fastapi import APIRouter, Depends, HTTPException
from app.entities.dtos.user_schemas import UserCreateSchema
from app.usecases.user_usecase import UserUseCase
from infrastructure.db.mysql.repositories.user_repository import UserRepository 
from infrastructure.logging.logging_implementation import LoggingImplementation
from infrastructure.db.mysql.settings.connection import DBConnectionHandler 

router = APIRouter()

user_repository = UserRepository()
log_implementation = LoggingImplementation()
user_usecase = UserUseCase(user_repository,
                           log_implementation) #adiciona todas as dependencias que vao ser carregadas para o gateway no usecase
get_user_usecase = lambda: user_usecase

@router.post("/users/", response_model=None)
def create_user(
    user_data: UserCreateSchema,
    user_usecase: UserUseCase = Depends(get_user_usecase)
):
    try:
        user_usecase.create_user(user_data.username, user_data.email, user_data.cpf, user_data.phone_number)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
