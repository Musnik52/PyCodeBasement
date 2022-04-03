import time
import threading
from db_repo import DbRepo
from db_config import local_session, config
from tables.users import Users

class DbRepoConnectionPool(object):
    
    _instance = None
    _lock = threading.Lock()
    _lock_pool = threading.Lock()
    _max_connections = int(config["db"]["max_conn"])

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance: return cls._instance
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls.__new__(cls)
                cls._instance.connections = [DbRepo(local_session) for i in range(cls._max_connections)]
            return cls._instance

    def get_free_count(self):
        return len(self.connections)

    def get_max_possible_connections(cls):
        return cls._max_connections

    def get_connection(self):
       while True:
            if len(self.connections) == 0:
                time.sleep(1/2)
                continue
            with self._lock_pool:
                if len(self.connections) > 0: return self.connections.pop(0)

    def return_connection(self, conn):
        with self._lock_pool: self.connections.append(conn)

'''sing1 = DbRepoConnectionPool.get_instance()
sing2 = DbRepoConnectionPool.get_instance()
print(sing1 == sing2)
print(sing1)
print(sing2)
print(DbRepoConnectionPool.get_max_possible_connections(sing2))

sing1.get_connection()
print(sing1)
sing1.get_connection().add(Users(username='333b0r1s', password='boris1992', email='bo333ris@jb.com', user_role=config['user_roles']['airline']))'''