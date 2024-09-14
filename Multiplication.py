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

def MultTask ():
    a = rand.randint(1, 10)
    b = rand.randint(1, 10)
    return str(a) + '*' + str(b)

def SolveTask (task):
    Stask = task.split('*')
    return int(Stask[0]) * int(Stask[1])

def Game ():
    task = MultTask()
    print(task, '= ?')
    answer = IntInput('Answer:')
    if SolveTask(task) == answer:
        print('Correct!\n')
    else:
        print('Wrong!\n')

while(True):
    Game()
    
