from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# main window
root = Tk()
root.geometry("1000x1000+0+0")
root.configure(bg = "Powder blue")
root.title("BUTTON WINDOW")
root.iconbitmap(r'image/buttons1.ico')

# creating button window

def click():
    lbl = Label(root,text="Please Subscribe the channel !!! ",font=("TIMES NEW ROMAN",20,"italic"))
    lbl.place(x=300,y=0)
    
def exitbutton():
    root.destroy()

MyButton = Button(root,text="Click Me",font=("arial",22,"bold"),fg="red",bg="gold",command=click,relief=RAISED,bd=5,activebackground='black',width=10,activeforeground="gold")
MyButton.place(x=0,y=0)

MyButton1 = Button(root,text="Exit",font=("arial",22,"bold"),fg="red",bg="gold",relief=RAISED,bd=5,activebackground='black',activeforeground="gold",width=10,command=exitbutton)
MyButton1.place(x=804,y=0)


#  Button using button image

label_frame = LabelFrame(root,text="Button Window",font=("times new roman",15,"bold"),bg="red")
label_frame.place(x=5,y=70,width=400,height=610)
# function
def thing():
    lable1 = Label(label_frame,text="You have entered your text successfully  !!!!! ",font=("times new roman",15,"bold"))
    lable1.grid(row=0,column=0)
    
def window_break():
    label_frame.destroy()
def message_exit():
    msg = messagebox.showinfo("Good ","Work completed!!!!")
    
# buttons 
my_image = PhotoImage(file=r"image/enter.png")
img_resize = my_image.subsample(10,10)
# img_lbl = Label(root,image=img_resize)
button_img = ttk.Button(label_frame,image=img_resize,command=thing)
button_img.place(x=334,y=522)
    
my_image1 = PhotoImage(file=r"image/cross.png")
img_resize1 = my_image1.subsample(10,10)
# img_lbl = Label(root,image=img_resize)
button_img1 = ttk.Button(label_frame,image=img_resize1,command=window_break)
button_img1.place(x=270,y=522)


if __name__ == "__main__":
    Tk.mainloop(root)