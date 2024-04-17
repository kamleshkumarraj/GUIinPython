#import all module and function
from tkinter import *
import math
#function for binding the button
def get_number(event):
    p=event.widget
    num=p["text"]
#command give on the "=" button    
    if num=="=":
        k=(num_entry.get())
        answer=eval(k)
        answer=float(answer)
        num_entry.delete(0,END)
        num_entry.insert(0,answer)
        return
#command give on the "fact" button
    if num=="fact":
        k=int(num_entry.get())
        answer=math.factorial(k)
        num_entry.delete(0,END)
        num_entry.insert(0,answer)
        return
#command give on the "root" button    
    if num=="root":
        k=float(num_entry.get())
        answer=k ** .5
        num_entry.delete(0,END)
        num_entry.insert(0,answer)
        return 
#command give on the "square" button
    if num=="square":
        k=float(num_entry.get())
        answer=k*k
        num_entry.delete(0,END)
        num_entry.insert(0,answer)
        return
#command give on the "remainder" button 
    if num=="remainder":
        num_entry.insert(END,"%")
        return
#command give on the "power" button
    if num=="power":
        num_entry.insert(END,"**")
        return   
#command give on the total rest number button
    num_entry.insert(END,num)
#command give on the "clear" button for clear the screen
def clear():
     num_entry.delete(0,END)
#command give on the "backspace" button for backspac the number
def backspace():
     ex=num_entry.get()
     ex=ex[0:len(ex)-1]
     num_entry.delete(0,END)
     num_entry.insert(0,ex)
#create a window for making a calculator
root=Tk()
root.geometry("460x605")
root.title("****Simple Calculator Created by Kamlesh Raj****")
root.maxsize(460,605)
root.minsize(460,605)
f=("Times New Roman",12,"bold")
#create a frame for pack a calculator
frame=Frame(root,bd=20,relief=SUNKEN,width=445)
frame.place(x=10,y=10,height=550)
#create a label for design in calculator
Label(frame,text="********* SIMPLE CALCULATOR *********",fg="green",bg="black",font=("Times New Roman",15,"italic")).place(x=3,y=2)
#create a button from 1-9 using for loop and bind with command
b=300
d=1
for i in range(1,4):
    a=35
    for j in range(1,4):
        btn=Button(root,text=d,font=f,bg="cyan",fg="blue",activebackground="green",width=8,bd=6)
        btn.place(x=a,y=b,height=45)
        btn.bind("<Button-1>",get_number)
        d=d+1
        a=a+100
    b=b+50
#create a button for perform some task
btn2=Button(root,text="-",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn2.place(x=335,y=300)
btn3=Button(root,text="clear",font=f,bg="cyan",fg="blue",activebackground="green",width=8,bd=6,command=clear)
btn3.place(x=35,y=250)
btn4=Button(root,text="/",font=f,bg="cyan",fg="blue",activebackground="green",width=8,bd=6)
btn4.place(x=135,y=250)
btn5=Button(root,text="*",font=f,bg="cyan",fg="blue",activebackground="green",width=8,bd=6)
btn5.place(x=235,y=250)
btn6=Button(root,text="back(X)",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6,command=backspace)
btn6.place(x=335,y=250)
btn7=Button(root,text="+",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn7.place(x=335,y=350)
btn8=Button(root,text="fact",font=f,bg="cyan",fg="blue",activebackground="orange",width=8,bd=6)
btn8.place(x=35,y=450)
btn9=Button(root,text="0",font=f,bg="cyan",fg="blue",activebackground="orange",width=8,bd=6)
btn9.place(x=135,y=450)
btn10=Button(root,text=".",font=f,bg="cyan",fg="blue",activebackground="orange",width=8,bd=6)
btn10.place(x=235,y=450)
btn15=Button(root,text="=",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn15.place(x=335,y=400,height=90)
btn11=Button(root,text="remainder",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn11.place(x=35,y=500)
btn12=Button(root,text="square",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn12.place(x=135,y=500)
btn13=Button(root,text="root",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn13.place(x=235,y=500)
btn14=Button(root,text="power",font=f,bg="gray",fg="blue",activebackground="orange",width=8,bd=6)
btn14.place(x=335,y=500)
#create a text box 
Text=Text(frame,bg="lightblue",fg="red",bd=5,width=48)
Text.place(x=5,y=50,height=130)
#create a result box for enter the value and get the result
num_entry=Entry(Text,width=30,font=("Times New Roman",18,"bold"),fg="red",bg="lightblue",justify=CENTER)
num_entry.place(x=10,y=20,height=80)
#bind all button with function and command
btn2.bind("<Button-1>",get_number)
btn4.bind("<Button-1>",get_number)
btn5.bind("<Button-1>",get_number)
btn7.bind("<Button-1>",get_number)
btn8.bind("<Button-1>",get_number)
btn9.bind("<Button-1>",get_number)
btn10.bind("<Button-1>",get_number)
btn11.bind("<Button-1>",get_number)
btn12.bind("<Button-1>",get_number)
btn13.bind("<Button-1>",get_number)
btn14.bind("<Button-1>",get_number)
btn15.bind("<Button-1>",get_number)
Label(root,text="This Calculator Is Created By- Kamlesh Raj",font=("Times New Roman",17,"italic"),fg="blue",bg="red").place(x=10,y=570)
root.mainloop()