import datetime
import logging

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

logging.basicConfig(level='DEBUG')
logger = logging.getLogger("-admin facade-")

logging.info('info message')

def print_to_log(level, msg):
    logger.log(level, f'{datetime.datetime.now()} {logging.getLevelName(level)} {msg}')

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

print_to_log(logging.INFO, 'starting facade ....')
try:
    print_to_log(logging.DEBUG, 'input x about to happen')
    x = int(input('number: '))
    print_to_log(logging.DEBUG, 'input x was success')
    print_to_log(logging.DEBUG, f'x is {x}')
except ValueError:
    #print('invalid')
    print_to_log(logging.CRITICAL, "wrong input for int")

def repo_add_ticket(obj_ticket):
    print_to_log(logging.DEBUG, f'adding ticket : {obj_ticket}')
    try:
        pass
    except BaseException as e:
        print_to_log(logging.ERROR, f'error during adding ticket : {obj_ticket}, error: {e}')