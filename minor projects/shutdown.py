from tkinter import *  # import whole tkinker library

import os   # operating system 

def restart():
    os.system('shutdown / r /t 1') # shut down in 1 second

def restart_time():
    os.system('shutdown/r /t 20') # shutdown in 20 second

def log_out():
    os.system('shutdown -l')

def shutdown():
    os.system('shutdown /s /t 1')




 

st = Tk()    # object of the class 
st.title('Shutdown App ___aryan_code ')        # making title  
st.geometry('800x600')           # changing the geometry

st.config(bg='Green')    # change color
r_button = Button(st,text = 'Restart',font = ('Time New Roman',20,'bold'),relief = RAISED,cursor = 'plus',command = restart)  
r_button.place(x = 280,y=10,height = 50,width = 250)
# calling button class 
# 1. st object call 
# 2.font  = times change , size = 30 ,style = bold
# 3.  for 3D ness   using releif   
# 4. cursor 
#

r_button = Button(st,text = 'Restart time',font = ('Time New Roman', 20,(('bold')or ('italic'))),relief = RAISED,cursor = 'plus',command = restart_time)
r_button.place(x = 280,y = 130, height = 50,width = 250) # command use to call the funtion s1

r_button = Button(st,text = 'Log_Out',font = ('Time New Roman',20,'bold'),relief = RAISED ,cursor = 'plus', command = log_out)
r_button.place(x = 280,y = 260,height = 50,width = 250)

r_button = Button(st,text = 'ShutDown',font = ('time New Roman',20,'bold'),relief = RAISED , cursor = 'plus',command = shutdown)
r_button.place(x = 280,y = 380 , height = 50,width = 250)


r_button = Button(st,text = 'aryan_program',font = ('Time New Roman',10,'bold'),relief = RAISED , cursor = 'plus')
r_button.place(x=0,y =500 , height = 30,width = 800)


st.mainloop()
 