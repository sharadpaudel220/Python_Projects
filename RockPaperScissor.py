import random
# from secrets import choice

while True:
    choices = ['rock', 'paper', 'scissor']
    computer= random.choice(choices)
    user= None

    while user not in choices:
        user= input('Enter a choice: rock or paper or scissor? ').lower()

    if(user==computer):
        print('Computer: ',computer)
        print('user: ', user)
        print('TIE!!')

    elif(user== 'rock'):
        if(computer=='paper'):
             print('Computer: ',computer)
             print('user: ', user)
             print('You loose!')
    
        if(computer=='scissor'):
             print('Computer: ',computer)
             print('user: ', user)
             print('You Win!!!!')

    elif(user== 'scissor'):
        if(computer=='rock'):
             print('Computer: ',computer)
             print('user: ', user)
             print('You loose!')
    
        if(computer=='paper'):
             print('Computer: ',computer)
             print('user: ', user)
             print('You Win!!!!')

    elif(user== 'paper'):
        if(computer=='scissor'):
             print('Computer: ',computer)
             print('user: ', user)
             print('You loose!')
    
        if(computer=='rock'):
             print('Computer: ',computer)
             print('user: ', user)
             print('You Win!!!!')

    play_again = input('play again? Yes or No? ').lower()
    if(play_again!='yes'):
        break
print('bye')