# import all module for our using to make this project
from tkinter import *
import math
import time

#function is define for time
def start():
    k=time.strftime("%I:%M:%S %p")
    lb3.config(text=k)
    lb3.after(200,start)

#function is define for Date
def date():
    k=time.strftime("%d:%m:%Y")
    lb6.config(text=k)
    lb6.after(200,start)

#function is define for Day
def day():
    k=time.strftime("%A")
    lb7.config(text=k)
    lb7.after(200,start)

#function is define for take input number from entry box
def get_number1(event):
    p = event.widget
    num = p["text"]
#function for checking number is armstrong or not
    if num == "Check Armstrong Or Not":
        a = (num_entry.get())
        k = len(a)
        a = int(a)
        n = a
        sum = 0
        while (n > 0):
            b = n % 10
            sum = sum+(b**k)
            n = n//10
        if (sum == a):
            num_entry.delete(0, END)
            num_entry.insert(END, f"{a} Is Armstrong Number.")
        else:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{a} Is Not Armstrong Number.")
        return
    
#function for checking number is prime or not
    if num == "Check Prime Or Not":
        a = int(num_entry.get())
        c = 0
        for i in range(1, a+1):
            if (a % i == 0):
                c = c+1
        if c == 2:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{a} Is A Prime Number ")
        else:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{a} Is Not A Prime Number ")
        return
    
#function for checking number is palindrom or not
    if num == "Check Palindrom Or Not":
        a = int(num_entry.get())
        rev = 0
        i = a
        while (i > 0):
            b = i % 10
            rev = rev*10+b
            i = i//10
        if rev == a:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{a} Is A Palindrom Number")
        else:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{a} Is A Not Palindrom Number")
        return
    
#function for checking number is Strong number or not
    if num == "Check Strong Or Not":
        n = int(num_entry.get())
        i = n
        sum = 0
        while (i > 0):
            b = i % 10
            k = math.factorial(b)
            sum = sum+k
            i = i//10
        if sum == n:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{n} Is A Strong Number")
        else:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{n} Is Not A Strong Number")
        return
    
#for  give command on find the Area of square button
    if num == "Area Of Square":
        side = float(num_entry.get())
        r = side*side
        num_entry.delete(0, END)
        num_entry.insert(END, f"Area Of Square = {r} ")
        return
    
#for  give command on find the Area of Rectanlge button    
    if num == "Area Of Rectangle":
        l, b = (num_entry.get()).split(",")
        l = float(l)
        b = float(b)
        r = l*b
        num_entry.delete(0, END)
        num_entry.insert(END, f"Area Of Rectangle = {r} ")
        return
    
#for  give command on find the Area of Triangle button
    if num == "Area Of Triangle":
        h, b = (num_entry.get()).split(",")
        h = float(h)
        b = float(b)
        r = .5*h*b
        num_entry.delete(0, END)
        num_entry.insert(END, f"Area Of Triangle = {r} ")
        return
    
#for  give command on find the Area of Circle button
    if num == "Area Of Circle":
        r = float(num_entry.get())
        res = 3.14*r*r
        num_entry.delete(0, END)
        num_entry.insert(END, f"Area Of Circle = {res} ")
        return
    
#for  give command on find the Perimeter of Square button
    if num == "Perimeter Of Square":
        side = float(num_entry.get())
        r = 4*side
        num_entry.delete(0, END)
        num_entry.insert(END, f"Perimeter Of Square = {r} ")
        return
    
#for  give command on find the Perimeter of Rectangle button
    if num == "Perimeter Of Rectangle":
        l, b = (num_entry.get()).split(",")
        l = float(l)
        b = float(b)
        r = 2*(l+b)
        num_entry.delete(0, END)
        num_entry.insert(END, f"Perimeter Of Rectangle = {r} ")
        return
    
