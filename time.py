import time
from tkinter import *
root=Tk()
root.title("OUR HOME WORK")
root.geometry("1000x800")
def start():
    k=time.strftime("%H:%M:%S")
    label.config(text=k)
    label.after(200,start)
label=Label(root,text="time",font=("ds-digital",50,"bold"),fg="red")
label.place(x=50,y=50)
start()
root.mainloop()
