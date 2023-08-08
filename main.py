from fastapi import FastAPI
from fastapi import Depends
from infrastructure.config import get_environment_variables
from app.controllers.user_controller import router as user_router

env = get_environment_variables()

app = FastAPI(title=env.APP_NAME,
    version=env.API_VERSION)

app.include_router(user_router)