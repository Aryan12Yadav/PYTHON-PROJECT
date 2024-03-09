# from cProfile import label
import tkinter as tk
win = tk.Tk() # tk .label print number start from 0
y = 0


def sayHi():
    global y 
    y += 1
    print(y)    # this helps to update number in each click
    # label.config(text=y)
 
win.geometry("200x100")
b = tk.Button(
    win,
    text = 'click here',
    command = sayHi
)

b.pack()
win.mainloop() # mainloop is event driver loop do events like 
              # do event like clicking the button
if __name__=='__main__':
    print(sayHi())