#  typing speed calculator
from time import *  # alias give all the libraries inside time

import random as r   # to given string in random


 
def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i]!= usertest[i]:
                error = error +1
        except:
            error = error +1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e- time_s
    time_ro = round(time_delay)
    speed = len(userinput)/time_ro
    print(int(time_delay),'second')
    return round(speed)
    
if __name__ == '__main__':
    while True:
        ck = input(''' ready to test -- yes:: 
                or  NO ::''')
        if ck == 'yes':
            

            test = ['the quick brown fox jumped over the lazy dog',
            'cost soup notion thrive plate school here seal column around decade glance' ,
            'mutter demand outer pump use assure need signal break effort month public net ',
            'term plenty black basis nine engage tray patch eighth talk part mass target easy dozen strike ',
            'second chain match gently hey lack chop wash catch top basic rent humor whose mentor goal ground inside',
            'monkey derive top guitar sign string unlike later remove design manner may avoid pray pound heel',
            'crawl melt car unless hope stir warm prize pit item steer doctor black thick hook cousin virus',
            'knife index that web eat shot too act not Asian dirt yard turn dawn sphere herb boost rally across',
            'unfair fifty so rubber upon retain PM power sensor bend and/or front start light salary jury ',
            'decent touch own under royal shit above bulk twin long favor ie about dig close ring patron pen vs',
            'pool choose solely blind bloody submit charge weapon slope pillow forty active blink sacred our appeal']


            test1 = r.choice(test)
            print("______________typing speed____________________")

            print(test1)

            print()
            print()

            time_1 = time()

            testinput = input('enter : ')

            time_2 = time()
            print()
            print('Speed = ',speed_time(time_1,time_2,testinput),"WPM")

            print('error = ',mistake(test1,testinput))

        elif ck == 'no':
            break

        else:
            print('wrong input')