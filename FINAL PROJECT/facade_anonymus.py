from facade_base import FacadeBase
from db_config import local_session, create_all_entities
from db_repo import DbRepo

repo = DbRepo(local_session)

class AnonymusFacade(FacadeBase):

    def __init__(self):
        super().__init__

    def login(self, username, password):
        pass

    def create_user(user):
        pass

    def __str__(self):
        return f'{super().__init__}'
