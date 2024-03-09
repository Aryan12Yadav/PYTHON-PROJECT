from tkinter import * 
from tkcalendar import *
root = Tk()


def choice_date():
    present_date = display_cal.get_date()
    user_date = Label(text = present_date)
    user_date.pack(padx = 40 ,pady = 10)
    #  pixels
    # padx provide extra space in horizontly in the widget or container
    # pady povide extra vertical space in the widget





open_cal = Button(root,text = ' Select date',bg = 'Red' , fg = 'Black',relief = RAISED,command= choice_date)
# open_cal.place(x = 200,y = 40,height = 80 ,width = 20)
open_cal.pack(padx = 15, pady = 15)
    #  here root store whole in the tkinter window


display_cal = Calendar(root,setmode = "day",date_pattern = 'dd/m/yy')

display_cal.pack(padx =25,pady = 30)


root.geometry('600x500')
root.title('_______________Aryan yadav Calendar_____________')


root.configure(bg = "yellow")


root.mainloop()

