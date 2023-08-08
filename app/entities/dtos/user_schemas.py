from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    username: str
    email: str
    cpf: str
    phone_number: str

class UserResponseSchema(BaseModel):
    user_id: int
    username: str
    email: str