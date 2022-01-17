from facade_base import FacadeBase

class AnonymusFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def login(self, username, password):
        pass

    def create_user(user):
        pass

    def __str__(self):
        return f'{super().__init__}'