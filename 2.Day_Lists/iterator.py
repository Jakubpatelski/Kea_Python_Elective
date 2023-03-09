i=0

while i < 5:
    print(i)
    i+=1

print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution,
#  so If you want to see prints during whle loop, print to the input box (This is specific to this platform)


num = 15
guess = 0
guess_attemps = 3
guess_number = 0

while  guess_number < guess_attemps:
    guess_number+=1
    guess = input(f'this is your attempt {guess_number}/3.guess number 1-20: ')
    # guess = int(input(f'this is your attempt {guess_number}/3.guess number 1-20: '))

    if num == int(guess):
        print(f'you guessed the number, the number is {num}')
        break
    elif num > int(guess):
        print(f'your guess {guess}. The num is higher')
    
    elif num < int(guess):
        print(f'you guess {guess}. the number is lower ')
if num != int(guess):
     print(f'Sorry you lost. The number was {num}')
# if guess_number == guess_attemps:
#         print(f'Sorry you lost. The number was {num}')

    



        
     