'''
the snake water gun game is the game played by 2 players which is same like rock paper siccors but with different themes.
let ,
    snake = @
    water = #
    gun = $
the rules are as follows:
    snake vs snake = draw
    snake vs water = player 1 wins
    snake vs gun = player 2 wins
    water vs water = draw
    water vs gun = player 1 wins
    water vs snake = player 2 wins
    gun vs gun = draw
    gun vs snake = player 1 wins
    gun vs water = player 2 wins
'''

import random 
def game(cpu, player):
    if cpu == player:
        return "draw"
    elif cpu == '@' and player == '#':
        return "cpu wins"
    elif cpu == '@' and player == '$':
        return "player wins"
    elif cpu == '#' and player == '@':
        return "player wins"
    elif cpu == '#' and player == '$':
        return "cpu wins"
    elif cpu == '$' and player == '@':
        return "cpu wins"
    elif cpu == '$' and player == '#':
        return "player wins"    
    else:
        return "invalid input"
    
print("welcome to snake water gun game ")

while True:
    print("\nenter your choice: @ for snake, # for water, $ for gun (or 'q' to quit)")
    player = input("your choice: ")
    
    if player.lower() == 'q':
        print("Thanks for playing!")
        break
        
    cpu = random.choice(['@', '#', '$'])
    print("cpu choice: ", cpu)
    print("Result: ", game(cpu, player))