#for  give command on find the Perimeter of Triangle button
    if num == "Perimeter Of Triangle":
        a, b, c = (num_entry.get()).split(",")
        a = float(a)
        b = float(b)
        c = float(c)
        r = (a+b+c)/2
        num_entry.delete(0, END)
        num_entry.insert(END, f"Perimeter Of Triangle = {r} ")
        return
    
#for  give command on find the Perimeter of Circle button
    if num == "Perimeter Of Circle":
        r = float(num_entry.get())
        s = 2*3.14*r
        num_entry.delete(0, END)
        num_entry.insert(END, f"Perimeter Of Circle = {s}")
        return
    
#for  give command on find the Volume of Cube button
    if num == "Volume Of Cube":
        side = float(num_entry.get())
        s = side*side*side
        num_entry.delete(0, END)
        num_entry.insert(END, f"Volume Of Cube = {s}")
        return

#for  give command on find the Volume of Cuboid button
    if num == "Volume Of Cuboid":
        l, b, h = num_entry.get().split(",")
        l = float(l)
        b = float(b)
        h = float(h)
        s = l*b*h
        num_entry.delete(0, END)
        num_entry.insert(END, f"Volume Of Cuboid = {s}")
        return
    
#for  give command on find the Surface area of Cube button
    if num == "Surfacearea Of Cube":
        side = float(num_entry.get())
        s = 6*side*side
        num_entry.delete(0, END)
        num_entry.insert(END, f"Surface Area Of Cube = {s}")
        return
    
#for  give command on find the Surface area of Cuboid  button
    if num == "Surfacearea Of Cuboid":
        l, b, h = num_entry.get().split(",")
        l = float(l)
        b = float(b)
        h = float(h)
        s = 2*(l*b+b*h+h*l)
        num_entry.delete(0, END)
        num_entry.insert(END, f"Volume Of Cuboid = {s}")
        return
    
#for  give command on Check the given number is odd or even  button
    if num == "Check Even Or Odd":
        n = int(num_entry.get())
        if n % 2 == 0:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{n} Is A Even No.")
        else:
            num_entry.delete(0, END)
            num_entry.insert(END, f"{n} Is A Odd No.")
        return
    
#for  give command on find the Diagonal of Cube  button
    if num == "Diagonal Of Cube":
        side = float(num_entry.get())
        s = math.sqrt(3)*side
        num_entry.delete(0, END)
        num_entry.insert(END, f"Diagonal Of Cube = {s}")
        return

#for  give command on find the Diagonal of Cuboid  button
    if num == "Diagonal Of Cuboid":
        l, b, h = num_entry.get().split(",")
        l = float(l)
        b = float(b)
        h = float(h)
        s = math.sqrt(l*l+b*b+h*h)
        num_entry.delete(0, END)
        num_entry.insert(END, f"Diagonal Of Cuboid = {s}")
        return

#for  give command on find the Volume of Cylinder button
    if num == "Volume of cylinder":
        r, h = num_entry.get().split(",")
        r = float(r)
        h = float(h)
        s = 3.14*r*r*h
        num_entry.delete(0, END)
        num_entry.insert(END, f"Volume Of Cylinder = {s}")
        return

#for  give command on find the Volume of Cone button
    if num == "Volume of Cone":
        r, h = num_entry.get().split(",")
        r = float(r)
        h = float(h)
        s = .33*3.14*r*r*h
        num_entry.delete(0, END)
        num_entry.insert(END, f"Volume Of Cone = {s}")
        return

#for  give command on find the Volume of Cylinder button
    if num == "Sum Of N Number":
        n = int(num_entry.get())
        sum = 0
        for i in range(1, n+1):
            sum = sum+i
        num_entry.delete(0, END)
        num_entry.insert(END, f"sum of 1 - {n} = {sum}")
        return

#for  give command on find the Surface area of Cone button
    if num == "Surfacearea Of Cone":
        r, l = num_entry.get().split(",")
        r = float(r)
        l = float(h)
        s = 3.14*r*l
        num_entry.delete(0, END)
        num_entry.insert(END, f"Surface Area Of Cone = {s}")
        return

