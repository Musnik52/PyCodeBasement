import random
import time

def start_message():    #intro message & timer start
    print('Welcome to "Guess-Mess" - start guessing letters.\nEach correct guess is 5 points!\nEach mistake deducts 1 point.\nFor bonus 100 points - complete within 30 seconds.')
    time.sleep(5)
    print('We begin in 3')
    time.sleep(1)
    print('We begin in 2')
    time.sleep(1)
    print('We begin in 1')
    time.sleep(1)

def begin(x = random.randint(0,9)):     #phrase choosing 
    phrase =[['all','is','well']
        ,['keep','it','real']
        ,['just','do','it']
        ,['always','be','yourself']
        ,['cash','is','king']
        ,['cashflow','is','queen']
        ,['get','over','it']
        ,['let','it','go']
        ,['sharing','is','caring']
        ,['seize','the','day']]
    return phrase[x]

def countdown():
    return time.time()

def game(a):    #the game
    score = 0
    ans = ""
    fans = " ".join(a)
    for k in range(3):
        ans = ans+('_'*len(a[k]))+' '
    while True:
        print(ans)
        print(f'Your current score is: {score}')
        guess = input('Guess a missing letter: ')
        if guess == " " or len(guess) > 1: continue
        elif guess.isalpha() and guess in fans:
            print('Correct!')
            score += 5
            ans = list(ans)
            for l in range(len(fans)):
                if fans[l] == guess: ans[l] = guess
            ans = "".join(ans).rstrip()
            if ans == fans: break
        else:
            print('Wrong!')
            score -= 1
            if score < 0: score = 0
    return score, countdown()

def final_score(totime, score, answer):
    print(f'Game over! Your prase was: "{" ".join(answer)}". Solved within {int(totime)} seconds')
    if totime < 30: print(f'Your final score is: {score + 100}')
    else: print(f'Your final score is: {score}')

def main():
    start_message()
    stime = countdown()
    answer = begin()
    score, etime = game(answer)
    final_score(etime - stime, score, answer)

main()