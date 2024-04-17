from tkinter import *
def get_number(event):
    p=event.widget
    num=p["text"]
    if num=="Check":
        a=(num_entry.get())
        k=len(a)
        a=int(a)
        n=a
        sum=0
        while(n>0):
            b=n%10
            sum=sum+(b**k)
            n=n//10
        if(sum==a):
            num_entry.delete(0,END)
            num_entry.insert(END,f"{a} Is Armstrong Number.")
        else:
            num_entry.delete(0,END)
            num_entry.insert(END,f"{a} Is Not Armstrong Number.") 
        return  
    if num=="Clear":
        num_entry.delete(0,END)
        return         
    num_entry.insert(END,num)
def get_number1(event):
    p=event.widget
    num=p["text"]
    if num=="Check1":
        a=int(num_entry1.get())
        b=0
        for i in range(1,a+1):
            if(a%i==0):
                b=b+1
        if b==2:
            num_entry1.delete(0,END)
            num_entry1.insert(END,f"{a} Is A Prime No.")
        else:
            num_entry1.delete(0,END)
            num_entry1.insert(END,f"{a} Is  Not A Prime No.")
        return
    if num=="Clear":
        num_entry1.delete(0,END)
        return   
    num_entry1.insert(END,num)
root=Tk()
root.title("OUR HOME WORK")
root.geometry("1000x800")
frame1=Frame(root,bd=15,width=280,relief=RIDGE)
frame1.place(x=0,y=5,height=300)
lb1=Label(frame1,text="******Check Armstrong Number Or Not*******")
lb1.place(x=2,y=0)
x,y,b=20,100,1
a=b
y1=y
for i in range(3):
    x1=x
    for j in range(3):
        t=5
        btn_t=Button(root,text=a,width=8,bg="cyan",activebackground="green",bd=8)
        btn_t.place(x=x1,y=y1,height=45)
        btn_t.bind("<Button-1>",get_number)
        a=a+1
        x1=x1+80
    y1=y1+50
t=t+1
x1=x1-240
btn0=Button(root,text=0,bg="cyan",activebackground="green",bd=8,width=8)
btn0.place(x=x1,y=y1,height=40)
btn0.bind("<Button-1>",get_number1)
num_entry=Entry(frame1,width=25,font=("Times New Roman",13,"bold"),fg="red",bg="orange",justify=CENTER,bd=5)
num_entry.place(x=5,y=20,height=50)
btn_arm=Button(root,text="Check",bg="cyan",activebackground="green",bd=8,width=8)
btn_arm.place(x=100,y=250,height=40)
btn_arm.bind("<Button-1>",get_number)
btn_clear=Button(root,text="Clear",bg="cyan",activebackground="green",bd=8,width=8)
btn_clear.place(x=180,y=250,height=40)
btn_clear.bind("<Button-1>",get_number)

#for checking prime number

frame2=Frame(root,bd=15,width=280,relief=RIDGE)
frame2.place(x=330,y=5,height=300)
lb1=Label(frame2,text="******Check Prime Number Or Not*******")
lb1.place(x=2,y=0)
num_entry1=Entry(frame2,width=25,font=("Times New Roman",13,"bold"),fg="red",bg="orange",justify=CENTER,bd=5)
num_entry1.place(x=5,y=20,height=50)
btn_prime=Button(root,text="Check1",bg="cyan",activebackground="green",bd=8,width=8)
btn_prime.place(x=430,y=250,height=40)
btn_prime.bind("<Button-1>",get_number1)
btn_clear=Button(root,text="Clear",bg="cyan",activebackground="green",bd=8,width=8)
btn_clear.place(x=510,y=250,height=40)
btn_clear.bind("<Button-1>",get_number1)
x,y,b=350,100,1
a=b
y1=y
for i in range(3):
    x1=x
    for j in range(3):
        btn_t=Button(root,text=a,width=8,bg="cyan",activebackground="green",bd=8)
        btn_t.place(x=x1,y=y1,height=45)
        btn_t.bind("<Button-1>",get_number1)
        a=a+1
        x1=x1+80
    y1=y1+50
x1=x1-240
btn0=Button(root,text=0,bg="cyan",activebackground="green",bd=8,width=8)
btn0.place(x=x1,y=y1,height=40)
btn0.bind("<Button-1>",get_number1)
root.mainloop()
#for checking Other