#for  give command on find the Volume of Sphere button
    if num == "Volume Of Sphere":
        r = float(num_entry.get())
        s = 4/3*3.14*r*r*r
        num_entry.delete(0, END)
        num_entry.insert(END, f"Volume Of Sphere = {s}")
        return

#for  give command on find the Surface area of Cylinder button
    if num == "Surfacearae Of Cylinder":
        r, h = num_entry.get().split(",")
        r = float(r)
        h = float(h)
        s = 2*3.14*r*h
        num_entry.delete(0, END)
        num_entry.insert(END, f"Surface Area Of Cylinder = {s}")
        return

#for  give command on find the Total Surface area of Cylinder button
    if num == "T_S.area Of cylinder":
        r, h = num_entry.get().split(",")
        r = float(r)
        h = float(h)
        s = 2*3.14*r*(r+h)
        num_entry.delete(0, END)
        num_entry.insert(END, f"Total Surface Area Of Cylinder = {s}")
        return
    
#for  give command on find the Total Surface area of Sphere button
    if num == "T_S.area Of Sphere":
        r = float(num_entry.get())
        s = 4*3.14*r*r
        num_entry.delete(0, END)
        num_entry.insert(END, f"Total Surface Area Of Sphere = {s}")
        return

#for  give command on find the Total Surface area Of Cone button
    if num == "T_S.area of cone":
        r, l = num_entry.get().split(",")
        r = float(r)
        l = float(h)
        s = 3.14*r*(r+l)
        num_entry.delete(0, END)
        num_entry.insert(END, f"Total Surface Area Of Cone = {s}")
        return

#for  give command on find the Surface area of Half Sphere button
    if num == "Surfacearea Of H_Sphere":
        r = float(num_entry.get())
        s = 2*3.14*r*r
        num_entry.delete(0, END)
        num_entry.insert(END, f"Surface Area Of Half Sphere = {s}")
        return

#for  give command on find the Diagonal of Square button
    if num == "Diagonal Of Square":
        side = float(num_entry.get())
        r = math.sqrt(2)*side
        num_entry.delete(0, END)
        num_entry.insert(END, f"Diagonal Of Square = {r} ")
        return

#for  give command on find the Diagonal of rectangle button
    if num == "Diagonal Of Rectangle":
        l, b = (num_entry.get()).split(",")
        l = float(l)
        b = float(b)
        r = math.sqrt(l*l+b*b)
        num_entry.delete(0, END)
        num_entry.insert(END, f"Diagonal Of Rectangle = {r} ")
        return

#for  give command on "=" Button
    if num == "=":
        k = (num_entry.get())
        answer = eval(k)
        answer = float(answer)
        num_entry.delete(0, END)
        num_entry.insert(0, answer)
        return
    
# command give on the "fact" button
    if num == "Fact":
        k = int(num_entry.get())
        answer = math.factorial(k)
        num_entry.delete(0, END)
        num_entry.insert(0, answer)
        return
    
# command give on the "root" button
    if num == "Root":
        k = float(num_entry.get())
        answer = k ** .5
        num_entry.delete(0, END)
        num_entry.insert(0, answer)
        return
    
# command give on the "square" button
    if num == "Square":
        k = float(num_entry.get())
        answer = k*k
        num_entry.delete(0, END)
        num_entry.insert(0, answer)
        return
    
# command give on the "remainder" button
    if num == "remainder":
        num_entry.insert(END, "%")
        return

# command give on the "power" button
    if num == "Power":
        num_entry.insert(END, "**")
        return

    if num == "Remainder":
        num_entry.insert(END, "%")
        return
    
#command on reverse button for find the reverse
    if num == "Reverse":
        a = int(num_entry.get())
        rev = 0
        i = a
        while (i > 0):
            b = i % 10
            rev = rev*10+b
            i = i//10
        num_entry.delete(0, END)
        num_entry.insert(END, f"Diagonal Of Reverse = {rev} ")
        return

