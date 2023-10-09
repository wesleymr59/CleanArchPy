# Em infrastructure/logging_implementation.py
import logging
from app.gateways.logging_gateway import LoggingInterface

class LoggingImplementation(LoggingInterface):
    def log_debug(self, message):
        logging.debug(message)

    def log_info(self, message):
        logging.info(message)

    # Outros métodos de log conforme necessário
