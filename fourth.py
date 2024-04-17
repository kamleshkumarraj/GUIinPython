from tkinter import *
import homework as hm
def get_number(event):
    p=event.widget
    num=p["text"]
    if num=="Reverse":
        a=(num_entry.get())
        k=len(a)
        a=int(a)
        n=a
        sum=0
        p=1
        while(n>0):
            b=n%2
            sum=sum+b*p
            n=n//2
            p=p*10
        num_entry.delete(0,END)
        num_entry.insert(END,sum)
        return  
    if num=="Clear":
        num_entry.delete(0,END)
        return         
    num_entry.insert(END,num)
hm.root=Tk()
hm.root.geometry("800x1000")
hm.root.title("OUR HOME WORK")
frame1=Frame(hm.root,bd=15,width=280,relief=RIDGE)
frame1.place(x=10,y=255,height=300)
lb1=Label(frame1,text="******Print Binary*******")
lb1.place(x=2,y=0)
x,y,b=20,350,1
a=b
y1=y
for i in range(3):
    x1=x
    for j in range(3):
        t=5
        btn_t=Button(hm.root,text=a,width=8,bg="cyan",activebackground="green",bd=8)
        btn_t.place(x=x1,y=y1,height=45)
        btn_t.bind("<Button-1>",get_number)
        a=a+1
        x1=x1+80
    y1=y1+50
t=t+1
x1=x1-240
btn0=Button(hm.root,text=0,bg="cyan",activebackground="green",bd=8,width=8)
btn0.place(x=x1,y=y1,height=40)
btn0.bind("<Button-1>",get_number)
num_entry=Entry(frame1,width=25,font=("Times New Roman",13,"bold"),fg="red",bg="orange",justify=CENTER,bd=5)
num_entry.place(x=5,y=20,height=50)
btn_arm=Button(hm.root,text="Reverse",bg="cyan",activebackground="green",bd=8,width=8)
btn_arm.place(x=100,y=500,height=40)
btn_arm.bind("<Button-1>",get_number)
btn_clear=Button(hm.root,text="Clear",bg="cyan",activebackground="green",bd=8,width=8)
btn_clear.place(x=180,y=500,height=40)
btn_clear.bind("<Button-1>",get_number)
hm.root.mainloop()