#command on Binary to Decimal Number button for find the Binary to Decimal Number
    if num == "Bin-Dec.":
        n = int(num_entry.get())
        i = n
        decimal = 0
        k = 0
        while (i > 0):
            a = i % 10
            decimal = decimal+a*(2**k)
            k = k+1
            i = i//10
        num_entry.delete(0, END)
        num_entry.insert(END, f"Decimal Number = {decimal} ")
        return

#command on Binary to Decimal Number button for find the Decimal to Binary Number
    if num == "Dec-Bin.":
        n = int(num_entry.get())
        c = 1
        binary = 0
        while (n > 0):
            b = n % 2
            binary = binary+b*c
            c = c*10
            n = n//2
        num_entry.delete(0, END)
        num_entry.insert(END, f"Binary Number = {binary} ")
        return

#for give command on clear button for do total clear
    if num == "Clear":
        num_entry.delete(0, END)
        return
    num_entry.insert(END, num)

#for give command on backspace button for do total backspace
def backspace():
    ex = num_entry.get()
    ex = ex[0:len(ex)-1]
    num_entry.delete(0, END)
    num_entry.insert(0, ex)

#create a new window for make our project
root = Tk()
root.title("OUR HOME WORK")
root.geometry("850x760")
root.minsize(850, 760)
root.maxsize(850, 760)

#create a new frame for make our project
frame1 = Frame(root, bd=15, width=820, relief=RIDGE)
frame1.place(x=10, y=5, height=740)

#create n number entry box for entry the number
num_entry = Entry(frame1, width=54, font=("Times New Roman",
                  20, "bold"), fg="blue", bg="lightblue", justify=CENTER, bd=10)
num_entry.place(x=5, y=50, height=110)

lb1 = Label(frame1, text="******************************************This Calculator Is Created By - Kamlesh Raj ***********************************",font=("Times New Roman",10,"italic"),fg="blue")
lb1.place(x=2, y=0)
lb2 = Label(frame1, text='''**** In This Calculator We Want To Give Multiple Parameter Then We Use comma (,) Buttton Like As We Want To Give Length,Breadth,Height
 Then Write(10,15,20) Becuase Here Comma Button Is Works As Seperator****''' , font=("Times New Roman",10,"italic"),fg="blue")
lb8=Label(frame1,text="                                                                                                       ",font=("Times New Roman",20,"bold"),fg="red",bg="lightblue")
lb8.place(x=15,y=59)

lb2.place(x=0, y=15)

lb3=Label(frame1,text="time and date",font=("Times New Roman",20,"bold"),fg="red",bg="lightblue")
lb3.place(x=105,y=59)
lb4=Label(frame1,text="Time :-",font=("Times New Roman",20,"bold"),fg="red",bg="lightblue")
lb4.place(x=15,y=59)
lb5=Label(frame1,text="Date :-",font=("Times New Roman",20,"bold"),fg="red",bg="lightblue")
lb5.place(x=560,y=59)
lb6=Label(frame1,text="Time :-",font=("Times New Roman",20,"bold"),fg="red",bg="lightblue")
lb6.place(x=640,y=59)
lb7=Label(frame1,text="Time :-",font=("Times New Roman",20,"bold"),fg="red",bg="lightblue")
lb7.place(x=350,y=59)
# for Font style
f = ("Times New Roman", 12, "bold")
f1 = ("Times New Roman", 8, "bold")

x, y, b = 30, 200, 1
a = b
y1 = y
for i in range(3):
    x1 = x
    for j in range(3):
        t = 5
        btn_t = Button(root, text=a, width=6, bg="orange",
                       activebackground="green", bd=8, font=f)
        btn_t.place(x=x1, y=y1, height=45)
        btn_t.bind("<Button-1>", get_number1)
        a = a+1
        x1 = x1+80
    y1 = y1+50
t = t+1
x1 = x1-240

