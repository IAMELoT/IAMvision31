# logging_agent.py

import logging

class LoggingAgent:
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger('LoggingAgent')
        self.logger.setLevel(log_level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def log(self, message, level=logging.INFO):
        """ Logs a message to the console or a file. """
        self.logger.log(level, message)