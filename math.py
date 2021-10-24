from typing import DefaultDict


def div(j,k):
    return j/k
def add(j,k):
    return j+k
def mul(j,k):
    return j*k
def sub(j,k):
    return j-k

x = int(input('Enter a number: '))
if x == 0: x = 1
y = int(input('Enter another number: '))
if y == 0: y =1
print(f'div: {div(x,y)} add: {add(x,y)}, mul: {mul(x,y)} sub: {sub(x,y)}')