btn_back = Button(root, text="Back <<-", bg="cyan",
                  activebackground="green", bd=8, width=8, command=backspace)
btn_back.place(x=x1, y=y1, height=45)


# button for arithmetic operator
btn_add = Button(root, text="+", bg="cyan",
                 activebackground="green", bd=8, width=6, font=f)
btn_add.place(x=270, y=200, height=45)
btn_add.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_sub = Button(root, text="-", bg="cyan",
                 activebackground="green", bd=8, width=6, font=f)
btn_sub.place(x=270, y=250, height=45)
btn_sub.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_mul = Button(root, text="*", bg="cyan",
                 activebackground="green", bd=8, width=6, font=f)
btn_mul.place(x=270, y=300, height=45)
btn_mul.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_div = Button(root, text="/", bg="cyan",
                 activebackground="green", bd=8, width=6, font=f)
btn_div.place(x=270, y=350, height=45)
btn_div.bind("<Button-1>", get_number1)

# butoon for Factorial with binding
btn_fact = Button(root, text="Fact", bg="red",
                  activebackground="green", bd=8, width=6, font=f)
btn_fact.place(x=350, y=200, height=45)
btn_fact.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_rev = Button(root, text="Reverse", bg="red",
                 activebackground="green", bd=8, width=6, font=f)
btn_rev.place(x=350, y=250, height=45)
btn_rev.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_bin = Button(root, text="Bin-Dec.", bg="red",
                 activebackground="green", bd=8, width=6, font=f)
btn_bin.place(x=350, y=300, height=45)
btn_bin.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_dec = Button(root, text="Dec-Bin.", bg="red",
                 activebackground="green", bd=8, width=6, font=f)
btn_dec.place(x=350, y=350, height=45)
btn_dec.bind("<Button-1>", get_number1)

# Button for square , root , power & Remainder
btn_sqr = Button(root, text="Square", bg="red",
                 activebackground="green", bd=8, width=6, font=f)
btn_sqr.place(x=430, y=200, height=45)
btn_sqr.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_pow = Button(root, text="Power", bg="red",
                 activebackground="green", bd=8, width=6, font=f)
btn_pow.place(x=430, y=250, height=45)
btn_pow.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_rt = Button(root, text="Root", bg="red",
                activebackground="green", bd=8, width=6, font=f)
btn_rt.place(x=430, y=300, height=45)
btn_rt.bind("<Button-1>", get_number1)

# Button for subtraction with binding
btn_remind = Button(root, text="Remainder", bg="red",
                    activebackground="green", bd=8, width=6, font=f)
btn_remind.place(x=430, y=350, height=45)
btn_remind.bind("<Button-1>", get_number1)

btn_comma = Button(root, text=" , ", bg="blue",
                   activebackground="green", bd=8, width=6, font=f)
btn_comma.place(x=30, y=400, height=50)
btn_comma.bind("<Button-1>", get_number1)

btn_n = Button(root, text="=", bg="blue",
               activebackground="green", bd=8, width=6, font=f)
btn_n.place(x=110, y=400, height=50)
btn_n.bind("<Button-1>", get_number1)

btn_n = Button(root, text=".", bg="blue",
               activebackground="green", bd=8, width=6, font=f)
btn_n.place(x=190, y=400, height=50)
btn_n.bind("<Button-1>", get_number1)

# Button for perform checking problem  armstrong :
btn_prime = Button(root, text="Check Prime Or Not", bg="blue",
                   activebackground="green", bd=8, width=24, font=f)
btn_prime.place(x=270, y=400, height=50)
btn_prime.bind("<Button-1>", get_number1)

# Button for perform checking problem  armstrong :
btn_palid = Button(root, text="Check Palindrom Or Not", bg="blue",
                   activebackground="green", bd=8, width=24, font=f)
btn_palid.place(x=30, y=455, height=50)
btn_palid.bind("<Button-1>", get_number1)

