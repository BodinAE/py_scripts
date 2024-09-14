import random as rand

def IntInput (message = 'int:'):
    success = False
    while (not(success)):
        inputval = input(message + ' ')
        if not(inputval.isdigit()):
            print('err: Not int')
        else:
            success = True
    inputval = int(inputval)
    return inputval

def Game (tries = 3):
    secretInt = rand.randint(1, 100)
    print ('Guess the number!')
    print('DEBUG: ', secretInt)
    while tries > 0:
        print('Remaning tries: ', tries)
        guess = IntInput()
        if guess == secretInt:
            print('Correct!')
            break
        else:
            print('Wrong!')
        tries -= 1
    if tries > 0:
        print('You won!')
    else:
        print('You lose!')

running = True
while running:
    Game()
    print('type exit to exit')
    if input() == 'exit':
        running = False
