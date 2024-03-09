def printBoard():
    print(f" 0| 1 | 2")
    print(f"--|---|---")
    print(f" 3| 4 | 5")
    print(f"--|---|---")
    print(f" 6| 7 | 8")
if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O
    print("WELCOME  TO TIC TAC game")
    while(True):
        if turn == 1:
            print("X's Chance")
            value = input("please enter a value : ")
        else:
            print("X's chance ")
            value = input("Please enter the value")
        printBoard()
        break