# Button for perform checking problem  strong :
btn_strong = Button(root, text="Check Strong Or Not", bg="blue",
                    activebackground="green", bd=8, width=24, font=f)
btn_strong.place(x=270, y=455, height=50)
btn_strong.bind("<Button-1>", get_number1)

# Button for finding Area Of Squar :
btn_asq = Button(root, text="Area Of Square", bg="blue",
                 activebackground="green", bd=8, width=24, font=f)
btn_asq.place(x=30, y=510, height=50)
btn_asq.bind("<Button-1>", get_number1)

# Button for finding Area Of Squar :
btn_arc = Button(root, text="Check Armstrong Or Not", bg="blue",
                 activebackground="green", bd=8, width=24, font=f)
btn_arc.place(x=270, y=510, height=50)
btn_arc.bind("<Button-1>", get_number1)

# Button for finding Area Of Squar :
btn_atr = Button(root, text="Area Of Triangle", bg="blue",
                 activebackground="green", bd=8, width=24, font=f)
btn_atr.place(x=30, y=565, height=50)
btn_atr.bind("<Button-1>", get_number1)

# Button for finding Area Of Squar :
btn_acr = Button(root, text="Area Of Circle", bg="blue",
                 activebackground="green", bd=8, width=24, font=f)
btn_acr.place(x=270, y=565, height=50)
btn_acr.bind("<Button-1>", get_number1)

# Button for finding Perimeter Of Square :
btn_psqr = Button(root, text="Perimeter Of Square", bg="magenta",
                  activebackground="green", bd=8, width=24, font=f)
btn_psqr.place(x=30, y=620, height=50)
btn_psqr.bind("<Button-1>", get_number1)

# Button for finding Perimeter Of Square :
btn_prc = Button(root, text="Perimeter Of Rectangle", bg="magenta",
                 activebackground="green", bd=8, width=24, font=f)
btn_prc.place(x=270, y=620, height=50)
btn_prc.bind("<Button-1>", get_number1)

# Button for finding Perimeter Of Square :
btn_ptr = Button(root, text="Perimeter Of Triangle", bg="gray",
                 activebackground="green", bd=8, width=24, font=f, fg="blue")
btn_ptr.place(x=30, y=675, height=50)
btn_ptr.bind("<Button-1>", get_number1)

# Button for finding Perimeter Of Square :
btn_pcr = Button(root, text="Perimeter Of Circle", bg="gray",
                 activebackground="green", bd=8, width=24, font=f, fg="blue")
btn_pcr.place(x=270, y=675, height=50)
btn_pcr.bind("<Button-1>", get_number1)


btn_Vcb = Button(root, text="Volume Of Cube", bg="magenta",
                 activebackground="green", bd=8, width=18, font=f1)
btn_Vcb.place(x=510, y=200, height=45)
btn_Vcb.bind("<Button-1>", get_number1)

