month = int(input('What is the month in question? '))
if month == 2:
    year = int(input('What is the year in question? '))
    if (year%4==year%100==year%400==0) or (year%4==0!=year%100): print(f'{year} is a leap year! and month {month} has 29 days.')
    else: print (f'{year} is a regular year, so month {month} has 28 days.')
else:
    if month == 4 or month == 6 or month == 9 or month == 11: print(f'Month {month} has 30 days.')
    else: print(f'It has 31 days.')