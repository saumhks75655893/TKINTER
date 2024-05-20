from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# main window
root = Tk()
root.geometry("600x430+400+150")
root.title("AREA OF THE TRIANGLE")
root.configure(bg  = '#99FFCC')
root.resizable(False,False)
# root.iconbitmap(r'image/buttons2.ico')


# Label frame 
area_frame = LabelFrame(root,text="Area",font=("times new roman",12,"italic"),bg='#EE9A49')
area_frame.place(x=10,y=2,width=580,height=200)

# taking width and height
#width
width1 = DoubleVar()
height1 = DoubleVar()

width_lbl = Label(area_frame,text="The Breadth of the triangle :   ",font=("times new roman",14,'italic','bold'))
width_lbl.grid(row=0,column=0,padx=30,pady=20)
width_input = Entry(area_frame,textvariable=width1,width=10,font=("Times new roman",20,'bold'))
width_input.grid(row=0,column=1,padx=20,pady=20)
#height
height_lbl = Label(area_frame,text="The Height of the triangle :   ",font=("times new roman",14,'italic','bold'))
height_lbl.grid(row=1,column=0,padx=30,pady=20)
height_input = Entry(area_frame,textvariable=height1,width=10,font=("Times new roman",20,'bold'))
height_input.grid(row=1,column=1,padx=20,pady=20)

# calculate function

def calculation():
    cal_lbl = Label(output_frame,text=f"Area of Triangle breadth : {float(width1.get())},height : {float(height1.get())} = ",font=('times new roman',15,'bold','italic'),bg='#FF6347',fg='#FFFF00')
    cal_lbl.grid(row=0,column=0)
    calculate_value = round(0.5 * height1.get() * width1.get(),4)
    lblArea = Label(output_frame,text=calculate_value,font=("times new roman",17,'bold','italic'))
    lblArea.grid(row=0, column=1)
    
def exitbutton():
    root.destroy()
        
# calculate frame

calculate_frame = Frame(root,bg='#8B2252')
calculate_frame.place(x=200,y=210,width=209,height=71)

calculate_button = Button(calculate_frame,text="CALCULATE",font=("arial",16,"bold"),width=13,border=13,bg='#D02090',fg='#FFFF00',activebackground='#8B2500',activeforeground='#C0FF3E',command=calculation)
calculate_button.grid(row=0,column=0,padx=4,pady=4)

# output window
output_frame = LabelFrame(root,text='Area Of Triangle',font=("times new roman",10,"italic"),bg='#FF6347')
output_frame.place(x=10,y=290,width=580,height=60)

# exit button
exit_button = Button(root,text="EXIT",font=("arial",16,"bold"),width=10,border=10,bg='#D02090',fg='#FFFF00',activebackground='#8B2500',activeforeground='#C0FF3E',command=exitbutton,relief=RIDGE)
exit_button.place(x=220,y=360)



# main runner window
if __name__ == "__main__":
    Tk.mainloop(root)


# Area of triangle : 1/2 * breadth * heigh 
