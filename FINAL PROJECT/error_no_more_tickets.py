class NoMoreTicketsLeft(Exception):
    def __init__(self, message="There are no more tickets available. Order canceled!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'NoMoreTicketsLeft: {self.message}'