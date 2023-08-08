from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.config import get_environment_variables

env = get_environment_variables()
class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            env.MYSQL_USER,
            env.MYSQL_PASSWORD,
            env.MYSQL_HOST,
            env.MYSQL_PORT,
            env.MYSQL_DATABASE
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()