#!/usr/bin/python

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print (f"{threadName} {time.ctime(time.time())}")

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) ) # daemon
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) ) # daemon
except:
   print ("Error: unable to start thread")
print('123')
#while 1:
   #pass