import datetime as dt
from configparser import ConfigParser
import logging

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)
config = ConfigParser()
config.read("c:/git/pyCodeBasement/Logging123/config.conf") #מיקום הקובץ
LOG_LEVEL = config["lo"]["level"] # מחלקה + נתון
print(LOG_LEVEL)
LOG_FILE_NAME_PREFIX = config["lo"]["logfile_name_prefix"] # מחלקה + שימוש הנתון באותה נמחלקה
LOG_FILE_NAME_EXT = config["lo"]["logfile_name_ext"] # מחלקה + שימוש הנתון באותה נמחלקה

print(LOG_LEVEL)
print(LOG_FILE_NAME_PREFIX)
print(LOG_FILE_NAME_EXT)
today = dt.datetime.today() #שליפת התאריך היום
day = f'{today.year:02d}-{today.month:02d}-{today.day:02d}' #פורמט 2 ספרות
filename = f'{LOG_FILE_NAME_PREFIX}-{day}.{LOG_FILE_NAME_EXT}' #בניית שם הקובץ
print(filename)
logging.basicConfig(level=LOG_LEVEL) #ציון הרמה
logger = logging.getLogger("-admin facade-") #ציון מיקום\איזה קובץ

logging.info('Info message')

def print_to_log(level, msg): #פונ' להכנסת נתונים לקובץ
    logger.log(level, f'{logging.getLogger("-admin facade-")}{dt.datetime.now()}{logging.getLevelName(level)}{msg}')

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

print_to_log(logging.INFO, 'starting facade ....')
try:
    print_to_log(logging.DEBUG, 'input x about to happen')
    x = int(input('number: '))
    print_to_log(logging.DEBUG, 'input x was success')
    print_to_log(logging.DEBUG, f'the input is {x}')
except ValueError:
    #print('invalid')
    print_to_log(logging.CRITICAL, "wrong input for int")

def repo_add_ticket(obj_ticket):
    print_to_log(logging.DEBUG, f'adding ticket : {obj_ticket}')
    try:
        pass
    except BaseException as e:
        print_to_log(logging.ERROR, 'FAILED QUERY: INSERT INTO TICKETS ...')
        print_to_log(logging.ERROR, f'error during adding ticket : {obj_ticket}, error: {e}')