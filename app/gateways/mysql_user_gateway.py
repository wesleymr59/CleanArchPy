from app.gateways.user_gateway import UserGateway
from app.entities.mysql.user import User

class MySQLUserGateway(UserGateway):
    def save_user(self, user: User):
        # Implementação para salvar o usuário no MySQL
        pass

    def get_user_by_id(self, user_id: int) -> User:
        # Implementação para buscar usuário por ID no MySQL
        pass