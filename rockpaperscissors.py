import random
import time

from symbol import eval_input

# In this section of the code,
# The imports of extra python functions we'll need 
# for the code - they're still parts of the standard 
# python Libraries, just mot part of the default environment


rock =1
paper = 2
scissors = 3


names = {rock:'Rock', paper: 'Paper', scissors: 'scissors'}

rules = {rock: scissors, paper: rock, scissors:paper}

player_score = 0
computer_score = 0

   
# With this section, the initial rules of the 
# game are created here. The three variables 
# we're using and their relationship is defined, 
# we also provide a variables so we can keep 
# score of the games


def start():
    print('Let us play a rock paper scissors game ')
    while game():
        pass
    scores()
    
#In this section, we begin the game code by 
# defining the start of each round. The end of 
# each play session comes back through here, 
# whether we want to again or not   
    
    
    
def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return player_score()

# In this section, the game is actually contained
# all in  here, asking for the player input, 
# getting the computer input and passing these 
# on to get the results. at the end of that, 
# it then asks if you'd like to play again.  
def move():
    while True:
        print
        player = eval_input('Rock =1 \n Paper =2 \n Scissors =3 \n Make a move: ')
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print('Oops! I didnot understand that Please enter 1,2,3')


#Player input is done here. We give the player 
# information on how to play this particular 
# version of the game and then allow their 
# choice to be used in the next step. We 
# also have something in place in case they 
# enter an invalid option.




def result(player, computer):
    print('1...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('3!')
    time.sleep(0.5)
    print('Computer threw (0)!').format(names[computer])
    
    global player_score, computer_score
    if player == computer:
        print('Tie game')
    else:
        if rules[player] == computer:
            print('Your victory has been assured.')
            player_score += 1
        else:
            print('The computer laughs as you realise that you have been defeated')
            computer_score +=1

# There are a few things going on when we 
# show the reults. First, we're putting in 
# a delay to add some tension, appending a 
# variable to some printed text, and then 
# comparing what the player and computer did. 
# Through an if statement, we shoose what 
# outcome to print, and how update the scores 



def play_agin():
    answer = raw_input('Would you like to play again? y/n: ')
    if answer in ('y', 'Y', 'yes','Yes', 'Of course!'):
        return answer
    else : 
        print('Thank you very much for playing our game, See you next time!')

# We now ask for text input on whether of not 
# someone  wants to play again. Depending on 
# their response, we go back to the start, 
# or end the game and display the results.

def scores():
    global player_score, computer_score
    print ('HIGH SCORES')
    print ('Player: ', player_score)
    print ('Computer: ', computer_score)
    
    
if __name__ == '__main__':
    start()
    