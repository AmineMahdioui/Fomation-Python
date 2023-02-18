import random
rand=str(random.randint(0,999))
while len(rand)!=3:
    rand='0'+rand


correct_numbr=rand

print(""" game rules:
this is a guessing game 
bagels kht2ti
fermi correct digit in correct place
pico correct digit in incorrect place """)


max_tries=20
tries=0
while tries < max_tries:
    guess=input(f'Give me a number of 3 digits {tries+1} guess:  ')
    while len(guess)!=3:
        guess=input('Your guess is not 3 digits long try again: ')
    Results=''
    if str(guess) == correct_numbr:
        print('You won the game!')
    else:
        for i in range(3):

            if guess[i]==correct_numbr[i]:
                Results+='fermi '
            elif guess[i] in correct_numbr:
                Results+='Pico '
    if not Results:
        Results ="Bagels"

    print(Results)
    tries+=1