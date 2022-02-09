
from tkinter import *
from turtle import width
from PIL import ImageTk,Image
root=Tk()
root.title("window")
root.iconbitmap('icon.ico')  


img1=Image.open("n1.jpg")
img1=img1.resize((600,500))
img1=ImageTk.PhotoImage(img1)
lab1=Label(root, image=img1)
lab1.image=img1


img2=Image.open("n2.jfif")
img2=img2.resize((600,500))
img2=ImageTk.PhotoImage(img2)
lab2=Label(root, image=img2)
lab2.image=img2


img3=Image.open("n3.jfif")
img3=img3.resize((600,500))
img3=ImageTk.PhotoImage(img3)
lab3=Label(root, image=img3)
lab3.image=img3

img4=Image.open("n4.jpg")
img4=img4.resize((600,500))
img4=ImageTk.PhotoImage(img4)
lab4=Label(root, image=img4)
lab4.image=img4

img5=Image.open("n5.jfif")
img5=img5.resize((600,500))
img5=ImageTk.PhotoImage(img5)
lab5=Label(root, image=img5)
lab5.image=img5

img6=Image.open("n6.jfif")
img6=img6.resize((600,500))
img6=ImageTk.PhotoImage(img6)
lab6=Label(root, image=img6)
lab6.image=img6

img7=Image.open("n7.jfif")
img7=img7.resize((600,500))
img7=ImageTk.PhotoImage(img7)
lab7=Label(root, image=img7)
lab7.image=img7


images=[img1,img2,img3,img4,img5,img6,img7]  
lab=Label(image=images[0])
lab.grid(row=2,column=0,columnspan=3)

def forward(num):
    global lab
    global button_forward
    global button_backward
    lab.grid_forget()   
    
    lab=Label(image=images[num])
    lab.grid(row=2,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda: forward(num+1))
    button_backward=Button(root,text="<<",command=lambda: backward(num-1))

    if num==6:
        button_forward=Button(root,text=">>",state=DISABLED)
    button_forward.grid(row=1,column=2)
    button_backward.grid(row=1,column=0)

def backward(num):
    global lab
    global button_forward
    global button_backward
    lab.grid_forget()
   
    lab=Label(image=images[num])
    lab.grid(row=2,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda: forward(num+1))
    button_backward=Button(root,text="<<",command=lambda: backward(num-1))
    if num==1:
        button_backward=Button(root,text="<<",state=DISABLED)
    button_forward.grid(row=1,column=2)
    button_backward.grid(row=1,column=0)



button=Button(root,text="Exit",command=root.destroy).grid(row=1,column=1)
button_forward=Button(root,text=">>",command=lambda: forward(1)).grid(row=1,column=2)   
button_backward=Button(root,text="<<",command=backward,state=DISABLED).grid(row=1,column=0)
root.mainloop()