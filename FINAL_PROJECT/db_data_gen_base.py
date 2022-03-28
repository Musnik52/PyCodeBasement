from abc import ABC, abstractmethod
from db_repo import DbRepo
from db_config import local_session, config
from logger import Logger
from db_repo_connection_pool import DbRepoConnectionPool


class BaseDbDataGen(ABC):

    @abstractmethod
    def __init__(self):
        self.repool = DbRepoConnectionPool.get_instance()
        self.repo = self.repool.get_connection()
        self.logger = Logger.get_instance()
