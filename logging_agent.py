
import logging

class LoggingAgent:
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger('LoggingAgent')
        # Clear any existing handlers
        if self.logger.handlers:
            self.logger.handlers.clear()
        self.logger.setLevel(log_level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)
        # Prevent propagation to root logger
        self.logger.propagate = False

    def log(self, message, level=logging.INFO):
        """ Logs a message to the console or a file. """
        self.logger.log(level, message)
