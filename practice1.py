from tkinter import *
root=Tk()
root.geometry("1000x800")
root.title("Practice")
f = ("Times New Roman", 12, "bold")
def button1(k,x1,y1):
    btn_random = Button(root, text=k, bg="red",
                  activebackground="green", bd=8, width=8,font=f)
    btn_random.place(x=x1, y=y1, height=45)
    # btn_random.bind("<Button-1>", get_number1)
p=["fact","clear","square","root","button","dec","bin","check","ram","aam","kam","seb","papya","turn","on","off"]
x=50
y=50
a=1
for i in p:
    button1(i,x,y)
    x=x+100
    a=a+1
    if a==5:
        y=y+50
        x=50
        a=1
root.mainloop()