while True:
    num = input('Enter a number. A negative input will end the program: ')
    if int(num) < 0: break
    i = len(num)
    k = 0
    while i > 0:  
        n = num [i-1] 
        k += int(n)
        i -= 1
    print(f"The sum of the number's digits is: {k}")