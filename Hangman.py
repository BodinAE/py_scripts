import random as rand

wordlist = ['apple', 'hangman', 'home', 'python', 'mouse']
guessword = ''
displayword = ''
guessedlist = []
tries = 5

def StartGame(newtries = 5):
    global guessword, displayword, guessedlist, tries
    guessword = rand.choice(wordlist)
    displayword = len(guessword) * '_'
    guessedlist = []
    tries = newtries
    Game()

def PrintDisplayWord():
    global guessword, displayword
    for i in range (len(displayword)):
        print(displayword[i], end = ' ')
    print('')

def PrintGuessedList():
    global guessedlist
    print("Guessed letters", end = ': ')
    for i in range (len(guessedlist)):
        print(guessedlist[i], end = ' ')
    print('')

def PrintTries():
    global tries
    print('Remaining tries: ' + str(tries))

def UpdateDisplayWord(guess):
    global guessword, displayword
    dwordlist = []
    for i in range (len(displayword)):
        dwordlist.append(displayword[i])
    for i in range (len(guessword)):
        if guessword[i] == guess:
            dwordlist[i] = guess
    displayword = dwordlist[0]
    for i in range (1, len(dwordlist)):
        displayword += dwordlist[i]          

def Game():
    global guessword, displayword, guessedlist, tries
    running = True
    while (tries > 0):
        PrintDisplayWord()
        PrintGuessedList()
        PrintTries()
        guess = input('Guess a letter: ')
        if not(guess in guessedlist):
            guessedlist.append(guess)
            if guess in guessword:
                UpdateDisplayWord(guess)
            else:
                tries -= 1
        else:
            print('Letter already guessed')
        print('')
        if not('_' in displayword):
            break;
    if not(tries > 0):
        print('You lose!')
    else:
        PrintDisplayWord()
        print('You won!')
            
        
StartGame()
