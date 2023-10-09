from app.gateways.user_gateway import UserGateway
from app.gateways.logging_gateway import LoggingInterface

class UserUseCase:
    def __init__(self, user_gateway: UserGateway, logging_service: LoggingInterface):
        self.user_gateway = user_gateway
        self.logging_gateway = logging_service

    def create_user(self, username, email, cpf, phone_number):
        # Lógica de validações e criação do usuário
        new_user = self.user_gateway.save_user(username, email, cpf, phone_number)
        return new_user