btn_Vcuboid = Button(root, text="Volume Of Cuboid", bg="gray",
                     activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Vcuboid.place(x=660, y=200, height=45)
btn_Vcuboid.bind("<Button-1>", get_number1)

btn_sacube = Button(root, text="Surfacearea Of Cube", bg="magenta",
                    activebackground="green", bd=8, width=18, font=f1)
btn_sacube.place(x=510, y=250, height=45)
btn_sacube.bind("<Button-1>", get_number1)

btn_sacuboid = Button(root, text="Surfacearea Of Cuboid", bg="gray",
                      activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_sacuboid.place(x=660, y=250, height=45)
btn_sacuboid.bind("<Button-1>", get_number1)

btn_Dcube = Button(root, text="Diagonal Of Cube", bg="magenta",
                   activebackground="green", bd=8, width=18, font=f1)
btn_Dcube.place(x=510, y=300, height=45)
btn_Dcube.bind("<Button-1>", get_number1)

btn_Dcuboid = Button(root, text="Diagonal Of Cuboid", bg="gray",
                     activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Dcuboid.place(x=660, y=300, height=45)
btn_Dcuboid.bind("<Button-1>", get_number1)
# operation perform on


btn_Vcy = Button(root, text="Volume of cylinder", bg="magenta",
                 activebackground="green", bd=8, width=18, font=f1)
btn_Vcy.place(x=510, y=350, height=45)
btn_Vcy.bind("<Button-1>", get_number1)

btn_Vcone = Button(root, text="Volume of Cone", bg="gray",
                   activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Vcone.place(x=660, y=350, height=45)
btn_Vcone.bind("<Button-1>", get_number1)

######################
btn_Sacone = Button(root, text="Surfacearea Of Cone", bg="magenta",
                    activebackground="green", bd=8, width=18, font=f1)
btn_Sacone.place(x=510, y=400, height=50)
btn_Sacone.bind("<Button-1>", get_number1)

btn_Vsphere = Button(root, text="Volume Of Sphere", bg="gray",
                     activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Vsphere.place(x=660, y=400, height=50)
btn_Vsphere.bind("<Button-1>", get_number1)

btn_SAcly = Button(root, text="Surfacearae Of Cylinder", bg="magenta",
                   activebackground="green", bd=8, width=18, font=f1)
btn_SAcly.place(x=510, y=455, height=50)
btn_SAcly.bind("<Button-1>", get_number1)

btn_SAsphr = Button(root, text="Surfacearea Of H_Sphere", bg="gray",
                    activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_SAsphr.place(x=660, y=455, height=50)
btn_SAsphr.bind("<Button-1>", get_number1)

btn_TScly = Button(root, text="T_S.area Of cylinder", bg="magenta",
                   activebackground="green", bd=8, width=18, font=f1)
btn_TScly.place(x=510, y=510, height=50)
btn_TScly.bind("<Button-1>", get_number1)

btn_TSsphr = Button(root, text="T_S.area Of Sphere", bg="gray",
                    activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_TSsphr.place(x=660, y=510, height=50)
btn_TSsphr.bind("<Button-1>", get_number1)
# operation perform on
btn_TScone = Button(root, text="T_S.area of cone", bg="magenta",
                    activebackground="green", bd=8, width=18, font=f1)
btn_TScone.place(x=510, y=565, height=50)
btn_TScone.bind("<Button-1>", get_number1)

btn_Dsqr = Button(root, text="Diagonal Of Square", bg="gray",
                  activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Dsqr.place(x=660, y=565, height=50)
btn_Dsqr.bind("<Button-1>", get_number1)


btn_TScone = Button(root, text="Sum Of N Number", bg="magenta",
                    activebackground="green", bd=8, width=18, font=f1)
btn_TScone.place(x=510, y=620, height=50)
btn_TScone.bind("<Button-1>", get_number1)

btn_Dsqr = Button(root, text="Diagonal Of Rectangle", bg="gray",
                  activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Dsqr.place(x=660, y=620, height=50)
btn_Dsqr.bind("<Button-1>", get_number1)

btn_TScone = Button(root, text="Area Of Rectangle", bg="gray",
                    activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_TScone.place(x=510, y=675, height=50)
btn_TScone.bind("<Button-1>", get_number1)

btn_Dsqr = Button(root, text="Check Even Or Odd", bg="gray",
                  activebackground="green", bd=8, width=18, font=f1, fg="blue")
btn_Dsqr.place(x=660, y=675, height=50)
btn_Dsqr.bind("<Button-1>", get_number1)


# button for zero
btn_arm = Button(root, text="0", bg="cyan",
                 activebackground="green", bd=8, width=8)
btn_arm.place(x=110, y=350, height=45)
btn_arm.bind("<Button-1>", get_number1)


btn_clear = Button(root, text="Clear", bg="cyan",
                   activebackground="green", bd=8, width=8)
btn_clear.place(x=190, y=350, height=45)
btn_clear.bind("<Button-1>", get_number1)
start()
date()
day()
root.mainloop()
