from tkinter import *
from PIL import ImageTk,Image;
root=Tk()
root.geometry("1000x800")
root.title("This Is Our ATM Machine")
pin=0

Amount=[]


mobileno=[]


otp="1234"


def get_val(event):
    p=event.widget
    num=p["text"]


    if num=="Press-1":
        struct()
        def result():
            k=(num_entry_otp.get())
            if k==otp:
                k1=int(num_entry_pin.get())
                pin=k1
                k2=num_entry_amo.get()
                Amount.append(k2)
                lbl_r.config(text="*Your Pin Is Generate Successfully")
                lbl_t.config(text="*Thank You*")
            else:
                lbl_k.config(text="* OTP Is Wrong Please Enter Correct OTP")
            print(Amount)
        def clear():
            num_entry_otp.delete(0,END)
            num_entry_pin.delete(0,END)
            num_entry_amo.delete(0,END)

        btn_sub=Button(root,text="Submit",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5,command=result)
        btn_sub.place(x=200,y=480,height=38)
        btn_sub=Button(root,text="Clear",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5,command=clear)
        btn_sub.place(x=310,y=480,height=38)

        lbl_k=Label(root,text="",font=f3,bg="thistle1",fg="red")
        lbl_k.place(x=30,y=250)
        lbl_r=Label(root,text="",font=f3,bg="thistle1",fg="red")
        lbl_r.place(x=50,y=550)
        lbl_t=Label(root,text="",font=f3,bg="thistle1",fg="red")
        lbl_t.place(x=200,y=650)



        lbl_1=Label(root,text="Enter Your Green OTP : ",font=f3,bg="thistle1",fg="blue")
        lbl_1.place(x=30,y=200)
        lbl_2=Label(root,text="Enter Your New PIN : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=300)
        lbl_2=Label(root,text="Enter Your Amount : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=400)

        num_entry_otp=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_otp.place(x=320,y=200,height=35)
        num_entry_pin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_pin.place(x=320,y=300,height=35)
        num_entry_amo=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_amo.place(x=320,y=400,height=35)


                

            

        


    if num=="Press-2":
        struct()

        def check():
            global pin
            k1=int(num_entry_opin.get())
            if k1==pin:
                m=int(num_entry_pin.get())
                pin=m
                lbl_b.config(text="*Your Pin Change Seccessfully*")
                lbl_c.config(text="*ThankYou*")
                print("update pin=",pin)
            else:
                lbl_a.config(text="Pin Is Wrong Please Enter Correct Pin")





        lbl_a=Label(root,text="",font=f3,bg="thistle1",fg="red")
        lbl_a.place(x=30,y=250)
        lbl_b=Label(root,text="",font=f3,bg="thistle1",fg="red")
        lbl_b.place(x=50,y=550)
        lbl_c=Label(root,text="",font=f3,bg="thistle1",fg="red")
        lbl_c.place(x=200,y=650)
        lbl_1=Label(root,text="Enter Your Old Pin : ",font=f3,bg="thistle1",fg="blue")
        lbl_1.place(x=30,y=200)
        lbl_2=Label(root,text="Enter Your New PIN : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=350)
        btn_sub1=Button(root,text="Submit",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5,command=check)   
        btn_sub1.place(x=200,y=480,height=38)
        num_entry_opin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_opin.place(x=320,y=200,height=35)
        num_entry_pin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_pin.place(x=320,y=350,height=35)


          

    if num=="Press-3":
        struct()
        lbl_2=Label(root,text="Enter Your PIN Number : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=250)
        num_entry_pin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_pin.place(x=320,y=250,height=35)
        btn_sub=Button(root,text="Submit",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5)   
        btn_sub.place(x=200,y=440,height=38)
     

    if num=="Press-4":
        struct()
        lbl_2=Label(root,text="Enter Your  PIN : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=200)
        lbl_2=Label(root,text="Enter Your Amount : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=350)
        btn_sub=Button(root,text="Submit",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5)
        btn_sub.place(x=200,y=460,height=38)
        num_entry_pin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_pin.place(x=320,y=200,height=35)
        num_entry_amo=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_amo.place(x=320,y=350,height=35)
      

    if num=="Press-5":
        struct()
        lbl_2=Label(root,text="Enter Your  PIN : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=200)
        lbl_2=Label(root,text="Enter Amount For Deposite : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=350)
        btn_sub=Button(root,text="Submit",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5)
        btn_sub.place(x=200,y=460,height=38)
        num_entry_pin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_pin.place(x=320,y=200,height=35)
        num_entry_amo=Entry(root,font=f3,bg="lightblue",width=14,justify="center")
        num_entry_amo.place(x=340,y=350,height=35)
     

    if num=="Press-6":
        struct()
        lbl_2=Label(root,text="Enter Your  PIN : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=200)
        lbl_2=Label(root,text="Enter Your Mobile No. : ",font=f3,bg="thistle1",fg="blue")
        lbl_2.place(x=30,y=350)
        btn_sub=Button(root,text="Submit",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5)
        btn_sub.place(x=200,y=460,height=38)
        num_entry_pin=Entry(root,font=f3,bg="lightblue",width=15,justify="center")
        num_entry_pin.place(x=320,y=200,height=35)
        num_entry_amo=Entry(root,font=f3,bg="lightblue",width=14,justify="center")
        num_entry_amo.place(x=340,y=350,height=35)
              



def label(a,x1,y1):
    lbl=Label(root,text=a,font=f,bg="thistle1",fg="blue")
    lbl.place(x=x1,y=y1)



f = ("Times New Roman", 20, "bold")
f1 = ("Times New Roman", 15, "bold")







def p3():
    frame=LabelFrame(root,text="**ATM Machine Is Created By Kamlesh Raj**",font=f,bd=15,width=500,bg="cyan",fg="blue")
    frame.place(x=20,y=20,height=700)
    frame1=Frame(root,bg="orangered4",bd=15,width=500)
    frame1.place(x=20,y=20,height=150)
p3()

photo=PhotoImage(file="Tkinter\kamlesh.png")
photo1=Image.open("Tkinter\punjab.jpg")
k3=ImageTk.PhotoImage(photo1)
photo2=Image.open("Tkinter\images2.jpg")
k1=ImageTk.PhotoImage(photo2)
def img():
    k=Label(root,image=photo,bg="orangered4",width=300)
    k.place(x=150,y=20)
    k2=Label(root,image=k1,width=500)
    k2.place(x=20,y=170,height=550)
img()
def img2():
    k1=Label(root,image=k3,width=100,bg="orangered4")
    k1.place(x=30,y=40)
img2()


def button():
    x, y, b = 100, 450, 1
    a = b
    y1 = y
    for i in range(3):
        x1 = x
        for j in range(3):
            btn_t = Button(root, text=a, width=4, bg="cyan",
                        activebackground="green", bd=8, font=f)
            btn_t.place(x=x1, y=y1, height=45)
            #btn_t.bind("<Button-1>", get_number1)
            a = a+1
            x1 = x1+100
        y1 = y1+50
    btn_10 = Button(root, text=0, width=4, bg="cyan",
                activebackground="green", bd=8, font=f)
    btn_10.place(x=200, y=600, height=45)
    btn_11 = Button(root, text="Clear", width=4, bg="cyan",
                activebackground="green", bd=8, font=f)
    btn_11.place(x=100, y=600, height=45)
    btn_12 = Button(root, text=".", width=4, bg="cyan",
                activebackground="green", bd=8, font=f)
    btn_12.place(x=300, y=600, height=45)

    


def data():
    l=["Click For Genereate Your new Pin","Click For Change Your  Pin","Click For Check Your Balance ","Click For Withdrawl ","Click For Do Deposite","Click For Update Your Mobile No."]
    a=100
    b=200
    for i in l:
        label(i,a,b)
        b=b+80

    l2=["Press-1","Press-2","Press-3","Press-4","Press-5","Press-6",]
    a=20
    b=200
    for i in l2:
        btn5=Button(root,text=i,bg="orange",activebackground="yellow",width=5,font=f1,fg="blue",bd=5)
        btn5.place(x=a,y=b,height=38)
        btn5.bind("<Button-1>",get_val)
        b=b+80
data()
def back():
    struct()
    data()  

def btn():
    btn1=Button(root,text="Back <<--",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5,command=back)
    btn1.place(x=20,y=680,height=38)
    btn2=Button(root,text="Next -->>",bg="orange",activebackground="yellow",width=7,font=f1,fg="blue",bd=5)
    btn2.place(x=425,y=680,height=38)
    btn2.bind("<Button-1>",get_val)
btn()

def struct():
    img()
    img2()
    btn()

f3=("Times New Roman",18,"bold")   
root.mainloop()
    



