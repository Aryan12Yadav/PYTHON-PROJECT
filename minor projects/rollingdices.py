# python program for rolling dices

import random
min = 1
max = 6
roll_again = 'yes'
while roll_again == 'yes':
    print("rolling the dices : ...")
    print("the values are..")
    print(random.randint(min,max))  # randint give the integer value 
    roll_again  = input('roll the dice again..')