class IndianStatesCensusException(Exception):
    """In this Exception class we are raising the exception"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
