import threading
import time


def wait():
    print('Waiting 1 sec')
    time.sleep(1)
    print('Done waiting')


# יצירת 2 נתיבים עבור הפונ' להרצה מקבילה
t1 = threading.Thread(target=wait)
t2 = threading.Thread(target=wait)
# הפעלת הנתיבים והפונ' הרצויות
t1.start()
t2.start()
# ווידוא שהתוכנית תסתיים רק אחרי שהפונ' סיימו את פעולתן
t1.join()
t2.join()
