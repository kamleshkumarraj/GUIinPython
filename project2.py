from tkinter import *
root=Tk()
root.title("Attendence Sheet")
root.geometry("1000x1400")
count=0
def get_val(event):
    k=event.widget
    num=k["text"]
    count=5
    if num=="submit":
        a1=1
        for i in range(20):
            for j in range(30):
                p=a1.get()
                a1=a1+1
                if p==k:
                    count=count+1
    t=count
    lal.config(text=t)




b=50
a1=1
for i in range(20):
    a=50
    for j in range(30):
        a1=Entry(root,bg="cyan",width=7,justify="center")
        a1.place(x=a,y=b)
        a1=a1+1
        a=a+50
    b=b+30
btn=Button(root,text="submit",bd=5,relief=SUNKEN,bg="pink",activebackground="red")
btn.bind("<Button-1>",get_val)
btn.place(x=600,y=700)
lal=Label(root,text="total",width=8)
lal.place(x=400,y=700)

root.mainloop()