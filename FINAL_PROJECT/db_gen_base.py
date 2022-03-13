from abc import ABC, abstractmethod
from logger import Logger
from db_repo_connection_pool import DbRepoConnectionPool

class BaseDbDataGen(ABC):

    @abstractmethod
    def __init__(self):
        self.repool = DbRepoConnectionPool.get_instance()
        self.repo = self.repool.get_connection()
        self.logger = Logger.get_instance()

    def get_data(self):
        pass

    def make_airlines(self, num):
        pass

    def make_customers(self, num):
        pass

    def make_flights_per_company(self, num):
        pass

    def make_tickets_per_customer(self, num):
        pass

    def make_countries(self, num):
        pass