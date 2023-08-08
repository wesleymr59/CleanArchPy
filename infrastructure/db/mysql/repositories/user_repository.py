from app.gateways.user_gateway import UserGateway
from infrastructure.db.mysql.settings.connection import DBConnectionHandler 
from app.entities.mysql.user import User

class UserRepository(UserGateway):
    def get_user_by_id(self, user_id):
        # Implementação para buscar usuário por ID no banco de dados
        with DBConnectionHandler() as database:
            try:
                print("faz a operação de GETUSER no mysql")
                print(User.nome)
            except Exception as exception:
                database.session.rollback()
                raise exception


    def save_user(self, name, email, cpf, phone_number):
        # Implementação para salvar usuário no banco de dados
        with DBConnectionHandler() as database:
            try:
                print("faz a operação de SAVEUSER no mysql")
                print(name)
            except Exception as exception:
                database.session.rollback()
                raise exception