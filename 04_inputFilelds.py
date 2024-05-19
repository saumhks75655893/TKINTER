from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# compulsory window
root = Tk()
root.geometry("1000x680+0+0")
root.title("INPUT FIELDS")
root.configure(bg  = '#99FFCC')
root.iconbitmap(r'image/server_input.ico')


# input window
input_label = LabelFrame(root,text="INPUT WINDOW",font=("times new roman",12,'bold'))
input_label.place(x=2,y=2,width=950,height=630)

# name

namelbl = Label(input_label,text="Name : ",font=("times new roman",14,'bold','italic'))
namelbl.grid(row=0,column=0)
entry_box = ttk.Entry(input_label,width=20,font=("times new roman",14,'italic'))
entry_box.grid(row=0,column=1)

def inputvalue():
    text1 = "hello !! " + entry_box.get()
    lbltext = Label(input_label,text=text1,font=("times new roman",16,'bold','italic'))
    lbltext.place(x=3,y=30)

# enter button
enter_button = PhotoImage(file = r'image/enter.png')
enterbtn_resize = enter_button.subsample(7,15)
enter_btn = ttk.Button(input_label,image=enterbtn_resize,command=inputvalue)
enter_btn.place(x=862,y=563)


# main window
if __name__ == "__main__":
    Tk.mainloop(root)