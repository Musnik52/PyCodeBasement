import pytest
from class_dao import Dao
import time

#Run once before all tests
@pytest.fixture(scope='session', autouse=True)
def dao_init():
    time.sleep(3)
    print('setting up stuff')
    yield()
    print('cleanup')
    time.sleep(3)

#create a dao_connection object once for ALL tests
@pytest.fixture(scope='session')
def dao_connection():
    print('setting up dao')
    return Dao()

#Run before EACH test
@pytest.fixture(scope='function', autouse=True)
def dao_init_before_each_test():
    print('initialize before each function')

#create a NEW dao_connection object for EACH test
@pytest.fixture(scope='function')
def dao_connection_new_each_time():
    print('setting up a new dao for each test')
    return Dao()

def test_get_all(dao_connection):
    assert dao_connection.get_all() == [1, 2, 3, 4, 5]

def test_get_first(dao_connection):
    assert dao_connection.get_first() == [1]

'''

'''