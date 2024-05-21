# TEXT BOXES 
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# compulsory window
root = Tk()
root.geometry("1000x680+0+0")
root.title("TEXT BOXES")
root.configure(bg  = '#99FFCC')
root.iconbitmap(r'image/server_input.ico')


# entry field 

def output_box():
    text1 = "Hello ! , " + name_var.get() 
    output_lbl.config(text=str(text1))
    
def output_box2():
    text1 = "Address : " + text_area.get('1.0',END)
    output_lbl2.config(text=str(text1))

# function for exit the window
def exit_window():
    root.destroy()
# text area 
text_area = Text(root,font=("times new roman",14,'italic'),bg="gold",fg="green")
text_area.place(x=0,y=100,relwidth=0.5,relheight=0.3)

# entry filed 

name_var = StringVar()
entry_field = Entry(root,textvariable=name_var,font=("times new roman",14,'italic'),border=2,bg='green')
entry_field.place(x=0,y=10,relwidth=1,relheight=0.06)

# button related with entry field
# for entry
entry_button = Button(root,text="SUBMITEntry",font=("times new roman",14,"bold"),bg='red',fg='black',activebackground='gold',activeforeground='black',command=output_box)
entry_button.place(x=450,y=450)

# for text
entry_button = Button(root,text="SUBMITText",font=("times new roman",14,"bold"),bg='red',fg='black',activebackground='gold',activeforeground='black',command=output_box2)
entry_button.place(x=300,y=450)
# exit button 
entry_button = Button(root,text="EXIT",font=("times new roman",14,"bold"),bg='red',fg='black',activebackground='gold',activeforeground='black',command=exit_window)
entry_button.place(x=600,y=450)

# output label 
output_lbl = Label(root,text="",font=("times new roman",14,'italic'))
output_lbl.place(x=200,y=495)

output_lbl2 = Label(root,text="",font=("times new roman",14,'italic'))
output_lbl2.place(x=200,y=550)



if __name__ == "__main__":
    Tk.mainloop(root)