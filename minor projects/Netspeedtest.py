# speed test module
#  tkinter GUI

from tkinter import *
import speedtest



def speed_check():
    sp = speedtest.Speedtest() 
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + 'Mbps'  # it give in mbps dega
    up = str(round(sp.upload()/(10**6),3)) + 'Mbps'
    lab_down.config(text = down)
    lab_up.config(text = up)







sp = Tk()

sp.title(' Aryan____ Internet speed Tester_________________ARYAN______________________ ')
sp.geometry('700x660')
sp.config(bg = 'Orange')

lab = Label(sp,text = '_____Internet_speed_Test_____ ',fg = 'Black', bg = 'Orange', font = ('Times New Roman',34 ,'bold','underline'))

# You can usually use common fonts like
#  Arial, Courier, Times New Roman, Helvetica, Verdana, Tahoma, etc
# types of relief in tkinter = RAISED ,FLAT ,GROOVE,SUKKEN,RIDGE

lab.place(x = 110 , y = 50, height = 50 ,width = 500 )



lab = Label(sp,text = 'Downloading_speed',fg = 'Yellow' ,bg = 'Orange', font = ('Arial',24,'bold'))
lab.place(x = 175,y = 150,height = 50,width = 350)

lab_down = Label(sp,text = '00',fg = 'Blue',bg = 'Orange' ,font = ('Time New Roman',20,'bold'))
lab_down.place(x = 180,y =250 ,height =50,width = 300)


lab = Label(sp,text = 'Upload_Speed',fg = 'Yellow',bg = 'Orange' ,font = ('Time New Roman',24,'bold'))
lab.place(x = 180,y =350 ,height =50,width = 350)

lab_up = Label(sp,text = '00',fg = 'Blue',bg = 'Orange' ,font = ('Time New Roman',20,'bold'))
lab_up.place(x = 180,y =450 ,height =50 ,width = 300)

button = Button(sp,text  = ' press this Check speed',font = ('Time New Roman',20,'bold'),fg = 'Silver',bg = 'Green',relief = RAISED,cursor = 'plus',command = speed_check)
button.place(x = 150,y= 550,height = 50 , width = 400)



lab = Label(sp,text = '__________Aryan Yadav______________-',fg = 'Black',bg = 'Blue' ,font = ('Time New Roman',12,'bold'),relief = FLAT,cursor = 'shuttle')
lab.place(x = 0,y =630 ,height =35,width = 700)

lab = Label(sp,text = ' ',fg = 'Black',bg = 'Blue' ,font = ('Time New Roman',12,'bold'),relief = FLAT,cursor = 'shuttle')
lab.place(x = 665,y = 0 ,height =700,width = 35)

lab = Label(sp,text = ' ',fg = 'Black',bg = 'Blue' ,font = ('Time New Roman',12,'bold'),relief = FLAT,cursor = 'shuttle')
lab.place(x = 0,y =0 ,height =700,width = 35)

lab = Label(sp,text = ' ___________Aryan Yadav______________',fg = 'Red',bg = 'Blue' ,font = ('Time New Roman',12,'bold'),relief = FLAT,cursor = 'shuttle')
lab.place(x = 0,y =0 ,height =35 ,width = 700)




#  font size = 40 , font = bold
sp.mainloop()