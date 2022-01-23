import datetime
import time

class MyTimer(object):

    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.name = 'Boris Almighty - Timelord'
        return cls._instance

    def start_timer(self):
        return datetime.datetime.now()

    def get_timer(self, start_time):
        return datetime.datetime.now() - start_time

sing1 = MyTimer.get_instance()
sing2 = MyTimer.get_instance()
print(sing1 == sing2)
print(sing1.name)
sing11 = sing1.start_timer()
time.sleep(3)
sing22 = sing2.get_timer(sing11)
print(sing22)