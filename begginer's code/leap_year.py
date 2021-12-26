year = int(input('What is the year in question? '))
if (year%4==year%100==year%400==0) or (year%4==0!=year%100): print(f'{year} is a leap year!')
else: print (f'{year} is a regular year.')