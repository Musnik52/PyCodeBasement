name = input("Hi, What's your name? ")
inc= float(input(f'Well, {name}, what is your monthly income? '))
if inc <= 23000:
    tax = inc*0.1
elif 23000 < inc <= 46000:
    tax = 23000*0.1 + (inc-23000)*0.2
elif 4600 < inc <= 120000:
    tax = 23000*0.3 + (inc-74000)*0.3
elif 120000 < inc <= 220000:
    tax = 23000*0.3 + 74000*0.3 + (inc-100000)*0.4
else:
    tax = 23000*0.3 + 74000*0.3 + 100000*0.4 + (inc-220000)*0.5
print (f'{name}, you need to pay {tax} income tax.')