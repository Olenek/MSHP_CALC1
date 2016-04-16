from tkinter import *
import random
def move_wall(event):
    canv.coords(wall1,event.x-50,570,event.x+50,570)


def destroy_bricks():
    global D
    global T
    D=[]
    if T!=0:
        for i in range (10):
            canv.delete(brick[i])
            
    bricks()
    
    
def bricks():
    global T
    global s
    global brick
    brick=[]
    s=0
    T+=1
    for i in range(10):         
        brick.append(canv.create_rectangle(0+i*80,0,(i+1)*80,50, fill="#"+str(hex(random.randint(1048576, 16777215)))[2:]))
      
def creating_oval():
    global oval1
    global eye1
    global eye2
    global nose1
    global smile1
    global T
    global a
    global b
    a=1
    b=1
    oval1=canv.create_oval(0, 100, 100, 200,fill="#"+str(hex(random.randint(1048576, 16777215)))[2:])
    eye1=canv.create_oval(25,125,35,135)
    eye2=canv.create_oval(65,125,75,135)
    nose1=canv.create_line(40,160,60,160,50,145,40,160)
    smile1=canv.create_line(15,160,30,175,70,175,85,160)
    destroy_bricks()
    
    
def creating_wall():
    global wall1
    wall1=canv.create_line(200,570,300,570,fill="#"+str(hex(random.randint(1048576, 16777215)))[2:])


def move_oval():
    global a
    global b
    global s
    global t
    global D
    canv.move(oval1,a,b)
    canv.move(eye1,a,b)
    canv.move(eye2,a,b)
    canv.move(nose1,a,b)
    canv.move(smile1,a,b)
    if canv.coords(oval1) [0] == 0 or canv.coords(oval1) [2] == n:
        a=-a     
    if canv.coords(oval1) [3] == m:
        canv.after(1000,creating_oval)
    if canv.coords(oval1) [1] == 0 :
        b=-b
    if canv.coords(oval1) [3] == 570 and canv.coords(oval1) [0]+50 < canv.coords(wall1)[2] and canv.coords(oval1) [0]+50 > canv.coords(wall1)[0] and b!=-1:
        b=-b
    for j in range(10):
        if canv.coords(oval1) [1]>=50 and canv.coords(oval1) [1] <= 60 and canv.coords(oval1) [0]+50 > j*80 and canv.coords(oval1) [0]+50 < (j+1)*80 and j not in D and b!=1:
            D.append(j)
            b=-b
            canv.delete(brick[j])
            s+=1
            if s>=10:
                label2['text']='You Are Great'
    label['text'] = s
    canv.after(t, move_oval)



label = Label(font='sans 20')
label2=Label(font='sans 48')
label.pack()
label2.pack()            
root= Tk()
a=1
D=[]
b=1
T=0
s=0
t=5
n=800
m=600
canv = Canvas(root, width=n, height=m, bg="white")
canv.pack()
label = Label(font='sans 20')
label.pack()
creating_oval()
move_oval()
creating_wall()
destroy_bricks()
canv.bind("<Motion>", move_wall)
root.mainloop()