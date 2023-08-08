from abc import ABC, abstractmethod
from app.entities.mysql.user import User

class UserGateway(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def save_user(self, name, email, cpf, phone_number):
        pass