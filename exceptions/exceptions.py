try:
    f1 = open('c:/temp/1.txt')
    for l in f1.readlines():
        print(l, end='')
except FileNotFoundError as e:
    print(e)
    print('That means the file is not here, buddy')
finally:
    print('DUMBASS!')
    f1.close()