from infrastructure.db.mysql.repositories.user_repository import UserRepository 

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username, email, cpf, phone_number):
        # Lógica de validações e criação do usuário
        new_user = self.user_repository.save_user(username, email, cpf, phone_number)
        return new_user
